BEGIN TRANSACTION;
CREATE TABLE "Users" (
	`id`	INTEGER NOT NULL,
	`username`	VARCHAR NOT NULL UNIQUE,
	PRIMARY KEY(id)
);
INSERT INTO `Users` VALUES(1,'rrhoover');
INSERT INTO `Users` VALUES(2,'lastashero');
INSERT INTO `Users` VALUES(4,'monikkinom');
INSERT INTO `Users` VALUES(5,'pooran');
INSERT INTO `Users` VALUES(6,'vijayanands');
INSERT INTO `Users` VALUES(7,'AbhilashaDafria');
INSERT INTO `Users` VALUES(8,'Ravi');
INSERT INTO `Users` VALUES(9,'gagarwal89');
INSERT INTO `Users` VALUES(10,'user_name');
INSERT INTO `Users` VALUES(11,'agarwal__gaurav');
INSERT INTO `Users` VALUES(12,'swamidigital');
CREATE TABLE "TwitterKeys" (
	`Username`	TEXT,
	`Password`	TEXT,
	`ConsumerKey`	TEXT,
	`ConsumerSecret`	TEXT,
	`AccessToken`	TEXT,
	`TokenSecret`	TEXT,
	`id`	INTEGER,
	`inUse`	INTEGER,
	PRIMARY KEY(id)
);
INSERT INTO `TwitterKeys` VALUES('RoyHelfer','oOP2111vxznl885','AQpzokfQTPmKdRTIgbMmuRV6n','Z2bvoZI3XIZJ0YU8arHYHEX6UdXjDGWwRO2VpNSZe7UHEKFODl','4365741082-gq3LN5lv6Q2jTuWWoOeoxcAZICiLcIsLOWcFZj2','zS5mJQD4o5ZW07RXTZdQGxqrJYYEKqN5Xlirmtwek6fI9',1,1);
INSERT INTO `TwitterKeys` VALUES('GeorgeEgleton','fUV7342jgpju123','J1nCoRoMxkouE9KxRdhXYgE0V','2gr6mi7Ag09uE09DAK9oRqMEtYSdNVm1dS5HrD1J0hYzVcSrqy','4361202442-B3KllLunAKgtlshwJNF3zCNiSgAzEQEGseUsQin','2el7RnXjBq44uJMDH5T3nLFngIGufAJuxzNCpVZsIrWsl',2,1);
INSERT INTO `TwitterKeys` VALUES('BaoSilbaugh','wLbZ6YUk6ynNd748','R50DSnVLM879Gsf5Wf2GEvUmw','zyhnlQqSvJOFz2WRkSHfK7lnT8HcJKWKLeDgupvEfFLbSIssdt','4381536681-t7QQ5W2GAjpvpCVnlVLfQgaCFUMJRdv1SGQMiEf','p2UrtV7AuxedXO0lNvJc0jxJJ5kDx545QhoYm827Vy4ve',3,1);
INSERT INTO `TwitterKeys` VALUES('LeeDeveja','aAB3736dnztz101','vxmZltjT3cQod9asbOWR1m2fP','9CWLeaufHn5nsdP6ffyS3qQzq9aO0Q9hChGolFy59mNMzM4RRd','4370012183-6Yw7kM065ogjywXSBBAJwlAewjKTEaML8ZYNAVv','U5quGKaC7JgEONww1l2cq6Jb5yz1BnexbG4IUDT6fXn9J',4,1);
INSERT INTO `TwitterKeys` VALUES('YungChadick','jnPS2JSGviXq889','CElS7SynSCds1yD6Hln6nHzCK','GYjnFP5KAVpdCrkLbh0xbm4gRbLXLCfPhh2qbJEfz66elNZ9Ym','4398572841-v8BZsirS2U6mo4ZODI8pD5Qav2hjE3493NVJjWG','ziTHb6lBftsOMzI43sPL86JLkZHkZFECJ90X97S4BIFK7',5,1);
INSERT INTO `TwitterKeys` VALUES('FreddyThieme','qEF3871jjiij669','Z1X2OqE0n08iRSaPngrIeDH0U','bHC22hzx4hBYXSCx94fFjrGJ9NCZpKuOEmGMVxyJlcuPj6W1Oh','4387427255-6u5T2jjfoJ10LXFcJpiTvXeLvxoCGFxn0Im4NlV','9C4WBtupykKWIX1LT6mSXsAyMazINKZpiO6IpUEPyaeyy',6,1);
INSERT INTO `TwitterKeys` VALUES('AlaineFarney','jUV5126perqq321','deb73e62sY86kwxiZOaDcUy6V','niJbC9SxCLDD82dDPn9ZmVtPqHQAeEARxEEV4R0bUGT3ATrsoK','4368153616-QqOGvBqovrubKJdi1sUzEyhCrOrKq2g3zDVNCvB','QYZW4Vsv2NmwWjx8n8C8elI0gP5EeTJoS6HZcRzHhPX6R',7,0);
INSERT INTO `TwitterKeys` VALUES('GeraldMulhollen','uKL2828aasnf321','FMlM1gZ2WWqH4L7QyI5Ouz56P','RXOaGg6dRjZcrdwx7se38pECmWMsZ3oDblvhecUZk2MA0wzXdD','4371500537-fa1Il9DwOeNWfHs4gIaqYnLTND12gycMQnTpLRr','jB6qjFBYHboKgTcJ11BzYnm9ZtH7a9hJcmCHvIwQZIxCA',8,0);
INSERT INTO `TwitterKeys` VALUES('DionHenigan','oifjbo2803l007','0BhLQfb0U0ZKGYoeCqLifl7fC','7KZOTqv28M2d1nA1guuCuUVGJjP5145W7YWerwRUojlNThDXuX','4367916441-AIPEJ7orwUkod5rWouOgasRTj0rhFHuVF0chzcs','z8sBrrJr9jKCZCBQCkB4gzb4EXva12qw67T4xiTFmPAFT',9,0);
INSERT INTO `TwitterKeys` VALUES('GregSlawski','uCD4439fenxf321','e7xcq8mE6wIKQ8u6nT13d0FS9','lgqdKNbeqKRKXsLijb7HJ2we2ArKUgT2vBeqOKy3h524Hxj3SQ','4370147357-9jzpVX81cloumgOfwe6CcWLNweuys9XMVGyQ5jO','v30CmrPIZuvhOoVfoG78SGhwx2FqhUGPR65u6cbSLSOr7',10,0);
INSERT INTO `TwitterKeys` VALUES('TobieSprenkel','gAB4795nielt768','KOuwGME2T64K8sjoHTBYpmO4K','zSXE5TsTocR6Ow8eTaAloYR2UDFLB0uU3O6e8AprV2FpLPMTQJ','4365355156-u30tlYfaAQopyVX8fukmLFbbcZHOzlp7lfPuRSD','2zGXvG6o1jnIFB4j40aGa0OUlZUiCr9HfLMpLA213VHkt',11,0);
INSERT INTO `TwitterKeys` VALUES('RickiGoettsche','fORXtrr7nngu','OuovzhTHl8RitW41iOuvC73gz','GH1sOggdZ248PcqkAdMc8EAw0H0XIVKjqE6ywaltTZ3jFErDlB','4381962089-5dJbtZ1wDiM0UitlVufCVyOrmo3RAcfjS7musqv','xDu9LYepFHdJzVmhrCrrUdnlhduAAVMJjn1gH099TG08m',12,0);
INSERT INTO `TwitterKeys` VALUES('TommieNealen','wIJ8802rrypd','fVJhYvql0zAogXaGu6vjfYY3j','ebm7fmlRvtjTlEubK8nlhutZegyGNIIhgZdnMh5qomdTnGdAzV','4377539595-GrcFa8cQp7RFZgQ6Y5xd7N6HZNyceHRzabypP8s','iiYEtub6wpnyY1KnxiqaR4X7alpSN0PuPubBFfJpSISRc',13,0);
INSERT INTO `TwitterKeys` VALUES('DovieBasco','rMN0435oljni','2niAQLlI35WRMjgHn7J4Soq3A','04oQ1vJLnfTKncDUshyFYN18Z7NvnsIewTQ1pV1LXqWdICnfiW','4372214416-T8gFS6eZQl8gybTB5z8JZnCYfK52mypj6LiZnXb','ILzCKdtP1zD2YQ3NlH4ep77awMWIKOZ5CIc905H1XSHIU',14,0);
INSERT INTO `TwitterKeys` VALUES('IdellaClairday','321gvpmkl4678t','u3JlbkJwjaWWyPVsBTpvJmTr9','Uvq2c3mQY03objZSOvj4FRIrmmd072SudgjnZOOITssKI5YSJ3','4359911237-HPL9iXqdQkhWTB4fU1Uv1lD5mT4y5TLu35qmink','vq6BrwrHlX8r7zhs48bsogUhJImk2zOZijC73wD8rWP51',15,0);
INSERT INTO `TwitterKeys` VALUES('ShanitaHelscher','123mAB6251wewqn','x8ihk199HKMzquWKgy26LY9rK','qOZdzwbwCBLB6wO7X8eNGKNJmmf7wW3ViMcbKXtWu51MGqmM2U','4359731055-huWBdx0O2pKdF5L3K6zwJ51KQOZneFXSnz6Upa2','gIjoh6fWb0pcnyM4owDalZTagimwSTvCOSvFVmioiD5uK',16,0);
INSERT INTO `TwitterKeys` VALUES('VaniaCanonico','456iUV1199onpwr','Utzj788pVLQGD3E4b8n87FISI','FwOJrlcniL5HIaQvpIBCGDehnzsb5a6hJPavtKLokpkT1Lgq7y','4359935776-KXR9HdbVG9VajW4E6MsKkzeal3eAtg7J3wQZ48L','f4R1EAsq354eLUdeiCu0HlDM8cU1GhZBPucytKWf6Q0vn',17,0);
INSERT INTO `TwitterKeys` VALUES('LynettaKarch','fgxxrs5268u456','FejvSYHIOk4BTYecTRM44u0hD','NodaRucVe6DRP29CoqbNlkixTDxDelhD3RlH0QjwIQmaLUbrzG','4359998842-PaSQum1LZbmWRA1mQumE0x6zcgeixtcZfCWfucj','jZqpvOqrHptkfSYTbz7pByAUQFIvkNghsp6DEy4DUVkbE',18,0);
INSERT INTO `TwitterKeys` VALUES('CorettaFlinck','caevzc2991x879','3sH318DJrh3IfYiIqIyPdwDiL','BiVIpjGV3czhPeuHXZjJEgE6GUW1Mq1p7ctEH8d4ecEowroOdF','4359998237-MWRnBdruoifdXuKfJGzlDKwgDs1zjVEOhwMneHL','NPtTvdu0BjC4yvK2yRROTd7YHOB4AoC3hiBYaX8K8D94d',19,0);
INSERT INTO `TwitterKeys` VALUES('JessieByan','yCD1405vsreb439','CuKonssIpmiAhap9FjjpwX4O2','XuwDgAP8kBYfJXjoagT1pLVjXhdutHFtZOvd1WyM8gdCKClPPI','4360154242-TnvhT2PzE0Q2qV6eyufVsD1r8erpPTeN8VqhfFr','vjqv6qtMmv0EkuvvLkfSletHJZl8REIOXUwAfAVPUerlK',20,0);
INSERT INTO `TwitterKeys` VALUES('EdrisVeltri','blllpj2016y537','TbGogZtBLw2yKOGhvEo2SpNqM','1aqLqDKqxceGxe2Q0yj5esOfTFc1TrNuM8gP6bK22PFdSd4tIT','4360018457-QuARR4Au0OVKRdH9g0A38naxTbuBOR6xeauqxao','neGvd3RyTMiMub0FCCSjlXIZTl2cjoZX3S8Nx3VNR2uRc',22,0);
INSERT INTO `TwitterKeys` VALUES('LaurelOffner','eQR5993vbluv008','R7MT7z2Dt5KnZepfPhUIitcdn','cD7LhwNvyHDlhnCbEMn0bgb89XuEtp0hRgMMyy594q1m0cHWuY','4359905295-BCzF5qo3XWRnymGpGZeV0y0rNsp5DTuvN2TEk22','8xRZsHjn7kDyrRLjDVv1aEeNDIVg3OvhgGZVOcyelkq4D',23,0);
INSERT INTO `TwitterKeys` VALUES('MaeganLentsch','789xlfkte4833c','2EONhfVAlsLazcmegQiqIE1G1','LB6GapjEHbDKP4v9iXlW3sNR9sCoYg4kPawbzPaAimZ9XvIXH5','4360059195-Sn3u57u93UWCsh4plbFsW80RFmBkVoBvnlaoTFf','8nc68sRblDcOlhBRQBmaIpzXOUWl5mqnI8gNjzzD5Zo2e',24,0);
INSERT INTO `TwitterKeys` VALUES('RanaeCloninger','wllljd4374d112','V13U2yQUmrkkEUQ4dpD74cwLa','PtTQDrBL45qfASBsU16flEvlbvTHvc5e1AmzxAMzNIsyVtknEt','4360129697-H8mkPA5H5aDv90s5pskfQFDqbDUqjg5MhZJlpCG','A11A5e0QgL4s0ebhTOrGNV74zmurPEkac6lCaGeUEsFC7',25,0);
INSERT INTO `TwitterKeys` VALUES('TrenaUptain','rEF3123bcjhi321','3PFgtLWK7iqhzWgVsxEHMxUKc','m2WwZP8x8ganXrbmEwcgxLLgUS4fAPSyjwgSBAXCCIX1657kiC','4360194201-5d2uNIScpMRfXmqZYjPfwZzVslDiIf6lTWrdvaQ','gA8LTWevdvjbnIKjukS4aPqED60OQKTLd091O5qUSyV1q',26,0);
INSERT INTO `TwitterKeys` VALUES('NicolaHigbee','jST4924yqnoq321','22rsGc01WElJ0KH9j252XLuX2','6l8Sdd9789TrqTfQTU4x9TLVZEHIIFE3DgOn7iBNQ90obmXdr2','4359913756-tLRospO8oApcrm1pYqQ4QG5XETZOdEolzWPfX8n','5V7mHa1jau6aRsdMQCny7CJUryu5kY51lN6CPBb3bgkX9',27,0);
INSERT INTO `TwitterKeys` VALUES('PiaMoberly','fGH3444wkgg','YiMdh2voeRj1pXqUNl5gngR7i','TqarnzSskt8VJuoeO4cuxn5RRV8R2VJnVay3RngsprTIVwzE1p','4321318947-VIqsoT0xq3invxGklAKY2VdFlZuBJrTMZ60sZBk','YSOwq0xkZC6UJeyZqAYVWu8hMIVKyp3PwI6FxFx4KZARm',28,0);
INSERT INTO `TwitterKeys` VALUES('LeanaFaughn','cQR4131eoztx','Nf8PLfDw18XmpbjvuBaqcKpxt','ocVZFTc8UL4MFe1LFMgTd2bVJllJqKodZ3PPIhWYQ0Ke3m7vCO','4385958087-uuqOjFOuARXCjEr01K5UowWuGrLLKj4aAiyFtjY','h0KNxZw1KUZoPfYuSyJOYfLcurTSp2pCPCUskPuFB4EyZ',29,0);
CREATE TABLE "Friends" (
	id INTEGER NOT NULL, 
	friendname VARCHAR NOT NULL, 
	img VARCHAR NOT NULL, 
	img_local VARCHAR NOT NULL, 
	bio VARCHAR NOT NULL, 
	upvotes VARCHAR NOT NULL, 
	made VARCHAR NOT NULL, 
	followers VARCHAR NOT NULL, 
	following VARCHAR NOT NULL, 
	user_id VARCHAR NOT NULL, 
	users_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(users_id) REFERENCES "Users" (id)
);
INSERT INTO `Friends` VALUES(1,'alexander_raboin','https://ph-avatars.imgix.net/504791/original?auto=format&w=55&h=55&q=5&blur=0','images//504791.jpg','Entrepreneur',0,0,0,0,504791,1);
INSERT INTO `Friends` VALUES(2,'vanhinpuu','https://ph-avatars.imgix.net/171501/original?auto=format&w=55&h=55&q=5&blur=0','','Founder, Woodies Clothing',75,1,23,30,171501,1);
INSERT INTO `Friends` VALUES(3,'Krishna Prathab','https://ph-avatars.imgix.net/17016/original?auto=format&w=110&h=110','images//#17016.jpg','CEO, XLabz Technologies',83,3,62,39,'#17016',2);
INSERT INTO `Friends` VALUES(4,'','https://static.intercomassets.com/avatars/222993/square_128/ObY5lf14.jpg?1445088349','images//.jpg','CEO, XLabz Technologies','','','','','',3);
INSERT INTO `Friends` VALUES(5,'Monik Pamecha','https://ph-avatars.imgix.net/175547/original?auto=format&w=110&h=110','images//#175547.jpg','',1,0,280,426,'#175547',4);
INSERT INTO `Friends` VALUES(6,'R Pooran Prasad','https://ph-avatars.imgix.net/10476/original?auto=format&w=110&h=110','images//#10476.jpg','Consulting Architect, Zealous',10,0,110,323,'#10476',5);
INSERT INTO `Friends` VALUES(7,'Vijay Anand','https://ph-avatars.imgix.net/53381/original?auto=format&w=110&h=110','images//#53381.jpg','Founder, The Startup Centre',8,0,'2,364',849,'#53381',6);
INSERT INTO `Friends` VALUES(8,'Abhilasha Dafria','https://ph-avatars.imgix.net/230108/original?auto=format&w=110&h=110','images//#230108.jpg','Founder, The Venturator',0,0,14,3,'#230108',7);
INSERT INTO `Friends` VALUES(9,'','https://ph-avatars.imgix.net/162019/original?auto=format&w=110&h=110','images//#162019.jpg','Software Engineer',3,0,4,19,'#162019',9);
INSERT INTO `Friends` VALUES(10,'Ram','qrq','afwf','ggg',0,1,1,0,'q4342',8);
INSERT INTO `Friends` VALUES(11,'','https://ph-avatars.imgix.net/162019/original?auto=format&w=110&h=110','images//#162019.jpg','Software Engineer',3,0,4,19,'#162019',9);
INSERT INTO `Friends` VALUES(12,'Sean W Andersen','https://ph-avatars.imgix.net/200687/original?auto=format&w=110&h=110','images//#200687.jpg','',2,0,90,131,'#200687',9);
INSERT INTO `Friends` VALUES(13,'Adam Herscher','https://ph-avatars.imgix.net/71329/original?auto=format&w=110&h=110','images//#71329.jpg','Product Manager, Google',64,0,182,129,'#71329',9);
INSERT INTO `Friends` VALUES(14,'Yoav Sion','https://ph-avatars.imgix.net/160394/original?auto=format&w=110&h=110','images//#160394.jpg','',0,0,2,3,'#160394',9);
INSERT INTO `Friends` VALUES(15,'Jay Kannan','https://ph-avatars.imgix.net/417989/original?auto=format&w=110&h=110','images//#417989.jpg','',0,0,22,0,'#417989',9);
INSERT INTO `Friends` VALUES(16,'Ashish Virmani','https://ph-avatars.imgix.net/172198/original?auto=format&w=110&h=110','images//#172198.jpg','Sotware Engineer, Twitter',0,0,110,95,'#172198',9);
INSERT INTO `Friends` VALUES(17,'Jason Granado','https://ph-avatars.imgix.net/180499/original?auto=format&w=110&h=110','images//#180499.jpg','Jason Granado from TempCFO',4,0,484,304,'#180499',11);
INSERT INTO `Friends` VALUES(18,'Init.ai','https://ph-avatars.imgix.net/500376/original?auto=format&w=110&h=110','images//#500376.jpg','',4,0,110,'2,489','#500376',11);
INSERT INTO `Friends` VALUES(19,'Business Rockstars','https://ph-avatars.imgix.net/521639/original?auto=format&w=110&h=110','images//#521639.jpg','',1,0,181,'6,964','#521639',11);
INSERT INTO `Friends` VALUES(20,'ottspott','https://ph-avatars.imgix.net/342635/original?auto=format&w=110&h=110','images//#342635.jpg','ottspott.co',9,0,162,'1,357','#342635',11);
INSERT INTO `Friends` VALUES(21,'Sam Nissinen','https://ph-avatars.imgix.net/189879/original?auto=format&w=110&h=110','images//#189879.jpg','Founder, Hyper',41,0,112,14,'#189879',11);
INSERT INTO `Friends` VALUES(22,'Justin Wu','https://ph-avatars.imgix.net/9589/original?auto=format&w=110&h=110','images//#9589.jpg','Growth Engineer, Cofounder @Vytmn',108,1,'3,504','2,573','#9589',11);
INSERT INTO `Friends` VALUES(23,'Gotta','https://ph-avatars.imgix.net/412220/original?auto=format&w=110&h=110','images//#412220.jpg','',1,0,3,1,'#412220',12);
INSERT INTO `Friends` VALUES(24,'StartEngine','https://ph-avatars.imgix.net/180507/original?auto=format&w=110&h=110','images//#180507.jpg','Start Engine Accelerator',3,0,'1,772',241,'#180507',12);
INSERT INTO `Friends` VALUES(25,'Gotta','https://ph-avatars.imgix.net/412220/original?auto=format&w=110&h=110','images//#412220.jpg','',1,0,3,1,'#412220',12);
INSERT INTO `Friends` VALUES(26,'StartEngine','https://ph-avatars.imgix.net/180507/original?auto=format&w=110&h=110','images//#180507.jpg','Start Engine Accelerator',3,0,'1,772',241,'#180507',12);
INSERT INTO `Friends` VALUES(27,'poornima','https://ph-avatars.imgix.net/7911/original?auto=format&w=140&h=140','images//.jpg','@poornima',153,11,'3,691','7,288','',12);
INSERT INTO `Friends` VALUES(28,'poornima','https://ph-avatars.imgix.net/7911/original?auto=format&w=140&h=140','images//.jpg','@poornima',153,11,'3,691','7,288','',12);
INSERT INTO `Friends` VALUES(29,'Allan Jiang','https://ph-avatars.imgix.net/14905/original?auto=format&w=110&h=110','images//#14905.jpg','I make stuff.',52,0,30,375,'#14905',12);
INSERT INTO `Friends` VALUES(30,'Allan Jiang','https://ph-avatars.imgix.net/14905/original?auto=format&w=110&h=110','images//#14905.jpg','I make stuff.',52,0,30,375,'#14905',12);
INSERT INTO `Friends` VALUES(31,'','https://ph-avatars.imgix.net/412220/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@gottathing','','','3 Followers','1 Following','',12);
INSERT INTO `Friends` VALUES(32,'','https://ph-avatars.imgix.net/180507/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@startenginela','3 Upvotes','','1,807 Followers','241 Following','',12);
INSERT INTO `Friends` VALUES(33,'','https://ph-avatars.imgix.net/7911/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@poornima','162 Upvotes','12 Made','3,755 Followers','7,288 Following','',12);
INSERT INTO `Friends` VALUES(34,'','https://ph-avatars.imgix.net/14905/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@allan_jiang','52 Upvotes','','30 Followers','375 Following','',12);
INSERT INTO `Friends` VALUES(35,'','https://ph-avatars.imgix.net/507928/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@kimberli_hudson','0 Upvotes','','19 Followers','19 Following','',12);
INSERT INTO `Friends` VALUES(36,'','https://ph-avatars.imgix.net/138643/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@snap_eda','0 Upvotes','','49 Followers','104 Following','',12);
INSERT INTO `Friends` VALUES(37,'','https://ph-avatars.imgix.net/417248/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@paveyn','','','38 Followers','372 Following','',12);
INSERT INTO `Friends` VALUES(38,'','https://ph-avatars.imgix.net/45720/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@dpwalsh','5 Upvotes','','314 Followers','871 Following','',12);
INSERT INTO `Friends` VALUES(39,'','https://ph-avatars.imgix.net/479203/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@czekalla','23 Upvotes','','10 Followers','10 Following','',12);
INSERT INTO `Friends` VALUES(40,'','https://ph-avatars.imgix.net/165425/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@radicandlab','3 Upvotes','','145 Followers','80 Following','',12);
INSERT INTO `Friends` VALUES(41,'','https://ph-avatars.imgix.net/44973/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@np_bartlett','38 Upvotes','','366 Followers','560 Following','',12);
INSERT INTO `Friends` VALUES(42,'','https://ph-avatars.imgix.net/13150/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@mbelinsky','65 Upvotes','BenchMade Modern','426 Followers','667 Following','',12);
INSERT INTO `Friends` VALUES(43,'','https://ph-avatars.imgix.net/268045/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@pch_intl','','','772 Followers','729 Following','',12);
INSERT INTO `Friends` VALUES(44,'','https://ph-avatars.imgix.net/165124/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@kaetheblue','10 Upvotes','','105 Followers','158 Following','',12);
INSERT INTO `Friends` VALUES(45,'','https://ph-avatars.imgix.net/126517/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@gautamrao11','','','74 Followers','123 Following','',12);
INSERT INTO `Friends` VALUES(46,'','https://ph-avatars.imgix.net/519561/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@lovelygoswami','6 Upvotes','','2 Followers','57 Following','',12);
INSERT INTO `Friends` VALUES(47,'','https://ph-avatars.imgix.net/87758/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@dbrodovich','5 Upvotes','','678 Followers','877 Following','',12);
INSERT INTO `Friends` VALUES(48,'','https://ph-avatars.imgix.net/369761/original?auto=format&w=140&h=140&fit=crop','images//.jpg','@projectenergize','','','2 Followers','4 Following','',12);
;
COMMIT;
