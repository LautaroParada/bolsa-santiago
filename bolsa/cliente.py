# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:28:11 2021

@author: lauta
"""

import requests
import json
from typing import Dict, Type

# from bolsa import modelos
# from bolsa.modelos import unmarshal

class RESTCliente(object):
    
    def __init__(self, token, timeout: int=60):
        self.token = token
        self.DEFAULT_HOST = 'startup.bolsadesantiago.com/api/consulta'
        self.url = 'https://' + self.DEFAULT_HOST
        self.timeout = timeout
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }

        self.params = {
            'access_token': self.token
            }
        
    # def __handle_response(self, response_type: str, endpoint: str, params: Dict[str, str]) -> Type[modelos.AnyDefinition]:
    #     resp = requests.post(endpoint, params=params, headers=self.headers, timeout=self.timeout)
    #     if resp.status_code == 200:
    #         return unmarshal.unmarshal_json(response_type, resp.json())
    #     else:
    #         resp.raise_for_status()
        
    def id_instrumentos_validos(self):
        endpoint = f"{self.url}/InstrumentosDisponibles/getInstrumentosValidos"
        r = requests.post(endpoint, params=self.params, headers=self.headers, timeout=self.timeout)
        
        # return self.__handle_response(endpoint)
        return r