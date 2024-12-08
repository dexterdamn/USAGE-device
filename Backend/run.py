# from flask import Flask
# from routes.user_routes import user_routes
# from database.models import db
# from config import Config

# app = Flask(__name__)
# app.config.from_object(Config)

# # Initialize database
# db.init_app(app)

# # Register routes
# app.register_blueprint(user_routes, url_prefix="/api")

# if __name__ == "__main__":
#     app.run(debug=True)
# from database.db_init import test_connection
# from database.models import Base, engine

# # Test the database connection
# test_connection()

# # Create tables if they do not exist
# Base.metadata.create_all(bind=engine)

# print("Database tables are ready!")

from flask import Flask
from routes.users_routes import user_routes

app = Flask(__name__)

# Register the routes
app.register_blueprint(user_routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
