from mongoengine import Document
from mongoengine import StringField, ReferenceField
from .model import Model


class Team(Document, Model):
    teamname = StringField(max_length=64, required=True, unique=True, primary_key=True)
    captain = ReferenceField('User')
    captain_name = StringField(max_length=64)
