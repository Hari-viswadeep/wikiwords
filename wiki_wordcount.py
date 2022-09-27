import requests

titles = ["volkswagon","ferrari","porche"]
wiki_base = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&format=json&titles="

def wikiArticles():
  for each_title in titles:
    response = requests.get(url= wiki_base + each_title)
    print(response.text)
    print("##################################")

wikiArticles()