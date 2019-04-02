
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv('./Fruit.csv')

def NaiveBaye(Fruit,condition):
    sumfruit=data.sum(1)
    sumcond=data.sum(0)
    coll=data.columns.tolist() 
    Pfc= data[condition][data.loc[data['FRUIT'] == Fruit].index[0]]
    Pc=sumcond[coll.index(condition)]
    Pf=sumfruit[data.loc[data['FRUIT'] == Fruit].index[0]]
    Pt=0
    for x in sumfruit:
        Pt=Pt+x
    P=((Pfc/Pc)*(Pc/Pt))/(Pf/Pt)
    return P
Pyf=NaiveBaye('banana','Yellow ')
Psf=NaiveBaye('banana','Sweet')
Plf=NaiveBaye('banana','Long')

print(Pyf*Psf*Plf)

