#!/usr/bin/python3
from flask import jsonify
from api.v1.views import app_views
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def api_status():
    cvb = {'status': "OK"}
    return jsonify(cvb)

@app_views.route('/stats', methods=['GET'])
def get_stats():
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)