from dotenv import load_dotenv

load_dotenv("config.env")

HEROKU = True  # NOTE Make it false if you're not deploying on heroku or docker.

if HEROKU:
    from os import environ

    BOT_TOKEN = environ.get("BOT_TOKEN", 1874293991:AAHj-YZrqr_pMtZ4ZYv4439HPHczMt1MIho)
    API_ID = int(environ.get("API_ID", 6798455))
    API_HASH = environ.get(
        "API_HASH", "50e975d09902b74b371d0e8acef83f61"
    )
    SESSION_STRING = environ.get("SESSION_STRING", AQC_h6JmSqn5uZqiCPFaXUU04sXjmKa-HeS_C186UOytlTiTpx8YmAgRWUWFbq3trTleMMeDX40Rp7PCtht6nSJ5gAV1dDfgYbit_4E1JGHdb0O_3dS48wltmOACTY5kapfJPvtHIU_LMSvBBm0qvXz2DgUZty_EEMhiqA6DLnElfeETDxAFhStohi9DLhS6zSWW1rc9z1x6IxRqVHniG269iYPjFbOBVtbT-qdHqD2xmrsdncuglWWT9xgi3KWxTymuhGm5fwHne0n1JKex__vgckeio-5FVFy78q-XFZJ2L66bhyr1BjUAEraMoDXJb4VjuJ2s8QHihcRCJ5Il2UL6b7d05wE)

    USERBOT_PREFIX = environ.get("USERBOT_PREFIX", ".")
    SUDO_USERS_ID = list(
        int(x) for x in environ.get("SUDO_USERS_ID", "").split()
    )
    LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
    GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
    MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
    FERNET_ENCRYPTION_KEY = environ.get("FERNET_ENCRYPTION_KEY", None)
    WELCOME_DELAY_KICK_SEC = int(
        environ.get("WELCOME_DELAY_KICK_SEC", None)
    )
    MONGO_DB_URI = environ.get("MONGO_DB_URI", None)
    ARQ_API_URL = environ.get("ARQ_API_URL", None)
    ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
    LOG_MENTIONS = (
        True if int(environ.get("LOG_MENTIONS", None)) == 1 else False
    )
    RSS_DELAY = int(environ.get("RSS_DELAY", None))
else:
    BOT_TOKEN = "1874293991:AAHj-YZrqr_pMtZ4ZYv4439HPHczMt1MIho"
    API_ID = 6798455
    API_HASH = "50e975d09902b74b371d0e8acef83f61"
    USERBOT_PREFIX = "."
    PHONE_NUMBER = "+628986304400"  # Need for Helper Userbot
    SUDO_USERS_ID = [
        1832439274,
        1832439274,
    ]  # Sudo users have full access to everythin, don't trust anyone
    LOG_GROUP_ID = -1001389283656
    GBAN_LOG_GROUP_ID = -1001389283656
    MESSAGE_DUMP_CHAT = -1001389283656
    FERNET_ENCRYPTION_KEY = "iKMq0WZMnJKjMQxZWKtv-cplMuF_LoyshXj0XbTGGWM="  # Leave this as it is
    WELCOME_DELAY_KICK_SEC = 300
    MONGO_DB_URI = "mongodb+srv://username:password@cluster0.ksiis.mongodb.net/YourDataBaseName?retryWrites=true&w=majority"
    ARQ_API_KEY = "Get this from @ARQRobot"
    ARQ_API_URL = "https://thearq.tech"
    LOG_MENTIONS = False
    RSS_DELAY = 300  # In seconds
