# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 04:35:11 2016

@author: rishikesh
"""

import matplotlib.pyplot as plt
import numpy as np
import csv 
# Using CSV file function
firstLine=True
labelX=''
labelY=''
x=[]
y=[]
# Read CSV file using csv library
with open('USAccDeaths.csv','r') as csvfile:
    plots=csv.reader(csvfile, delimiter=',')
    for row in plots:
        if firstLine :
            labelX=row[1]
            labelY=row[2]
            firstLine=False
            continue
        x.append(float(row[1]))
        y.append(float(row[2]))
        
plt.bar(x,y)

plt.xlabel(labelX)
plt.ylabel(labelY)
plt.title('Intresting Graph \n Check it out')
plt.show()

#Using numpy lib

n,x,y=np.loadtxt('USAccDeaths.csv',delimiter=',',unpack=True)
plt.bar(x,y)

plt.xlabel(labelX)
plt.ylabel(labelY)
plt.title('Intresting Graph \n Check it out')
plt.show()

# Data from Internet
import urllib2
import matplotlib.dates as mdates
def stockData(stock):
    stock_price_url='http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'    
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
        
    plt.plot_date(date,closep,'-',label='price')
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
