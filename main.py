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
ip=input("Enter the match number: ")
datapath=datapath[ip-1]
series_names=series_names[ip-1]
com_url=datapath+"commentary.xml"
while(True):
    r=requests.get(com_url)
    soup=BeautifulSoup(r.content,'html.parser')
    temp=soup.find('c')
    comm=str(temp)
    comm=comm.replace('<c><![CDATA[',"")
    comm=comm.replace("]]></c>","")
    print "____"*20
    print comm
    test=comm
    temp=str(soup.find_all('mscr'))
    runs=temp.split('r="')[3]
    runs=runs.split('"')[0]
    wickets=temp.split('wkts="')[1]
    wickets=wickets.split('"')[0]
    overs=temp.split('ovrs')
    overs=overs[1]
    overs=overs.split('"')[1]
    batsman=temp.split('btsmn')
    bat1=batsman[1].split('sname="')[1].split('"')[0]
    bat2=batsman[3].split('sname="')[1].split('"')[0]
    r1=batsman[1].split('r="')[1].split('"')[0]
    r2=batsman[3].split('r="')[1].split('"')[0]
    # print "____"*20
    print "Score :"+runs + "/"+wickets
    print "Overs :"+str(overs)
    print bat1+" :"+r1," "+bat2+" :"+r2
    time.sleep(15)

# print datapath,series_names








# print datapath
# print series_names
