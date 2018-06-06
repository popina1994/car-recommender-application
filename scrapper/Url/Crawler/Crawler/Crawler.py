from bs4 import BeautifulSoup
import urllib.request 
import os

import requests

HOME_PAGE_URL = ["https://www.polovniautomobili.com", "https://www.autoscout24.com"]
SEARCH_PAGE_URL = ["https://www.polovniautomobili.com/putnicka-vozila/pretraga?page={}&sort=renewDate_desc&brand={}&model%5B0%5D={}&city_distance=0&showOldNew=all&without_price=1",
                   "https://www.autoscout24.com/results?sort=price&desc=0&ustate=N%2CU&page={}&mmvmk0={}&mmvmd0={}&body={}&atype=C&size=20&doorfrom={}&doorto={}&fregfrom={}&fregto={}"]
DIV_SEARCH_PAGE = [{"class": "uk-grid uk-margin-remove"}, {"class": "cldt-summary-titles"}]
DIV_GALLERY_PAGE = [ ("li", {"class" : "uk-text-center"}, "href"), 
                    ("div", {"class" : "gallery-picture sc-lazy-image"}, ["data-src", "src"])]
DB_MODELS = {}
IDX_LIMIT = 100000
    
PROXY = {
    
    'http': 'http://proxy.rcub.bg.ac.rs:8080',
    'https': 'http://proxy.rcub.bg.ac.rs:8080'
    
}


class ParserPage:

    def __init__(self, home_page: str, url: str, div):
        self.home_page = "" if home_page is None else home_page
        self.url = url
        self.div = div

    def parse(self):
        r  = requests.get(self.url, proxies=PROXY)
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
            r  = requests.get(self.url, proxies=PROXY)
        except:
            print("Sub page exception")
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
    def __init__(self, model, model_name:str, home_page: str, search_page: str,
                 div_search_page, crawl_element):
        self.model = model 
        self.model_name = model_name
        self.home_page = home_page
        self.search_page = search_page
        self.div_search_page = div_search_page
        self.crawl_element = crawl_element

    def parse(self):
        url_path = self.search_page
        
        images_to_download = []
        for pg_idx in range(1, self.model["num_pages"] + 1):
            url = url_path.format(pg_idx, self.model["company"], 
                                  self.model["model"], self.model["body"],
                                  self.model["doorfrom"], self.model["doorto"],
                                  self.model["fregfrom"], self.model["fregto"])
            images_to_download += self.parse_search_page(url)
            print("Finished page{}".format(pg_idx))
        
        self.download_images(images_to_download)


    def parse_search_page(self, url):
        pages = ParserPage(self.home_page, url, self.div_search_page).parse()
        list_images =[]
        with open('pictures.txt', "w") as f:
            for idx, page in enumerate(pages):
                if (idx == IDX_LIMIT): break
                pictures = ParserSubPage(page, self.crawl_element).parse()
                for it in pictures:
                    list_images.append(it)
                    f.write(it+"\n")
                print("Passed: {}/{}".format(idx, len(pages)))
        
        return list_images
        
    
    def download_images(self, images_to_download):
        proxy = urllib.request.ProxyHandler(PROXY)
        opener = urllib.request.build_opener(proxy)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        if not os.path.exists(self.model_name):
            os.makedirs(self.model_name)

        for idx, url_image in enumerate(images_to_download):
            try:
                urllib.request.urlretrieve(url_image, os.path.join(self.model_name, str(idx) + ".jpg"))
            except:
                print("Unsuccessful download{}".format(idx))
            if (idx % 100 == 0):
                print("Downloaded: {}/{}".format(idx, len(images_to_download)))

