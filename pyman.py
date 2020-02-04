from __future__ import print_function

class Pyman(object):
    def __init__(self):
        self.headers = {}
        self.body = {}
        self.engine = None
    
    def withHeader(self, key, value):
        self.headers[key] = value
        return self

    def withBody(self, key, value):
        self.body[key] = value
        return self

    def execute(self):
        if self.engine == None:
            print("Fatal: no engine")
            return

        self.engine.execute(self.headers, self.body)

    # override print
    def __str__(self):
        return self.headers.__str__() + ", " + self.body.__str__()

def main():
    p = Pyman()
    p.withHeader("this", "header")\
        .withHeader("this second", "header")\
        .withBody("this", "body")
    p.execute()
    print(p)

if __name__ == "__main__":
    main()