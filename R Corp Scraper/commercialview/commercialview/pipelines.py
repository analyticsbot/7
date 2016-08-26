# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
import pandas as pd
from openpyxl import load_workbook

class CommercialviewPipeline(object):
    def process_item(self, item, spider):
        return item

class MyPipeline(object):
    
    def __init__(self):        
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
        self.__hdr = ['dateCrawled', 'source', 'IsGoogleIndexRequired', 'PageTitle', 'DisplayablePrice', 'ConjunctionalAgencyColour', 'PropertyDetailsUrl', 'ConjunctionalAgencyBannerURL', 'OccupancyStatus', 'TruncatedDescription', 'ConjunctionalAgencyContactPhone', 'ParkingOptions', 'DisplayableAddressStreet', 'RecommendedListingViewModel', 'Suburb', 'DateFirstListed', 'SaleID', 'EoiRecipientName', 'AgencyBannerUrlCre', 'HasInspections', 'PropertyWebLink', 'EoiDeliveryAddress', 'CardType', 'Inspections', 'Availability', 'State', 'TenderDeliveryAddress', 'Type', 'AgencyAddress', 'LeaseListingUrl', 'InspectionTime', 'ConjunctionalAgencyId', 'DisplayableAddressSuburb', 'Categories', 'Postcode', 'AuctionDate', 'AgencyLogoURLCRE', 'VideoURL', 'ConjunctionAgency', 'ListingCategory', 'BuildingType', 'TenderEndDateAndTime', 'ConjunctionalAgencyLogoLargeURL', 'LeaseEndDate', 'CaptionType', 'LastUpdated', 'BrandingBannerUrl', 'AgencyId', 'AgencyName', 'PrimaryAgencyColor', 'Address', 'ListingContacts', 'LogoUrl', 'PriceDisplayText', 'AdID', 'Images', 'BuildArea', 'MapLongitude', 'LeaseStartDate', 'DisplayAddressType', 'AgencyLogoLargeURLCRE', 'TenantName', 'UnitDetails', 'DatePlatinumBilling', 'AnnualReturn', 'AuctionAddress', 'VideoInfo', 'LeaseOptions', 'LandArea', 'DisplayableAddressTruncated', 'SaleType', 'ConjunctionalAgencyAddress', 'AuctionTerms', 'NabersRating', 'TenantInformation', 'IsArchived', 'TenderRecipientName', 'EoiEndDateAndTime', 'Parking', 'PrimaryImageFullSizeUrl', 'Headline', 'MapLatitude', 'ConjunctionalAgencyName', 'AdFormat', 'Description', 'BuildOrLandArea', 'EoiEndDate', 'VirtualTourUrl', 'PdfUploads', 'RentID', 'ConjunctionalAgencyContactName', 'TypeString', 'ResultItemName', 'BreadCrumbItems', 'DateUpdated', 'FirstPropertyTypeName', 'DateEliteBilling', 'TenantRentDetail', 'SaleListingUrl', 'ConjunctionalAgencyLogoURL', 'DisplayableAddress', 'PageID', 'TitanContentType', 'IsSPA', 'TitanAdZone', 'ctype', 'Member', 'SubCategory4', 'SubCategory2', 'SubCategory3', 'SubCategory1', 'PageName', 'PageType', 'PageDescription', 'IsTitanEnabled', 'PrimaryCategory', 'AdSlots', 'startDate', 'name', 'url', 'sameAs', 'context', 'addressLocality', 'addressRegion', 'streetAddress', 'postalCode', 'type', 'description', 'ListingInspectionKnowledgeGraph', 'ImageNumber_0_url', 'ImageNumber_0_url_transformed', 'ImageNumber_1_url', 'ImageNumber_1_url_transformed', 'ImageNumber_2_url', 'ImageNumber_2_url_transformed', 'ImageNumber_3_url', 'ImageNumber_3_url_transformed', 'ImageNumber_4_url', 'ImageNumber_4_url_transformed', 'ImageNumber_5_url', 'ImageNumber_5_url_transformed', 'ImageNumber_6_url', 'ImageNumber_6_url_transformed', 'ImageNumber_7_url', 'ImageNumber_7_url_transformed', 'ImageNumber_8_url', 'ImageNumber_8_url_transformed', 'ImageNumber_9_url', 'ImageNumber_9_url_transformed', 'ImageNumber_10_url', 'ImageNumber_10_url_transformed', 'ImageNumber_11_url', 'ImageNumber_11_url_transformed', 'ImageNumber_12_url', 'ImageNumber_12_url_transformed', 'ImageNumber_13_url', 'ImageNumber_13_url_transformed', 'ImageNumber_14_url', 'ImageNumber_14_url_transformed', 'ImageNumber_15_url', 'ImageNumber_15_url_transformed', 'ImageNumber_16_url', 'ImageNumber_16_url_transformed', 'ImageNumber_17_url', 'ImageNumber_17_url_transformed', 'ImageNumber_18_url', 'ImageNumber_18_url_transformed', 'ImageNumber_19_url', 'ImageNumber_19_url_transformed', 'ImageNumber_20_url', 'ImageNumber_20_url_transformed', 'ImageNumber_21_url', 'ImageNumber_21_url_transformed', 'ImageNumber_22_url', 'ImageNumber_22_url_transformed', 'ImageNumber_23_url', 'ImageNumber_23_url_transformed', 'ImageNumber_24_url', 'ImageNumber_24_url_transformed', 'ImageNumber_25_url', 'ImageNumber_25_url_transformed', 'ImageNumber_26_url', 'ImageNumber_26_url_transformed', 'ImageNumber_27_url', 'ImageNumber_27_url_transformed', 'ImageNumber_28_url', 'ImageNumber_28_url_transformed', 'ImageNumber_29_url', 'ImageNumber_29_url_transformed', 'Agent_0_Fax', 'Agent_0_MugshotUrl', 'Agent_0_Mobile', 'Agent_0_Telephone', 'Agent_0_Address', 'Agent_0_FullName', 'Agent_1_Fax', 'Agent_1_MugshotUrl', 'Agent_1_Mobile', 'Agent_1_Telephone', 'Agent_1_Address', 'Agent_1_FullName', 'Agent_2_Fax', 'Agent_2_MugshotUrl', 'Agent_2_Mobile', 'Agent_2_Telephone', 'Agent_2_Address', 'Agent_2_FullName', 'Agent_3_Fax', 'Agent_3_MugshotUrl', 'Agent_3_Mobile', 'Agent_3_Telephone', 'Agent_3_Address', 'Agent_3_FullName', 'Agent_4_Fax', 'Agent_4_MugshotUrl', 'Agent_4_Mobile', 'Agent_4_Telephone', 'Agent_4_Address', 'Agent_4_FullName', 'Agent_5_Fax', 'Agent_5_MugshotUrl', 'Agent_5_Mobile', 'Agent_5_Telephone', 'Agent_5_Address', 'Agent_5_FullName', 'Agent_6_Fax', 'Agent_6_MugshotUrl', 'Agent_6_Mobile', 'Agent_6_Telephone', 'Agent_6_Address', 'Agent_6_FullName', 'Agent_7_Fax', 'Agent_7_MugshotUrl', 'Agent_7_Mobile', 'Agent_7_Telephone', 'Agent_7_Address', 'Agent_7_FullName', 'Agent_8_Fax', 'Agent_8_MugshotUrl', 'Agent_8_Mobile', 'Agent_8_Telephone', 'Agent_8_Address', 'Agent_8_FullName', 'Agent_9_Fax', 'Agent_9_MugshotUrl', 'Agent_9_Mobile', 'Agent_9_Telephone', 'Agent_9_Address', 'Agent_9_FullName', 'Agent_10_Fax', 'Agent_10_MugshotUrl', 'Agent_10_Mobile', 'Agent_10_Telephone', 'Agent_10_Address', 'Agent_10_FullName', 'Agent_11_Fax', 'Agent_11_MugshotUrl', 'Agent_11_Mobile', 'Agent_11_Telephone', 'Agent_11_Address', 'Agent_11_FullName', 'Agent_12_Fax', 'Agent_12_MugshotUrl', 'Agent_12_Mobile', 'Agent_12_Telephone', 'Agent_12_Address', 'Agent_12_FullName', 'Agent_13_Fax', 'Agent_13_MugshotUrl', 'Agent_13_Mobile', 'Agent_13_Telephone', 'Agent_13_Address', 'Agent_13_FullName', 'Agent_14_Fax', 'Agent_14_MugshotUrl', 'Agent_14_Mobile', 'Agent_14_Telephone', 'Agent_14_Address', 'Agent_14_FullName', 'Agent_15_Fax', 'Agent_15_MugshotUrl', 'Agent_15_Mobile', 'Agent_15_Telephone', 'Agent_15_Address', 'Agent_15_FullName', 'Agent_16_Fax', 'Agent_16_MugshotUrl', 'Agent_16_Mobile', 'Agent_16_Telephone', 'Agent_16_Address', 'Agent_16_FullName', 'Agent_17_Fax', 'Agent_17_MugshotUrl', 'Agent_17_Mobile', 'Agent_17_Telephone', 'Agent_17_Address', 'Agent_17_FullName', 'Agent_18_Fax', 'Agent_18_MugshotUrl', 'Agent_18_Mobile', 'Agent_18_Telephone', 'Agent_18_Address', 'Agent_18_FullName', 'Agent_19_Fax', 'Agent_19_MugshotUrl', 'Agent_19_Mobile', 'Agent_19_Telephone', 'Agent_19_Address', 'Agent_19_FullName','TenantInfoTermOfLeaseFrom', 'TenantInfoTermOfLeaseTo','AgencyContacts', 'AgencyID', 'IsYoutube', 'Height', 'Width', 'YoutubeId', 'VideoRequired', 'VideoSrc', 'Autoplay']

    def spider_opened(self, spider):
        print("Pipeline.spider_opened called")
        try:
            self.book = load_workbook('commercial_view_data.xlsx')
            self.writer = pandas.ExcelWriter('commercial_view_data.xlsx') 
            self.writer.book = self.book
            self.writer.sheets = dict((ws.title, ws) for ws in self.book.worksheets)
        except:
            self.writer = pd.ExcelWriter('commercial_view_data.xlsx', engine='xlsxwriter')
            cols_data = self.__hdr
            self.df_data = pd.DataFrame(columns=cols_data)
        
    def spider_closed(self, spider):
        print("Pipeline.spider_closed called")
        self.df_data.to_excel(self.writer,'Sheet1', index = False, header=self.__hdr)
        self.writer.save()

    def makeGood(self, text):
        return ''.join([i if ord(i) < 128 else ' ' for i in text])

    def process_item(self, item, spider):
        if self.df_data.query('Address == "' +item['Address'] + '"').shape[0] == 0:
            print("Processsing item " + item['url'])
            values = ['NA']*len(self.__hdr)
            for key in item.keys():
                ix = self.__hdr.index(key)
                values[ix] = (item[key])
            nrow_data = self.df_data.shape[0]
            nrow_data +=1
            self.df_data.loc[nrow_data] =  values
