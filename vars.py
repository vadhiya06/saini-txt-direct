#RAJU
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "14662552"))
API_HASH = environ.get("API_HASH", "cd56687a177fe2355e64c91659facf3e")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "5885218829"))
CREDIT = "⍣⃝Raju 𝘽𝙊𝙏𝙎"
AUTH_USER = os.environ.get('AUTH_USERS', '5885218829').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
