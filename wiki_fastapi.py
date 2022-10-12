#!/usr/bin/python
# -*- coding: utf-8 -*-
from fastapi import FastAPI
import pymongo
from elasticsearch import Elasticsearch

app = FastAPI()

## Mongodb

mongodb_url = 'mongodb://root:example@localhost:27017/'
client = pymongo.MongoClient(mongodb_url)
database = 'wikiarticles'
collection = 'random'


@app.get('/search/mongo/{word}')
def searchMongo(word):
    data = []
    db = client['wikiarticles']
    db_collection = db['random']
    query = {'revisions.*': {'$regex': word}}
    for each in db_collection.find(query):
        data.append(str(each))
    return data


@app.get('/wordcount/mongo/{word}')
def mongoWordCount(word):
    db = client['wikiarticles']
    db_collection = db['random']
    query = {'revisions.*': {'$regex': word}}
    word_count = 0
    for each in db_collection.find(query):
        word_count = word_count + str(each).count(word)
    return "Word Count For ' " + word + "' : " + str(word_count)


@app.get('/search/elastic/{word}')
def searchDataElastic():
    elastic_url = 'http://localhost:9200'
    es = Elasticsearch(elastic_url)
    resp = es.search(index='test-index', query={'match_all': {}})
    result = 'Got %d Hits:' % resp['hits']['total']['value']
    return result
