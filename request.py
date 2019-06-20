from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
httpresponse = urlopen('http://www.naver.com')
body = httpresponse.read()
print(body)

# POST
data = {
    'email' : 'cafe24@cafe24.com',
    'password' : '1234',
    'name' : '유재형'
}

# 반복문을 통해 계속 요청을 보내는것을 막기위해서는 csrf를 사용해야한다.

data =urlencode(data).encode('utf-8') # 기본적으로 utf-8이지만 형식의 경우는 바꿔야함

request = Request('http://www.example.com', data)
request.add_header('Content-Type', 'text/html')


httpresponse = urlopen(request)
print(httpresponse.read())