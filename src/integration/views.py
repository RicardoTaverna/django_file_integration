import csv
from os import scandir, stat
import requests

from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from integration.forms import DocumentForm
from integration.models import Mensagem, Broker, ValidDDD, Envio

def homepage(request):
    """Função que renderiza a página inicial."""
    form = DocumentForm()
    if request.method == 'POST' and 'upload-file' in request.POST:
        _save_file(request)

    if request.method == 'POST' and 'send-message' in request.POST:
        _send_message()

    context = {
        'values': Mensagem.objects.all,
        'form': form,
        'envios': Envio.objects.all
    }
    return render(request, 'integration/home.html', context)


def _save_file(request):
    """Função privada para salvar o arquivo enviado

    Args:
        request ([any]): request enviado para o back.
    """
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        print()
        _handle_upload_file(request.FILES['documento'])

def _handle_upload_file(uploaded_file):
    """Função privada para lidar com o arquivo enviado.

    Args:
        uploaded_file (str): nome do arquivo enviado para o back.
    """
    with open(f"static/media/documents/{uploaded_file}", 'r') as open_file:
        data = csv.reader(open_file, delimiter=',')
        for line in data:
            status = _validate_rules(ddd=line[1], phone=line[2], send_time=line[4], message=line[5])            
            _save_message(data=line, status=status)

def _validate_rules(ddd, phone, send_time, message):
    """Função que valida os telefone e mensagem conforme as regras de negocio.

    Args:
        ddd (int): ddd enviado
        phone (int): telefone enviado
        send_time (str): hora do envio agendada
        message (str): mensagem enviada
    """
    valid_time = datetime.strptime("19:59:59", '%H:%M:%S').time()
    send_time = datetime.strptime(send_time, '%H:%M:%S').time()
    valid_ddd = ValidDDD.objects.filter(ddd=ddd)
    first_digit = str(phone)
    first_digit = first_digit[0:1]
    second_digit = str(phone)
    second_digit = second_digit[1:2]

    if len(str(ddd)) != 2 or len(valid_ddd) < 1:
        status = 'Inválido'
        return status

    if valid_ddd[0].estado == 'SP' or send_time > valid_time or len(message) > 140:
        status = 'Não Permitido'
        return status

    if len(str(phone)) != 9 or int(first_digit) != 9 or int(second_digit) <= 6:
        status = 'Inválido'
        return status

    if _check_blacklist(ddd=ddd, phone=phone) == 200:
        status = 'Blacklist'
        return status

    status = 'Valido'
    return status

def _check_blacklist(ddd, phone):
    """Função privada para checar se o número está na blacklist.

    Args:
        ddd (int): ddd enviado
        phone (int): telefone a ser checado
    """
    complete_phone = str(ddd) + str(phone)
    check = requests.get(f'https://front-test-pg.herokuapp.com/blacklist/{complete_phone}')
    return check.status_code

def _save_message(data, status):
    """Função para salvar a mensagem a partir do upload de um arquivo.

    Args:
        data (list): valores a serem adicionados.
        status (str): status da mensagem.
    """
    mensagem = Mensagem(
        id_mensagem=data[0],
        ddd=data[1],
        numero=data[2],
        operadora=data[3],
        hora_envio=data[4],
        mensagem=data[5],
        status=status
    )
    mensagem.save()

def _send_message():
    """Função privada que realiza o envio das mensagens."""
    mensagens = Mensagem.objects.all().filter(status='Valido')
    print(mensagens)
    for mensagem in mensagens:
        broker = Broker.objects.get(operadora=mensagem.operadora)
        print('passei aqui')
        envio = Envio(
            id_mensagem=mensagem.id_mensagem,
            numero=mensagem.numero,
            id_broker=broker.id_broker,
            operadora=broker.operadora
        )
        envio.save()