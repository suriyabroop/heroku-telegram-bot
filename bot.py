# -*- coding: utf-8 -*-
import redis
import os
import telebot
# import some_api_lib
# import ...

# Example of your code beginning
#           Config vars
token = os.environ['5239292055:AAEmXmBmnRtlEi8KmCkC9naRH1Zny2Oz9fg']
some_api_token = os.environ['5239292055:AAEmXmBmnRtlEi8KmCkC9naRH1Zny2Oz9fg']
#             ...

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...
