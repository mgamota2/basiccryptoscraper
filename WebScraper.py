#!/usr/bin/env python
# coding: utf-8

# In[143]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[150]:


page = requests.get("https://www.marketwatch.com/market-data/cryptocurrency?mod=currencies-market-data")


# In[151]:


soup=BeautifulSoup(page.content, "html5lib")


# In[203]:


names=[]
price=[]
change=[]

data={"Name":names,"Price":price,"Change":change}

area=soup.find('div', class_='layout layout--5050')
table=area.find('table',class_='table')
body=table.find('tbody',class_='table__body')

rows = body.find_all('td', class_=['table__cell w55 ticker-positive', 'table__cell w55 ticker-negative'])
r2 = body.find_all('td', class_='table__cell w15')

for row in rows:
    if row.find('a',class_='link').text:
        name=row.find('a', class_="link").text
        names.append(name)

for r in r2:
     if r.find('bg-quote',class_=('ignore-color')):
        prices=r.find('bg-quote',class_=('ignore-color')).text
        price.append(prices)
        
for r in r2:
    if r.find('bg-quote',class_=['positive','negative']):
        if '%' in r.find('bg-quote',class_=['positive','negative']).text:
            if r.find('bg-quote',class_=['positive','negative']):
                percent=r.find('bg-quote').text
                change.append(percent)   


             
        
df = pd.DataFrame(data)
print(df)


# In[ ]:





# In[ ]:




