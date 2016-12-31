#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask, request, make_response
import logging
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/callback')
def callback():
    code = request.args.get('code')
    logging.info(code) 
    return make_response('OK', 200)

@app.route('/privacy_policy')
def privacy_policy():
    code = request.args.get('code')
    logging.info(code) 
    return make_response('OK', 200)

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
