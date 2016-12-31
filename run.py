#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import os
from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/.well-known/acme-challenge/<post_id>')
def auth(post_id):
    if post_id == os.environ['LETSENCRYPT_REQUEST']:
        return os.environ['LETSENCRYPT_RESPONSE']

@app.route('/callback')
def callback():
    post_obj = json.loads(request.body)
    from_person = post_obj['result'][0]['content']['from']
    to_channel = os.environ['CHANNEL_ID']
    event_type = '138311608800106203'
    content = 'response'


    return 'OK'


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
#    context=('fullchain.pem', 'privkey.pem')
#    app.run(host='0.0.0.0', port=port, ssl_context=context)
