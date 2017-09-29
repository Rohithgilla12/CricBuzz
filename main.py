import requests
from bs4 import BeautifulSoup
import time
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
for i in range(len(datapath)):
    print str(i+1)+")"+series_names[i]
ip=input("Enter the match number")
datapath=datapath[ip-1]
series_names=series_names[ip-1]
com_url=datapath+"commentary.xml"
while(True):
    time.sleep(15)
    r=requests.get(com_url)
    soup=BeautifulSoup(r.content,'html.parser')
    temp=soup.find('c')
    temp=str(temp)
    temp=temp.replace('<c><![CDATA[',"")
    temp=temp.replace("]]></c>","")
    print temp
# print datapath,series_names








# print datapath
# print series_names
