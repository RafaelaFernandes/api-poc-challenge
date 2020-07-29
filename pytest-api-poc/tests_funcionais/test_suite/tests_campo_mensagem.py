import requests
from test_utils import *


class TestsPositivos:

    def test_valor_max_caracteres(self):
        payload = LambdaPayload("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", 12345678901)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 200)
        assert(response_data["statusCode"] == 200)
        assert(response_data["body"] == '"Mensagem enviada com sucesso"')

        pretty_print_request(response.request)
        pretty_print_response(response)

    def test_caracteres_estrangeiros(self):
        payload = LambdaPayload("我想在这里工作", 12345678901)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 200)
        assert(response_data["statusCode"] == 200)
        assert(response_data["body"] == '"Mensagem enviada com sucesso"')

        pretty_print_request(response.request)
        pretty_print_response(response)


class TestsNegativos:

    def test_valor_minimo_caracteres(self):
        payload = LambdaPayload("", 12345678901)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)


        pretty_print_request(response.request)
        pretty_print_response(response)


    def test_valor_acima_permitido_caracteres(self):
        payload = LambdaPayload("111111111111111111111111111111111111@@@@@@@@@@@@@@@aaaaaaaaaaaaaaaaaaaa%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@", 12345678901)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert (response.status_code == 400)
        assert (response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)

    def test_sem_o_campo(self):
        payload = LambdaPayload(12345678901)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert (response.status_code == 400)
        assert (response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)



    def test_XSS(self):
        payload = LambdaPayload("<script>alert(123);</script>", 12345678901)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert (response.status_code == 400)
        assert (response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)