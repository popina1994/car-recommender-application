from bs4 import BeautifulSoup
import urllib.request 
import os

import requests

HOME_PAGE_URL = ["https://www.polovniautomobili.com", "https://www.autoscout24.com"]
SEARCH_PAGE_URL = ["https://www.polovniautomobili.com/putnicka-vozila/pretraga?page={}&sort=renewDate_desc&brand={}&model%5B0%5D={}&city_distance=0&showOldNew=all&without_price=1",
                   "https://www.autoscout24.com/results?sort=price&desc=0&ustate=N%2CU&size=20&page={}&mmvmk0={}&mmvmd0={}&fregfrom=2016&atype=C&"]
DIV_SEARCH_PAGE = [{"class": "uk-grid uk-margin-remove"}, {"class": "cldt-summary-titles"}]
DIV_GALLERY_PAGE = [ ("li", {"class" : "uk-text-center"}, "href"), 
                    ("div", {"class" : "gallery-picture sc-lazy-image"}, ["data-src", "src"])]

DB_MODELS = {}
IDX_LIMIT = 100

class ParserPage:

    def __init__(self, home_page: str, url: str, div):
        self.home_page = "" if home_page is None else home_page
        self.url = url
        self.div = div

    def parse(self):
        r  = requests.get(self.url)
        data = r.text
        soup = BeautifulSoup(data)
        page_download = []
        for data in soup.find_all("div", self.div):
            for imgDiv in data.find_all('a'):
                linkPage = imgDiv.get('href') 
                linkPage = "" if linkPage is None else linkPage.strip()
                if ((linkPage) != ''):
                    page_download.append(self.home_page + linkPage)
        return page_download

class ParserSubPage:
    def __init__(self, url: str, crawl_element):
        self.url = url
        self.crawl_element = crawl_element

    def parse(self):
        try:
            r  = requests.get(self.url)
        except:
            return []
        data = r.text
        soup = BeautifulSoup(data)
        page_download = []
        for data in soup.find_all(self.crawl_element[0], self.crawl_element[1]):
            for imgDiv in data.find_all('img'):
                for source in self.crawl_element[2]:
                    linkPage = imgDiv.get(source) 
                    linkPage = "" if linkPage is None else linkPage.strip()
                    if ((linkPage) != ''):
                        page_download.append(linkPage)
        return page_download

class ParserModel:
    def __init__(self, model: str, num_page: int, home_page: str, search_page: str,
                 div_search_page, crawl_element):
        self.model = model 
        self.num_page = num_page
        self.home_page = home_page
        self.search_page = search_page
        self.div_search_page = div_search_page
        self.crawl_element = crawl_element

    def parse(self):
        url_path = self.search_page
        
        images_to_download = []
        for pg_idx in range(1, self.num_page + 1):
            url = url_path.format(pg_idx, DB_MODELS[self.model]["company"], 
                                  DB_MODELS[self.model]["model"])
            images_to_download += self.parse_search_page(url)
            print("Finished page{}".format(pg_idx))
        
        self.download_images(images_to_download)


    def parse_search_page(self, url):
        pages = ParserPage(self.home_page, url, self.div_search_page).parse()
        list_images =[]
        with open('pictures.txt', "w") as f:
            for idx, page in enumerate(pages):
                pictures = ParserSubPage(page, self.crawl_element).parse()
                if (idx == IDX_LIMIT): break
                for it in pictures:
                    list_images.append(it)
                    f.write(it+"\n")
                print("Passed: {}/{}", idx, len(pages))
        
        return list_images
        
    
    def download_images(self, images_to_download):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        if not os.path.exists(self.model):
            os.makedirs(self.model)

        for idx, url_image in enumerate(images_to_download):
            urllib.request.urlretrieve(url_image, os.path.join(self.model, str(idx) + ".jpg"))
            if (idx % 100 == 0):
                print("Downloaded: {}/{}", idx, len(images_to_download))

if __name__ == "__main__":
    #DB_MODELS["X3"] = {"company": "37", "model" : "1054"}
    #ParserModel(model="X3", num_page=1, home_page=HOME_PAGE_URL[0], search_page=SEARCH_PAGE_URL[0],
    #            div_search_page=DIV_SEARCH_PAGE[0], crawl_element=DIV_GALLERY_PAGE[0]).parse()
    
    DB_MODELS["X3"] = {"company": "13", "model" : "18387"}
    ParserModel(model="X3", num_page=20, home_page=HOME_PAGE_URL[1], search_page=SEARCH_PAGE_URL[1],
                div_search_page=DIV_SEARCH_PAGE[1], crawl_element=DIV_GALLERY_PAGE[1]).parse()
