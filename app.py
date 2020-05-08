from flask import request
from init import init_app
from models.user import User
import logging
import json
import redis
#
logging.basicConfig(
    format='%(levelname)-8s %(asctime)s,%(msecs)d  [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO
    )
#
log = logging.getLogger(__name__)
app = init_app()
#
redis_client = redis.Redis(port=6379)
#
#
@app.route('/')
def welcome():
    log.info('hello world')
    return "Welcome to cache 101"


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    phone_number = data.get('phone_number')
    redis_client.hmset(email, data)
    user = User(
        name=name,
        email=email,
        phone_number=phone_number
    )

    User.create_user(user)
    return json.dumps({'message': 'user created successfully'})


@app.route('/user-no-cache', methods=['POST'])
def create_user_no_cache():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    phone_number = data.get('phone_number')
    user = User(
        name=name,
        email=email,
        phone_number=phone_number
    )

    User.create_user(user)
    return json.dumps({'message': 'user created successfully'})


@app.route('/get-user', methods=['POST'])
def get_user():
    data = request.get_json()
    user = redis_client.hgetall(data.get('email'))
    if user:
        log.info("Cache hit ...!!!!!")
        user = {key.decode(): val.decode() for key, val in user.items()}

    else:
        log.info("cache miss ....!!!!!")
        user = User.get_user_by_email(data.get('email'))
        log.info("cache write around ....!!!!!")

    return json.dumps({"message": user})


if __name__ == '__main__':
    app.run(debug=True)
