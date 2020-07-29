import json

LAMBDA_URL = "https://7eb984w4j4.execute-api.us-east-1.amazonaws.com/dev/lambdastresstest"


class LambdaPayload:
    def __init__(self, mensagem, num_destinatario):
        self.mensagem = mensagem
        self.num_destinario = num_destinatario
        self.body = self.construir_body()
        self.header = self.construir_header()

    def construir_body(self):
        return {"mensagem": self.mensagem, "num_destinatario": self.num_destinario}

    def construir_header(self):
        return {'Content-Type': 'application/json'}


def pretty_print_request(request):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '-----------Request----------->',
        request.method + ' ' + request.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
        request.body)
    )


def pretty_print_response(response):
    print('\n{}\n{}\n\n{}\n\n{}\n'.format(
        '<-----------Response-----------',
        'Status code:' + str(response.status_code),
        '\n'.join('{}: {}'.format(k, v) for k, v in response.headers.items()),
        response.text)
    )