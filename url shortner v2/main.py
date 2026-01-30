# Functional requirements :
#     covert a long or oginal url to shart urllib
#     check if the short url is valid
#     reditevt short url to long url
#
# non functional requirements:
#
#     resolving misslion of requets pre minutes
#     vaild fo atleadt 10 years
from pydoc import resolve

import repository
# exception :
#     no delete
#     no oustom alias
#     long url can genrate multi short url


# Capacity estimation
#     100M*356*10*500= 1.825*10^14=182.5 TB
# with indexing and replication  it take 500-600 GB
# here we need to implement horizontal scaling or sharding for same
# here auto incremt should code fails
# we need here is centralise id genrater

# short url :
#     attributes : short code, original url, is active
# services:
#     Repository:
#         Method - save , find short url
#
#     cretae reposiroty:
#     method : create, savetorepo
#
#     resolve repository:
#         resolve
from repository import Repository
from url_shortning_service import Url_Shortning_Service
from url_resolving_service import UrlResolvingService
def main():
    repo=Repository()

    url_shortner=Url_Shortning_Service(repo)
    url_resolver=UrlResolvingService(repo)

    original_url = "https://example.com/some/very/long/url"
    short_url=url_shortner.create(original_url)
    print("Short Code:", short_url.short_code)
    print("Original URL:", short_url.url)
    resolved_url=url_resolver.resolve(short_url.short_code)
    print(resolved_url)

if __name__ == "__main__":
    main()