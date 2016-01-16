# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 02:57:36 2016

@author: rishikesh
"""
#Simple plot

import matplotlib.pyplot as plt
x=[1,2,3]
y=[5,7,4]
x2=[6,6,5]
y2=[3,8,6]
plt.plot(x,y,label="First")
plt.plot(x2,y2,label="Second")
plt.xlabel('Plot Number')
plt.ylabel('Impotant var')
plt.title('Intresting Graph \n Check it out')
plt.legend()
plt.show()

# Bar chart
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[6,5,7,8,3]
plt.bar(x,y,label="Bar Chart",color='c')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresting Graph \n Check it out')
plt.legend()
plt.show()

#Histogram
population_ages=[10,40,30,90,80,34,56,78,34,56,23,12,32,43,54,65,6,53,65,78,87,65,43,23]
#ids=[x for x in range(len(population_ages))]
#plt.bar(ids,population_ages)
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresting Graph \n Check it out')
plt.show()

#Scatter Plot
x=[1,2,3,4,5,6,7,8,9]
y=[9,8,7,6,5,4,3,2,1]

plt.scatter(x,y,label="scatter plot",color="k",s=10,marker="*")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresting Graph \n Check it out')
plt.legend()
plt.show()

#Stack Plot
days=[1,2,3,4,5]
sleeping=[5,6,7,5,6]
eating=[2,1,3,4,2]
working=[8,9,7,9,9]
playing=[2,3,2,4,3]

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])
# Stack plot can't labeled, so for labelling purpose
plt.plot([],[],color='m',label='Sleeping', linewidth=5)
plt.plot([],[],color='c',label='Eating', linewidth=5)
plt.plot([],[],color='r',label='Working', linewidth=5)
plt.plot([],[],color='k',label='Playing', linewidth=5)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresting Graph \n Check it out')
plt.legend()
plt.show()

#Pie Chart
days=[1,2,3,4,5]
sleeping=[5,6,7,5,6]
eating=[2,1,3,4,2]
working=[8,9,7,9,9]
playing=[2,3,2,4,3]

slices=[6,2,9,3]
activities=['Sleeping','Eating','Working','Playing']
colours=['m','c','r','b']
plt.pie(slices,
        labels=activities,
        colors=colours,
        startangle=90,          #startangle by default=0 degree
        shadow=True,            # Give nice shadowing effect
        explode=(0,0.1,0,0),    # Slice out Eating piece section from main pie 
        autopct='%1.2f%%')      # For showing %

#plt.xlabel('x')
#plt.ylabel('y')
plt.title('Intresting Graph \n Check it out')
#plt.legend()
plt.show()


# CandleStick OHLC graphs

import numpy as np
import urllib2
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc

def stockData(stock):
    fig=plt.figure()
    subPlot=plt.subplot2grid((1,1),(0,0))
    stock_price_url='http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'    
    source_req=urllib2.Request(stock_price_url)
    source_response=urllib2.urlopen(source_req)
    source_code=source_response.read().decode()
    
    stock_data=[]
    split_source=source_code.split('\n')
    
    for  line in split_source:
        split_line=line.split(',')
        if len(split_line)==6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)
                
                
    date,closep,highp,lowp,openp,volume=np.loadtxt(stock_data,
                                              delimiter=',',
                                              unpack=True,
                                              converters={0: bytespdate2num('%Y%m%d')})
        
    x=0
    y=len(date)
    ohlc=[]
    
    while x<y:
        append_me=date[x],openp[x],highp[x],lowp[x],closep[x],volume[x]
        ohlc.append(append_me)
        x+=1
        
    candlestick_ohlc(subPlot,ohlc,width=0.4,colorup='#77d899',colordown='#db4f3f')
    
    for label in subPlot.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    subPlot.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    subPlot.xaxis.set_major_locater(mticker.MaxNLocator(10))
    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Intresting Graph \n Check it out')
    plt.show()
    
def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    


stockData('TSLA') #forecasting tesla stock prices