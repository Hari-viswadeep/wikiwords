from fastapi import FastAPI
import pymongo

app = FastAPI()

mongodb_url = "mongodb://root:example@localhost:27017/"
myclient = pymongo.MongoClient(mongodb_url)

elastic_url = "http://localhost:9200"
es = Elasticsearch(elastic_url)

@app.get("/search/mongo/{word}")
def searchMongo(word):
    mydb = myclient["wikiarticles"]
    mycol = mydb["random"]
    query = {"revisions.*": {"$regex": word}}
    for each in mycol.find(query):
        print(each)
    return "hello"

@app.get("/wordcount/mongo/{word}")
def mongoWordCount(word):
    mydb = myclient["wikiarticles"]
    mycol = mydb["random"]
    query = {"revisions.*": {"$regex": word}}
    word_count = 0
    for each in mycol.find(query):
        word_count = word_count + str(each).count(word)
    return "Word Count For "+ word + " : " + str(word_count)

@app.get("/search/elastic/{word}")
def searchDataElastic():
    resp = es.search(index="test-index", query={"match_all": {}})
    print("Got %d Hits:" % resp['hits']['total']['value'])
    for hit in resp['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])