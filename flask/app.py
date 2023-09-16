from flask import Flask
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def hello():
    visits = redis_client.incr('visits')
    return f'Hello! You have visited this page {visits} times.'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
