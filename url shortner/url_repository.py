class URLRepository:

    def __init__(self):
        self.dict={}

    def save(self, short_url):
        self.dict[short_url.short_code]=short_url

    def find_by_short_code(self, short_code):
        return self.dict.get(short_code)
