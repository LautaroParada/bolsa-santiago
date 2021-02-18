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

#%% Negociacion
neg_bs = NegociacionAPI(token=api_key)