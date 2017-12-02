
#simple app that returns a hash

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hash():
    u = str(random.randint(0, 10000000))
    return u

@app.route('/<name>')
def hello(name):
    return 'Hello {}'.format(name)

if __name__ == '__main__':
    app.run()