# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:24:43 2019

@author: Mary Mae
"""

import pandas as pd
DataF = {'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],
         'Dimension':['Length','Width','Height','Length','Width','Height'],
         'Value':[6,4,2,5,3,4]}
Messy=pd.DataFrame(DataF,columns=['Box','Dimension','Value'])
Tidy=Messy.pivot(index='Box',columns='Dimension',values='Value').reset_index()
Data= Tidy[['Height','Length','Width']].transpose().prod().tolist()
Vol1= {'Box':['Box1','Box2'],
         'Volume':Data}
Vol=pd.DataFrame(Vol1,columns=['Box','Volume'])
TidyVolume=pd.merge(Tidy,Vol,how='inner', on='Box')