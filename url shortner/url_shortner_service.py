import uuid
from datetime import datetime, UTC
from short_url import ShortUrl


class URLShorteningService:
    def __init__(self, repository):
        self.repository = repository

    def create_short_url(self, original_url):
        # generate a unique short code
        short_code = self._generate_short_code()

        # create entity
        short_url = ShortUrl(
            short_code=short_code,
            original_url=original_url,
            created_at=datetime.now(UTC),
            is_active=True
        )

        # persist entity
        self.repository.save(short_url)

        return short_url

    def _generate_short_code(self):
        return uuid.uuid4().hex[:8]
