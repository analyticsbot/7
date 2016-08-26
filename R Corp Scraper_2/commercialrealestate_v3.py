import requests, json, re, ast, csv, hashlib
import pandas as pd

__hdr = ['IsGoogleIndexRequired', 'PageTitle', 'DisplayablePrice', 'ConjunctionalAgencyColour', 'PropertyDetailsUrl', \
         'ConjunctionalAgencyBannerURL', 'OccupancyStatus', 'TruncatedDescription', 'ConjunctionalAgencyContactPhone', \
         'ParkingOptions', 'DisplayableAddressStreet', 'RecommendedListingViewModel', 'Suburb', 'DateFirstListed', 'SaleID', \
         'EoiRecipientName', 'AgencyBannerUrlCre', 'HasInspections', 'PropertyWebLink', 'EoiDeliveryAddress', 'CardType', 'Inspections', \
         'Availability', 'State', 'TenderDeliveryAddress', 'Type', 'AgencyAddress', 'LeaseListingUrl', 'InspectionTime', \
         'ConjunctionalAgencyId', 'DisplayableAddressSuburb', 'Categories', 'Postcode', 'AuctionDate', 'AgencyLogoURLCRE', \
         'VideoURL', 'ConjunctionAgency', 'ListingCategory', 'BuildingType', 'TenderEndDateAndTime', 'ConjunctionalAgencyLogoLargeURL', \
         'LeaseEndDate', 'CaptionType', 'LastUpdated', 'BrandingBannerUrl', 'AgencyId', 'AgencyName', 'PrimaryAgencyColor', 'Address', \
         'ListingContacts', 'LogoUrl', 'PriceDisplayText', 'AdID', 'Images', 'BuildArea', 'MapLongitude', 'LeaseStartDate', \
         'DisplayAddressType', 'AgencyLogoLargeURLCRE', 'TenantName', 'UnitDetails', 'DatePlatinumBilling', 'AnnualReturn', \
         'AuctionAddress', 'VideoInfo', 'LeaseOptions', 'LandArea', 'DisplayableAddressTruncated', 'SaleType', \
         'ConjunctionalAgencyAddress', 'AuctionTerms', 'NabersRating', 'TenantInformation', 'IsArchived', 'TenderRecipientName', \
         'EoiEndDateAndTime', 'Parking', 'PrimaryImageFullSizeUrl', 'Headline', 'MapLatitude', 'ConjunctionalAgencyName', 'AdFormat', \
         'Description', 'BuildOrLandArea', 'EoiEndDate', 'VirtualTourUrl', 'PdfUploads', 'RentID', 'ConjunctionalAgencyContactName', \
         'TypeString', 'ResultItemName', 'BreadCrumbItems', 'DateUpdated', 'FirstPropertyTypeName', 'DateEliteBilling', 'TenantRentDetail', \
         'SaleListingUrl', 'ConjunctionalAgencyLogoURL', 'DisplayableAddress', 'PageID', 'TitanContentType', 'IsSPA', 'TitanAdZone', \
         'ctype', 'Member', 'SubCategory4', 'SubCategory2', 'SubCategory3', 'SubCategory1', 'PageName', 'PageType', 'PageDescription', \
         'IsTitanEnabled', 'PrimaryCategory', 'AdSlots', 'startDate', 'name', 'url', 'sameAs', 'context', 'addressLocality', \
         'addressRegion', 'streetAddress', 'postalCode', 'type', 'description', 'ListingInspectionKnowledgeGraph', 'ImageNumber_0_url', \
         'ImageNumber_0_url_transformed', 'ImageNumber_1_url', 'ImageNumber_1_url_transformed', 'ImageNumber_2_url', \
         'ImageNumber_2_url_transformed', 'ImageNumber_3_url', 'ImageNumber_3_url_transformed', 'ImageNumber_4_url', \
         'ImageNumber_4_url_transformed', 'ImageNumber_5_url', 'ImageNumber_5_url_transformed', 'ImageNumber_6_url', \
         'ImageNumber_6_url_transformed', 'ImageNumber_7_url', 'ImageNumber_7_url_transformed', 'ImageNumber_8_url', \
         'ImageNumber_8_url_transformed', 'ImageNumber_9_url', 'ImageNumber_9_url_transformed', 'ImageNumber_10_url', \
         'ImageNumber_10_url_transformed', 'ImageNumber_11_url', 'ImageNumber_11_url_transformed', 'ImageNumber_12_url', \
         'ImageNumber_12_url_transformed', 'ImageNumber_13_url', 'ImageNumber_13_url_transformed', 'ImageNumber_14_url', \
         'ImageNumber_14_url_transformed', 'ImageNumber_15_url', 'ImageNumber_15_url_transformed', 'ImageNumber_16_url', \
         'ImageNumber_16_url_transformed', 'ImageNumber_17_url', 'ImageNumber_17_url_transformed', 'ImageNumber_18_url', \
         'ImageNumber_18_url_transformed', 'ImageNumber_19_url', 'ImageNumber_19_url_transformed', 'Agent_0_Fax', 'Agent_0_MugshotUrl', \
         'Agent_0_Mobile', 'Agent_0_Telephone', 'Agent_0_Address', 'Agent_0_FullName', 'Agent_1_Fax', 'Agent_1_MugshotUrl', \
         'Agent_1_Mobile', 'Agent_1_Telephone', 'Agent_1_Address', 'Agent_1_FullName', 'Agent_2_Fax', 'Agent_2_MugshotUrl', \
         'Agent_2_Mobile', 'Agent_2_Telephone', 'Agent_2_Address', 'Agent_2_FullName', 'Agent_3_Fax', 'Agent_3_MugshotUrl', \
         'Agent_3_Mobile', 'Agent_3_Telephone', 'Agent_3_Address', 'Agent_3_FullName', 'Agent_4_Fax', 'Agent_4_MugshotUrl', \
         'Agent_4_Mobile', 'Agent_4_Telephone', 'Agent_4_Address', 'Agent_4_FullName', 'Agent_5_Fax', 'Agent_5_MugshotUrl', \
         'Agent_5_Mobile', 'Agent_5_Telephone', 'Agent_5_Address', 'Agent_5_FullName', 'Agent_6_Fax', 'Agent_6_MugshotUrl', \
         'Agent_6_Mobile', 'Agent_6_Telephone', 'Agent_6_Address', 'Agent_6_FullName', 'Agent_7_Fax', 'Agent_7_MugshotUrl',\
         'Agent_7_Mobile', 'Agent_7_Telephone', 'Agent_7_Address', 'Agent_7_FullName', 'Agent_8_Fax', 'Agent_8_MugshotUrl', \
         'Agent_8_Mobile', 'Agent_8_Telephone', 'Agent_8_Address', 'Agent_8_FullName', 'Agent_9_Fax', 'Agent_9_MugshotUrl', \
         'Agent_9_Mobile', 'Agent_9_Telephone', 'Agent_9_Address', 'Agent_9_FullName', 'Agent_10_Fax', 'Agent_10_MugshotUrl', \
         'Agent_10_Mobile', 'Agent_10_Telephone', 'Agent_10_Address', 'Agent_10_FullName', 'Agent_11_Fax', 'Agent_11_MugshotUrl', \
         'Agent_11_Mobile', 'Agent_11_Telephone', 'Agent_11_Address', 'Agent_11_FullName', 'Agent_12_Fax', 'Agent_12_MugshotUrl', \
         'Agent_12_Mobile', 'Agent_12_Telephone', 'Agent_12_Address', 'Agent_12_FullName', 'Agent_13_Fax', 'Agent_13_MugshotUrl', \
         'Agent_13_Mobile', 'Agent_13_Telephone', 'Agent_13_Address', 'Agent_13_FullName', 'Agent_14_Fax', 'Agent_14_MugshotUrl',\
         'Agent_14_Mobile', 'Agent_14_Telephone', 'Agent_14_Address', 'Agent_14_FullName', 'Agent_15_Fax', 'Agent_15_MugshotUrl', \
         'Agent_15_Mobile', 'Agent_15_Telephone', 'Agent_15_Address', 'Agent_15_FullName', 'Agent_16_Fax', 'Agent_16_MugshotUrl', \
         'Agent_16_Mobile', 'Agent_16_Telephone', 'Agent_16_Address', 'Agent_16_FullName', 'Agent_17_Fax', 'Agent_17_MugshotUrl', \
         'Agent_17_Mobile', 'Agent_17_Telephone', 'Agent_17_Address', 'Agent_17_FullName', 'Agent_18_Fax', 'Agent_18_MugshotUrl', \
         'Agent_18_Mobile', 'Agent_18_Telephone', 'Agent_18_Address', 'Agent_18_FullName', 'Agent_19_Fax', 'Agent_19_MugshotUrl', \
         'Agent_19_Mobile', 'Agent_19_Telephone', 'Agent_19_Address', 'Agent_19_FullName','TenantInfoTermOfLeaseFrom', \
         'TenantInfoTermOfLeaseTo','AgencyContacts', 'IsYoutube', 'Height', 'Width', 'YoutubeId', 'VideoRequired', 'VideoSrc', 'Autoplay']
