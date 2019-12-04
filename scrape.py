from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://en.wikipedia.org/wiki/List_of_Wheeler_Dealers_episodes'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")
#print(page_soup.h1)

containers = page_soup.find_all('tr')
#print (len(containers))
#print(soup.prettify(containers[0]))
container = containers[0]
#print("Name: " , container.div.img["alt"])
price = container.find_all("div",{"class":"col col-5-12 _2o7WAb"})
#print("Price: ", price[0].text)
rating = container.find_all("div",{"class":"hGSR34"})
#print("Rating: ", rating[0].text)

filename = "products.csv"
f = open(filename,"w")
headers="Product,Price,Ratings\n"
f.write(headers)

for container in containers:
    product_name  = container.div.img["alt"]
    print("Product name:", product_name)
    price_container = container.find_all("div",{"class":"_1vC4OE _2rQ-NK"})
    price = price_container[0].text

    removeOldRupeeSymbol=price.replace("₹","RS ")
    print("Price:",  removeOldRupeeSymbol)
    rating_container = container.find_all("div",{"class":"hGSR34"})
    rating=rating_container[0].text.strip()
    print("Rating:",rating)
    print("")
    fixed_product_name=product_name.replace(",","|")
    fixed_price=removeOldRupeeSymbol.replace(",","")

    details=(fixed_product_name+","+fixed_price+","+rating+"\n")

    f.write(details)


f.close()