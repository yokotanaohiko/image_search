#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/callback')
def callback():
    return 'Hello World'

@app.route('/privacy_policy')
def privacy_policy():
    return 'Hello World'

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
