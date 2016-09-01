import json


class JsonHelper:
    def __init__(self, filename):
        self.filename = filename

    def get_json(self):
        try:
            with open(self.filename) as f:
                return json.load(f)
        except FileNotFoundError:
            pass
    def save(self, url_dict):
        with open(self.filename, "w") as f:
            f.write(json.dumps(url_dict))
