import mongoengine as me
from bson import ObjectId
from datetime import datetime
from db.models.user import User


class IdeaCategorization(me.Document):
    user_id = me.ReferenceField(User, required=True)
    date_created = me.DateTimeField()
    idea_name = me.StringField()
    idea_key_features = me.ListField()
    idea_benefits = me.ListField()
    idea_title = me.StringField()
    idea_description = me.StringField()
    idea_footer_description = me.StringField()
    idea_categorization = me.StringField()

    meta = {
        'collection': 'idea_categorization'  # Specify the collection name
    }

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
        user_id: str,
        idea_name: str,
        idea_key_features: dict,
        idea_benefits: dict,
        idea_title: str,
        idea_description: str,
        idea_footer_description: str,
        idea_categorization: str = None,
    ):
        record = cls(
            user_id=ObjectId(user_id),
            date_created=datetime.now(),
            idea_name=idea_name,
            idea_title=idea_title,
            idea_key_features=idea_key_features,
            idea_benefits=idea_benefits,
            idea_description=idea_description,
            idea_footer_description=idea_footer_description,
            idea_categorization=idea_categorization,
        )
        record.save()
        return record

    @classmethod
    def get_by_user(cls, user_id: str, user_name: str):
        try:
            query = {}
            if user_id:
                query["user_id"] = ObjectId(user_id)
            if user_name:
                query["user_name"] = user_name
            records = cls.objects.filter(**query)
            return records

        except me.DoesNotExist:
            return {}
