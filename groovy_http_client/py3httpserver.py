#!/Users/mtiapko/pyenv/py36/bin/python

from http.server import HTTPServer, BaseHTTPRequestHandler
import re
from io import BytesIO


PORT = 9000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if None != re.search('/api/add|sub|mult|div/[0-9]{1,5}/[0-9]{1,5}',self.path):
			num1 = float(self.path.split('/')[-1])
			num2 = float(self.path.split('/')[-2])
			op = str(self.path.split('/')[-3])
			print("operations is "+op)
			res="Unknown error"
			if op=="sub":
				res = str(num1-num2)
			elif op=="add":
				res = str(num1+num2)
			elif op=="mult":
				res = str(num1*num2)
			elif op=="div":
				res = str(num1*num2)
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			print("the result is"+res)
			self.wfile.write(res.encode())
		else:
			self.send_response(403)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write("403 error".encode())
		return

	def do_POST(self):
		try:
			content_length = int(self.headers['Content-Length'])
			body = self.rfile.read(content_length)
			self.send_response(200)
			self.end_headers()
			response  = BytesIO()
			bt = body.decode('utf-8')
			print(str(bt))
			a = int(bt[bt.index('a')+2:bt.index('&')])
			b = int(bt[bt.index('b')+2:bt.index("&op")])
			op = bt[bt.index("op")+3::1]
			if op=="0":
				answer = str(a-b)
			elif op=="1":
				answer = str(a+b)
			elif op=="2":
				answer = str(a*b)
			elif op=="3":
				answer = str(a/b)
			else:
				answer = "Choose the operation among +,-,* and /"
			response.write(answer.encode())
			self.wfile.write(response.getvalue())
		except:
			self.send_response(403)
			self.end_headers()
			response.write(b'Unknown error')
			self.wfile(response.getvalue())

httpd = HTTPServer(('',PORT),SimpleHTTPRequestHandler)

print("Server at port "+str(PORT))
httpd.serve_forever()
