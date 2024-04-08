#!/usr/bin/env python

"""
	Simple HTTP Server in Python

	Mostly from Pre Written Code
"""

from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from os import environ

def main(port:int):
	"""
		HTTP Server
	"""
	with TCPServer(
		("", PORT), SimpleHTTPRequestHandler
	) as httpd:
		print(f"Serving on PORT: {PORT}")
		httpd.serve_forever()

if __name__ == '__main__':
	PORT = int(environ['PORT'])
	main(PORT)


