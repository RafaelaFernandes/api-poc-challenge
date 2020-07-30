import requests
from test_utils import *


class TestsNegativos:

    def test_payload_valores_vazios(self):
        payload = LambdaPayload("", "")
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)


        pretty_print_request(response.request)
        pretty_print_response(response)

    def test_payload_vazio(self):
        payload = LambdaPayload()
        response = requests.request("POST", LAMBDA_URL, headers=payload.header, json=payload.body)

        response_data = response.json()

        assert(response.status_code == 400)
        assert(response_data["statusCode"] == 400)

        pretty_print_request(response.request)
        pretty_print_response(response)

