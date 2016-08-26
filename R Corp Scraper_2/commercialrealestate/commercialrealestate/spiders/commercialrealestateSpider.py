from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from commercialrealestate.items import CommercialrealestateItem
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
from scrapy.http import HtmlResponse

class JSMiddleware(object):
    def process_request(self, request, spider):
        driver = webdriver.Firefox()
        driver.get(request.url)

        body = driver.page_source
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)

class CommercialRealEstateView(CrawlSpider):
    name = "commercialrealestate"
    allowed_domains = ["commercialrealestate.com.au"]
    start_urls = [
        "http://www.commercialrealestate.com.au/for-sale/?so=2&bb=-32.23626626934806%2c-41.14991096942575%2c153.44867726562507%2c136.28803273437507%2c6"
]
    rules = [Rule(LinkExtractor( allow = ['search']),                   
                   process_links='process_links',
                  callback='parse_item',                   
                   follow=True)]

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):        
        sel = Selector(response)
        sites = sel.xpath("//a[@linkSearchResult@href']")
        #items = []
        for site in sites:
            item = CommercialrealestateItem()
            link = site.xpath('@href').extract()
            #print link, '\n\n'
            item['link'] = link
            link = str(link[0])
            #print 'link!!!!!!=', link
            new_request = Request(link, callback=self.parse_file_page)
            new_request.meta['item'] = item
            yield new_request
            #items.append(item)
        yield item
        return
        
    def process_links(self, links):
        print 'inside process links'
        for i, w in enumerate(links):
            print w.url,'\n\n\n'
            w.url = w.url
            print w.url,'\n\n\n'
            links[i] = w
            
        return links
    
    def parse_file_page(self, response):
        #item passed from request
        #print 'parse_file_page!!!'
        item = response.meta['item']
        #selector
        sel = Selector(response)
        title = sel.xpath('//*[@class="row address-bar"]/div[1]/h1/text()').extract()
        #print title
        item['title'] = title
        
        return item
