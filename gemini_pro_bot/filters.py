import os
from telegram import Update
from telegram.ext.filters import UpdateFilter, COMMAND, TEXT, PHOTO
from dotenv import load_dotenv

load_dotenv()

_AUTHORIZED_USERS = [
    i.strip() for i in os.getenv("AUTHORIZED_USERS", "").split(",") if i.strip()
]


class AuthorizedUserFilter(UpdateFilter):
    def filter(self, update: Update):
        return True


AuthFilter = AuthorizedUserFilter()
MessageFilter = AuthFilter & ~COMMAND & TEXT
PhotoFilter = AuthFilter & ~COMMAND & PHOTO
