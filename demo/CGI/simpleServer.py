from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 8080
httphand = CGIHTTPRequestHandler

httpd = HTTPServer(('', PORT), httphand)
print('start server at port', PORT)
httpd.serve_forever()