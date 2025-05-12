import json
def read_json(path) -> list:
    with open(path, "r") as f:
        return json.load(f)