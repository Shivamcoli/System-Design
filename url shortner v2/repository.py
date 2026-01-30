from short_url import Short_Url

class Repository:
    def __init__(self):
        self.store={}

    def save(self,short_url):
        self.store[short_url.short_code]=short_url

    def find_by_short_code(self,short_code):
        return self.store.get(short_code)