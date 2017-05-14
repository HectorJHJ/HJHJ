# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:31:59 2017

@author: Hector
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import csv
import pandas as pd   

#data from https://www7.ncdc.noaa.gov/CDO/CDODivisionalSelect.jsp#
f = open("PNYCTemp.csv")
reader = csv.DictReader(f)

minTemp = []
maxTemp = []

for row in reader:
     if (row['YearMonth'][-2:] == '12'):
         minTemp.append(float(row['TMIN']))
         maxTemp.append(float(row['TMAX']))
      
f.close()
#testing
#print(minTemp[0])
#print(maxTemp[0])
#print(minTemp[36])
#print(maxTemp[36])

avgTemp = []
avg = 0
cooldestYears = []
warmestYears = []

for n in range(0,37):
    avgTemp.append(float("{0:.2f}".format((minTemp[n] + maxTemp[n])/2)))
    #print(avgTemp[n])
    avg = avg + avgTemp[n]
    if n == 36:
        avg = float("{0:.2f}".format(avg/37))
        print("The average temperature is" , avg , "degrees.")
        print("The lowest average temperature is" , min(avgTemp) , "degrees.")
        print("The highest average temperature is" , max(avgTemp) , "degrees.")
        for x in range(0,37):
            if avgTemp[x] == min(avgTemp):
                cooldestYears.append(1980+x)
            if avgTemp[x] == max(avgTemp):
                warmestYears.append(1980+x)
        print('Temperature averages for Decembers in NYC from 1980 to 2016')
        print(avgTemp)
        print('Cooldest Years:')
        print(cooldestYears)
        print('Warmest Years:')
        print(warmestYears)
        
x = [n for n in range(1980,2017)]

plt.plot(x, avgTemp, color='purple') 
plt.plot([1980, 2016], [avg, avg], 'b--', label='Overall Average Temperature')
#plt.plot(x, minTemp, label='Lowest Temperature', color='b') 
#plt.plot(x, maxTemp, label='Highest Temperature', color='r')
plt.title("Average Temperature in NYC(DEC) from 1980 to 2016")
plt.ylabel("Average Temperature")
plt.xlabel("Year")
plt.axis([1980, 2016, 0, 40])
plt.grid(True)
plt.legend()
plt.savefig('tempData.png', format='png', dpi=100)
plt.show()        

firstDecade = [] 
secondDecade = [] 
thirdDecade = [] 
for n in range(7,37):
    if n >= 7 and n <=16:
        firstDecade.append(avgTemp[n])
    if n >=17 and n <=26:
        secondDecade.append(avgTemp[n])
    if n >=27 and n <=36:
        thirdDecade.append(avgTemp[n])
print("The average temperature in December for NYC from 1987-1996 was: {0:.2f}".format(sum(firstDecade)/10))    
print("The average temperature in December for NYC from 1997-2006 was: {0:.2f}".format(sum(secondDecade)/10))    
print("The average temperature in December for NYC from 2007-2016 was: {0:.2f}".format(sum(thirdDecade)/10))    

x = [n for n in range(0,10)]
plt.plot(x, firstDecade, label='1987-1996', color='blue') 
plt.plot(x, secondDecade, label='1997-2006', color='c') 
plt.plot(x, thirdDecade, label='2007-2016', color='m') 
plt.title("Average Temperature in NYC(DEC) by Decade")
plt.ylabel("Average Temperature")
plt.xlabel("Curresponding Year in Decade")
plt.axis([0, 9, 0, 40])
plt.grid(True)
plt.legend()
plt.savefig('tempData2.png', format='png', dpi=100)
plt.show()    

#data form http://www.weather.gov/okx/CentralParkHistorical

p = open("monthlyseasonalsnowfall.csv")
reader2 = csv.DictReader(p)

snowfall = []

for row in reader2:
         snowfall.append(row['DEC '])
      
p.close()

#print(len(snowfall))

print('\n \n')

traceOfHail = []
noSnow = []
highestSnowfall = 0
highest = []
# Holds snowfall data with T replace with 2.7 so it can be shown on a graph
snowfall2 = []
# Holds snowfall data with T replace with 0 to calculate average snowfall
snowfall3 = []
snowToPlay = []

for n in range(111,len(snowfall)):
    if snowfall[n] == 'T ':
        traceOfHail.append((1980+(n-111)))
        snowfall2.append(2.7)
        snowfall3.append(0)
    else:
        snowfall2.append(float(snowfall[n]))
        snowfall3.append(float(snowfall[n]))
        if float(snowfall[n]) > highestSnowfall:
            highestSnowfall = float(snowfall[n])
    if snowfall[n] == '0':
        noSnow.append(1980+(n-111))      
    if n == len(snowfall)-1:
        print('Years with only trace of hail:')
        print(traceOfHail)
        print('Years with no snowfall:')
        print(noSnow)
        print('Year with the highest snowfall:')
        for x in range(111,len(snowfall)):
            if snowfall[x] != 'T ':
                if float(snowfall[x]) == highestSnowfall: 
                    highest.append(1980+(x-111))
                if float(snowfall[x]) >= 4: 
                    snowToPlay.append(1980+(x-111))
        print(highest)
        print('Years with 4 or more inches of snow:')
        print(snowToPlay)
        

print('Most inches of snowfall in Central Park: {}'.format(max(snowfall3)))
print('Average inches of snowfall in Central Park: {0:.2f}'.format(sum(snowfall3)/len(snowfall3)))


x = [n for n in range(1980,2017)]
#df = pd.DataFrame(snowfall2, index = season[111:])
df = pd.DataFrame(snowfall2, index = x)

dfstacked = df.stack()
mask = dfstacked == 2.7
colors = np.array(['b']*len(dfstacked))
colors[mask.values] = 'm'

pliz = dfstacked.plot.bar(title='December Snowfall in Central Park by Season', legend = False, width = .8, figsize = (80,8), color = colors)
pliz.title.set_size(35)
pliz.set_xlabel("Season", fontsize=20)
pliz.set_ylabel("Inches of Snowfall", fontsize=20)
HA = mpatches.Patch(color='m', label='Traces of Hail')
pliz.legend(handles=[HA], loc=2)
