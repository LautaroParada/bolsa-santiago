# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:44:58 2021

@author: lauta
"""

from typing import Type
from bolsa import modelos

def unmarshal_json(response_type, resp_json) -> Type[modelos.AnyDefinition]:
    obj = modelos.name_to_class[response_type]()
    obj.unmarshal_json(resp_json)
    return obj