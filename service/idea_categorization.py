from db.core.idea_categorization import IdeaCategorizationModel
from db.models.idea_categorization import IdeaCategorization
from datetime import datetime


class IdeaCategorizationService:
    @staticmethod
    def create_new_idea_categorization_record(
        user_id: str,
        idea_name: str,
        idea_key_features: dict,
        idea_benefits: dict,
        idea_title: str,
        idea_description: str,
        idea_footer_description: str,
    ):
        best_category_suggestion = IdeaCategorizationModel.find_category(idea_str=idea_title).get("result")
        return IdeaCategorization.add_new_record(
            user_id=user_id,
            idea_name=idea_name,
            idea_key_features=idea_key_features,
            idea_benefits=idea_benefits,
            idea_title=idea_title,
            idea_description=idea_description,
            idea_footer_description=idea_footer_description,
            idea_categorization=best_category_suggestion,
        )

    @staticmethod
    def get_category_ideas_by_user(
        user_id: str,
        user_name: str
    ):
        category_ideas = IdeaCategorization.get_by_user(
            user_id=user_id,
            user_name=user_name
        )
        to_return = []
        for category_idea in category_ideas:
            _dict = category_idea.to_dict()
            _date = _dict.get("date_created")
            try:
                datetime_obj = datetime.strptime(_date, '%Y-%m-%dT%H:%M:%S.%f')
                formatted_string = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
            except:
                formatted_string = ""

            to_return.append({
                "date": formatted_string,
                "name": _dict.get("idea_name"),
                "keyFeatures": _dict.get("idea_name"),
                "name": _dict.get("idea_key_features"),
                "benefits": _dict.get("idea_benefits"),
                "title": _dict.get("idea_title"),
                "description": _dict.get("idea_description"),
                "footerDescription": _dict.get("idea_footer_description"),
            })
        return to_return
