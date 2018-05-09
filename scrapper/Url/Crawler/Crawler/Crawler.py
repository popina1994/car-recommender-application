from bs4 import BeautifulSoup
import urllib.request 
import os

import requests

HOME_PAGE_URL = "https://www.polovniautomobili.com"
mapping_models = {}

class ParserPage:
    def __init__(self, url: str):
        self.url = url

    def parse(self):
        r  = requests.get(self.url)
        data = r.text
        soup = BeautifulSoup(data)
        page_download = []
        for data in soup.find_all("div", {"class" : "uk-grid uk-margin-remove"}):
            for imgDiv in data.find_all('a'):
                linkPage = imgDiv.get('href').strip()
                if ((linkPage) != ''):
                    page_download.append(HOME_PAGE_URL + linkPage)
        return page_download

class ParserSubPage:
    def __init__(self, url: str):
        self.url = url

    def parse(self):
        try:
            r  = requests.get(self.url)
        except:
            return []
        data = r.text
        soup = BeautifulSoup(data)
        page_download = []
        for data in soup.find_all("li", {"class" : "uk-text-center"}):
            for imgDiv in data.find_all('img'):
                linkPage = imgDiv.get('src').strip()
                if ((linkPage) != ''):
                    page_download.append(linkPage)
        return page_download

class ParserModel:
    def __init__(self, model: str, num_page):
        self.model = model 
        self.num_page = num_page

    def parse(self):
        url_path = "https://www.polovniautomobili.com/putnicka-vozila/pretraga?page={}&sort=renewDate_desc&brand={}&model%5B0%5D={}&city_distance=0&showOldNew=all&without_price=1"
        
        for pg_idx in range(1, self.num_page + 1):
            url = url_path.format(pg_idx, mapping_models[self.model]["brand"], mapping_models[self.model]["model"])
            self.parse_page(url)

    def parse_page(self, url):
        pages = ParserPage(url).parse()
        list_images =[]
        with open('pictures.txt', "w") as f:
            for idx, page in enumerate(pages):
                pictures = ParserSubPage(page).parse()
                
                for it in pictures:
                    list_images.append(it)
                    f.write(it+"\n")
                print("Passed: {}/{}", idx, len(pages))
    
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        if not os.path.exists(self.model):
            os.makedirs(self.model)
        for idx, url_image in enumerate(list_images):
            urllib.request.urlretrieve(url_image, os.path.join(self.model, str(idx) + ".jpg"))
            if (idx % 100 == 0):
                print("Downloaded: {}/{}", idx, len(list_images))


if __name__ == "__main__":
    mapping_models["X3"] = {"brand": "37", "model" : "1054"}
    ParserModel("X3", 1).parse()
