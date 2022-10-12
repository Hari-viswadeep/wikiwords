#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import pymongo

wiki_base = \
  'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&format=json&titles='
mongodb_url = 'mongodb://root:example@localhost:27017/'
client = pymongo.MongoClient(mongodb_url)
filename = 'articles.txt'
database = 'wikiarticles'
collection = 'random'


## MongoDB

def readTitles():
  with open(filename, mode='r') as file:
    data = file.read().splitlines()
  return data


def mongoConnect():
  database = client['local']
  print client.list_database_names()


def mongoCreate(data):
  db = client[database]
  db_collection = db[collection]
  result = db_collection.insert_one(data)
  return result


def writeWikiArticles():
  titles = readTitles()
  for each_title in titles:
    response = requests.get(url=wiki_base + each_title)
    data = json.loads(response.text)
    pageid = list(data['query']['pages'].keys())[0]
    result = mongoCreate(data['query']['pages'][pageid])


if __name__ == '__main__':
  writeWikiArticles()

