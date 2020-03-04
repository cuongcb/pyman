from __future__ import print_function
from engine import Engine
from constants import http
import json

class Pyman(object):
    def __init__(self, engine):
        self.url = ""
        self.headers = {}
        self.body = {}
        self.engine = engine

    def setURL(self, url):
        self.url = url
        return self

    def withHeader(self, key, value):
        self.headers[key] = value
        return self

    def withBody(self, key, value):
        self.body[key] = value
        return self

    def GET(self):
        if self.check() == False:
            return

        self.execute(http.GET)

    def POST(self):
        if self.check() == False:
            return
        
        self.execute(http.POST)

    def PUT(self):
        if self.check() == False:
            return

        self.execute(http.PUT)

    def PATCH(self):
        if self.check() == False:
            return

        self.execute(http.PATCH)

    def DELETE(self):
        if self.check() == False:
            return

        self.execute(http.DELETE)

    def execute(self, method):
        self.engine.execute(self.url, self.headers, self.body, method)

    def check(self):
        if self.url == "":
            print("Fatal: invalid url", url)
            return False

        if self.engine == None:
            print("Fatal: no engine")
            return False

    # override print
    def __str__(self):
        return self.url + ", " + self.headers.__str__() + ", " + self.body.__str__()

env_file = "env.json"
test_file = "leetcode.json"

def prepare(p, path, prefix):
    with open(path + prefix + env_file) as json_file:
        env = json.load(json_file)
        for key in env:
            p.withHeader(key, env[key])

    with open(path + prefix + test_file) as json_file:
        headers = json.load(json_file)
        for key in headers:
            if key == "url":
                p.setURL(headers[key])
                continue
            p.withHeader(key, headers[key])

    return p

def main():
    e = Engine()
    p = Pyman(e)

    p = prepare(p, "./pyfood", "/leetcode/")

    p.GET()

if __name__ == "__main__":
    main()