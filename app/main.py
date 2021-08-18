from flask import Flask, request, render_template, abort, Response
import os
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/healthz')
def healthz():
    resp = Response("OK", status=200)
    return resp

@app.route('/crashme')
def crash_me():
    if os.environ.get('CAN_CRASH') == "True":
        os._exit(0)
    else:
        resp = Response("Can't crash!", status=200)
        return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)