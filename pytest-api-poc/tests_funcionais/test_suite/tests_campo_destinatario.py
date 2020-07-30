import requests
from test_utils import *


class TestsPositivos:

    def test_payload_valido(self):
        payload = LambdaPayload("Mensagem de teste", 11111111111)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 200)
        assert(response_data["statusCode"] == 200)
        assert(response_data["body"] == '"Mensagem enviada com sucesso"')

        pretty_print_request(response.request)
        pretty_print_response(response)


class TestsNegativos:

    def test_valor_acima_permitido(self):
        payload = LambdaPayload("Mensagem de teste", 111111111110)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)


        pretty_print_request(response.request)
        pretty_print_response(response)

    def test_valor_abaixo_permitido(self):
        payload = LambdaPayload("Mensagem de teste", 1010101010)
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)

    def test_letras(self):
        payload = LambdaPayload("Mensagem de teste", "101010df10")
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)

    def test_sem_o_campo(self):
        payload = LambdaPayload("Mensagem de teste")
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)

    def test_campo_vazio(self):
        payload = LambdaPayload("Mensagem de teste", "")
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)

    def test_xss(self):
        payload = LambdaPayload("Mensagem de teste", "<script>alert(123);</script>")
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)