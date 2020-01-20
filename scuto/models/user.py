from mongoengine import Document
from mongoengine import StringField, ReferenceField, BooleanField, EmailField, ValidationError
from .model import Model

def password_validator(password):
    try:
        password.decode('ascii') if isinstance(password, bytes) else password.encode('ascii')
    except UnicodeDecodeError:
        raise ValidationError('Password contains non-ASCII codes')
    return

class User(Document, Model):
    username = StringField(max_length=64, required=True, primary_key=True)
    password = StringField(max_length=64, required=True, validation=password_validator)
    salt = StringField(max_length=64, required=True)
    email = EmailField(required=True)
    admin = BooleanField(default=False)
    team = ReferenceField('Team')
    lastlogin = ReferenceField('Login')
    meta = {
        'strict': False
    }
