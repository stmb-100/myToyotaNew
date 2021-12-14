#Funktioniert
import requests

files=[]
url='https://ssoms.toyota-europe.com/authenticate'
login_headers={'X-TME-BRAND':'TOYOTA','X-TME-LC':'de-de','Accept':'application/json,text/plain,*/*','Sec-Fetch-Dest':'empty'}


#, 'Content-Type': 'application/json'}

config_data={'username':'stefan.muehlbauer@smb-soft.de','password':'12stefan34'}

#r = requests.post('https://ssoms.toyota-europe.com/authenticate', headers=login_headers, data=config_data)

r=requests.request('POST',url,headers=login_headers,data=config_data,files=files)

print(r.status_code)
print(r)

#print(r.json())
#print(r.text)
