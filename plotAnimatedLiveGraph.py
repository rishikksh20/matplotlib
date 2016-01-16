# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 00:27:32 2016

@author: rishikesh
"""

import matplotlib.pyplot as plt
import matplotlib.animation as anime



fig=plt.figure()
axisPlot=fig.add_subplot(1,1,1)

def animate(i):
    plot_data=open('sampleData.txt','r').read()
    lines = plot_data.split('\n')
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x,y=line.split(',')
            xs.append(x)
            ys.append(y)
    axisPlot.clear()
    axisPlot.plot(xs,ys)
    
ani= anime.FuncAnimation(fig,animate,interval=1000)
    