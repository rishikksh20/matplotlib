# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 08:17:47 2016

@author: rishi
"""


import matplotlib.pyplot as plt
import numpy as np
import urllib2
import matplotlib.dates as mdates

def stockData(stock):
    fig=plt.figure()
    subPlot=plt.subplot2grid((1,1),(0,0))
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
        
    #Customization to the plot 
    subPlot.plot_date(date,closep,'-',label='price')
    subPlot.fill_between(date,closep,150,where=(closep>150),facecolor='g',alpha=0.5) #Fill the graph 
    subPlot.fill_between(date,closep,150,where=(closep<150),facecolor='r',alpha=0.5) #Fill the graph
    #Rotate the dates label
    for label in subPlot.xaxis.get_ticklabels():
        label.set_rotation(45)
    subPlot.grid(True)#,color='b',linestyle='-',linewidth=1)
    subPlot.xaxis.label.set_color('c')  #Change the color of x-axis label
    subPlot.yaxis.label.set_color('r')  #Change the color of y-axis label
    subPlot.set_yticks([0,100,200,300]) #Customize the y-axis  value ticks  
    
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