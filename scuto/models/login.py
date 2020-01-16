from mongoengine import Document
from mongoengine import StringField, ReferenceField, DateTimeField
from .model import Model
import datetime


class Login(Document, Model):
    user = ReferenceField('User')
    ip = StringField(max_length=16)
    status = StringField(max_length=64, choices=['success', 'failed'])
    time = DateTimeField(default=datetime.datetime.utcnow)
