from mongoengine import Document
from mongoengine import StringField, ReferenceField
from .model import Model


class Flag(Document, Model):
    type = StringField(choices=['static', 'dynamic'])
    # master_generate: scuto generates the flag and container can get it from environment variavle FLAG
    generation_method = StringField(choices=['master_generate', 'container_generate'])
    # if type is static or generation method is master_generate
    flag = StringField()
    # if flag is generated in container, scuto will run it and retrive output as flag
    flag_script = StringField()
