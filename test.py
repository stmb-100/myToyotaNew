import requests

url='https://ssoms.toyota-europe.com/authenticate/'

payload={'username':'stefan.muehlbauer@smb-soft.de','password':'12stefan34'} 
# , 'vin': 'yyyyy', 'timezone': 'Europe/Berlin'\r\n}"

headers={
  'X-TME-BRAND':'TOYOTA',
  'X-TME-LC':'de-de',
  'Accept':'application/json,text/plain,*/*',
  'Sec-Fetch-Dest':'empty'
}

response = requests.post(url, headers=headers, data=payload)

print(response.status_code)
print(response)


