# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:55:47 2019

@author: Mary Mae
"""

import pandas as pd
Math= {'Student':['Ice Bear','Panda','Grizzly'],
        'Math':[80,95,79]}
Electronics= {'Student':['Ice Bear','Panda','Grizzly'],
        'Electronics':[85,81,83]}
GEAS= {'Student':['Ice Bear','Panda','Grizzly'],
        'GEAS':[90,79,93]}
ESAT= {'Student':['Ice Bear','Panda','Grizzly'],
        'ESAT':[93,89,88]}
MathA=pd.DataFrame(Math,columns=['Student','Math'])
ElectronicsA=pd.DataFrame(Electronics,columns=['Student','Electronics'])
G=pd.DataFrame(GEAS,columns=['Student','GEAS'])
E=pd.DataFrame(ESAT,columns=['Student','ESAT'])

WBB1=pd.merge(MathA,ElectronicsA,how='inner', on='Student')
WBB2=pd.merge(WBB1,G,how='inner', on='Student')
WBB3=pd.merge(WBB2,E,how='inner', on='Student')

LongFormat1= WBB3.melt(id_vars=['Student'], var_name='Subject', value_name='Grades')
LongFormat2= LongFormat1.sort_values('Student')