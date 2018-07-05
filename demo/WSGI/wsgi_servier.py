from wsgiref.simple_server import make_server
from wsgi_app import application
PORT = 8080

httpd = make_server('', PORT, application)
print('Serving HTTP on port', PORT)
httpd.serve_forever()