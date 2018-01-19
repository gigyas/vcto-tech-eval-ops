from flask import Flask
from flask_env import MetaFlaskEnv
from redis import Redis

class Configuration(metaclass=MetaFlaskEnv):
    ENV_PREFIX='COUNTME_'
    REDIS_SERVER='127.0.0.1'
    REDIS_PORT=6379

app = Flask(__name__)
app.config.from_object(Configuration)
redis = Redis(host=app.config['REDIS_SERVER'], port=app.config['REDIS_PORT'])

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    