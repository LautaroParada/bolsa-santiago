# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:26:46 2021

@author: lauta
"""

import requests
import json
from typing import Dict

class NegociacionAPI(object):
    """
    Ponemos a tu disposición un sandbox para que puedas probar el ingreso de
    ofertas mediante DMA y experimentes cómo se distribuyen los datos en el
    Market Data RV Negociación. Podrás ver mediante la suscripción de puntas
    los ingresos de ofertas y el resultado de los calces de ofertas compatibles
    en la suscripción de transacciones.
    
    MARKET DATA
    Un Market Data es una aplicación que mantiene en memoria el estado del 
    mercado en tiempo real. Estos reciben información sobre estados de 
    negociación, puntas, profundidad, resumen del mercado, entre otros, para 
    posteriormente distribuirla al mercado. Todo este tipo de información se 
    envía mediante protocolo FIX.

    CLIENTE MARKET DATA
    El Cliente Market Data Renta Variable es un producto creado por la Bolsa 
    de Comercio de Santiago con el fin de transcribir los mensajes FIX enviados
    por el Market Data de Renta Variable a una base de datos.
    
    DMA
    Los servicios DMA - Direct Market Acces - permiten la canalización o ruteo
    automático de órdenes de compra y venta de acciones en tiempo real, al 
    sistema SEBRA HT.
    
    FUENTE
    https://startup.bolsadesantiago.com/#/descripcion_negociacion
    """
    
    def __init__(self, token, timeout :int=60):
        self.token = token
        self.timeout = timeout
        self.NEGOCIACION_HOST = 'https://startup.bolsadesantiago.com/api/negociacion'
        
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }

        self.params = {
            'access_token': self.token
            }
        
        self.has_model = False
        
    # ------------------------------
    # Metodos para eliminar la redundancia en el cliente
    # ------------------------------
        
    def __handle_response(self, query_params: Dict[str, str]={}):
        """
        Este método manipula de manera centralizada las solicitudes a la API.

        Parameters
        ----------
        query_params : Dict[str, str], opcional
            DESCRIPTION. The default is {}.

        Returns
        -------
        list or dict
            Lista o Dictionario con los datos de la consulta o un mensaje de 
            error.

        """
        
        resp = requests.post(self.endpoint_pivot, params=self.params, headers=self.headers, json=query_params, timeout=self.timeout)
            
        if resp.status_code == 200:
             if 'listaResult' in resp.json().keys():
                 return resp.json()['listaResult']
             else:
                 return resp.json()
        else:
            resp.raise_for_status()
            
    def __endpoint_builder(self, endpoint: str):
        """
        Constructor centralizado de default host + endpoints

        Parameters
        ----------
        endpoint : str
            endpoint solicitado.

        Returns
        -------
        None.

        """
        self.endpoint_pivot = f"{self.NEGOCIACION_HOST}/{endpoint}"
        
    # ------------------------------
    # Instrumentos disponibles en ingreso de ofertas
    # ------------------------------
    
    def get_instrumentos_validos(self):
        self.__endpoint_builder('InstrumentosDisponibles/getInstrumentosValidos')
        return self.__handle_response()
    
    # ------------------------------
    # Request Usuario
    # ------------------------------
    
    def get_request_usuario(self):
        """
        Número de solcitudes disponibles a realizar.

        Returns
        -------
        dict
            Consumo actual y límite diario.

        """
        self.__endpoint_builder("RequestUsuario/getRequestUsuario")
        return self.__handle_response()
    
    # ------------------------------
    # Cliente Market Data
    # ------------------------------
    
    def get_puntas_rv(self):
        self.__endpoint_builder('ClienteMD/getPuntasRV')
        return self.__handle_response()
    
    def get_transacciones_rv(self):
        self.__endpoint_builder('ClienteMD/getTransaccionesRV')
        return self.__handle_response()
    
    # ------------------------------
    # DMA
    # ------------------------------
    def get_revision_ingreso(self):
        self.__endpoint_builder("DMA/getRevisionIngreso")
        return self.__handle_response()
    
    def get_revision_transaccion(self, **query_parameters):
        self.__endpoint_builder('DMA/getRevisionTransaccion')
        return self.__handle_response()
    
    