if __name__ == "__main__":
    t = 1
    body_convertible = "2"
    body_coupe = "3"
    body_sedan = "6"
    body_station_wagon = "5"
    """   
   DB_MODELS["X3"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                       1:{"company": "13", "model" : "18387", "num_pages": 20}}
    
    DB_MODELS["114"] = {0: {"company": "37", "model" : "1054", "num_pages" : 1}, 
                       1:{"company": "13", "model" : "20149", "num_pages": 20, "body":"6"}}
    DB_MODELS["116"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                       1:{"company": "13", "model" : "18480", "num_pages": 20, "body":"6"}}
    DB_MODELS["118"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "18481", "num_pages": 20, "body":"6"}}
    DB_MODELS["120"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "18482", "num_pages": 20, "body":"6"}}
    DB_MODELS["Series2_Coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-98", "num_pages": 20, "body":"3"}}
    DB_MODELS["Series2_Convertible"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-98", "num_pages": 20, "body":"2"}}
    DB_MODELS["Series3_2doors_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-38", "num_pages": 20, "body":"3",
                       "doorfrom": "2", "doorto" : "3"}}
    DB_MODELS["Series3_2doors_convertible"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-38", "num_pages": 20, "body":"2",
                       "doorfrom": "2", "doorto" : "3"}}
    
    DB_MODELS["Series3_4doors_freg_2013_sedan"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-38", "num_pages": 20, "body":"6",
                       "doorfrom": "4", "doorto" : "5", "fregfrom" : "2013", "fregto": "2018"}}
    DB_MODELS["Series3_4doors_freg_2005_2011_sedan"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-38", "num_pages": 20, "body":"6",
                       "doorfrom": "4", "doorto" : "5", "fregfrom" : "2005", "fregto": "2011"}}
    DB_MODELS["Series4_2doors_convertible"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-97", "num_pages": 20, "body": body_convertible,
                       "doorfrom": "2", "doorto" : "3", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["Series4_2doors_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-97", "num_pages": 20, "body": body_coupe,
                       "doorfrom": "2", "doorto" : "3", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["Series4_4doors_sedan"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-97", "num_pages": 20, "body": body_sedan,
                       "doorfrom": "4", "doorto" : "5", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["Series5_freg_2000_sedan"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                1:{"company": "13", "model" : "-39", "num_pages": 20, "body": body_sedan,
                    "doorfrom": "2", "doorto" : "7", "fregfrom" : "2000", "fregto": "2018"}}
    DB_MODELS["Series5_freg_2000_station_wagon"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-39", "num_pages": 20, "body": body_station_wagon,
                       "doorfrom": "2", "doorto" : "7", "fregfrom" : "2000", "fregto": "2018"}}
    DB_MODELS["Series6_2doors_convertible"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-40", "num_pages": 20, "body": body_convertible,
                       "doorfrom": "2", "doorto" : "3", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["Series6_2doors_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                    1:{"company": "13", "model" : "-40", "num_pages": 20, "body": body_coupe,
                       "doorfrom": "2", "doorto" : "3", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["Series6_4doors_sedan"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                1:{"company": "13", "model" : "-40", "num_pages": 20, "body": body_sedan,
                    "doorfrom": "4", "doorto" : "5", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["Series7_4doors_sedan"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
            1:{"company": "13", "model" : "-41", "num_pages": 20, "body": body_sedan,
                "doorfrom": "4", "doorto" : "5", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["Series8_2doors_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                1:{"company": "13", "model" : "-42", "num_pages": 20, "body": body_coupe,
                    "doorfrom": "2", "doorto" : "3", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["M1_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                1:{"company": "13", "model" : "19741", "num_pages": 20, "body": body_coupe,
                    "doorfrom": "2", "doorto" : "7", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["M3_4doors_sedan"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
                1:{"company": "13", "model" : "1646", "num_pages": 20, "body": body_sedan,
                    "doorfrom": "4", "doorto" : "5", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["M3_2doors_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
            1:{"company": "13", "model" : "1646", "num_pages": 20, "body": body_coupe,
                "doorfrom": "2", "doorto" : "3", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["M4_2doors_convertible"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
            1:{"company": "13", "model" : "20393", "num_pages": 20, "body": body_convertible,
                "doorfrom": "2", "doorto" : "3", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["M4_2doors_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
            1:{"company": "13", "model" : "20393", "num_pages": 20, "body": body_coupe,
                "doorfrom": "2", "doorto" : "3", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["M5_sedan"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
            1:{"company": "13", "model" : "1655", "num_pages": 20, "body": body_sedan,
                "doorfrom": "2", "doorto" : "7", "fregfrom" : "1920", "fregto": "2018"}}
    DB_MODELS["M6_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
            1:{"company": "13", "model" : "18577", "num_pages": 20, "body": body_coupe,
                "doorfrom": "2", "doorto" : "7", "fregfrom" : "1920", "fregto": "2018"}}
    """
    DB_MODELS["M2_coupe"] = {0: {"company": "37", "model" : "1054", "num_pages" : 20}, 
            1:{"company": "13", "model" : "21157", "num_pages": 20, "body": body_coupe,
                "doorfrom": "2", "doorto" : "7", "fregfrom" : "1920", "fregto": "2018"}}
    for model_id in DB_MODELS.keys():
        model_list =  DB_MODELS[model_id]
        for site_id, model_site in model_list.items():
            if site_id == 0: continue
            ParserModel(model=model_site, model_name=model_id, home_page=HOME_PAGE_URL[site_id], 
                        search_page=SEARCH_PAGE_URL[site_id], div_search_page=DIV_SEARCH_PAGE[site_id], 
                        crawl_element=DIV_GALLERY_PAGE[site_id]).parse()
