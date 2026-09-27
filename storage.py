import json
import os

DATA_FILE = "student_grades.json"


def load_data():
    """Loads student records from a local JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning: Could not parse saved data. Starting fresh.")
    return {}


def save_data(data):
    """Saves student records to a local JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)