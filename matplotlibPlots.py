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
