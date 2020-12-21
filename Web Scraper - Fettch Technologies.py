import bs4
import pandas as pd
from time import sleep
from random import randint
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

Store_Name = []
Address = []
Phone_Number = []
# loop over multiple pages
for i in range(1, 2):
    my_url = "https://www.yellowpages.ca/search/si/" + str(i) + "/watches/Toronto+ON"
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    # initialize storage
    # first page on the url
    # page_soup.h1
    # parse and find structure of store listings only on HTML

    pattern_types = ["listing listing--bottomcta", "listing listing--bottomcta placement"]
    listings = []

    for pattern in pattern_types:
        listings = listings + page_soup.findAll("div", {"class": pattern})

    uniqueList = list(set(listings))
    print("listings " + str(len(listings)))

    print("unique listings" + str(len(uniqueList)))

    # listing=page_soup.findAll("div", {"class":"listing listing--bottomcta"})
    sleep(randint(2, 10))
    # listing=listing=page_soup.findAll("div", {"class":"listing listing--bottomcta placement"})
    # checking the lenght of the list created,ie number of stores
    # len(listing)
    # listing[0]
    # contain = listing [0]
    # container = listing [0]
    # Looping to find store name and adress
    for container in listings:
        Vendor = container.a["title"]
        # store in list created above
        Store_Name.append(Vendor)
        Location = container.find("span", itemprop="postalCode").get_text()
        Address.append(Location)
        Contact = container.h4.get_text()
        Phone_Number.append(Contact)
        # print (Vendor)
        # print(Location)
        # print(Contact)
        # building dataframe
        Vendors = pd.DataFrame({
            'Vendor': Store_Name,
            'Location': Address,
            'Contact': Phone_Number,
        })
print(Vendors)

# "https://www.yellowpages.ca/search/si/" + str(i) + "/Men%27s+Fashion/Toronto+ON"

# https://www.yellowpages.ca/search/si/" +str(i)+ "/phone/Toronto+ON"
# https://www.yellowpages.ca/search/si/" +str(i)+ "/watches/Toronto+ON"
# https://www.yellowpages.ca/search/si/" +str(i)+ "/women%27s+fashion/Toronto+ON"