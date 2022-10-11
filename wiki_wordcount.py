import requests
import json
from datetime import datetime
from elasticsearch import Elasticsearch
import pymongo

titles = ("mango","ferrari","porche")
wiki_base = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&format=json&titles="
elastic_url = "http://localhost:9200"
es = Elasticsearch(elastic_url)

mongodb_url = "mongodb://root:example@localhost:27017/"
myclient = pymongo.MongoClient(mongodb_url)


## ElasticSearch
def insertDataElastic(index):
  doc = {
    'author': 'author_name',
    'text': 'Interensting content...yes yes yes',
    'timestamp': datetime.now(),
  }
  resp = es.index(index=index, id=1, document=doc)
  print(resp['result'])

def readDataElastic(index):
  resp = es.get(index=index, id=1)
  print(resp['_source'])

def deleteData(index):
  es.delete(index=index, id=1)

def createIndex():
  self.connection.indices.create(
    index="wikipedia",
    body={
      "mappings": {
        "properties": {
          "namespace": {"type": "keyword"},
          "title": {"type": "search_as_you_type"},
          "lastedit": {"type": "date"},
          "content": {"type": "text"},
          "target": {"type": "keyword"}
        }
      }
    }
  )


## MongoDB
def pymongoConnect():
  mydb = myclient["local"]
  print(myclient.list_database_names())

def pymongoCreate(data):
  mydb = myclient["wikiarticles"]
  mycol = mydb["random"]
  result = mycol.insert_one(data)
  return result

def pymongoSearch(txt):
  mydb = myclient["wikiarticles"]
  mycol = mydb["random"]
  query = {"revisions.*": {"$regex": txt}}
  for each in mycol.find(query):
    txt_count = str(each).count(txt)
    print(txt_count)

def wikiArticles():
  es = Elasticsearch(elastic_url)
  for each_title in titles:
    response = requests.get(url= wiki_base + each_title)
    data = json.loads(response.text)
    pageid = list(data["query"]["pages"].keys())[0]
    result = pymongoCreate(data["query"]["pages"][pageid])

#pymongoSearch("text")
#wikiArticles()

pymongoSearch("car")