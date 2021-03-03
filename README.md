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

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut pharetra feugiat dui eget cursus. Aliquam eu ligula non tortor auctor scelerisque. Fusce nec tincidunt ligula. Pellentesque commodo tincidunt auctor. Donec vel tellus sed metus scelerisque dapibus vel at dolor. Phasellus eleifend at mauris vehicula egestas. Aenean id purus ut sem ultrices sodales sit amet bibendum tortor.

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

### Documentación servicios de consulta [:arrow_up:](#bolsa-de-santiago-startup-api)

La API de Servicios de Consulta posee varios endpoints disponibles para su uso. A continuación se explicara los metodos del cliente que estandarizan las solicitudes a la API.

1. **Client Market Data:** Un Market Data es una aplicación que mantiene en memoria el estado del mercado en tiempo real. Estos reciben información sobre estados de negociación, puntas, profundidad, resumen del mercado, entre otros, para posteriormente distribuirla al mercado. Todo este tipo de información se envía mediante protocolo FIX. Entre los metodos dispobles se encuentran: 

- ```get_indices_rv```: Valor de los principales índices de renta variable junto con su variación porcentual y volumen. 

	**Parametros:** Ninguno

```python
resp = con_bs.get_indices_rv()
print(f"Indices de renta variable\n {resp}")
```

- ```get_instrumentos_rv```: Detalle de los instrumentos disponibles para transar en el mercado de renta variable. Se muestra precio de apertura, mínimos y máximos y volumen transado, entre otros.
	
	**Parametros:** Ninguno.

```python
resp = con_bs.get_instrumentos_rv()
print(f"Instrumentos de renta variable\n {resp}")
```

- ```get_puntas_rv```: Mejores ofertas que se encuentran ingresadas en el mercado de renta variable. Se muestra precio de compra, precio de venta, cantidad, monto, condición de liquidación, entre otros.
	
	**Parametros:** Ninguno.

```python
resp = con_bs.get_puntas_rv()
print(f"Puntas de renta variable\n {resp}")
```

- ```get_transacciones_rv```: Detalle de las ultimas transacciones de los instrumentos disponibles en renta variable. Se muestra instrumento, condición de liquidación y cantidad, entre otros.

	**Parametros:** Ninguno.

```python
resp = con_bs.get_transacciones_rv()
print(f"Transacciones de renta variable\n {resp}")
````

2. **Instrumentos Disponibles**
- ```get_instrumentos_validos```: Este endpoint permite conocer cuales son los instrumentos del mercado de renta variable que estan disponibles para utilizar.

	**Parametros:** Ninguno.

```python
resp = con_bs.get_instrumentos_validos()
print(f"Instrumentos validos\n {resp}")
````

3. **Request Usuario**
- ```get_request_usuario```: Número de solcitudes disponibles a realizar y limite diario.

	**Parametros:** Ninguno.

```python
resp = con_bs.get_request_usuario()
print(f"Solicitudes del usuario\n {resp}")
```
4. **Ticker on Demand**
- ```get_indices```: Información sobre los indices que trazan la actividad comercial de la bolsa de stgo. Se muestra el nombre del índice, el valor actual, el mayor y menor valor del día y la variación porcentual.

	**Parametros:** Ninguno.

```python 
resp = con_bs.get_indices()
print(f"Indices de la Bolsa de Santiago\n {resp}")
```

- ```get_resumen_accion```: Información bursátil detallada de alguna instrumento/acción en particular.

	**Parametros:** *Obligatorios*
	- ```Nemo```(str): Nemotecnico o nombre del simbolo del instrumento a analizar.

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

- ```get_variaciones_capital```: Variación de capital asociada a un Nemotécnico/nombre del instrumento en particular. ***Este metodo esta en estado BETA, dado que el equipo que soporta la API tiene inconvenientes tecnicos para este endpoint***.

	**Parametros:** *Obligatorios*
	- ```Nemo```(str): Nemotecnico o nombre del simbolo del instrumento a analizar.
	- ```Fecha_Desde```(str): Inicio de la fecha para solicitar variación de capital. El formato es el siguiente YYYYmmDDhhMMss
	- ```Fecha_Hasta```(str): Fin de la fecha para solicitar variación de capital. El formato es el siguiente YYYYmmDDhhMMss

```python
resp = con_bs.get_variaciones_capital(Nemo=ticker, Fecha_Desde='2021020111000000', Fecha_Hasta='2021020411000000')
print(f"Variacion de capital para {ticker}\n {resp}")
```
## Demo Servicios de Negociación [:arrow_up:](#bolsa-de-santiago-startup-api)

Los endpoints de las APIs de ingreso de ofertas te permitirán el ingreso de ofertas mediante **DMA** y experimentar cómo se distribuyen los datos en el mercado de negociaciones de instrumentos financieros. A continuación un demo de su uso:

