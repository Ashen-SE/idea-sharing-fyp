from flask import Blueprint, jsonify, request
from service.user_service import UserService
from service.idea_categorization import IdeaCategorizationService

idea_categorization = Blueprint("idea_categorization", __name__, url_prefix="/api/v1/idea-categorization")


@idea_categorization.route("", methods=["POST"])
def add_idea_categorization():
    json = request.json
    new_record = IdeaCategorizationService.create_new_idea_categorization_record(
        user_id=json.get("user_id"),
        idea_name=json.get("name"),
        idea_title=json.get("title"),
        idea_key_features=json.get("keyFeatures"),
        idea_benefits=json.get("benefits"),
        idea_description=json.get("description"),
        idea_footer_description=json.get("footerDescription"),
    )
    return jsonify({"data": new_record}), 200


@idea_categorization.route("/user/", methods=["GET"])
def get_idea_categorization_by_id():
    user_name = request.args.get("user_name", type=str)
    user_id = request.args.get("user_name", type=str)

    user_result = IdeaCategorizationService.get_category_ideas_by_user(
        user_id=user_id,
        user_name=user_name
    )
    return jsonify({"data": user_result}), 200

