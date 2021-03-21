from django.test import TestCase
from integration.views import _validate_phone, _check_blacklist

# Create your tests here.
class ViewTestCase(TestCase):
    
    def test_validate_phone_success(self):
        """Testa se uma mensagem foi criada com sucesso."""
        ddd = 41
        phone = 999100389
        send_time = "18:45:25"
        message = "dui luctus rutrum nulla tellus in sagittis dui"
        status = _validate_phone(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            
        )
        message = Mensagem.objects.get(id_mensagem="asdf-dffg-ewr-123dfg")
        status = message.status
        self.assertEqual(status, 'V')