from django.test import TestCase
from integration.models import ValidDDD
from integration.views import _validate_rules, _check_blacklist

# Create your tests here.
class ViewTestCase(TestCase):
    def setUp(self) -> None:
        ValidDDD.objects.create(ddd=41, cidade="Curitiba", estado="PR")
        ValidDDD.objects.create(ddd=46, cidade="Francisco Beltrão/Pato Branco", estado="PR")
        ValidDDD.objects.create(ddd=11, cidade="São Paulo", estado="SP")
        return super().setUp()

    def test_validate_phone_success(self):
        """Testa se uma mensagem foi criada com sucesso."""
        ddd = 41
        phone = 999100389
        send_time = "18:45:25"
        message = "dui luctus rutrum nulla tellus in sagittis dui"
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Valido')

    def test_validate_phone_invalid_ddd(self):
        """Testa se uma mensagem tem ddd inválido, não possui correspondente no db."""
        ddd = 111
        phone = 999100389
        send_time = "18:45:25"
        message = "dui luctus rutrum nulla tellus in sagittis dui"
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Inválido')

    def test_validate_phone_invalid_estate(self):
        """Testa se uma mensagem é do estado de SP."""
        ddd = 11
        phone = 999100389
        send_time = "18:45:25"
        message = "dui luctus rutrum nulla tellus in sagittis dui"
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Não Permitido')

    def test_validate_phone_invalid_send_time(self):
        """Testa se uma mensagem tem o horario de envio inválido."""
        ddd = 41
        phone = 999100389
        send_time = "20:45:25"
        message = "dui luctus rutrum nulla tellus in sagittis dui"
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Não Permitido')

    def test_validate_phone_invalid_send_time(self):
        """Testa se uma mensagem tem o horario de envio inválido."""
        ddd = 41
        phone = 999100389
        send_time = "20:45:25"
        message = "dui luctus rutrum nulla tellus in sagittis dui"
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Não Permitido')

    def test_validate_phone_invalid_message_len(self):
        """Testa se uma mensagem tem mais de 140 caracteres."""
        ddd = 41
        phone = 999100389
        send_time = "16:45:25"
        message = """dui luctus rutrum nulla tellus in sagittis dui dui luctus rutrum nulla tellus in
        sagittis dui dui luctus rutrum nulla tellus in sagittis dui tellus"""
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Não Permitido')

    def test_validate_phone_invalid_number(self):
        """Testa se o número é diferente de nove digitos."""
        ddd = 41
        phone = 9991003
        send_time = "15:45:25"
        message = """dui luctus rutrum nulla tellus in sagittis."""
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Inválido')
    
    def test_validate_phone_invalid_number_first_digit(self):
        """Testa se o número tem o primeiro digito diferente de nove."""
        ddd = 41
        phone = 899100389
        send_time = "15:45:25"
        message = """dui luctus rutrum nulla tellus in sagittis."""
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Inválido')

    def test_validate_phone_invalid_number_second_digit(self):
        """Testa se o número tem o segundo digito menor que 6."""
        ddd = 41
        phone = 959100389
        send_time = "15:45:25"
        message = """dui luctus rutrum nulla tellus in sagittis."""
        status = _validate_rules(
            ddd=ddd,
            phone=phone,
            send_time=send_time,
            message=message
        )
        self.assertEqual(status, 'Inválido')
    
    def test_on_blacklist(self):
        """Testa se o número está na blacklist."""
        ddd = 46
        phone = 950816645
        status_code = _check_blacklist(
            ddd=ddd,
            phone=phone
        )
        self.assertEqual(status_code, 200)
    
    def test_not_blacklist(self):
        """Testa se o número está na blacklist."""
        ddd = 41
        phone = 999100389
        status_code = _check_blacklist(
            ddd=ddd,
            phone=phone
        )
        self.assertEqual(status_code, 404)