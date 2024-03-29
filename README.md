# Bolsa de Santiago startup API
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://shields.io/) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)

**Contenidos**

1. [Descripcion general](#descripcion-general-arrow_up)
2. [Instalación y requisitos](#instalación-y-requisitos-arrow_up)
3. [Demo Servicios de Consulta](#demo-servicios-de-consulta-arrow_up)
    - [Documentación servicios de consulta](#documentación-servicios-de-consulta-arrow_up)
4. [Demo Servicios de Negociación](#demo-servicios-de-negociación-arrow_up)
	- [Documentación servicios de negociacion](#documentación-servicios-de-negociacion-arrow_up)
5. [Disclaimer](#disclaimer-arrow_up)

## Descripcion general [:arrow_up:](#bolsa-de-santiago-startup-api)
 
Cliente de la [API](https://startup.bolsadesantiago.com/#/) de la bolsa de Santiago. Este cliente estandariza la llamada de datos de la API mediante un SDK desarrollado en Python :snake:.

## Instalación y requisitos [:arrow_up:](#bolsa-de-santiago-startup-api)

#### Requisitos
- Se debe solicitar una api key con el equipo que mantiene la API. Para aquello deben ir al siguiente [link](https://startup.bolsadesantiago.com/#/)
- ```Python``` >= 3.8

#### Instalación
```python
pip install bolsa-stgo
```

## Demo Servicios de Consulta [:arrow_up:](#bolsa-de-santiago-startup-api)

Los endpoints de las APIs de información de mercado te permitirán simular el uso del de datos de mercado de instrumentos de renta variable, a través del consumo de un **web-service**. A continuación un demo de su uso:

```python
import os
from bolsa.consultas import ConsultasAPI # Cliente de la API Servicios de Consulta

# cargar la api key desde las variables de entorno del sistma
api_key = os.environ['API_BS']

# Creación de la instancia que manipulara las solicitudes a la API
con_bs = ConsultasAPI(token=api_key)

# Instrumentos validos o disponibles para el usuario
resp = con_bs.get_instrumentos_validos()
print('Instrumentos validos')
print(resp)
print('-'*70)

# Número de solicitudes utilizadas y disponibles para el usuario
resp = con_bs.get_request_usuario()
print('Request usuario')
print(resp)
print('-'*70)
```

*tutorial sobre como guardar y cargar variables de entorno en Python -> [Hiding Passwords and Secret Keys in Environment Variables (Windows)](https://youtu.be/IolxqkL7cD8)*

### Documentación servicios de consulta [:arrow_up:](#bolsa-de-santiago-startup-api)

La API de Servicios de Consulta posee varios endpoints disponibles para su uso. A continuación se explicaran los métodos del cliente que estandarizan las solicitudes a la API.

1. **Client Market Data:** UUn Market Data es una aplicación que mantiene en memoria el estado del mercado en tiempo real. Se recibe información sobre estados de negociación, puntas de cotización, profundidad del libro de órdenes, resumen o snapshot del mercado, entre otros. Todo esta información se envía mediante protocolo **FIX**. Los métodos disponibles para realizar consultas son:

- ```get_indices_rv```: Valor de los principales índices de renta variable junto con su variación porcentual y volumen. 

	**Parámetros:** Ninguno

```python
resp = con_bs.get_indices_rv()
print(f"Indices de renta variable\n {resp}")
```

- ```get_instrumentos_rv```: Detalle de los instrumentos disponibles para transar en el mercado de renta variable. Se muestra el precio de apertura, mínimos y máximos y volumen transado, entre otros.
	
	**Parámetros:** Ninguno.

```python
resp = con_bs.get_instrumentos_rv()
print(f"Instrumentos de renta variable\n {resp}")
```

- ```get_puntas_rv```: Mejores ofertas que se encuentran ingresadas en el mercado de renta variable (compra más cara y venta barata). Se muestra precio de compra, precio de venta, cantidad, monto, condición de liquidación, entre otros.
	
	**Parámetros:** Ninguno.

```python
resp = con_bs.get_puntas_rv()
print(f"Puntas de renta variable\n {resp}")
```

- ```get_transacciones_rv```: Detalle de las ultimas transacciones de los instrumentos disponibles en renta variable. Se muestra instrumento, condición de liquidación y cantidad, entre otros.

	**Parámetros:** Ninguno.

```python
resp = con_bs.get_transacciones_rv()
print(f"Transacciones de renta variable\n {resp}")
````

2. **Instrumentos Disponibles**
- ```get_instrumentos_validos```: Permite conocer cuales son los instrumentos del mercado de renta variable que estan disponibles para utilizar.

	**Parámetros:** Ninguno.

```python
resp = con_bs.get_instrumentos_validos()
print(f"Instrumentos validos\n {resp}")
````

3. **Request Usuario**
- ```get_request_usuario```: Número de solcitudes disponibles a realizar y limite diario.

	**Parámetros:** Ninguno.

```python
resp = con_bs.get_request_usuario()
print(f"Solicitudes del usuario\n {resp}")
```
4. **Ticker on Demand**
- ```get_indices```: Información sobre los índices que trazan la actividad comercial de la Bolsa de Santiago. Se muestra el nombre del índice, el valor actual, el mayor y menor valor del día y la variación porcentual.

	**Parámetros:** Ninguno.

```python 
resp = con_bs.get_indices()
print(f"Indices de la Bolsa de Santiago\n {resp}")
```

- ```get_resumen_accion```: Información bursátil detallada de alguna instrumento/acción en particular.

	**Parámetros:** *Obligatorios*
	- ```Nemo```(str): **Requerido** - Nemotécnico o nombre del símbolo del instrumento a analizar.

```python
import numpy as np

# Solicitar los nombres de instrumentos disponibles 
resp = con_bs.get_instrumentos_validos()
# seleccionar alguno al azar
ticker = con_bs.get_instrumentos_validos()[np.random.randint(len(resp))]['NEMO']
# solicitar el resumen del instrumento.
resp = con_bs.get_resumen_accion(Nemo=ticker)
print(f'Resumen de la accion de {ticker}\n {resp}')
```

- ```get_variaciones_capital```: Variación de capital asociada a un Nemotécnico/nombre del instrumento en particular. ***Este método está en estado BETA, dado que el equipo que soporta la API tiene inconvenientes técnicos para este endpoint.***

	**Parámetros:** *Obligatorios*
	- ```Nemo```(str): **Requerido** - Nemotecnico o nombre del simbolo del instrumento a analizar.
	- ```Fecha_Desde```(str): **Requerido** - Inicio de la fecha para solicitar variación de capital. El formato es el siguiente YYYYmmDDhhMMss
	- ```Fecha_Hasta```(str): **Requerido** - Fin de la fecha para solicitar variación de capital. El formato es el siguiente YYYYmmDDhhMMss

```python
resp = con_bs.get_variaciones_capital(Nemo=ticker, Fecha_Desde='2021020111000000', Fecha_Hasta='2021020411000000')
print(f"Variacion de capital para {ticker}\n {resp}")
```
## Demo Servicios de Negociación [:arrow_up:](#bolsa-de-santiago-startup-api)

Los endpoints de las APIs de ingreso de ofertas te permitirán el ingresar ofertas mediante el sistema **DMA** y experimentar cómo se distribuyen los datos en el mercado de negociaciones de instrumentos financieros. A continuación un demo de su uso:

```python
import os
from bolsa.negociacion import NegociacionAPI

# Cargar la api key desde las variables de entorno del sistma
api_key = os.environ['API_BS']

# Creación de la instancia que manipulara las solicitudes a la API
neg_bs = NegociacionAPI(token=api_key)

# Instrumentos validos o disponibles para el usuario
resp = neg_bs.get_instrumentos_validos()
print('Instrumentos validos - NEGOCIACION API')
print(resp)
print('-'*70)

# Número de solicitudes utilizadas y disponibles para el usuario
resp = neg_bs.get_request_usuario()
print('Request usuario - NEGOCIACION API')
print(resp)
print('-'*70)
```

*tutorial sobre como guardar y cargar variables de entorno en Python -> [Hiding Passwords and Secret Keys in Environment Variables (Windows)](https://youtu.be/IolxqkL7cD8)*

### Documentación servicios de negociacion [:arrow_up:](#bolsa-de-santiago-startup-api)

1. **Instrumentos disponibles en ingreso de ofertas**
	
- ```get_instrumentos_validos```: Instrumentos de mercado de renta variable disponibles para ingresar ordenes.

	- **Parámetros:** Ninguno

```python
resp = neg_bs.get_instrumentos_validos()
print(f"Instrumentos validos\n {resp}")
```

2. **Request Usuario**

- ```get_request_usuario```: Número de solcitudes utilizadas y disponibles a ocupar.

	- **Parámetros:** Ninguno

```python
resp = neg_bs.get_request_usuario()
print(f"Request usuario\n {resp}")
```

3. **Cliente Market Data**: El Market Data Renta Variable es un producto creado por la Bolsa de Comercio de Santiago con el fin de transcribir los mensajes FIX enviados por el Market Data de Renta Variable a una base de datos.

*fuente: [Bolsa de Santiago](https://startup.bolsadesantiago.com/#/descripcion_negociacion)*

- ```get_puntas_rv```: Mejor oferta del libro de órdenes para cada instrumento (***compra más cara, venta más barata***). Estas ofertas fueron ingresada mediante el **sistema DMA**. Se muestran los precios de compra y venta, cantidad, monto, condición de liquidación, entre otros.

	- **Parámetros:** Ninguno

```python
resp = neg_bs.get_puntas_rv()
print(f"Puntas de negociacion para renta variable\n {resp}")
```

- ```get_transacciones_rv```: Detalle de las transacciones de renta variable que el usuario ha realizado a través del sistema DMA. Precio de compra, precio de venta, cantidad, monto, condición de liquidación, entre otros.

	- **Parámetros:** Ninguno

```python
resp = neg_bs.get_transacciones_rv()
print(f"Transacciones del mercado\n {resp}")
```

4. **DMA (Direct Market Access):** Los servicios **DMA** - Direct Market Access - permiten la canalización o ruteo automático de órdenes de compra y venta de acciones en tiempo real, al sistema **SEBRA HT**.

*fuente: [Bolsa de Santiago](https://startup.bolsadesantiago.com/#/descripcion_negociacion)*

- ```set_ingreso_oferta```: Ingreso de ofertas para algún instrumento seleccionado.

	- **Parámetros:** *Obligatorios*
	   - ```nemo```(str): Código  del nombre del instrumentos de renta variable.
       - ```cantidad```(int): Número de instrumentos a ofertar.
       - ```precio```(int): Precio a pagar o recibir por el instrumento.
       - ```tipo_operac```(str): C de compra, V de venta.
       - ```condicion_liquidacion```(str): Cuando se liquida la operación, las opciones disponibles son CN, PH o PM.

```python
import numpy as np

# Instrumentos validos o disponibles para el usuario
resp = neg_bs.get_instrumentos_validos()

# Muestra aleatoria para el ingreso de ordenes
# Elegir aleatoriamente una accion y su ultimo precio de transaccion para
# ingresar una orden
random_ticker = np.random.randint(len(resp))
nemo_test = resp[random_ticker]['NEMO']
nemo_precio = resp[random_ticker]['PRECIO']

# Ingreso de una orden de venta a precio mercado de un tamaño de 100 acciones
orden_ingresada = neg_bs.set_ingreso_oferta(nemo=nemo_test, 
                                            cantidad=100, 
                                            precio=nemo_precio, 
                                            tipo_operac='V', 
                                            condicion_liquidacion='PM')
print(f"Ingreso de la orden\n {orden_ingresada}")
```

- ```get_revision_ingreso```: Revisión de los datos correspondientes al ingreso de ofertas a través del sistema DMA.

	- **Parámetros:**
		- ```sec_orden```(int): **Requerido** - número de la orden a revisar

```python
resp = neg_bs.get_revision_ingreso(sec_orden=orden_ingresada['SEC_ORDEN'])
print(f"Detalles de la orden ingresada:\n {resp}")
```

- ```get_revision_transaccion```: Revisión de los datos correspondientes a una transacción de una orden ingresada por el método ```set_ingreso_oferta```

	- **Parámetros:** Ninguno

```python
resp = neg_bs.get_revision_transaccion()
print(f"Revision de las transacciones\n {resp}")
```

## Disclaimer [:arrow_up:](#bolsa-de-santiago-startup-api)

La información contenida en este documento es solo para fines informativos y educativos. Nada de lo contenido en este documento se podrá interpretar como asesoramiento financiero, legal o impositivo. El contenido de este documento corresponde únicamente a la opinión del autor, el cual no es un asesor financiero autorizado ni un asesor de inversiones registrado. El autor no está afiliado como promotor de los servicios de la Bolsa de Santiago.

Este documento no es una oferta para vender ni comprar instrumentos financieros. Nunca invierta más de lo que puede permitirse perder. Usted debe consultar a un asesor profesional registrado antes de realizar cualquier inversión.
