from decouple import config

BOT_TOKEN = config("BOT_TOKEN")

admins = [
    config("ADMIN_ID"),
]

PG_HOST = config('HOST')
PG_USER = config('USER')
PG_PASS = config('PASS')
