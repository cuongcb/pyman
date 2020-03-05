from __future__ import print_function
import os
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
            print("Fatal: invalid url", self.url)
            return False

        if self.engine == None:
            print("Fatal: no engine")
            return False

    # override print
    def __str__(self):
        return self.url + ", " + self.headers.__str__() + ", " + self.body.__str__()

env_file = "env.json"
# test_file = "leetcode.json"

def exist(file):
    return os.path.exists(file)

def prepare(p, path, prefix, file):
    if exist(env_file):
        with open(path + prefix + env_file) as json_file:
            env = json.load(json_file)
            for key in env:
                p.withHeader(key, env[key])

    if exist(path + prefix + file):
        with open(path + prefix + file) as json_file:
            json_data = json.load(json_file)
            # url
            p.setURL(json_data["url"])
            # headers
            headers = json_data["headers"]
            for key in headers:
                p.withHeader(key, headers[key])
            # data
            data = json_data["data"]
            for key in data:
                p.withBody(key, data[key])
    return p

def main():
    e = Engine()
    p = Pyman(e)

    p = prepare(p, "./pyfood", "/gami/", "get_token.json")

    p.POST()

if __name__ == "__main__":
    main()