values = ['NA']*len(__hdr)
__headr = []
pg_num = 0

new_headers = []

try:
    df = pd.read_csv('commercialrealestate_listing_url.csv')
except:
    cols = ['URLs', 'Hash_url', 'Crawled']
    df = pd.DataFrame(columns=cols)

def returnURL(pg_num):
    return 'http://www.commercialrealestate.com.au/for-sale/?pn=' + str(pg_num) + '&so=2&bb=-32.23626626934806%2C-41.14991096942575%2C153.44867726562507%2C136.28803273437507%2C6&format=json'

##while True:
##    pg_num +=1
##    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
##    headers = {'content-type': 'application/json', 'User-Agent': user_agent,\
##               'Connection':'keep-alive', 'Accept-Encoding':'gzip, deflate',\
##               'Accept-Language':'en-US,en;q=0.8', 
##               'Origin': 'http://www.commercialrealestate.com.au/',\
##               'Referer':'http://www.commercialrealestate.com.au/'}
##
##    response = requests.get(returnURL(pg_num), headers=headers, allow_redirects=True)
##    
##    if response.status_code==200:        
##        json_response = json.loads(response.text)
##
##        resulItems = json_response['ResultItems']
##        for resulItem in resulItems:
##            nrows = df.shape[0]
##            url = resulItem['PropertyDetailsUrl']
##            hash_url = hashlib.md5(url).hexdigest()
##
##            if df.query('Hash_url == "' + hash_url + '"').shape[0] == 0:
##                df.loc[nrows] = [url, hash_url, 'N' ]
##    else:
##        break
##
##    if pg_num==100:
##        break

