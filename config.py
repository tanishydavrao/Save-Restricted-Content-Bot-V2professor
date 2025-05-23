# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "28185042"))
API_HASH = getenv("API_HASH", "05eed5fc575c6c7fbc1d25e3670e5891")
BOT_TOKEN = getenv("BOT_TOKEN", "7408996363:AAESHbJ7CO8p3NZl1hlwFIJxOgr8gDyJz9c")
OWNER_ID = list(map(int, getenv("OWNER_ID", "974423344").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://atlas-sample-dataset-load-67fb6a3b3e06be489dd5d7e6:vEObWVVAEfk9MCIn@cluster0.yex7tnh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1002581586453")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-2533222285"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "50000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
