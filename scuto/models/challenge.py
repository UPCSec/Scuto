from mongoengine import Document
from mongoengine import StringField, IntField, ReferenceField, ListField
from .model import Model


class Challenge(Document, Model):
    type = StringField(choices=['Coding', 'Static', 'Dynamic'])
    title = StringField()
    description = StringField()
    tags = ListField(StringField())
    file = StringField()
    image = StringField()
    ports = ListField(IntField())
    flag = ReferenceField('Flag')
    score = IntField()
    blood_bonus = ListField(IntField())
    writeup = StringField()
