import json
from datetime import datetime
import os

DATA_FILE = "project_data.json"

def save_task(update):
    data = load_data()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "update": update
    }
    data.append(entry)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)