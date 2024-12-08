from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

# In-memory storage for demonstration purposes
users = []
devices = []
usage_statistics = []

# Utility functions for usage categorization
def categorize_screen_time(st):
    if st < 2:
        return 'Light'
    elif 2 <= st <= 5:
        return 'Moderate'
    else:
        return 'Heavy'

def categorize_app_usage(aut):
    if aut < 1:
        return 'Light'
    elif 1 <= aut <= 3:
        return 'Moderate'
    else:
        return 'Heavy'

def categorize_battery_drain(bd):
    if bd < 10:
        return 'Light'
    elif 10 <= bd <= 20:
        return 'Moderate'
    else:
        return 'Heavy'

def categorize_data_consumption(dc):
    if dc < 100:
        return 'Light'
    elif 100 <= dc <= 500:
        return 'Moderate'
    else:
        return 'Heavy'

# Routes for the Users table
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {
        "UserID": len(users) + 1,
        "Age": data['Age'],
        "Gender": data['Gender']
    }
    users.append(user)
    return jsonify({"message": "User created successfully!", "user": user}), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users}), 200

# Routes for the Devices table
@app.route('/devices', methods=['POST'])
def create_device():
    data = request.get_json()
    device = {
        "DeviceID": len(devices) + 1,
        "DeviceModel": data['DeviceModel'],
        "OperatingSystem": data['OperatingSystem'],
        "UserID": data['UserID']
    }
    devices.append(device)
    return jsonify({"message": "Device added successfully!", "device": device}), 201

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify({"devices": devices}), 200

# Routes for the UsageStatistics table
@app.route('/usage_statistics', methods=['POST'])
def add_usage_statistics():
    data = request.get_json()
    usage = {
        "UsageID": len(usage_statistics) + 1,
        "AppUsageTime": data['AppUsageTime'],
        "ScreenOnTime": data['ScreenOnTime'],
        "BatteryDrain": data['BatteryDrain'],
        "NumberOfAppsInstalled": data['NumberOfAppsInstalled'],
        "DataUsage": data['DataUsage'],
        "UserID": data['UserID']
    }
    usage_statistics.append(usage)
    return jsonify({"message": "Usage statistics added successfully!", "usage": usage}), 201

@app.route('/usage_statistics', methods=['GET'])
def get_usage_statistics():
    return jsonify({"usage_statistics": usage_statistics}), 200

# Route for categorizing usage (original functionality)
@app.route('/usage', methods=['POST'])
def handle_usage():
    data = request.get_json()
    # username = data.get('username')
    screen_time = data.get('screen_time')
    app_usage_time = data.get('app_usage_time')
    battery_drain = data.get('battery_drain')
    data_consumption = data.get('data_consumption')

    screen_time_category = categorize_screen_time(screen_time)
    app_usage_time_category = categorize_app_usage(app_usage_time)
    battery_drain_category = categorize_battery_drain(battery_drain)
    data_consumption_category = categorize_data_consumption(data_consumption)

    overall_result = {
        "screen_time": {
            "value": screen_time,
            "category": screen_time_category
        },
        "app_usage_time": {
            "value": app_usage_time,
            "category": app_usage_time_category
        },
        "battery_drain": {
            "value": battery_drain,
            "category": battery_drain_category
        },
        "data_consumption": {
            "value": data_consumption,
            "category": data_consumption_category
        }
    }

    return jsonify(overall_result), 200

if __name__ == '__main__':
    app.run(debug=True)
