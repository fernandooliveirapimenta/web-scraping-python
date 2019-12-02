from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

url = 'http://www.alura.com.br'
headers = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
try:
    req = Request(url,headers=headers)
    response = urlopen(req)
    print(response.read())
except HTTPError as e:
    print(e.status, e.reason)
except URLError as e:
    print(e.reason)