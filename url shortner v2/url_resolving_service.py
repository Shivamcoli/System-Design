class UrlResolvingService:
    def __init__(self,repository):
        self.repository=repository

    def resolve(self,short_code):
        self.short_url=self.repository.find_by_short_code(short_code)

        if self.short_url is None or not self.short_url.is_active:
            return None
        return self.short_url.url

