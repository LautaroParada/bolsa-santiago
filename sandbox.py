# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:59:33 2021

@author: lauta
"""

import os
import numpy as np

from bolsa.consultas import ConsultasAPI
from bolsa.negociacion import NegociacionAPI

#%% Request the data
api_key = os.environ['API_BS']

#%% Consulta
con_bs = ConsultasAPI(token=api_key)

resp = con_bs.get_instrumentos_validos()
print('Instrumentos validos')
print(resp)
print('-'*70)
resp = con_bs.get_request_usuario()
print('Request usuario')
print(resp)
print('-'*70)
resp = con_bs.get_indices_rv()
print('Indices de renta variable')
print(resp)
print('-'*70)
resp = con_bs.get_instrumentos_rv()
print('Instrumentos de renta variable')
print(resp)
print('-'*70)
resp = con_bs.get_puntas_rv()
print('Puntas de renta variable')
print(resp)
print('-'*70)
resp = con_bs.get_transacciones_rv()
print('Transacciones de renta variable')
print(resp)
print('-'*70)
resp = con_bs.get_indices()
print('Indices de la Bolsa de Santiago')
print(resp)
print('-'*70)
# Get random ticket from the available instruments
ticker = con_bs.get_instrumentos_validos()[np.random.choice([0,5])]['NEMO']
resp = con_bs.get_resumen_accion(Nemo=ticker)
print(f'Resumen de la accion de {ticker}')
print(resp)
print('-'*70)
resp = con_bs.get_variaciones_capital(Nemo=ticker, Fecha_Desde='2021020111000000', Fecha_Hasta='2021020411000000')
print(f'Variacion de capital para {ticker}')
print(resp)
print('-'*70)
print('\n')

#%% Negociacion
neg_bs = NegociacionAPI(token=api_key)

resp = neg_bs.get_instrumentos_validos()
# muestra aleatoria para el ingreso de ordenes
nemo_test = resp[np.random.randint(len(resp))]['NEMO']
nemo_precio = resp[np.random.randint(len(resp))]['PRECIO']
print('Instrumentos validos - NEGOCIACION API')
print(resp)
print('-'*70)
resp = neg_bs.get_request_usuario()
print('Request usuario - NEGOCIACION API')
print(resp)
print('-'*70)
resp = neg_bs.get_puntas_rv()
print('Puntas de negociacion para renta variable - NEGOCIACION API')
print(resp)
print('-'*70)
resp = neg_bs.get_transacciones_rv()
print('Transacciones - NEGOCIACION API')
print(resp)
print('-'*70)
resp = neg_bs.set_ingreso_oferta(nemo=nemo_test, cantidad=100, 
                                 precio=nemo_precio, tipo_operac='C', 
                                 condicion_liquidacion='CN')
print('Ingreso de orden')
print(resp)
print('-'*70)
resp = neg_bs.get_revision_ingreso(sec_orden=resp['SEC_ORDEN'])
print('Revision de ingreso de orden')
print(resp)
print('-'*70)