from goose3 import Goose

def extract_news(url):
    g = Goose()
    article = g.extract(url=url)
    titulo = article.title
    g.close()
    return titulo