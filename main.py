import requests
from gi.repository import Notify
from bs4 import BeautifulSoup
import time
Notify.init("#CricBuzz!")
url="http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
temp=soup.find_all('match')
series_names=[]
datapath=[]
count=0
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
old_overs="0"
counter=0;
loop_v=0
while(loop_v==0):
    r=requests.get(com_url)
    soup=BeautifulSoup(r.content,'html.parser')
    try:
        temp=soup.find('c')
        comm=str(temp)
        comm=comm.replace('<c><![CDATA[',"")
        comm=comm.replace("]]></c>","")
        test=comm
    except:
        counter+=1
        pass
    temp=str(soup.find_all('mscr'))
    runs=temp.split('r="')[3]
    runs=runs.split('"')[0]
    wickets=temp.split('wkts="')[1]
    wickets=wickets.split('"')[0]
    overs=temp.split('ovrs')
    overs=overs[1]
    overs=overs.split('"')[1]
    batsman=temp.split('btsmn')
    try:
        bat1=batsman[1].split('sname="')[1].split('"')[0]
        r1=batsman[1].split('r="')[1].split('"')[0]
    except:
        counter+=1
        pass
    try:
        bat2=batsman[3].split('sname="')[1].split('"')[0]
        r2=batsman[3].split('r="')[1].split('"')[0]
    except:
        counter+=1
        pass
    # print "____"*20
    if(old_overs ==overs):
        Notify.Notification.new("Score :"+runs + "/"+wickets + '\n'+"Overs :"+str(overs)).show()
        pass
    else:
            print "____"*20
            print comm
            print "Score :"+runs + "/"+wickets
            print "Overs :"+str(overs)
            Notify.Notification.new("Score :"+runs + "/"+wickets + '\n'+"Overs :"+str(overs)).show()
            try:
                print bat1+" :"+r1," "+bat2+" :"+r2
            except:
                pass
    old_overs=overs
    if(int(wickets)==10):
        loop_v=1
    time.sleep(5)
    count+=1
    if(count>3):
        Notify.Notification.new(bat1+" :"+r1," "+bat2+" :"+r2)
        count=0
# print datapath,series_names








# print datapath
# print series_names
