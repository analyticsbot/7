from boilerpipe.extract import Extractor
#extractor = Extractor(extractor='ArticleExtractor', url=your_url)
extractor = Extractor(extractor='ArticleExtractor', html='C:\\Users\\Ravi Shankar\\Documents\\Upwork\\Raymond\\dragnet_HTML\\HTML\\9.html')
extracted_text = extractor.getText()
