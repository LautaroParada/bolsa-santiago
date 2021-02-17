# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:44:29 2021

@author: lauta
"""

import keyword
from typing import List, Dict, Any

from bolsa import modelos

class Definition(object):
    _swagger_name_to_python: Dict[str, str]
    _attribute_is_primitive: Dict[str, bool]
    _attributes_to_types: Dict[str, Any]
    
    def unmarshal_json(self, input_json):
        if isinstance(input_json, dict):
            self._unmarshal_json_object(input_json)
            return self
        elif isinstance(input_json, float) or isinstance(input_json, int):
            return input_json

    def _unmarshal_json_object(self, input_json):
        for key, value in input_json.items():
            if key in self._swagger_name_to_python:
                attribute_name = self._swagger_name_to_python[key]
                if not self._attribute_is_primitive[attribute_name]:
                    if attribute_name in self._attributes_to_types:
                        attribute_type = self._attributes_to_types[attribute_name]
                        if attribute_type in modelos.name_to_class:
                            model = modelos.name_to_class[attribute_type]()
                            value = model.unmarshal_json(input_json[key])
            else:
                attribute_name = key + ('_' if keyword.iskeyword(key) else '')

            self.__setattr__(attribute_name, value)
        return self
    
class IndicesRV(Definition):
    