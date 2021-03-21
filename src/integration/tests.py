from django.test import TestCase
from integration.models import Mensagem, Broker, ValidDDD, Envio
from integration.views import _validate_phone, _check_blacklist

# Create your tests here.
class ModelTestCase(TestCase):
    def setup(self):
        Mensagem.objects.create(
            id_mensagem="asdf-dffg-ewr-123dfg",
            ddd=55,
            numero=999100389,
            operadora="TESTE",
            hora_envio="19:45:20",
            mensagem="mensagem de teste",
            status="V"
        )
        Broker.objects.create(
            id_broker=4,
            operadora="TESTE"
        )
        ValidDDD.objects.create(
            ddd=55,
            cidade="cidade de teste",
            estado="TS"
        )
    
    def test_created_message(self):
        """Testa se uma mensagem foi criada com sucesso."""
        message = Mensagem.objects.get(id_mensagem="asdf-dffg-ewr-123dfg")
        status = message.status
        self.assertEqual(status, 'V')