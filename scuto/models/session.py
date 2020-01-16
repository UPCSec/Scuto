from mongoengine import Document
from mongoengine import StringField, ReferenceField, DateTimeField, UUIDField
import datetime
from .model import Model


class Session(Document, Model):
    user = ReferenceField('User')
    login = ReferenceField('Login')
    start_time = DateTimeField(default=datetime.datetime.utcnow)
    sessionid = UUIDField(primary_key=True)
    meta = {
        'indexes': [
            {'fields': ['start_time'], 'expireAfterSeconds': 604800} # expires after a week
        ]
    }
