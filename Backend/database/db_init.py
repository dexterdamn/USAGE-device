# from flask import Flask
# from models import db

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)

# with app.app_context():
#     db.create_all()
#     print("Database initialized!")
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker
# from config import DB_CONFIG

# # Create the database connection URL
# # DATABASE_URL = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['']}@{DB_CONFIG['host']}/{DB_CONFIG['UserDevice']}"
# DATABASE_URL = f"mysql+mysqlconnector://{DB_CONFIG['user']}@{DB_CONFIG['host']}/{DB_CONFIG['UserDevice']}"

# # Initialize SQLAlchemy engine and session
# engine = create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# # Metadata to reflect existing database
# metadata = MetaData()
# metadata.reflect(bind=engine)

# # Function to check database connection
# def test_connection():
#     try:
#         connection = engine.connect()
#         print("Database connected successfully!")
#         connection.close()
#     except Exception as e:
#         print(f"Failed to connect to the database: {e}")
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG

# Create the database connection URL
DATABASE_URL = f"mysql+mysqlconnector://{DB_CONFIG['user']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"

# Initialize SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Metadata to reflect existing database
metadata = MetaData()
metadata.reflect(bind=engine)

# Function to check database connection
def test_connection():
    try:
        connection = engine.connect()
        print("Database connected successfully!")
        connection.close()
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
