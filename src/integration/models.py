from django.db import models

class Documento(models.Model):
    """Mode referente ao upload de arquivos."""
    descricao = models.CharField(max_length=255, blank=True)
    documento = models.FileField(upload_to='documents/')
    data_upload = models.DateTimeField(auto_now_add=True)


class Mensagem(models.Model):
    """Model com os mesmos campos do arquivo de entrada."""
    STATUS_MENSAGEM = (
        ('Blacklist', 'Blacklist'),
        ('Inválido', 'Inválido'),
        ('Valido', 'Valido'),
        ('Não Permitido', 'Não Permitido')
    )

    id_mensagem = models.CharField(max_length=50, blank=True, null=True)
    ddd = models.IntegerField(blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    operadora = models.CharField(max_length=50, blank=True, null=True)
    hora_envio = models.CharField(max_length=20, blank=True, null=True)
    mensagem = models.CharField(max_length=140, blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS_MENSAGEM, blank=True, null=True)

    def __str__(self):
        """função para sobreescrever o nome apresentado na tela de admin."""
        return self.id_mensagem
    

class Broker(models.Model):
    """Model da tabela broker."""
    OPERADORAS = (
        ('CLARO', 'CLARO'),
        ('NEXTEL', 'NEXTEL'),
        ('OI', 'OI'),
        ('TIM', 'TIM'),
        ('VIVO', 'VIVO'),
    )

    id_broker = models.IntegerField(blank=True, null=True)
    operadora = models.CharField(max_length=15, choices=OPERADORAS, blank=True, null=True)

    def __str__(self):
        """função para sobreescrever o nome apresentado na tela de admin."""
        return self.operadora

class ValidDDD(models.Model):
    """Model para tabela de DDDs válidos."""
    ddd = models.IntegerField()
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        """função para sobreescrever o nome apresentado na tela de admin."""
        return str(self.ddd) + '-' + self.cidade + '-' + self.estado

class Envio(models.Model):
    """Model para a tabela de envios."""
    id_mensagem = models.CharField(max_length=50, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    id_broker = models.IntegerField(blank=True, null=True)
    operadora = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        """função para sobreescrever o nome apresentado na tela de admin."""
        return self.id_mensagem
