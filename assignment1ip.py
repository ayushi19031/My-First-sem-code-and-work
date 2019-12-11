import urllib.request
import json
date = input("date: ")
currency = input("Currency: ")
desiredcurrency = input("Desired Currency: ")
amount = int(input("amount: "))

def changebase(amount, currency, desiredcurrency, date):
    url1 = urllib.request.urlopen("https://api.exchangeratesapi.io/" + str(date))
    data1 = url1.read()
    chdata = bytes.decode(data1)


#print(chdata)
#print(type(chdata))


#url2 = urllib.request.urlopen("https://api.exchangeratesapi.io/2010-01-12")
#data2 = url2.read()
#print(data2)
#currency = "CAD"
#
#    
#

    x = (chdata[(chdata.index(currency)) + 5 : chdata.index(",", (chdata.index(currency)) + 5)])
    currency1 =float(x)


#y = chdata[(chdata.index(desiredcurrency)) + 5 : int(chdata.index(","))]
#print(y)

    y = (chdata[(chdata.index(desiredcurrency)) + 5 : chdata.index(",", (chdata.index(desiredcurrency)) + 5)])
    des_currency =float(y)


    answer = (float(amount)*float(y))/float(x)
    return (answer)
changebase(amount, currency, desiredcurrency, date)
    

import urllib.request

url1 = urllib.request.urlopen("https://api.exchangeratesapi.io/2010-01-12")
data1 = str(url1.read())
def printAscending(json):
    
    original = input("Hey ")
    y = float((data1[(data1.index(original)) + 5 : data1.index(",", (data1.index(original)) + 5)]))

    k = data1[(data1.index("{", 3 ))+1: (data1.index("}",(data1.index("{", 2 )) ))]
    t = k.split(",")
    print(t)

    a= "" 
    mla = ""

#m = "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" 
    for num in t:
        x = float(num[num.index(":") + 1:])
        ans = x/y
        z = "1 " + original + " = " + str( x/y ) + num[num.index('"')+1 : num.index('"', 1)]
        #   print("1 " + original + " = " + str( x/y ) + num[num.index('"')+1 : num.index('"', 1)])
        mla = mla + "," + z
        
        a = a + str(ans) + " "
        print(a)
        b = a.split()
        print(b)
        d = [float(m) for m in b]

    d.sort()
    print(*d)
    mla = mla + ","

    for num in d:
        q = mla.index(str(num))
        print("1 " + original + " = " + mla[q:mla.index(",", q)])
printAscending(data1)   
exit()     
#    
import urllib.request
import datetime

currency = input("currency: ")
desiredcurrency = "CAD"

year1 = int(input("year1: "))
year2 = int(input("year2: "))
month1 = int(input("month1: "))
month2 = int(input("month2: "))
day1 = int(input("day1: "))
day2 = int(input("day2: "))
r = []
t = []

sdate = datetime.date(year1, month1, day1)
edate = datetime.date(year2, month2, day2)

delta = edate - sdate
def extremeFridays(sdate, edate, currency ):
    
    for i in range(delta.days + 1):
        day = sdate + datetime.timedelta(days = i)
        
        if day.weekday() == 4:
            url = urllib.request.urlopen("https://api.exchangeratesapi.io/"  + str(day))
            data = str(url.read())
            
            cindex = data.index(currency)
            dcindex = data.index(desiredcurrency)
            cvalue = data[data.index(":", cindex) + 1 : data.index(",", cindex)]
            
            dcvalue = data[data.index(":", dcindex) + 1 : data.index(",", dcindex)]
            
            amt = float(dcvalue)/float(cvalue)
            jaan = currency + " = " + str(amt) + " " + desiredcurrency
            
            t.append(str(day))
            r.append(float(amt))        
    strengthval = max(r)
    strengthval_index = r.index(strengthval)
    print("Currency weakest on " + str(t[strengthval_index]) + " " + " and " + currency + " = " + str(strengthval) + " " + desiredcurrency)
    minval = min(r)
    minval_index = r.index(minval)
    print("Currency strongest on " + str(t[minval_index]) + " " + " and " + currency + " = " + str(minval) + " " + desiredcurrency)
extremeFridays(sdate, edate, currency)
exit()
import urllib.request
import datetime

currency = input("currency: ")
desiredcurrency = input("desiredcurrency: ")

year1 = int(input("year1: "))
year2 = int(input("year2: "))
month1 = int(input("month1: "))
month2 = int(input("month2: "))
day1 = int(input("day1: "))
day2 = int(input("day2: "))
r = []
t = []

sdate = datetime.date(year1, month1, day1)
edate = datetime.date(year2, month2, day2)

delta = edate - sdate
answer = []
def findMissingdates(sdate, edate):
    
    for i in range(delta.days + 1):
        day = sdate + datetime.timedelta(days = i)
    
        url = urllib.request.urlopen("https://api.exchangeratesapi.io/"  + str(day))
        data = str(url.read())
        kdata = data[::-1]
    
        date_in_reverse = kdata[: kdata.index(":")]
        original_date = date_in_reverse[::-1]
        original_datefinal = original_date[:original_date.index("}")]
        year = int(original_datefinal[1:5])
        month = int(original_datefinal[6:8])
        dayTE = int(original_datefinal[9:11])
        k = datetime.date(year, month, dayTE)
        if k != day:
            answer.append(str(day))
    print("The information for the following dates was not present: ")
    for num in answer:
        print(num)            
findMissingdates(sdate, edate)                     
exit()        
        