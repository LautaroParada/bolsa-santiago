# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:59:33 2021

@author: lauta
"""

import os
from bolsa import RESTCliente

import json
import requests

#%% Request the data
api_key = os.environ['API_BS']

bs = RESTCliente(token=api_key)
r = bs.id_instrumentos_validos()

#%% Instrumentos Disponibles












# host = 'https://startup.bolsadesantiago.com/api/consulta/'

# headers = {
#     'Content-Type': 'application/json',
#     'Accept': 'application/json'
#     }

# params = {
#     'access_token': api_key
#     }

# def info_request(resp):
#     resp_ = resp.json()
#     print(json.dumps(resp_, indent=4))
#     print(resp.headers)
#     print(f"Status of the request {resp.status_code}")
#     print('-'*50)

# #%% Instrumentos Disponibles
# r = requests.post(host+'InstrumentosDisponibles/getInstrumentosValidos', params=params, headers=headers)
# info_request(r)

# #%% Request Usuario

# r = requests.post(host + 'RequestUsuario/getRequestUsuario', params=params, headers=headers)
# info_request(r)

# #%% Ticker on Demand - PROBLEMA CON EL NEMO

# # Indices
# r = requests.post(host + 'TickerOnDemand/getIndices', params=params, headers=headers)

# info_request(r)

# # Resumen de accion
# payload = {
#     "nemo": "CCU"
#     }
# r = requests.post(host + 'TickerOnDemand/getResumenAccion', data=payload, params=params, headers=headers)

# info_request(r)

# # Variaciones de Capital


# #%% Cliente Market Data

# # Indices
# r = requests.post(host + 'ClienteMD/getIndicesRV', params=params, headers=headers)
# info_request(r)

# # Instrumentos
# r = requests.post(host + 'ClienteMD/getInstrumentosRV', params=params, headers=headers)
# info_request(r)

# # Puntas de RV
# r = requests.post(host + 'ClienteMD/getPuntasRV', params=params, headers=headers)
# info_request(r)

# # Transacciones
# r = requests.post(host + 'ClienteMD/getTransaccionesRV', params=params, headers=headers)
# info_request(r)