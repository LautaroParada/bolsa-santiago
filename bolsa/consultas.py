# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:26:46 2021

@author: lauta
"""

import requests
import json
from typing import Dict

class ConsultasAPI(object):
    """
    INFORMACIÓN DE MERCADO
    Entérate de los por menores del mercado de Renta Variable con las APIs 
    de información de mercado.

    Las APIs de información de mercado te permitirán simular el uso del 
    Market Data de Renta Variable y del cliente Market Data de Renta Variable
    mediante el consumo de datos productivos a través de web services.


    MARKET DATA
    Un Market Data es una aplicación que mantiene en memoria el estado del 
    mercado en tiempo real. Estos reciben información sobre estados de 
    negociación, puntas, profundidad, resumen del mercado, entre otros, para
    posteriormente distribuirla al mercado. Todo este tipo de información se
    envía mediante protocolo FIX.

    CLIENTE MARKET DATA
    El Cliente Market Data Renta Variable es un producto creado por la 
    Bolsa de Comercio de Santiago con el fin de transcribir los mensajes FIX
    enviados por el Market Data de Renta Variable a una base de datos.
    
    FUUENTE
    https://startup.bolsadesantiago.com/#/descripcion_consulta
    """
    
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
        self.endpoint_pivot = f"{self.CONSULTA_HOST}/{endpoint}"
            
            
    # ------------------------------
    # Instrumentos Disponibles
    # ------------------------------
    
    def get_instrumentos_validos(self):
        """
        Este endpoint te permitirá conocer cuales son los instrumentos del 
        mercado de renta variable que tendrás disponibles para utilizar en las 
        demás APIs.
        
        Ten en consideración que mañana los instrumentos disponibles pueden
        ser otros.

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.

        """
        self.__endpoint_builder("InstrumentosDisponibles/getInstrumentosValidos")
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
    
    def get_indices_rv(self):
        """
        Valor de los principales índices de renta variable junto con su 
        variación porcentual y volumen.

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.
            
        """
        self.__endpoint_builder("ClienteMD/getIndicesRV")
        return self.__handle_response()
    
    def get_instrumentos_rv(self):
        """
        Detalle de los instrumentos disponibles para transar en el 
        mercado de renta variable. Se muestra precio de apertura, mínimos y 
        máximos y volumen transado, entre otros.

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.

        """
        self.__endpoint_builder("ClienteMD/getInstrumentosRV")
        return self.__handle_response()
    
    def get_puntas_rv(self):
        """
        Mejores ofertas que se encuentran ingresadas en el mercado de renta 
        variable. Se muestra precio de compra, precio de venta, cantidad, monto, 
        condición de liquidación, entre otros.

        Returns
        -------
        list
            

        """
        self.__endpoint_builder("ClienteMD/getPuntasRV")
        return self.__handle_response()
    
    def get_transacciones_rv(self):
        """
        Detalle de las transacciones en renta variable. Se muestra instrumento, 
        condición de liquidación y cantidad, entre otros.

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.

        """
        self.__endpoint_builder("ClienteMD/getTransaccionesRV")
        return self.__handle_response()
    
    # ------------------------------
    # Ticker on Demand
    # ------------------------------
    
    def get_indices(self):
        """
        Información del nombre del índice, el valor actual, el mayor y menor 
        valor del día y la variación porcentual.

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.

        """
        self.__endpoint_builder("TickerOnDemand/getIndices")
        return self.__handle_response()
    
    def get_resumen_accion(self, **query_params):
        """
        Información bursátil detallada de una acción en particular.

        Parameters
        ----------
        **query_params : dict, required.
            Nemo o identificador del instrumento.

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.

        """
        self.__endpoint_builder("TickerOnDemand/getResumenAccion")
        
        # Verificando los parametros del metodo
        for key, value in query_params.items():
            if key != 'Nemo':
                print('El parametro aceptado por el metodo es Nemo')
                return
            value = value.upper()
        
        return self.__handle_response(query_params)