from __future__ import print_function
import subprocess
import os

class Engine(object):
    def __init__(self):
        pass

    def execute(self, url, headers, body, method):
        header = self.buildHeaders(headers)
        data = self.buildData(body)
        
        request = " -X " + method + " " + header + " " + data

        print("curl" + request + url)

        os.system("curl " + request + url)

    def buildHeaders(self, headers):
        header = ""
        for key in headers:
            h = '"' + key + ': ' + headers[key] + '"'
            header = header + "-H "
            header = header + h
            header = header + " "
        
        return header

    def buildData(self, body):
        data = ""
        for key in body:
            b = '"' + key + '=' + body[key] + '"'
            data = data + "-d "
            data = data + b
            data = data + " "
        
        return data
