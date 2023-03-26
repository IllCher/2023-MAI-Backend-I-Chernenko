from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = b''
    for i in range(10000):
        response_body += b'Hello, World!'
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()

