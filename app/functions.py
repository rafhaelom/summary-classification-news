from goose3 import Goose

g = Goose()
article = g.extract(url='http://this-url.html')
print(article.title)
g.close()