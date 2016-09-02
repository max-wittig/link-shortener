from json_helper import JsonHelper
import uuid


class LinkShortener:
    def __init__(self):
        self.url_dict = dict()
        self.json_helper = JsonHelper("short_links.json")
        self.link_length = 10
        self.link_dir = "/link/"
        self.port = 5000
        self.load_from_file()

    def load_from_file(self):
        self.url_dict = self.json_helper.get_json()
        if self.url_dict is None:
            self.url_dict = dict()

    def save_to_file(self):
        self.json_helper.save(self.url_dict)

    def get_generated_code(self):
        identifier = str(uuid.uuid4()).replace("-", "")
        return identifier[0:self.link_length]

    def add_http_before_url(self, url):
        if str(url).startswith("http://") or str(url).startswith("https://"):
            return url
        else:
            new_url = "http://" + url
            return new_url

    def get_code(self, url):
        url = self.add_http_before_url(url)
        if self.url_dict.get(url) is None:
            self.url_dict[url] = self.get_generated_code()
            self.save_to_file()
        return self.url_dict.get(url)

    def get_code_url(self, url, hostname):
        return hostname + ":" + str(self.port) + self.link_dir + self.get_code(url)

    def get_url(self, code):
        for key, value in self.url_dict.items():
            if value == code:
                return key
