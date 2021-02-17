# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:26:46 2021

@author: lauta
"""

import requests
import json

class ConsultasAPI(object):
    
    def __init__(self, token, timeout :int=60):
        self.token = token
        self.timeout = timeout
        self.CONSULTA_HOST = 'https://startup.bolsadesantiago.com/api/consulta'
        
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }

        self.params = {
            'access_token': self.token
            }
        
        self.has_model = False
        
    def __handle_response(self, endpoint: str, **kwargs):
        
        if self.has_model:
            resp = requests.post(endpoint, params=self.params, headers=self.headers)
        else:
            resp = requests.post(endpoint, params=self.params, headers=self.headers, json=kwargs)
            
        if resp.status_code == 200:
             if 'listaResult' in resp.json().keys():
                 return resp.json()['listaResult']
             else:
                 return resp.json()
        else:
            resp.raise_for_status()
    
    def get_instrumentos_validos(self):
        endpoint = f"{self.CONSULTA_HOST}/InstrumentosDisponibles/getInstrumentosValidos"
        return self.__handle_response(endpoint)
        