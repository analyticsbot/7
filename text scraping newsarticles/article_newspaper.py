from newspaper import Article

url = u'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'

def getArticleData(url):
    article = Article(url)
    article.download()

    html = article.html
    article.parse()

    authors = article.authors

    publish_date = article.publish_date

    text = article.text

    top_image = article.top_image

    movies = article.movies
    article.nlp()

    keywords = article.keywords

    summary = article.summary

    data = {'summary':summary, 'keywords':keywords, 'movies':movies,\
            'top_image':top_image, 'text':text, 'publish_date':publish_date,\
            'authors':authors, 'html':html}

    return data
