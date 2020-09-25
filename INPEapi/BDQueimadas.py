import requests
import json

class BDQueimadas:
    def __init__(self):
        self.base_url = "http://queimadas.dgi.inpe.br/queimadas/dados-abertos/api/focos/"

    def make_request(self):
        r = requests.get(self.base_url)

        return r.json()