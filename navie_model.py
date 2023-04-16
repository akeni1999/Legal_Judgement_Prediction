#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import joblib


# In[2]:


df = pd.read_csv('Final_Dataset.csv')


# In[3]:


df.head()


# In[4]:


X = df[['Attribute', 'Women?', 'Reason1', 'Reason2']]
Y = df['Lable']


# In[22]:


from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test = train_test_split(X, Y, test_size=0.1, random_state=1)


# In[23]:


from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB() 
gnb.fit(X_train, y_train)


# In[24]:


y_pred = gnb.predict(X_test)


# In[25]:


from sklearn import metrics 
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, y_pred)*100)


# ## User Input

# In[26]:


def lawinfo(a):
    df1= pd.read_csv("IPC Sections.csv")
    x = a.split(',')
    #print(x)
    output_json = {}
    data=df1.groupby(['IPC_Section'])
    for name, value in data:
        if name in x:
            output_json[str(name)] = {
                "title": value['Title'].tolist()[0],
                "description": value['Description.'].tolist()[0]
            }
            print('IPC Section: ',name,":",value['Title'].tolist()[0])
            print('Description:',value['Description.'].tolist()[0])
            print()
    return output_json
    
    
def labelmap(y):
    
    d={0:'302',1:'302,304',2:'304,308',3:'147,148,149,302,307,453,324',4:'147,148,149,323,307,302,326',5:'304',6:'302,299',7:'302,394,397,392',8:'363,366,302,201,376',9:'376,342,302,201',10:'302,307,452,506',11:'313,302',12:'148,149,302,304',13:'366,364',14:'302,307',15:'147,148,342,323,427,506(ii),302',16:'302,498,304-2',17:'302,307,147,148,149',18:'302,313,498',19:'302,304-2',20:'302,392,397,364',21:'302,307,324',22:'302,148,149,147',23:'147,148,302,149,396,397'}
    a=d[y]
    return a

def predict(gnb,x1,x2,x3,x4):
    
    y_pred = gnb.predict([[x1,x2,x3,x4]])
    return y_pred


    
def start():
    l1 = ['0) Murdered','1) Murdered with negligence','2) Culpable homicide','3) Attempt of Murder','4) Attempt to commit culpable homicide','5) Both 0 and 3','6) Both 0 and 2','7) Both 2 and 4']
    for i in l1:
        print(i)
    x1 = int(input("Select the Fact:"))
   
    print()
    
    print("Is victim a woman?")
    x2 = int(input("Yes-1/ No-0"))
    
    print()
    
    l3 = ['0) Dowry','1) Miscarriage without women consent','2) Rape/Gang Rape','3) Sexual intercourse','4) Cruelty by inlaws','5) Rioting','6) Kidnapping','7) Robbery','8) Housetrepass','9) Mischief with explosive substance causing damage','10) endangering life or personal safety of others','11) Voluntarily causing hurt by dangerous weapons or means','No Reason (Press -1)']
    for i in l3:
        print(i)
    x3 = int(input("Select the Reason 1:"))
    
    print()
    
    for i in l3:
        print(i)
    x4 = int(input("Select the Reason 2:"))

    joblib.dump(gnb, 'model.pkl')

    ans=predict(gnb,x1,x2,x3,x4)
    
    ans1=labelmap(ans[0])
    
    print()
    print("The possible IPC Sections applicable to your case :",ans1)
    
    z=input("Want to know more about this IPC Sections? (Y/N)")
    print()
    if z=='Y':
        lawinfo(ans1)
    
    

# start()


# In[ ]:




