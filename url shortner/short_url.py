class ShortUrl:
    def __init__(self, short_code, original_url, created_at, is_active=True):
        self.short_code = short_code
        self.original_url = original_url
        self.created_at = created_at
        self.is_active = is_active