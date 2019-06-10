import json
import os
from pathlib import Path


class JsonHelper:
    def __init__(self, filename):
        self.base_path = Path.cwd() / "link-cache"
        self.base_path.mkdir(exist_ok=True, parents=True)
        self.filename = self.base_path / filename

    def get_json(self):
        if self.filename.exists():
            with open(self.filename, "r") as f:
                return json.load(f)
        return {}

    def save(self, url_dict):
        with open(self.filename, "w") as f:
            f.write(json.dumps(url_dict, indent=2))
