# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:26:46 2021

@author: lauta
"""

import requests
import json
from typing import Dict

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
        
        self.endpoint_pivot = None
        
    # ------------------------------
    # Metodos para eliminar la redundancia en el cliente
    # ------------------------------
        
    def __handle_response(self, query_params: Dict[str, str]={}):
        
        resp = requests.post(self.endpoint_pivot, params=self.params, headers=self.headers, json=query_params, timeout=self.timeout)
            
        if resp.status_code == 200:
             if 'listaResult' in resp.json().keys():
                 return resp.json()['listaResult']
             else:
                 return resp.json()
        else:
            resp.raise_for_status()
            
    def __endpoint_builder(self, endpoint):
        self.endpoint_pivot = f"{self.CONSULTA_HOST}/{endpoint}"
            
            
    # ------------------------------
    # Instrumentos Disponibles
    # ------------------------------
    
    def get_instrumentos_validos(self):
        self.__endpoint_builder("InstrumentosDisponibles/getInstrumentosValidos")
        return self.__handle_response()
    
    # ------------------------------
    # Request Usuario
    # ------------------------------
    
    def get_request_usuario(self):
        self.__endpoint_builder("RequestUsuario/getRequestUsuario")
        return self.__handle_response()
    
    # ------------------------------
    # Cliente Market Data
    # ------------------------------
    
    def get_indices_rv(self):
        self.__endpoint_builder("ClienteMD/getIndicesRV")
        return self.__handle_response()
    
    def get_instrumentos_rv(self):
        self.__endpoint_builder("ClienteMD/getInstrumentosRV")
        return self.__handle_response()
    
    def get_puntas_rv(self):
        self.__endpoint_builder("ClienteMD/getPuntasRV")
        return self.__handle_response()
    
    def get_transacciones_rv(self):
        self.__endpoint_builder("ClienteMD/getTransaccionesRV")
        return self.__handle_response()
    
    # ------------------------------
    # Ticker on Demand
    # ------------------------------
    
    def get_indices(self):
        self.__endpoint_builder("TickerOnDemand/getIndices")
        return self.__handle_response()
    
    def get_resumen_accion(self, **query_params):
        self.__endpoint_builder("TickerOnDemand/getResumenAccion")
        
        # Verificando los parametros del metodo
        for key, value in query_params.items():
            if key != 'Nemo':
                print('El parametro aceptado por el metodo es Nemo')
                return
            value = value.upper()
        
        return self.__handle_response(query_params)