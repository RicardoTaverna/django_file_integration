import csv
from os import stat
import requests

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from integration.forms import DocumentForm
from integration.models import Mensagem, Broker, ValidDDD, Envio

def homepage(request):
    """Controller que cria a pagina inicial."""
    form = DocumentForm()
    if request.method == 'POST' and 'upload-file' in request.POST:
       _save_file(request)

    if request.method == 'POST' and 'send-message' in request.POST:
        mensagens = Mensagem.objects.all().filter(status='V')
        for mensagem in mensagens:
            broker = Broker.objects.get(operadora=mensagem.operadora)
            envio = Envio(
                id_mensagem=mensagem.id_mensagem,
                numero=mensagem.numero,
                id_broker=broker.id_broker,
                operadora=broker.operadora
            )
            envio.save()

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
            status = _validate_phone(line[1], line[2])            
            _save_message(data=line, status=status)

def _validate_phone(ddd, phone):
    """[summary]

    Args:
        ddd (int): ddd enviado
        phone (int): telefone enviado
    """
    
    valid_ddd = ValidDDD.objects.get(ddd=ddd)
    second_digit = int(str(phone[1:2]))
    if valid_ddd.estado == 'SP':
        status = 'N'
        return status

    if len(ddd) != 2 or not valid_ddd or len(phone) != 9 or second_digit <= 6:
        status = 'I'
        return status

    if _check_blacklist(ddd=ddd, phone=phone) == 200:
        status = 'B'
        return status

    status = 'V'
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