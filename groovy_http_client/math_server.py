#!/usr/bin/env python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class HandlerRequest(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        json_data = post_data.decode('utf-8')
        print(json_data)

        request_data = json.loads(json_data)
        operation = request_data.get("operation")
        arg1 = float(request_data.get("arg1"))
        arg2 = float(request_data.get("arg2"))

        value = 0
        if operation == "add":
            value = arg1 + arg2

        if operation == "sub":
            value = arg1 - arg2

        if operation == "mul":
            value = arg1 * arg2

        if operation == "div":
            value = arg1 / arg2

        self._set_response()
        json_data = json.dumps({"value": str(value)})
        print(json_data)

        self.wfile.write(json_data.encode())


def run(server_class=HTTPServer, handler_class=HandlerRequest, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    run()