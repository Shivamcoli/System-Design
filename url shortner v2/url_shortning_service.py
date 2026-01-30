import uuid
from short_url import Short_Url
from repository import Repository
class Url_Shortning_Service:
    def __init__(self,repository):
        self.repository=repository


    def create(self,url):
        shortcode=uuid.uuid4().hex[:8]
        short_url=Short_Url(shortcode,url,is_active=True)
        self.repository.save(short_url)
        return short_url