from mongoengine import Document, StringField, FloatField


class Meals(Document):
    name = StringField(required=True)
    description = StringField(max_length=240)
    price = FloatField()
    image_url = StringField()