import redis

import json


r = redis.Redis(
    host="127.0.0.1",
    port="6379"
)

with open("delimited.json", "r") as poem_file:
    poems = json.load(poem_file)

    for poem in poems:
        r.sadd("real_poems", poem)