```python
import os
from bolsa.negociacion import NegociacionAPI

# cargar la api key desde las variables de entorno del sistma
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

### Documentación servicios de negociacion [:arrow_up:](#bolsa-de-santiago-startup-api)

1. **Instrumentos disponibles en ingreso de ofertas**
	
- ```get_instrumentos_validos```: Instrumentos de mercado de renta variable disponibles para realizar consultas desde la API.

	- **Parametros:** Ninguno

```python
resp = neg_bs.get_instrumentos_validos()
print(f"Instrumentos validos\n {resp}")
```

2. **Request Usuario**

- ```get_request_usuario```: Número de solcitudes utilizadas y disponibles a ocupar.

	- **Parametros:** Ninguno

```python
resp = neg_bs.get_request_usuario()
print(f"Request usuario\n {resp}")
```

3. **Cliente Market Data**: El Cliente Market Data Renta Variable es un producto creado por la Bolsa de Comercio de Santiago con el fin de transcribir los mensajes FIX enviados por el Market Data de Renta Variable a una base de datos.

*fuente: [Bolsa de Santiago](https://startup.bolsadesantiago.com/#/descripcion_negociacion)*

- ```get_puntas_rv```: Mejor oferta del libro de ordenes para cada instrumento (***compra mas cara, venta mas barata***). Estas ofertas fueron ingresada mediante el **sitema DMA**. Se muestan los precios de compra y venta, cantidad, monto, condición de liquidación, entre otros.

	- **Parametros:** Ninguno

```python
resp = neg_bs.get_puntas_rv()
print(f"Puntas de negociacion para renta variable\n {resp}")
```

- ```get_transacciones_rv```: Detalle de las transacciones de renta variable que el usuario ha realizado a traves del sistema DMA. Precio de compra, precio de venta, cantidad, monto, condición de liquidación, entre otros.

	- **Parametros:** Ninguno

```python
resp = neg_bs.get_transacciones_rv()
print(f"Transacciones del mercado\n {resp}")
```

4. **DMA (Direct Market Access):** Los servicios DMA - Direct Market Acces - permiten la canalización o ruteo automático de órdenes de compra y venta de acciones en tiempo real, al sistema SEBRA HT.

*fuente: [Bolsa de Santiago](https://startup.bolsadesantiago.com/#/descripcion_negociacion)*

- ```set_ingreso_oferta```: Ingreso de ofertas para algún instrumento seleccionado.

	- **Parametros:** *Obligatorios*
	   ```nemo```(str): codigo del nombre del instrumentos de renta variable.
       ```cantidad```(int): número de instrumentos a ofertar.
       ```precio```(int): precio a pagar o recibir por el instrumento.
       ```tipo_operac```(str): C de compra, V de venta.
       ```condicion_liquidacion```(str): Cuando se liquida la operación, las opciones disponbles son CN, PH o PM.

```python
import numpy as np

# Instrumentos validos o disponibles para el usuario
resp = neg_bs.get_instrumentos_validos()

# Muestra aleatoria para el ingreso de ordenes
nemo_test = resp[np.random.randint(len(resp))]['NEMO']
nemo_precio = resp[np.random.randint(len(resp))]['PRECIO']

# Ingreso de la orden
orden_ingresada = neg_bs.set_ingreso_oferta(nemo=nemo_test, cantidad=100, precio=nemo_precio, tipo_operac='C', condicion_liquidacion='CN')
print(f"Ingreso de la orden\n {resp}")
```

- ```get_revision_ingreso```: Revisión de los datos correspondientes al ingreso de ofertas a través del sistema DMA.

	- **Parametros:**
	```sec_orden```(int): número de la orden a revisar

```python
resp = neg_bs.get_revision_ingreso(sec_orden=orden_ingresada['SEC_ORDEN'])
print(f"Detalles de la orden ingresada:\n {resp}")
```

- ```get_revision_transaccion```: Revisión de los datos correspondientes a una transacción de una orden ingresada por el metodo ```set_ingreso_oferta```

	- **Parametros:** Ninguno

```python
resp = neg_bs.get_revision_transaccion()
print(f"Revision de las transacciones\n {resp}")
```

## Disclaimer [:arrow_up:](#bolsa-de-santiago-startup-api)

La información contenida en este documento es solo para fines informativos y educativos. Nada de lo contenido en este documento se podrá interpretar como asesoramiento financiero, legal o impositivo. El contenido de este documento corresponde únicamente a la opinión del autor, el cual no es un asesor financiero autorizado ni un asesor de inversiones registrado. El autor no está afiliado como promotor de los servicios de la Bolsa de Santiago.

Este documento no es una oferta para vender ni comprar instrumentos financieros. Nunca invierta más de lo que puede permitirse perder. Usted debe consultar a un asesor profesional registrado antes de realizar cualquier inversión.