import urllib.request

url = 'https://api.bcr.com.ar/v1.0/Contratos'

url += '?fechaConcertacionDesde=2019-01-01&fechaConcertacionHasta=2019-01-10'

req = urllib.request.Request(url, None, {
    'Content-Type': 'application/json',
    'token': '<<<<<<<REPLACE_WITH_TOKEN_FROM_LOGIN_ENDPOINT>>>>>>>'
}, method="GET")
f = urllib.request.urlopen(req)
response = f.read()
print(response)
f.close()