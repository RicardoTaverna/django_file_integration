from django.contrib import admin
from .models import Mensagem, Documento, Broker, ValidDDD, Envio
# Register your models here.

admin.site.register(Mensagem)
admin.site.register(Documento)
admin.site.register(Broker)
admin.site.register(ValidDDD)
admin.site.register(Envio)