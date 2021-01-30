from mongoengine import (Document,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         ListField,
                         StringField,
                         EmailField,
                         BooleanField,
                         ReferenceField)


from flask_bcrypt import generate_password_hash, check_password_hash

from models.meals import Meals

import re


class Access(EmbeddedDocument):
   
    user = BooleanField(default=True)
    admin = BooleanField(default=False)


class PhoneField(StringField):
  
    REGEX = re.compile(r"((\(\d{3}\)?)|(\d{3}))([-\s./]?)(\d{3})([-\s./]?)(\d{4})")

    def validate(self, value):
       
        if not PhoneField.REGEX.match(string=value):
            self.error(f"ERROR: `{value}` Is An Invalid Phone Number.")
        super().validate(value=value)


class Users(Document):
   
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    access = EmbeddedDocumentField(Access, default=Access(user=True, admin=False))
    fav_meals = ListField(ReferenceField(Meals))
    name = StringField(unique=False)
    phone = PhoneField()

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')
    generate_pw_hash.__doc__ = generate_password_hash.__doc__

    def check_pw_hash(self, password: str):
        return check_password_hash(pw_hash=self.password, password=password)
    check_pw_hash.__doc__ = check_password_hash.__doc__

    def save(self, *args, **kwargs):
        self.generate_pw_hash()
        super().save(*args, **kwargs)