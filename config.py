import os
from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "19134188"))
    API_HASH = environ.get("API_HASH", "91587601a5d898e3341b7e4a9e1c2537")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6926411212:AAFwrdOOSXRkcA0DrwgcBG04E8t4d_eZedg") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DB_URI", "mongodb+srv://wojomo9537:RnVK9WPw4wNXpXkR@cluster0.4nars0z.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = environ.get("BOT_OWNER", "1802523258")

BOT_OWNER = int(environ.get("BOT_OWNER", "1802523258"))

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
