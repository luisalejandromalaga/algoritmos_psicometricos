# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:00:31 2023

@author: Alappont S.A.C.

Utrecht Work Engagement Scale (UWES)
"""

import numpy as np
import pandas as pd
import math


datos =  pd.read_excel('data.xlsx')


"""
Conversor de items
"""
#Likert
t1 = {}#Array vacio

for col in datos.columns[0:17]:
    row = []#aaray vacion
    for i in datos[col]:
        if i == "Nunca o ninguna vez" : row.append(0)
        if i == "Casi nunca o pocas veces al año" : row.append(1)
        if i == "Algunas veces o una vez al mes o menos" : row.append(2)
        if i == "Regularmente o pocas veces al mes" : row.append(3)
        if i == "Bastante veces o una vez por semana" : row.append(4)
        if i == "Casi siempre o pocas veces por semana" : row.append(5)
        if i == "Siempre o todos los días" : row.append(6)
    t1[col] = row
    
t1_key = pd.DataFrame(t1.keys())
t1_key.columns = ['key']

d = pd.DataFrame.from_dict(t1, orient='index')
test = d.T


"""
Declaración de items 
"""
items = test.columns
i1 = test[items[0]]
i2 = test[items[1]]
i3 = test[items[2]]
i4 = test[items[3]]
i5 = test[items[4]]
i6 = test[items[5]]
i7 = test[items[6]]
i8 = test[items[7]]
i9 = test[items[8]]
i10 = test[items[9]]
i11 = test[items[10]]
i12 = test[items[11]]
i13 = test[items[12]]
i14 = test[items[13]]
i15 = test[items[14]]
i16 = test[items[15]]
i17 = test[items[16]]


"""
Declaración de dimensiones
"""

#Vigor
vigor = pd.DataFrame(
    np.sum(
    pd.concat([i1, i4, i8, i12, i15, i17], axis=1)
    ,axis=1)
)
vigor = pd.DataFrame(vigor)
vigor = vigor/6
vigor.columns = ['Vigor']

#Dedicación
dedicacion = pd.DataFrame(
    np.sum(
    pd.concat([i2, i5, i7, i10, i13], axis=1)
    ,axis=1)
)
dedicacion = pd.DataFrame(dedicacion)
dedicacion = dedicacion/5
dedicacion.columns = ['Dedicación']


#Absorción
absorcion = pd.DataFrame(
    np.sum(
    pd.concat([i3, i6, i9, i11, i14, i16], axis=1)
    ,axis=1)
)
absorcion = pd.DataFrame(absorcion)
absorcion = absorcion/6
absorcion.columns = ['Absorción']


#Total
total = pd.DataFrame(
    np.sum(
    pd.concat([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17], axis=1)
    ,axis=1)
)
total = pd.DataFrame(total)
total = total/17
total.columns = ['Total']



"""
Conversión en categorías
"""

vigor_cat = []
for i in vigor['Vigor']:
   if(2.17>=i): vigor_cat.append(1)#Muy bajo
   if(3.20>=i>2.17): vigor_cat.append(2)#Bajo
   if(4.80>=i>3.20): vigor_cat.append(3)#Promedio
   if(5.65>=i>4.80): vigor_cat.append(4)#Alto
   if(i>5.65): vigor_cat.append(5)#Muy alto
vigor_cat = pd.DataFrame(vigor_cat)
vigor_cat.columns = ['Vigor']


dedicacion_cat = []
for i in dedicacion['Dedicación']:
   if(1.60>=i): dedicacion_cat.append(1)#Muy bajo
   if(3.00>=i>1.60): dedicacion_cat.append(2)#Bajo
   if(4.90>=i>3.00): dedicacion_cat.append(3)#Promedio
   if(5.79>=i>4.90): dedicacion_cat.append(4)#Alto
   if(i>5.79): dedicacion_cat.append(5)#Muy alto
dedicacion_cat = pd.DataFrame(dedicacion_cat)
dedicacion_cat.columns = ['Dedicación']


absorcion_cat = []
for i in absorcion['Absorción']:
   if(1.60>=i): absorcion_cat.append(1)#Muy bajo
   if(2.75>=i>1.60): absorcion_cat.append(2)#Bajo
   if(4.40>=i>2.75): absorcion_cat.append(3)#Promedio
   if(5.35>=i>4.40): absorcion_cat.append(4)#Alto
   if(i>5.35): absorcion_cat.append(5)#Muy alto
absorcion_cat = pd.DataFrame(absorcion_cat)
absorcion_cat.columns = ['Absorción']

total_cat = []
for i in total['Total']:
   if(1.93>=i): total_cat.append(1)#Muy bajo
   if(3.06>=i>1.93): total_cat.append(2)#Bajo
   if(4.66>=i>3.06): total_cat.append(3)#Promedio
   if(5.53>=i>4.66): total_cat.append(4)#Alto
   if(i>5.53): total_cat.append(5)#Muy alto
total_cat = pd.DataFrame(total_cat)
total_cat.columns = ['Total']



#Exportamos las puntuaciones directas y transformadas
cols= [vigor, dedicacion, absorcion, total, vigor_cat, dedicacion_cat, absorcion_cat, total_cat]
export = pd.concat(cols, axis=1)
export = pd.DataFrame(export)

export.to_excel('uwes_corr.xlsx', index = False)
    

















