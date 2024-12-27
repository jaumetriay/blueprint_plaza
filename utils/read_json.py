
import json
"""
Load advertisements from a JSON file.

This function reads the 'ads.json' file located in the 'static/json' directory
of the project and returns its contents as a Python object.

Returns:
    dict: A dictionary containing the advertisement data loaded from the JSON file.
"""
def load_ads():
    json_path = "static/json/data.json"
    with open(json_path, 'r') as f:
        return json.load(f)

