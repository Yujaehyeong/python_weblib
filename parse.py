from urllib.parse import urlparse

result = urlparse('http://www.python.org:80/guido/python.html;philosophy?overall=3#here')
# url을 파싱하여 쿼리스트링을 어떻게 dic에 담아낼까 ?를 생각
# 결과는 scheme='http', netloc='www.python.org:80', path='/guido/python.html', params='philosophy', query='overall=3', fragment='here'
print(result)