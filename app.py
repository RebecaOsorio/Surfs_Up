from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/route1')
def route1():
    return 'This will be the first route'

app.run()