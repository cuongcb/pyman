from __future__ import print_function
import subprocess
import os

class Engine(object):
    def __init__(self):
        pass

    def execute(self, url, headers, body, method):
        print("here")
        header = ""
        for key in headers:
            h = '"' + key + ': ' + headers[key] + '"'
            header = header + "-H "
            header = header + h
            header = header + " "
        
        data = ""
        for key in body:
            b = '"' + key + ': ' + body[key] + '"'
            data = data + "-d "
            data = data + b
            data = data + " "

        request = "-X " + method + " -i " + header + " " + data

        print("curl" + request + url)

        os.system("curl " + request + url)
