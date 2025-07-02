import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

productData=[]
def scrape(productID):

    url=f"https://webscraper.io/test-sites/e-commerce/allinone/product/{productID}"
    r = requests.get(url)
    soup = bs(r.content, 'lxml')
    productName= soup.find_all('h4', class_= "title card-title")[0].text.strip()
    productPrice= soup.find_all('h4', class_= "price float-end pull-right")[0].text.strip()
    numOfReviews= soup.find_all('span')[10].text.strip()
    productInfo={'name':productName,
                'price':productPrice,
                'number of reviews':numOfReviews}
    return productInfo

start=1
end=147
for productID in range(start,end+1):
    productInfo = scrape(productID)
    productData.append(productInfo)

df = pd.DataFrame(productData)
df.to_csv('productInfo.csv',index=False)

    