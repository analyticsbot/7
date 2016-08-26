from goose import Goose

url = 'http://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2'

def getArticleData(url):
    g = Goose()
    article = g.extract(url=url)
    title = article.title
    meta_description = article.meta_description
    cleaned_text = article.cleaned_text
    top_image = article.top_image.src

    data = {'top_image':top_image, 'title':title,\
            'meta_description':meta_description,\
            'cleaned_text':cleaned_text}

    return data
