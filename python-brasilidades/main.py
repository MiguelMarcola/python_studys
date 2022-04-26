from audioop import add
from access_cep import SearchAddress

address = SearchAddress("27197000")

print(address)
address.request_api()
