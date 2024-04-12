from flask import Blueprint, jsonify, request
from service.user_service import UserService

user = Blueprint("user", __name__, url_prefix="/api/v1/user")


@user.route("", methods=["POST"])
def add_user():
    json = request.json
    user_result = UserService.create_new_user_record(
        json.get("fullname"),
        json.get("user_name"),
        json.get("email"),
        json.get("password"),
        json.get("birthday"),
        json.get("mobile_number"),

    )
    return jsonify({"data": user_result}), 200


@user.route("/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user_result = UserService.get_user_by_id(
        user_id=user_id
    )
    return jsonify({"data": user_result}), 200


@user.route("/", methods=["GET"])
def get_user_by_username_password():
    user_name = request.args.get("user_name", type=str)
    password = request.args.get("password", type=str)
    user_result = UserService.get_user_by_credentials(
        user_name=user_name,
        password=password
    )
    return jsonify({"data": user_result}), 200
