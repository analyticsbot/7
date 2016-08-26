from boilerpipe.extract import Extractor
from readability.readability import Document
import urllib
from goose import Goose
from newspaper import Article
import requests
from dragnet import content_extractor, content_comments_extractor
import pandas as pd
import eatiht.v2 as v2

def getReadability(url):    
    #url = 'http://cnn.com/2016/07/17/health/south-africa-meerkat-telescope-galaxies/index.html'
    try:
        html = urllib.urlopen(url).read()
        readable_article = Document(html).summary().replace('\n','')
        readable_title = Document(html).short_title()
        return readable_title, readable_article
    except Exception,e:
        return '', ''

def getGoose(url):    
    #url = 'http://cnn.com/2016/07/17/health/south-africa-meerkat-telescope-galaxies/index.html'
    try:
        g = Goose()
        article = g.extract(url=url)
        title  = article.title
        text = article.cleaned_text.replace('\n','')
        return title, text
    except Exception,e:
        return '', ''

def getBoilerPlate(url):    
    #url = 'http://cnn.com/2016/07/17/health/south-africa-meerkat-telescope-galaxies/index.html'
    try:
        extractor = Extractor(extractor='ArticleExtractor', url=url)
        extracted_text = extractor.getText().replace('\n','')
        return '', extracted_text
    except Exception,e:
        return '', ''


def getNewspaper(url):
    #url = 'http://cnn.com/2016/07/17/health/south-africa-meerkat-telescope-galaxies/index.html'
    try:
        article = Article(url)
        article.download()
        article.parse()
        title = article.title
        text = article.text.replace('\n','')
        return title, text
    except Exception,e:
        return '', ''

def getDragnet(url):
    # fetch HTML
    #url = 'http://cnn.com/2016/07/17/health/south-africa-meerkat-telescope-galaxies/index.html'
    try:
        r = requests.get(url)
    # get main article without comments
        content = content_extractor.analyze(r.content).replace('\n','')
        return '', content
    except Exception,e:
        return '', ''

def getEatiht(url):    
    try:
        text = v2.extract(url).replace('\n','')
        return '', text
    except Exception,e:
        return '', ''

df = pd.read_csv('newsarticle.csv')
urls = list(df['newsUrls'])
print len(urls)

news_articles = pd.DataFrame(columns = ['url', 'eathit_title', 'eatiht_text', 'dragnet_title', \
                                        'dragnet_text', 'newspaper_title', 'newspaper_text',\
                                        'boiler_plate_title', 'boiler_plate_text',
                                        'goose_title', 'goose_text',\
                                        'readability_title', 'readability_text'])
count = 1
for url in urls:
    #print url
    try:
        eathit_title, eatiht_text = getEatiht(url)
    except Exception,e:
        print str(e)
        eathit_title, eatiht_text = '', ''
    try:
        dragnet_title,  dragnet_text = getDragnet(url)
    except Exception,e:
        print str(e)
        dragnet_title,  dragnet_text = '', ''
    try:
        newspaper_title, newspaper_text = getNewspaper(url)
    except Exception,e:
        print str(e)
        newspaper_title, newspaper_text = '', ''
    try:
        boiler_plate_title, boiler_plate_text = getBoilerPlate(url)
    except Exception,e:
        print str(e)
        boiler_plate_title, boiler_plate_text = '', ''
    try:
        goose_title, goose_text =getGoose(url)
    except Exception,e:
        print str(e)
        goose_title, goose_text = '', ''
    try:
        readability_title, readability_text =getReadability(url)
    except Exception,e:
        print str(e)
        readability_title, readability_text ='',''

    news_articles.loc[count] = [url, eathit_title, eatiht_text, dragnet_title,  dragnet_text, newspaper_title, newspaper_text, boiler_plate_title, boiler_plate_text, goose_title, goose_text, readability_title, readability_text]
    count+=1

    print '\n\n'

news_articles.to_csv('outputArticles.csv', index = False, encoding = 'utf-8')
