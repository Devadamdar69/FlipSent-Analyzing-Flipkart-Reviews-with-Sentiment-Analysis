import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

URL = 'https://www.flipkart.com/samsung-22-inch-full-hd-ips-panel-monitor-ls22c310eawxxl/product-reviews/itmac31067559ef1?pid=MONGAQTQKCEZGVSC&lid=LSTMONGAQTQKCEZGVSCG4LB7V&marketplace=FLIPKART&page='

comment=[]
rating=[]
    
for i in range(1,41):
    r=requests.get(URL+str(i))
    print(i,r)
    while(r.status_code == 429):
        time.sleep(3)
        r=requests.get(URL+str(i))
        print(i,r)

    soup = bs(r.content,'html.parser')
    soup1 = soup.find('body')
    soup2 = soup1.find_all('div', class_='cPHDOP col-12-12')
    soup2.pop(0)
    soup2.pop(0)
    soup2.pop(0)
    soup2.pop(10)
    # print(soup2[0])
    for i in soup2:
        temp= i.find_all('div',class_='row')
        comment.append((temp[1].text).replace('READ MORE',''))
        rating.append(temp[0].text[0])
        # print(temp)


dict = {'rating':rating,
         'comment':comment}

df = pd.DataFrame(dict)

df.to_csv('Review.csv')