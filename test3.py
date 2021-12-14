import requests

url = "https://ssoms.toyota-europe.com/authenticate"

payload={'username':'stefan.muehlbauer@smb-soft.de',
'password':'12stefan34',
'vin':'SB1K53BE60E030440'}
files=[

]
headers = {
  'X-TME-BRAND': 'TOYOTA',
  'X-TME-LC': 'de-de',
  'Accept': 'application/json, text/plain, */*',
  'Sec-Fetch-Dest': 'empty',
  'region': '\'europe\''
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response)
