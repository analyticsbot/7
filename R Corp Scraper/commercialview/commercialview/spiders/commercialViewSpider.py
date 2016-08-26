from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from commercialview.items import CommercialviewItem
from scrapy.selector import Selector
from scrapy.http import Request
import datetime
import requests, re, hashlib
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import pandas as pd

class CommercialView(CrawlSpider):
    name = "commercialview"
    allowed_domains = ["commercialview.com.au"]
    start_urls = [
        "http://www.commercialview.com.au/search?utf8=%E2%9C%93&search%5Bsale_lease%5D=sale&search%5Bsuburb_hint%5D=&search%5Bproperty_types%5D=&search%5Bquery%5D=&search%5Bmin_sale_price%5D=&search%5Bmax_sale_price%5D=&search%5Bradius%5D=10"
]
    rules = [Rule(LinkExtractor( allow = ['search\?page=']),                   
                   process_links='process_links',
                  callback='parse_item',                   
                   follow=False)]
    __hdr = ['dateCrawled', 'source', 'IsGoogleIndexRequired', 'PageTitle', 'DisplayablePrice', 'ConjunctionalAgencyColour', 'PropertyDetailsUrl', 'ConjunctionalAgencyBannerURL', 'OccupancyStatus', 'TruncatedDescription', 'ConjunctionalAgencyContactPhone', 'ParkingOptions', 'DisplayableAddressStreet', 'RecommendedListingViewModel', 'Suburb', 'DateFirstListed', 'SaleID', 'EoiRecipientName', 'AgencyBannerUrlCre', 'HasInspections', 'PropertyWebLink', 'EoiDeliveryAddress', 'CardType', 'Inspections', 'Availability', 'State', 'TenderDeliveryAddress', 'Type', 'AgencyAddress', 'LeaseListingUrl', 'InspectionTime', 'ConjunctionalAgencyId', 'DisplayableAddressSuburb', 'Categories', 'Postcode', 'AuctionDate', 'AgencyLogoURLCRE', 'VideoURL', 'ConjunctionAgency', 'ListingCategory', 'BuildingType', 'TenderEndDateAndTime', 'ConjunctionalAgencyLogoLargeURL', 'LeaseEndDate', 'CaptionType', 'LastUpdated', 'BrandingBannerUrl', 'AgencyId', 'AgencyName', 'PrimaryAgencyColor', 'Address', 'ListingContacts', 'LogoUrl', 'PriceDisplayText', 'AdID', 'Images', 'BuildArea', 'MapLongitude', 'LeaseStartDate', 'DisplayAddressType', 'AgencyLogoLargeURLCRE', 'TenantName', 'UnitDetails', 'DatePlatinumBilling', 'AnnualReturn', 'AuctionAddress', 'VideoInfo', 'LeaseOptions', 'LandArea', 'DisplayableAddressTruncated', 'SaleType', 'ConjunctionalAgencyAddress', 'AuctionTerms', 'NabersRating', 'TenantInformation', 'IsArchived', 'TenderRecipientName', 'EoiEndDateAndTime', 'Parking', 'PrimaryImageFullSizeUrl', 'Headline', 'MapLatitude', 'ConjunctionalAgencyName', 'AdFormat', 'Description', 'BuildOrLandArea', 'EoiEndDate', 'VirtualTourUrl', 'PdfUploads', 'RentID', 'ConjunctionalAgencyContactName', 'TypeString', 'ResultItemName', 'BreadCrumbItems', 'DateUpdated', 'FirstPropertyTypeName', 'DateEliteBilling', 'TenantRentDetail', 'SaleListingUrl', 'ConjunctionalAgencyLogoURL', 'DisplayableAddress', 'PageID', 'TitanContentType', 'IsSPA', 'TitanAdZone', 'ctype', 'Member', 'SubCategory4', 'SubCategory2', 'SubCategory3', 'SubCategory1', 'PageName', 'PageType', 'PageDescription', 'IsTitanEnabled', 'PrimaryCategory', 'AdSlots', 'startDate', 'name', 'url', 'sameAs', 'context', 'addressLocality', 'addressRegion', 'streetAddress', 'postalCode', 'type', 'description', 'ListingInspectionKnowledgeGraph', 'ImageNumber_0_url', 'ImageNumber_0_url_transformed', 'ImageNumber_1_url', 'ImageNumber_1_url_transformed', 'ImageNumber_2_url', 'ImageNumber_2_url_transformed', 'ImageNumber_3_url', 'ImageNumber_3_url_transformed', 'ImageNumber_4_url', 'ImageNumber_4_url_transformed', 'ImageNumber_5_url', 'ImageNumber_5_url_transformed', 'ImageNumber_6_url', 'ImageNumber_6_url_transformed', 'ImageNumber_7_url', 'ImageNumber_7_url_transformed', 'ImageNumber_8_url', 'ImageNumber_8_url_transformed', 'ImageNumber_9_url', 'ImageNumber_9_url_transformed', 'ImageNumber_10_url', 'ImageNumber_10_url_transformed', 'ImageNumber_11_url', 'ImageNumber_11_url_transformed', 'ImageNumber_12_url', 'ImageNumber_12_url_transformed', 'ImageNumber_13_url', 'ImageNumber_13_url_transformed', 'ImageNumber_14_url', 'ImageNumber_14_url_transformed', 'ImageNumber_15_url', 'ImageNumber_15_url_transformed', 'ImageNumber_16_url', 'ImageNumber_16_url_transformed', 'ImageNumber_17_url', 'ImageNumber_17_url_transformed', 'ImageNumber_18_url', 'ImageNumber_18_url_transformed', 'ImageNumber_19_url', 'ImageNumber_19_url_transformed', 'ImageNumber_20_url', 'ImageNumber_20_url_transformed', 'ImageNumber_21_url', 'ImageNumber_21_url_transformed', 'ImageNumber_22_url', 'ImageNumber_22_url_transformed', 'ImageNumber_23_url', 'ImageNumber_23_url_transformed', 'ImageNumber_24_url', 'ImageNumber_24_url_transformed', 'ImageNumber_25_url', 'ImageNumber_25_url_transformed', 'ImageNumber_26_url', 'ImageNumber_26_url_transformed', 'ImageNumber_27_url', 'ImageNumber_27_url_transformed', 'ImageNumber_28_url', 'ImageNumber_28_url_transformed', 'ImageNumber_29_url', 'ImageNumber_29_url_transformed', 'Agent_0_Fax', 'Agent_0_MugshotUrl', 'Agent_0_Mobile', 'Agent_0_Telephone', 'Agent_0_Address', 'Agent_0_FullName', 'Agent_1_Fax', 'Agent_1_MugshotUrl', 'Agent_1_Mobile', 'Agent_1_Telephone', 'Agent_1_Address', 'Agent_1_FullName', 'Agent_2_Fax', 'Agent_2_MugshotUrl', 'Agent_2_Mobile', 'Agent_2_Telephone', 'Agent_2_Address', 'Agent_2_FullName', 'Agent_3_Fax', 'Agent_3_MugshotUrl', 'Agent_3_Mobile', 'Agent_3_Telephone', 'Agent_3_Address', 'Agent_3_FullName', 'Agent_4_Fax', 'Agent_4_MugshotUrl', 'Agent_4_Mobile', 'Agent_4_Telephone', 'Agent_4_Address', 'Agent_4_FullName', 'Agent_5_Fax', 'Agent_5_MugshotUrl', 'Agent_5_Mobile', 'Agent_5_Telephone', 'Agent_5_Address', 'Agent_5_FullName', 'Agent_6_Fax', 'Agent_6_MugshotUrl', 'Agent_6_Mobile', 'Agent_6_Telephone', 'Agent_6_Address', 'Agent_6_FullName', 'Agent_7_Fax', 'Agent_7_MugshotUrl', 'Agent_7_Mobile', 'Agent_7_Telephone', 'Agent_7_Address', 'Agent_7_FullName', 'Agent_8_Fax', 'Agent_8_MugshotUrl', 'Agent_8_Mobile', 'Agent_8_Telephone', 'Agent_8_Address', 'Agent_8_FullName', 'Agent_9_Fax', 'Agent_9_MugshotUrl', 'Agent_9_Mobile', 'Agent_9_Telephone', 'Agent_9_Address', 'Agent_9_FullName', 'Agent_10_Fax', 'Agent_10_MugshotUrl', 'Agent_10_Mobile', 'Agent_10_Telephone', 'Agent_10_Address', 'Agent_10_FullName', 'Agent_11_Fax', 'Agent_11_MugshotUrl', 'Agent_11_Mobile', 'Agent_11_Telephone', 'Agent_11_Address', 'Agent_11_FullName', 'Agent_12_Fax', 'Agent_12_MugshotUrl', 'Agent_12_Mobile', 'Agent_12_Telephone', 'Agent_12_Address', 'Agent_12_FullName', 'Agent_13_Fax', 'Agent_13_MugshotUrl', 'Agent_13_Mobile', 'Agent_13_Telephone', 'Agent_13_Address', 'Agent_13_FullName', 'Agent_14_Fax', 'Agent_14_MugshotUrl', 'Agent_14_Mobile', 'Agent_14_Telephone', 'Agent_14_Address', 'Agent_14_FullName', 'Agent_15_Fax', 'Agent_15_MugshotUrl', 'Agent_15_Mobile', 'Agent_15_Telephone', 'Agent_15_Address', 'Agent_15_FullName', 'Agent_16_Fax', 'Agent_16_MugshotUrl', 'Agent_16_Mobile', 'Agent_16_Telephone', 'Agent_16_Address', 'Agent_16_FullName', 'Agent_17_Fax', 'Agent_17_MugshotUrl', 'Agent_17_Mobile', 'Agent_17_Telephone', 'Agent_17_Address', 'Agent_17_FullName', 'Agent_18_Fax', 'Agent_18_MugshotUrl', 'Agent_18_Mobile', 'Agent_18_Telephone', 'Agent_18_Address', 'Agent_18_FullName', 'Agent_19_Fax', 'Agent_19_MugshotUrl', 'Agent_19_Mobile', 'Agent_19_Telephone', 'Agent_19_Address', 'Agent_19_FullName','TenantInfoTermOfLeaseFrom', 'TenantInfoTermOfLeaseTo','AgencyContacts', 'AgencyID', 'IsYoutube', 'Height', 'Width', 'YoutubeId', 'VideoRequired', 'VideoSrc', 'Autoplay']

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
            item['url'] = link
            link = 'http://www.commercialview.com.au' + str(link[0])
            url = str(link)
            try:
                df = pd.read_csv('commercial_view_listing_url.csv')
            except:
                cols = ['URLs', 'Hash_url', 'Crawled']
                df = pd.DataFrame(columns=cols)
            nrows = df.shape[0]
            hash_url = hashlib.md5(link).hexdigest()
            if df.query('Hash_url == "' + hash_url + '"').shape[0] == 0:
                df.loc[nrows] = [url, hash_url, 'N' ]
                new_request = Request(link, callback=self.parse_file_page)
                new_request.meta['item'] = item
                yield new_request
                df.loc[nrows] = [url, hash_url, 'Y' ]
            #items.append(item)
            df.to_csv('commercial_view_listing_url.csv', index = False)
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
        values = ['NA']*len(self.__hdr)      
        
        item = response.meta['item']
        #selector
        sel = Selector(response)
        geolocator = Nominatim()
        title = str(sel.xpath('//*[@class="row address-bar"]/div[1]/h1/text()').extract()[0].replace('\n',''))           
        
        try:
            location = geolocator.geocode(title)
        except:
            location = 'NA'
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
        item['State'] = str(title.split(',')[1]).split()[-1]
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
        try:
            item['LastUpdated'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[5]/text()').extract()[0].replace('\n',''))
        except:
            item['LastUpdated'] = 
        item['BrandingBannerUrl'] = 'NA'
        item['AgencyId'] = str(sel.xpath('//*[@itemprop="seller"]/h4/a/@href').extract()[0].replace('\n','')).split('/')[-1] 
        item['AgencyName'] = str(sel.xpath('//*[@itemprop="seller"]/h4/a/text()').extract()[0].replace('\n',''))
        item['PrimaryAgencyColor'] = 'NA'
        item['Address'] = str(sel.xpath('//*[@class="row address-bar"]/div[1]/h1/text()').extract()[0].replace('\n','').encode("ascii","ignore"))
        item['ListingContacts'] = 'NA'
        item['LogoUrl'] = 'NA'
        item['PriceDisplayText'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[4]/text()').extract()[0].replace('\n','').encode("ascii","ignore"))
        item['AdID'] = str(sel.xpath('//*[@class="attributes"]/dl/dd[1]/text()').extract()[0].replace('\n',''))
        item['Images'] = 'NA'
        item['BuildArea'] = str(sel.xpath('//*[@class="row info-bar-with-icons"]/div[3]/p/text()'). extract()[0].replace('\n',''))
        try:
            item['MapLongitude'] = location.longitude
        except:
            item['MapLongitude'] = 'NA'
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
        item['Headline'] = str(sel.xpath('//*[@itemprop="name"]/h2/text()').extract()[0].encode("ascii","ignore"))
        try:
            item['MapLatitude'] = location.latitude
        except:
            item['MapLatitude'] = 'NA'
        item['ConjunctionalAgencyName'] = 'NA'
        item['AdFormat'] = 'NA'
        item['Description'] = self.makeGood(''.join([self.makeGood(str(el.replace('\n','').encode("ascii","ignore"))) for el in sel.xpath('//*[@class="description"]/p/text()').extract()]))
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
            try:
                if im.attrs['itemprop'] == 'image':
                    item['ImageNumber_'+str(count)+'_url'] =  im.attrs['src']
                    item['ImageNumber_'+str(count)+'_url_transformed'] = im.attrs['src']
                    count +=1
            except:
                pass

        for i in range(count, 30):
            item['ImageNumber_'+str(count)+'_url'] =  "NA"
            item['ImageNumber_'+str(count)+'_url_transformed'] = "NA"
            
        agent = soup.findAll(class_ = 'agent')
        count1 = 0        
        for a in agent:
            item['Agent_'+str(count1)+'_Fax'] = 'NA'
            item['Agent_'+str(count1)+'_MugshotUrl'] = 'NA'
            try:
                elem = requests.get('http://www.commercialview.com.au' + a.find(class_="mobile").find('a')['href'])  
                item['Agent_'+str(count1)+'_Mobile'] = re.findall(r'text\((.*?)\);', elem.text)[0].replace('"','')
            except:
                item['Agent_'+str(count1)+'_Mobile'] = 'NA'
            item['Agent_'+str(count1)+'_Telephone'] = 'NA'
            item['Agent_'+str(count1)+'_Address'] ='NA'
            try:
                item['Agent_'+str(count1)+'_FullName'] = a.find(class_='name').contents[0]
            except:
                item['Agent_'+str(count1)+'_FullName'] = 'NA'
            count1 +=1

        for i in range(count1, 20):
            item['Agent_'+str(i)+'_Fax'] = 'NA'
            item['Agent_'+str(i)+'_MugshotUrl'] = 'NA'                      
            item['Agent_'+str(i)+'_Mobile'] = 'NA'
            item['Agent_'+str(i)+'_Telephone'] = 'NA'
            item['Agent_'+str(i)+'_Address'] ='NA'
            item['Agent_'+str(i)+'_FullName'] = 'NA'
        
        return item
