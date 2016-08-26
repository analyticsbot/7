from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from commercialview.items import CommercialviewItem
from scrapy.selector import Selector
from scrapy.http import Request
import datetime
import requests, re
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import pandas as pd

class CommercialView(CrawlSpider):
    name = "commercialview+2dec"
    allowed_domains = ["commercialview.com.au"]
    start_urls = [
        "http://www.commercialview.com.au/search?utf8=%E2%9C%93&search%5Bsale_lease%5D=sale&search%5Bsuburb_hint%5D=&search%5Bproperty_types%5D=&search%5Bquery%5D=&search%5Bmin_sale_price%5D=&search%5Bmax_sale_price%5D=&search%5Bradius%5D=10"
]
    rules = [Rule(LinkExtractor( allow = ['/search?page']),                   
                   process_links='process_links',
                  callback='parse_item',                   
                   follow=True)]

    def parse_start_url(self, response):
        return self.parse_item(response)

    def makeGood(self, text):
        return ''.join([i if ord(i) < 128 else ' ' for i in text])
    
    def parse_item(self, response):        
        sel = Selector(response)
        sites = sel.xpath("//a[@class='view-btn btn btn-light']")
        #items = []
        for site in sites:
            item = CommercialviewItem()
            link = site.xpath('@href').extract()
            #print link, '\n\n'
            item['link'] = link
            link = 'http://www.commercialview.com.au' + str(link[0])
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
        title = str(sel.xpath('//*[@class="row address-bar"]/div[1]/h1/text()').extract()[0].replace('\n',''))
        #print title
        geolocator = Nominatim()
        location = geolocator.geocode(title)
        item['dateCrawled'] = str(datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        item['source'] = 'commercial_view'
        item['PageTitle'] = self.makeGood(str(sel.xpath('//*[@class="row address-bar"]/div[1]/h1/text()').extract()[0].replace('\n','')))
        item['DisplayablePrice'] = str(''.join(sel.xpath('//*[@class="price-view"]/text()').extract()).strip())
        item['PropertyDetailsUrl'] = str(response.url)
        item['ConjunctionalAgencyBannerURL'] = str(sel.xpath('//*[@class="listing-header"]/a/@href').extract()[0])
        item['OccupancyStatus'] = 'NA'
        item['ConjunctionalAgencyContactPhone'] = str(sel.xpath('//*[@class="attr"]/text()').extract()[0].strip())
        item['ParkingOptions'] = str(sel.xpath('//*[@class="row info-bar-with-icons"]/div[4]/p/text()'). extract()[0].replace('\n',''))
        item['DisplayableAddressStreet'] = str(title.split(',')[0])
        item['Suburb'] = str(title.split(',')[1])
        item['DateFirstListed'] = 'NA'
        item['SaleID'] = 'NA'
        item['EoiRecipientName'] = 'NA'
        item['AgencyBannerUrlCre'] = 'NA'
        item['HasInspections'] = 'NA'
        item['PropertyWebLink'] = str(response.url)
        item['EoiDeliveryAddress'] = 'NA'
        item['CardType'] = 'NA'
        item['Inspections'] = 'NA'
        item['Availability'] = 'NA'
        item['State'] = str(title.split(',')[1]).split()[1]
        item['TenderDeliveryAddress'] = 'NA'
        item['Type'] = str(sel.xpath('//*[@class="row info-bar-with-icons"]/div[1]/p/text()'). extract()[0].replace('\n',''))
        item['AgencyAddress'] = self.makeGood(str(sel.xpath('//*[@class="margin-top-10"]/text()').extract()[0].replace('\n','')))
        item['LeaseListingUrl'] = 'NA'
        item['InspectionTime'] = 'NA'
        item['ConjunctionalAgencyId'] =  'NA'
        item['DisplayableAddressSuburb'] = str(title.split(',')[1]).split()[0]
        item['Categories'] = 'NA'
        item['Postcode'] = str(title.split(',')[-1])
        item['AuctionDate'] = 'NA'
        item['AgencyLogoURLCRE'] = 'NA'
        item['VideoURL'] = 'NA'
        item['ConjunctionAgency'] = 'NA'
        item['ListingCategory'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[3]/text()').extract()[0].replace('\n',''))
        item['BuildingType'] = str(sel.xpath('//*[@class="row info-bar-with-icons"]/div[1]/p/text()'). extract()[0].replace('\n',''))
        item['TenderEndDateAndTime'] = 'NA'
        item['ConjunctionalAgencyLogoLargeURL'] = 'NA'
        item['LeaseEndDate'] = 'NA'
        item['CaptionType'] = 'NA'
        item['LastUpdated'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[5]/text()').extract()[0].replace('\n',''))
        item['BrandingBannerUrl'] = 'NA'
        item['AgencyId'] = str(sel.xpath('//*[@itemprop="seller"]/h4/a/@href').extract()[0].replace('\n','')).split('/')[-1] 
        item['AgencyName'] = str(sel.xpath('//*[@itemprop="seller"]/h4/a/text()').extract()[0].replace('\n',''))
        item['PrimaryAgencyColor'] = 'NA'
        item['Address'] = str(sel.xpath('//*[@class="row address-bar"]/div[1]/h1/text()').extract()[0].replace('\n',''))
        item['ListingContacts'] = 'NA'
        item['LogoUrl'] = 'NA'
        item['PriceDisplayText'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[4]/text()').extract()[0].replace('\n',''))
        item['AdID'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[1]/text()').extract()[0].replace('\n',''))
        item['Images'] = 'NA'
        item['BuildArea'] = str(sel.xpath('//*[@class="row info-bar-with-icons"]/div[3]/p/text()'). extract()[0].replace('\n',''))
        item['MapLongitude'] = location.longitude
        item['LeaseStartDate'] = 'NA'
        item['DisplayAddressType'] = 'NA'
        item['AgencyLogoLargeURLCRE'] = 'NA'
        item['TenantName'] = 'NA'
        item['UnitDetails'] = 'NA'
        item['DatePlatinumBilling'] = 'NA'
        item['AnnualReturn'] = 'NA'
        item['AuctionAddress'] = 'NA'
        item['VideoInfo'] = 'NA'
        item['LeaseOptions'] = 'NA'
        item['LandArea'] = str(sel.xpath('//*[@class="row info-bar-with-icons"]/div[2]/p/text()'). extract()[0].replace('\n',''))
        item['DisplayableAddressTruncated'] = 'NA'
        item['SaleType'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[3]/text()').extract()[0].replace('\n',''))
        item['ConjunctionalAgencyAddress'] = 'NA'
        item['AuctionTerms'] = 'NA'
        item['NabersRating'] = 'NA'
        item['TenantInformation'] = 'NA'
        item['IsArchived'] = 'NA'
        item['TenderRecipientName'] = 'NA'
        item['EoiEndDateAndTime'] = 'NA'
        if item['ParkingOptions']>=0:
            item['Parking'] = 'Y'
        else:
            item['ParkingOptions'] = 'N'
        item['PrimaryImageFullSizeUrl'] = 'NA'
        item['Headline'] = str(sel.xpath('//*[@itemprop="name"]/h2/text()').extract()[0])
        item['MapLatitude'] = location.latitude
        item['ConjunctionalAgencyName'] = 'NA'
        item['AdFormat'] = 'NA'
        item['Description'] = self.makeGood(''.join([str(el.replace('\n','')) for el in sel.xpath('//*[@class="description"]/p/text()').extract()]))
        item['BuildOrLandArea'] = str(sel.xpath('//*[@class="row info-bar-with-icons"]/div[2]/p/text()'). extract()[0].replace('\n',''))
        item['EoiEndDate'] = 'NA'
        item['VirtualTourUrl'] = 'NA'
        item['PdfUploads'] = 1
        item['RentID'] = 'NA'
        item['ConjunctionalAgencyContactName'] = 'NA'
        item['TypeString'] = 'NA'
        item['ResultItemName'] = 'NA'
        item['BreadCrumbItems'] = 'NA'
        item['DateUpdated'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[5]/text()').extract()[0].replace('\n',''))
        item['FirstPropertyTypeName'] = 'NA'
        item['DateEliteBilling'] = 'NA'
        item['TenantRentDetail'] = 'NA'
        item['SaleListingUrl'] = str(response.url)
        item['ConjunctionalAgencyLogoURL'] = 'NA'
        item['DisplayableAddress'] = str(sel.xpath('//*[@class="row address-bar"]/div[1]/h1/text()').extract()[0].replace('\n',''))
        item['PageID'] = 'NA'
        item['TitanContentType'] = 'NA'
        item['IsSPA'] = 'NA'
        item['TitanAdZone'] = 'NA'
        item['ctype'] = 'NA'
        item['Member'] = 'NA'
        item['SubCategory4'] = 'NA' 
        item['SubCategory2'] = 'NA'
        item['SubCategory3'] = 'NA'
        item['SubCategory1'] = 'NA'
        item['PageName'] = str(sel.xpath('//*[@class="no-side-margin"]/h1/text()').extract())[0]
        item['PageType'] = 'NA'
        item['PageDescription'] =  'NA'
        item['IsTitanEnabled'] = 'NA'
        item['PrimaryCategory'] =  'NA'
        item['AdSlots'] =  'NA'
        item['startDate'] =  'NA'
        item['name'] =  'NA'
        item['url'] = str(response.url)
        item['sameAs'] =  'NA'
        item['context'] =  'NA'
        item['addressLocality'] =  'NA'
        item['addressRegion'] =  'NA'
        item['streetAddress'] = 'NA' 
        item['postalCode'] =  'NA'
        item['type'] =  'NA'
        item['description'] =  'NA'
        item['TenantInfoTermOfLeaseFrom'] = 'NA' 
        item['TenantInfoTermOfLeaseTo'] = 'NA'
        item['AgencyContacts'] = 'NA'
        item['AgencyID'] = 'NA'
        item['IsYoutube'] = 'NA'
        item['Height'] = 'NA'
        item['Width'] = 'NA'
        item['YoutubeId'] = 'NA'
        item['VideoRequired'] = 'NA'
        item['VideoSrc'] = 'NA'
        item['Autoplay'] = 'NA'

        soup = BeautifulSoup((requests.get(response.url)).text, 'html.parser')
        imgs = soup.findAll('img')
        count = 0
        for im in imgs:
            item['ImageNumber_'+str(count)+'_url'] =  im.attrs['src']
            item['ImageNumber_'+str(count)+'_url_transformed'] = im.attrs['src']
            count +=1

        for i in range(count, 30):
            item['ImageNumber_'+str(count)+'_url'] =  "NA"
            item['ImageNumber_'+str(count)+'_url_transformed'] = "NA"
            i +=1
            
        agent = soup.findAll(class_ = 'agent')
        count1 = 0
        
        for a in agent:
            item['Agent_'+str(count1)+'_Fax'] = 'NA'
            item['Agent_'+str(count1)+'_MugshotUrl'] = 'NA'
            elem = requests.get('http://www.commercialview.com.au' + a.find(class_="mobile").find('a')['href'])  
            item['Agent_'+str(count1)+'_Mobile'] = re.findall(r'text\((.*?)\);', elem.text)[0].replace('"','')
            item['Agent_'+str(count1)+'_Telephone'] = 'NA'
            item['Agent_'+str(count1)+'_Address'] ='NA'
            item['Agent_'+str(count1)+'_FullName'] = a.find(class_='name').contents

        for i in range(count1, 20):
            item['Agent_'+str(i)+'_Fax'] = 'NA'
            item['Agent_'+str(i)+'_MugshotUrl'] = 'NA'                      
            item['Agent_'+str(i)+'_Mobile'] = 'NA'
            item['Agent_'+str(i)+'_Telephone'] = 'NA'
            item['Agent_'+str(i)+'_Address'] ='NA'
            item['Agent_'+str(i)+'_FullName'] = 'NA'
             
        print item
        return item
