from __future__ import print_function
import subprocess
import os
import json

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
        data = '-d '
        data = data + '"'
        data = data + json.dumps(body).strip()
        data = data + '" '
        
        return data
