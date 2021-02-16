# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:28:11 2021

@author: lauta
"""

import requests
import json

class RESTCliente(object):
    
    def __init__(self, token):
        self.token = token