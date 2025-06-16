# -*- coding: utf-8 -*-
"""
Created on Wed May 17 05:43:11 2023

@author: EDUARDO
"""

import requests
import json

URL="https://www.xxxxxxxxxxx.mx/ApiRest/Apixxxxx/v2/xxxxxxxxxx/get_Proveedores"
#params={'0':{'strAccion':['1']}, 'body':'hihi', 'userId':1}
payload={
0: {'strAccion' : ['1']},
1: {'strUsuario' : ['xxxxxxxxxx']},
2: {'strSucursal' : ['']},
3: {'strPeriodo' : ['5']},
4: {'strEjercicio' : ['2013']},
5: {'strID' : ['']},
6: {'strCoordinador' : ['']},
7: {'strConexion': ['connection']}
}
headers={'Content-Type': 'application/json; charset=utf-8'}

req = requests.post(URL,data=json.dumps(payload), headers=headers)
print(req.status_code)
print(req.content)
print(req.json())
print(req.headers)
print(req.reason)
print(payload)
if req.status_code == 200:
    print(req.content)
