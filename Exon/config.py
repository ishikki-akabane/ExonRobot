"""
MIT License

Copyright (c) 2022 ABISHNOI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

import json
import os


def get_user_list(config, key):
    with open("{}/Exon/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "13600724"
    API_HASH = "ee59fd28d0d065c6b7d105082c6a0ba0"
    APP_ID = "13600724"  # 2nd API_ID
    APP_HASH = "ee59fd28d0d065c6b7d105082c6a0ba0"  # 2ns API_HASH
    ARQ_API_KEY = "TENRCY-KDKSK-MSMSM-OXQYYO-ARQ"
    BOT_ID = "5408158735"
    TOKEN = "5458182410:KINGABISHNOI-UM"
    OWNER_ID = "5673766027" 
    OPENWEATHERMAP_ID = "22322"
    OWNER_USERNAME = "SHURYANSH"
    BOT_USERNAME = "ShizukaXDbot"
    SUPPORT_CHAT = "team_rocket_bot_suppot"
    UPDATES_CHANNEL = "Updatesxd"
    SUPPORT_CHANNEL = "updatesXD"
    JOIN_LOGGER = "-1001922924926"
    EVENT_LOGS = "-1001922924926"
    ERROR_LOGS = "-1001922924926"

    SQLALCHEMY_DATABASE_URI = "postgres://ishikki:FtY1vpm1x9CrHTUHghF5mXDzwv9wshPM@dpg-cgt6brl269vbmet0809g-a.oregon-postgres.render.com/shizuka"  # sql
    DATABASH_URL = "postgres://ishikki:FtY1vpm1x9CrHTUHghF5mXDzwv9wshPM@dpg-cgt6brl269vbmet0809g-a.oregon-postgres.render.com/shizuka"  # sql
    DB_URL = "postgres://qszfsijv:y6sYqkEb8Z9lFGBmriG7AYjbSbgAJBVk@peanut.db.elephantsql.com/qszfsijvxxqszfsijvx"
    MONGO_DB_URL = "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    MONGO_URL = "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority"
    DB_URL2 = "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority"  # YOUR MONGO_DB_URI
    ARQ_API_URL = "https://arq.hamker.dev"
    BOT_API_URL = "https://api.telegram.org/bot"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_SUPPORT_CHAT = "@devslab"

    REDIS_URL = "redis://Madharjoot:GuKhao123_@redis-12276.c275.us-east-1-4.ec2.cloud.redislabs.com:12276/Madharjoot"

    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "whitelists")
    DEMONS = get_user_list("elevated_users.json", "supports")
    INSPECTOR = get_user_list("elevated_users.json", "sudos")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = "https://t.me/ishikki_akabane"
    CERT_PATH = None
    STRICT_GBAN = "True"
    PORT = ""
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 8
    BAN_STICKER = ""
    ALLOW_EXCL = True
    CASH_API_KEY = "NAI H BRO"
    TIME_API_KEY = "5LB4TAKPEKZ0"
    WALL_API = "F-OFF"
    AI_API_KEY = "LOVEYOU"
    BL_CHATS = []
    SPAMMERS = None
    SPAMWATCH_API = "AHT~6SSflemqFZa5tfkKFQeiLnJUwoowWYozC3SN2ZY_aSGh83~9pItAmM4Mi40E"
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    REM_BG_API_KEY = "LSdLgCceYz8vNqFgJVzrkDgR"
    LASTFM_API_KEY = "FMLODA"
    CF_API_KEY = "KISS"
    BL_CHATS = []
    MONGO_PORT = "27017"
    MONGO_DB = "EXON"
    PHOTO = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    HELP_IMG = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    START_IMG = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    TIME_API_KEY = "5LB4TAKPEKZ0"
    INFOPIC = True
    GENIUS_API_TOKEN = "gIgMyTXuwJoY9VCPNwKdb_RUOA_9mCMmRlbrrdODmNvcpslww_2RIbbWOB8YdBW9"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True


# ENJOY
