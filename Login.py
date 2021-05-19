import urllib.request

url = 'https://api.bcr.com.ar/v1.0/Login'

req = urllib.request.Request(url, None, {
    'Content-Type': 'application/json',
    'api_key': '<<<<<<<REPLACE_WITH_API_KEY>>>>>>>',
    'secret': '<<<<<<<REPLACE_WITH_SECRET>>>>>>>'
}, method="POST")
f = urllib.request.urlopen(req)
response = f.read()
print(response)
f.close()