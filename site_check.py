from http.client import HTTPConnection

connection = HTTPConnection("indicium.tech",port = 80, timeout = 10)
connection.request("HEAD","/")

response = connection.getresponse()
response.getheaders()
[('Date', 'Tue, 20 Sep 2022 18:10:37 GMT'), ('Content-Type', 'text/html'), ('Content-Length', '178'), 
 ('Connection', 'keep-alive'), ('Cache-Control', 'max-age=600'), ('Location', 'https://www.globo.com/')]

