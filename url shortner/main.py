
# 1️⃣ Problem Statement
#
# Q: What is the problem statement?
# Design a system that generates a short URL for a given long URL and redirects users to the original URL when the short URL is accessed.
#
# 2️⃣ Functional Requirements
#
# Q: What are the functional requirements?
# The system should generate a short URL for a given long URL.
# The system should redirect users from the short URL to the original URL.
# The system should handle cases where a short URL does not exist.
#
# 3️⃣ Non-Functional Requirements
#
# Q: What are the non-functional requirements?
# The system should ensure uniqueness of generated short URLs.
# The redirect operation should be low latency since it is on the user request path.
# The system should be scalable to handle growth in the number of URLs.
# The system should be reliable so that generated URLs continue to work over long periods of time.
#
# 4️⃣ Assumptions
#
# Q: What assumptions are you making?
# Authentication and user management are out of scope
# Custom aliases and URL expiration are out of scope.
# The system is expected to be read-heavy compared to write operations.
#
# 5️⃣ Capacity & Scalability Estimation (High Level)
#
# Q: How do you reason about scalability and storage?
# Assume the system generates ~100 million URLs per year.
# Over 10 years, this results in ~1 billion URLs.
# Each URL mapping requires a few hundred bytes of storage.
# Total storage is in the order of a few hundred GB, which is manageable but requires horizontal scalability.
# The system is read-heavy, so redirect performance is more critical than URL creation.
#
# 6️⃣ Core Domain Entities
#
# Q: What are the core domain entities?
# ShortURL – Represents a shortened URL that maps a short identifier to an original URL and is used for redirection.
# Note: This is the minimum required entity.
# Additional entities are optional based on scope.
#
# 7️⃣ ShortURL Responsibilities
#
# Q: What are the responsibilities of the ShortURL entity?
# Represent the association between a short identifier and an original URL.
# Provide the information required to redirect a request to the original URL.
# Maintain metadata required for the lifecycle of the short URL.
#
# 8️⃣ ShortURL Invariants
#
# Q: What invariants must always hold for ShortURL?
# Each short URL identifier must be globally unique.
# Each short URL must always be associated with exactly one original URL.
# A short URL, once created, must consistently resolve to the same original URL.
#
# 9️⃣ Ownership Question
#
# Q: Does ShortURL need to know who created it?
# No.
# Justification:
# Because authentication and user management are out of scope, the short URL does not need to track creator information.
#
# 10️⃣ Entity Relationship
#
# Q: What is the relationship between ShortURL and Original URL?
# Many ShortURLs → One Original URL
# Justification:
# The same original URL can be shortened multiple times, each producing a different short URL.
# (Also acceptable to explain if you explicitly choose deduplication — but you must state the assumption.)
# 1️⃣1️⃣ Entity Operations
# Q: What operations does ShortURL support?
# createShortURL
# resolve
# deactivate
#
# 1️⃣3️⃣ Relationship
# Q: What is the relationship between ShortURL and original URL?
# Many ShortURLs → One Original URL
# (The same long URL can be shortened multiple times.)
#
# 1️⃣4️⃣ Read vs Write
# Q: Which operation is read-heavy and latency-critical?
# Resolving (redirecting) the short URL, because it happens on every user request.
#
# 1️⃣5️⃣ Service Layer
# Q: Why do we need services?
# To separate business logic from entity state.
# To isolate read-heavy and write-heavy workflows.
# Services:
# URLShorteningService – handles creation (write-heavy)
# URLResolutionService – handles redirection (read-heavy)
#
# 1️⃣6️⃣ Why Split Services?
# Q: Why separate creation and resolution?
# Creation is write-heavy and infrequent, while resolution is read-heavy and latency-critical.
# Separating them allows independent scaling and optimization.

#entity - short url
    # attributes :short code, original url, create at, is active
# services : RLShorteningService,URLResolutionService

from url_repository import URLRepository
from url_shortner_service import URLShorteningService
from url_resolution_service import URLResolutionService

def main():
    # initialize repository
    repository = URLRepository()

    # initialize services
    shortening_service = URLShorteningService(repository)
    resolution_service = URLResolutionService(repository)

    # create short URL
    original_url = "https://example.com/some/very/long/url"
    short_url = shortening_service.create_short_url(original_url)

    print("Short Code:", short_url.short_code)
    print("Original URL:", short_url.original_url)

    # resolve short URL
    resolved_url = resolution_service.resolve(short_url.short_code)

    print("Resolved URL:", resolved_url)


if __name__ == "__main__":
    main()
