# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class UserBehavior(db.Model):
#     __tablename__ = 'user_behavior'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     screen_time = db.Column(db.Float, nullable=False)
#     app_usage_time = db.Column(db.Float, nullable=False)
#     battery_drain = db.Column(db.Float, nullable=False)
#     data_consumption = db.Column(db.Float, nullable=False)
#     category = db.Column(db.String(50), nullable=False)

#     def __init__(self, username, screen_time, app_usage_time, battery_drain, data_consumption, category):
#         self.username = username
#         self.screen_time = screen_time
#         self.app_usage_time = app_usage_time
#         self.battery_drain = battery_drain
#         self.data_consumption = data_consumption
#         self.category = category

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Users table model
class User(Base):
    __tablename__ = "Users"
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    Age = Column(Integer, nullable=False)
    Gender = Column(Enum("Male", "Female"), nullable=False)

# Devices table model
class Device(Base):
    __tablename__ = "Devices"
    DeviceID = Column(Integer, primary_key=True, autoincrement=True)
    DeviceModel = Column(String(100), nullable=False)
    OperatingSystem = Column(String(50), nullable=False)
    UserID = Column(Integer, ForeignKey("Users.UserID"), nullable=False)

# UsageStatistics table model
class UsageStatistic(Base):
    __tablename__ = "UsageStatistics"
    UsageID = Column(Integer, primary_key=True, autoincrement=True)
    AppUsageTime = Column(Float, nullable=False)
    ScreenOnTime = Column(Float, nullable=False)
    BatteryDrain = Column(Float, nullable=False)
    NumberOfAppsInstalled = Column(Integer, nullable=False)
    DataUsage = Column(Float, nullable=False)
    UserID = Column(Integer, ForeignKey("Users.UserID"), nullable=False)
