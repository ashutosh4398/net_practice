from datetime import datetime, timedelta, timezone

import jwt
from django.conf import settings

import users.models as auth_model
from common.constants import DATE_TIME_FORMAT


def generate_token(user: auth_model.CustomUser) -> str:
    today = datetime.now().replace(tzinfo=timezone.utc).astimezone()
    expiry = today + +timedelta(days=2)
    payload = {
        "user_id": str(user.id),
        "expiry_date": expiry.strftime(DATE_TIME_FORMAT),
    }
    return jwt.encode(payload, key=settings.SECRET_KEY)


def decode_token(token: str) -> dict:
    return jwt.decode(token, key=settings.SECRET_KEY)
