from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis-service', port=6379)

import flaskapp.routes
