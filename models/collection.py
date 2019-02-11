from mongoengine import StringField,Document

class Message(Document):
    role = StringField()
    message = StringField()
