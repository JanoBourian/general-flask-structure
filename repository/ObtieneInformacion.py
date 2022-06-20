from config.env_reader import env
from creditkit_tools.auxiliar_message import RequestsMessage

class ObtieneInformacion:
    def __init__(self):
        self.example = env('EXAMPLE')
    
    def post(self, payload):
        response = RequestsMessage(**payload).make_request()
        return response