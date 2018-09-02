#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):

  #handle GET command
  def do_GET(self):
        f = open("timing.txt") #open requested file
        #send code 200 response
        self.send_response(200)
        #send header first
        self.send_header('Content-type','text-html')
        self.end_headers()
        #send file content to client
        self.wfile.write(f.read().encode())
        f.close()
        return

def run():
  print('http server is starting...')

  #ip and port of servr
  #by default http server port is 80
  server_address = ('localhost', 3001)
  httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
  print('http server is running...')
  httpd.serve_forever()

if __name__ == '__main__':
  run()
