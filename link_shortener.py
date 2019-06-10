from json_helper import JsonHelper
import urllib.parse
import uuid
import os
from pathlib import Path


class LinkShortener:
    def __init__(self):
        self.url_dict = {}
        self.json_helper = JsonHelper("short_links.json")
        self.link_length = 10
        self.port = os.getenv("PORT", 5000)
        self.load_from_file()

    def load_from_file(self):
        self.url_dict = self.json_helper.get_json()
        if not self.url_dict:
            self.url_dict = {}

    def save_to_file(self):
        self.json_helper.save(self.url_dict)

    def get_generated_code(self):
        identifier = str(uuid.uuid4()).replace("-", "")
        return identifier[0 : self.link_length]

    def add_http_before_url(self, url):
        if str(url).startswith("http://") or str(url).startswith("https://"):
            return url
        else:
            new_url = "http://" + url
            return new_url

    def get_code(self, url):
        url = self.add_http_before_url(url)
        if not self.url_dict or not self.url_dict.get(url):
            self.url_dict[url] = self.get_generated_code()
            self.save_to_file()
            print(self.url_dict)
        return self.url_dict.get(url)

    def get_code_url(self, url, to_shorten_url):
        return (
            self.add_http_before_url(str(url).strip("/"))
            + "/link/"
            + self.get_code(to_shorten_url)
        )

    def get_url(self, code):
        for key, value in self.url_dict.items():
            if value == code:
                return key
