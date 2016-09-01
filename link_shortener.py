import uuid


class LinkShortener():
    def __init__(self):
        self.url_dict = dict()
        self.link_length = 10
        self.domain = "127.0.0.1:5000"
        self.link_dir = "/link/"

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
        if self.url_dict.get(url) is None:
            url = self.add_http_before_url(url)
            print(url)
            self.url_dict[url] = self.get_generated_code()
        return self.url_dict[url]

    def get_code_url(self, url):
        return self.domain + self.link_dir + self.get_code(url)

    def get_url(self, code):
        for key, value in self.url_dict.items():
            if value == code:
                return key
