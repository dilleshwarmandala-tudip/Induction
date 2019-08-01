import requests

import json

import sys

API_ENDPOINT = "https://api.getpostman.com/monitors/1e9a492c-fffd-4060-9799-4ea050afef76/run?apikey=cef757d96bbe4a36871d2d4a40a0fdf6"

PARAMS = {}

response = requests.post(API_ENDPOINT)

postResult = json.loads(response.text)
if 'error' in postResult:
   result = requests.get("https://api.getpostman.com/monitors/1e9a492c-fffd-4060-9799-4ea050afef76?apikey=cef757d96bbe4a36871d2d4a40a0fdf6")
   getResult = json.loads(result.text)
   if getResult['monitor']['lastRun']['status'] == 'error' or getResult['monitor']['lastRun']['status'] == 'failed':
      print("Number of test cases failed: ", getResult['monitor']['lastRun']['stats'])
      sys.exit(-1)
   else:
      print("Result: ", getResult['monitor']['lastRun']['stats'])
      print("done!")
else:
   if postResult['run']['info']['status'] == 'error' or postResult['run']['info']['status'] == 'failed':
      print("Number of test cases failed: ", postResult['run']['stats'])
      sys.exit(-1)
   else:
      print("Number of test cases failed: ", postResult['run']['stats'])
      print("done!")