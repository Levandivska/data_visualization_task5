#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

#- карта, котра відображає рівень приросту / скорочення населення за регіонами станом на останній доступний рік

#- лінійний графік, котрий відображає рівень приросту / скорочення населення за регіонами за всіма роками (одна лінія на графіку - один регіон)
'''
'Ukraine', 'Crimea', 'Vinnytsya', 'Volyn', "Dnipropetrovs'k", "Donets'k", 'Zhytomyr', 'Transcarpathia', 'Zaporizhzhya', "Ivano-Frankivs'k", 'Kyiv', 'Kirovohrad', "Luhans'k", "L'viv", 'Mykolayiv', 'Odesa', 'Poltava', 'Rivne', 'Sumy', "Ternopil'", 'Kharkiv', 'Kherson', "Khmel'nyts'kyy", 'Cherkasy', 'Chernivtsi', 'Chernihiv', 'Kyiv City', "Sevastopol'"]
'''
OBL_CENTRY=[[50.45,30.52],[44.96,34.11],[49.23,28.48],[50.76,25.34],[48.46,35.04],[48.02,37.8],[52.26,28.68],[48.62,22.3],[47.82,35.19],[48.92,24.71],[50.45,30.52],[48.51,32.26],[48.57,39.32],[49.84,24.02],[49.97,32.0],[46.48,30.73],[49.59,34.54],[50.62,26.32],[50.92,34.8],[49.55,25.59],[49.98,36.25],[49.66,32.62],[49.42,27.0],[49.43,32.06],[48.29,25.94],[51.51,31.28],[50.45,30.52],[44.59,33.52]]


Data=pd.read_csv('population_trends.csv',sep=',')
Data.head(1)
print(Data)

#"region","year","rate"
provinces = Data.region.drop_duplicates().to_list()

#print(provinces)

REGIONS=[]
LAST=[]

for pr in provinces:
        rrs=Data.where(Data.region==pr).dropna().rate.to_list()   #list of populations
        yys=Data.where(Data.region==pr).dropna().year.to_list() 
        rr=[]
        for r in rrs:
                rr.append(float(r))
        yy=[]
        for y in yys:
                yy.append(int(y))
        ly=len(rr)
        lr=len(yy)
        
        print(f" У {pr} області динамика неселення за останній {rr[lr-1]} рік становить {yy[ly-1]}")
        REGIONS.append([ pr ,rr,yy ])
        LAST.append([pr,rr[lr-1], yy[ly-1]])

#print(REGIONS)        
#print (LAST)


fig,ax = plt.subplots()


for reg in REGIONS:
#       print(reg)
       ax.plot(reg[2],reg[1],label=reg[0])


ax.grid( axis='y',color='0.95')
ax.legend(title='')
plt.title('Динамика населення по областям:')
ax.set(xlabel='Рік',ylabel='Різниця')

plt.show()


fig = go.Figure(go.Scattermapbox(
    mode = "markers"
    ))

i=0
for reg in REGIONS:
        fig.add_trace(go.Scattermapbox(
            mode = "markers",
            lon = [ OBL_CENTRY[i][1]  ],
            lat = [ OBL_CENTRY[i][0]  ],
            text="Остання відома динамика населення "+str(reg[1][-1]),
    marker = {'size': 20}))        
        i+=1





fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})

fig.show()

