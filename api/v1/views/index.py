#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def get_status():
    response = {'status': "OK"}
    return jsonify(response)
