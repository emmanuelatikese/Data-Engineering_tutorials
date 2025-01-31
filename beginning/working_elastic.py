

import urllib3
from elasticsearch import Elasticsearch, helpers
from faker import Faker 
fake = Faker()
es = Elasticsearch(["https://localhost:9200"], http_auth=('elastic','Z+UDEk-BsA1pOpsW1OTn'), verify_certs=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# inserting few bodies into elastic search
# body = {"name": fake.name(), "street": fake.street_address() }
# res = es.index(index="users", body=body)


#inserting many bodies into elastic search
# action = [
#     {
#         "_index": "users",
#         "_source":{
#             "name": fake.name(), "street": fake.street_address()
#         }
#     }
#     for x in range(1000)
# ]

# helpers.bulk(es, action)


## extracting some data from elastic search ##

#below line -> extracting all
#ext = {"query": {"match_all": {}}}

#the code below is when you want to extract in a specific field
# ext = {"query": {"match": {'name': 'boyer'}}}

# res = es.search(index="users", body=ext, size=20)

#another way of writing this line
res = es.search(index="users", q="name: Derrick", size=20)

hits = res['hits']['hits']

[print(x["_source"]) for x in hits]