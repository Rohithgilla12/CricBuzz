import requests
from bs4 import BeautifulSoup
url="http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
temp=soup.find_all('match')
series_names=[]
datapath=[]
for i in temp:
    i=str(i)
    i=i.split('datapath')[1]
    i=i.split('"')
    datapath.append(i[1])
    series_names.append(i[13])
print datapath
print series_names
