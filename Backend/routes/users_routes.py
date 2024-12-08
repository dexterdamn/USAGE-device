# from flask import Blueprint, request, jsonify
# import joblib
# from database.models import db, UserBehavior

# # Load the trained model
# model = joblib.load("models/model.pkl")

# user_routes = Blueprint("user_routes", __name__)

# # Route for predicting user behavior
# @user_routes.route("/predict", methods=["POST"])
# def predict_behavior():
#     data = request.get_json()
#     username = data.get("username")
#     screen_time = data.get("screen_time")
#     app_usage_time = data.get("app_usage_time")
#     battery_drain = data.get("battery_drain")
#     data_consumption = data.get("data_consumption")

#     # Model prediction
#     input_data = [[screen_time, app_usage_time, battery_drain, data_consumption]]
#     prediction = model.predict(input_data)[0]

#     # Save to database
#     user_behavior = UserBehavior(
#         username=username,
#         screen_time=screen_time,
#         app_usage_time=app_usage_time,
#         battery_drain=battery_drain,
#         data_consumption=data_consumption,
#         category=prediction
#     )
#     db.session.add(user_behavior)
#     db.session.commit()

#     return jsonify({"username": username, "category": prediction}), 200

from flask import Blueprint, request, jsonify
from database.db_init import session
from database.models import User

user_routes = Blueprint("user_routes", __name__)

# Add a user
@user_routes.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    new_user = User(Age=data["age"], Gender=data["gender"])
    session.add(new_user)
    session.commit()
    return jsonify({"message": "User added successfully!"})

# Get all users
@user_routes.route("/users", methods=["GET"])
def get_users():
    users = session.query(User).all()
    return jsonify([{"UserID": u.UserID, "Age": u.Age, "Gender": u.Gender} for u in users])
