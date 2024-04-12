from datetime import datetime

import mongoengine as me
from bson import ObjectId


class User(me.Document):
    full_name = me.StringField(required=True)
    user_name = me.StringField(required=True)
    email = me.EmailField(required=True)
    birthday = me.DateField()
    mobile_number = me.StringField()
    new_password = me.StringField(required=True)
    old_password = me.StringField(required=True)

    def to_dict(self, exclude_fields=None):
        if exclude_fields is None:
            exclude_fields = []

        user_dict = {}
        for field_name in self._fields:
            if field_name not in exclude_fields:
                field_value = getattr(self, field_name)
                if isinstance(field_value, datetime):
                    field_value = field_value.isoformat()
                elif isinstance(field_value, ObjectId):
                    field_value = str(field_value)
                user_dict[field_name] = field_value

        return user_dict

    @classmethod
    def add_new_record(
        cls,
        fullname: str,
        user_name: str,
        email: str,
        password: str,
        birthday: datetime = None,
        mobile_number: str = None
    ):
        record = cls(
            full_name=fullname,
            user_name=user_name,
            email=email,
            new_password=password,
            old_password=password,
            birthday=birthday,
            mobile_number=mobile_number,
        )
        record.save()
        return record

    @classmethod
    def get_user_by_id(cls, user_id: str):
        try:
            user = cls.objects.get(id=ObjectId(user_id))
            return user.to_dict()

        except me.DoesNotExist:
            return {}

    @classmethod
    def get_user_by_credentials(cls, user_name: str, password: str):
        try:
            user = cls.objects.get(user_name=user_name, new_password=password)
            return user.to_dict()
        except me.DoesNotExist:
            return {}
