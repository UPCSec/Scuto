from mongoengine import Document
from mongoengine import StringField, IntField, ReferenceField, ListField
from .model import Model


class Challenge(Document, Model):
    type = StringField(choices=['coding', 'static', 'dynamic'])
    title = StringField()
    description = StringField()
    tag = ListField(StringField())
    file = StringField()
    image = StringField()
    ports = ListField(IntField())
    flag = ReferenceField('Flag')
    solution = ReferenceField('Solution')
