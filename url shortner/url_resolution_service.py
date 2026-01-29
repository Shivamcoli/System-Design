class URLResolutionService:
    def __init__(self, repository):
        self.repository = repository

    def resolve(self, short_code):
        short_url = self.repository.find_by_short_code(short_code)

        if short_url is None or not short_url.is_active:
            return None

        return short_url.original_url
