# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:26:46 2021

@author: lauta
"""

import requests
import json
from typing import Dict
import logging

class NegociacionAPI(object):
    """    
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
        self.resp = None
        
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
            }

        self.params = {
            'access_token': self.token
            }
        
        self.query_params_names = ["in_ruteo",
                            "out_ruteo",
                            "procesado",
                            "sec_orden",
                            "rut_cli",
                            "nemo",
                            "cantidad",
                            "precio",
                            "tipo_operac",
                            "fec_ing_orden",
                            "ind_validez",
                            "fec_vcto_validez",
                            "can_asig_acum",
                            "estado",
                            "moneda",
                            "bolsa",
                            "condicion_liquidacion",
                            "sponsoring_firm",
                            "mercado",
                            "sub_mercado",
                            "prepago",
                            "tasa_maxima",
                            "tasa_propia",
                            "id_referencia",
                            "fecha_vencimiento",
                            "divisible",
                            "od",
                            "sec_orden_od_compra",
                            "sec_orden_od_venta",
                            "op_interno",
                            "sec_orden_2",
                            "id_cliente"
                            ]
        
        self.order_model_json = {
                  "in_ruteo": "string",
                  "out_ruteo": "",
                  "procesado": "N",
                  "sec_orden": 0,
                  "rut_cli": "string",
                  "nemo": "string",
                  "cantidad": 0,
                  "precio": 0,
                  "tipo_operac": "string",
                  "fec_ing_orden": "string",
                  "ind_validez": "D",
                  "fec_vcto_validez": "string",
                  "can_asig_acum": 0,
                  "estado": "VT",
                  "moneda": "CLP",
                  "bolsa": "XSGO",
                  "condicion_liquidacion": "CN",
                  "sponsoring_firm": "",
                  "mercado": "AC",
                  "sub_mercado": "string",
                  "prepago": "",
                  "tasa_maxima": 1,
                  "tasa_propia": 1,
                  "id_referencia": "",
                  "fecha_vencimiento": "string",
                  "divisible": "",
                  "od": "N",
                  "sec_orden_od_compra": 0,
                  "sec_orden_od_venta": 0,
                  "op_interno": "001",
                  "sec_orden_2": "001",
                  "id_cliente": ""
                }
        self.name_error = False
    # ------------------------------
    # Metodos para eliminar la redundancia en el cliente
    # ------------------------------
        
    def __handle_response(self, query_params: Dict[str, str]={}):
        """
        Este método manipula de manera centralizada las solicitudes a la API.

        Parameters
        ----------
        query_params : Dict[str, str], opcional
            DESCRIPTION. El valor por defecto es {}.

        Returns
        -------
        list or dict
            Lista o Dictionario con los datos de la consulta o un mensaje de 
            error.

        """
        
        self.resp = requests.post(self.endpoint_pivot, params=self.params, headers=self.headers, json=query_params, timeout=self.timeout)
            
        if self.resp.status_code == 200:
             if 'listaResult' in self.resp.json().keys():
                 return self.resp.json()['listaResult']
             else:
                 return self.resp.json()
        else:
            self.resp.raise_for_status()
            
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
        
    def __param_checker(self, items_):
        """
        Metodo para validar los argumentos de los metodos de la clase

        Parameters
        ----------
        items_ : dict

        Returns
        -------
        None.

        """
        for key, value in items_:
            if key not in self.query_params_names:
                logging.error(f"El parametro {key} no es valido")
                self.name_error = True
                
    def __curl_checker(self, params_: dict):
        """
        Metodo para validar el ingreso de ordenes. El body del request necesita
        el modelo completo para ingresar la oferta.

        Parameters
        ----------
        params_ : dict
            parametros minimos para ingresar la orden.

        Returns
        -------
        None.

        """
        for key, value in params_.items():
            if key in self.order_model_json.keys():
                self.order_model_json[key] = value
        
    # ------------------------------
    # Instrumentos disponibles en ingreso de ofertas
    # ------------------------------
    
    def get_instrumentos_validos(self):
        """
        Instrumentos del mercado de renta variable que disponibles en la API

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.
            
        """
        self.__endpoint_builder('InstrumentosDisponibles/getInstrumentosValidos')
        return self.__handle_response()
    
    # ------------------------------
    # Request Usuario
    # ------------------------------
    
    def get_request_usuario(self):
        """
        Número de solcitudes ocupadas y disponibles a ocupar.

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
        """
        Ofertas de todos los instrumentos a los cuales se les han ingresado 
        ordenes mediante el DMA. Se muestan los precios de compra y venta, 
        cantidad, monto, condición de liquidación, entre otros.

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.

        """
        self.__endpoint_builder('ClienteMD/getPuntasRV')
        return self.__handle_response()
    
    def get_transacciones_rv(self):
        """
        Detalle de las transacciones de renta variable que el usuario haya 
        realizado a traves del DMA. Precio de compra, precio de venta, 
        cantidad, monto, condición de liquidación, entre otros.

        Returns
        -------
        list
            Lista donde cada elemento es un diccionario.

        """
        self.__endpoint_builder('ClienteMD/getTransaccionesRV')
        return self.__handle_response()
    
    # ------------------------------
    # DMA
    # ------------------------------
    def get_revision_ingreso(self, **query_params):
        """
        Revisión de los datos correspondientes al ingreso de ofertas a través
        del sistema DMA.

        Parameters
        ----------
        **query_params : sec_orden
            número de la orden a revisar (int)

        Returns
        -------
        dict
            Detalles de la orden ingresada.

        """
        self.__endpoint_builder("DMA/getRevisionIngreso")
        self.__param_checker(items_=query_params.items())
        
        if self.name_error:
            self.name_error = False
            return
        
        return self.__handle_response(query_params=query_params)
    
    def get_revision_transaccion(self):
        """
        Revisión de los datos correspondientes a una transacción de una orden
        ingresada por el metodo set_ingreso_oferta

        Returns
        -------
        dict
            detalles de la transaccion ingresada.

        """
        self.__endpoint_builder('DMA/getRevisionTransaccion')        
        return self.__handle_response()
    
    def set_ingreso_oferta(self, **query_params):
        """
        Ingreso de ofertas para algún instrumento seleccionado.

        Parameters
        ----------
        **query_params : multiples argumentos, todos obligatorios.
            nemo(str): codigo del nombre del instrumentos de renta variable.
            cantidad(int): número de instrumentos a ofertar.
            precio(int): precio a pagar o recibir por el instrumento.
            tipo_operac(str): C de compra, V de venta.
            condicion_liquidacion(str): Cuando se liquida la operación.

        Returns
        -------
        dict
            .

        """
        self.__endpoint_builder('DMA/setIngresoOferta')
        self.__param_checker(items_=query_params.items())
        
        if self.name_error:
            self.name_error = False
            return
        
        self.__curl_checker(params_=query_params)
        
        return self.__handle_response(query_params=self.order_model_json)