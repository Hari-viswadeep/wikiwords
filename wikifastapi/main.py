#!/usr/bin/python
# -*- coding: utf-8 -*-
from fastapi import FastAPI
import pymongo
from elasticsearch import Elasticsearch

app = FastAPI()

## Mongodb

mongodb_url = 'mongodb://root:example@mongodb:27017/'
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

