import os


class Config(object):
    TG_BOT_TOKEN = int(os.environ.get("TG_BOT_TOKEN", "5901305358:AAG_DA1t3CXnakCe8BAEsNWGG5uDU8MtpJk"))

    APP_ID = int(os.environ.get("APP_ID", 11750778))

    API_HASH = os.environ.get("API_HASH", "d0352df3ddb5e00bcf16b55dae071b52")