df.to_csv('commercialrealestate_listing_url.csv', index = False)

def getPageElements(url):
    response = requests.get(url ,allow_redirects=True)
    text = response.text
    soup = re.findall(r'listing:\s(.*?);\s*setTimeout',text)[0]
                                                                    
    
    d = ast.literal_eval(soup.replace('\\r\\n','').replace('@','').replace('/\u003e','').\
                         replace('\u0026','').\
      replace('\u003cbr','').replace('\u003e','').replace('"Land',"'Land").replace('Sqm"', "Sqm'").replace('\u003c','').\
      replace('\\"','"').replace('"Former',"'Former").replace('site"',"site'").replace('"{"context"','{"context"').\
      replace('","ListingInspectionKnowledgeGraph',\
              ',"ListingInspectionKnowledgeGraph')[:-1].replace('null',\
                                                                '"NULL"').\
                                                                replace('false',\
                                                                'False').replace('true',\
                                                                'True').replace('\u0026amp;','').replace('b/b *','').replace('\\r',''))

    return d
                    
def myprint(d):
  for k, v in d.iteritems():
    if isinstance(v, dict):
      myprint(v)
    else:
        if k not in __headr:
            try:
                ix= __hdr.index(k)
                values[ix] = v
                #print len(values)
                if k == 'Images':
                    images = v
                    count = -1
                    for image in images:
                        count +=1
                        for key, value in image.iteritems():
                            if key =='ImageNumber':
                                new_key = 'ImageNumber_'+str(count)+'_url'
                                new_key_transformed = 'ImageNumber_'+str(count)+'_url_transformed'
                                ix1 = __hdr.index(new_key)
                                ix2 = __hdr.index(new_key_transformed)
                                values[ix1] =image['FullSizeUrl']
                                values[ix2] ='http://res-1.cloudinary.com/cre/image/fetch/' + image['FullSizeUrl'].replace('://','%3A%2F%2F').replace('/','%2F')
                                
                elif k == 'ListingContacts':
                    contacts =  v
                    count1 = -1
                    for contact in contacts:
                        count1 +=1
                        
                        for key1, value1 in contact.iteritems():
                            #print 'Agent_'+str(count1) + '_' + key1
                            
                            ix3 = __hdr.index('Agent_'+str(count1) + '_' +  key1)
                            #print ix3
                            values[ix3] = value1
            except Exception,e:
                print e
                error = str(e).replace(' is not in list','')
                new_headers.append(error)

o = open('commercial_real_estate_data.csv', 'wb')
writer = csv.writer(o)
writer.writerow(__hdr)

df = pd.read_csv('commercialrealestate_listing_url.csv')

for i, row in df.iterrows():
    values = ['NA']*len(__hdr)
    url = row[0]
    crawled = row[2]
    print url, '*** ', crawled
    if crawled =='N':
        values = ['NA']*len(__hdr)
        dict_obj_from_page = getPageElements(url)
        myprint(dict_obj_from_page)
        writer.writerow(values)
        #df.loc[i, 'Crawled'] = 'Y'

        #print values

    
            

df.to_csv('commercialrealestate_listing_url.csv', index = False)
o.close()


