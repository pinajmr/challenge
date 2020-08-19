#1.Donwloads date titanic  kaggle.com/c/titanic
#2.Merge three CSVs( gender_submission,test y train)

#Answer this questions 
#1.How many people were going on the titanic?
#2.How many men and women survived?
# Top 10 ages taht more survived and the top 10 age not survived
# 4 How many positions or titles were going on the titanic? #Note: used regular expression
#  5 How much summary the valor tickets in USD ?

import pandas as pd 
import numpy as np

def run():

    df0 = pd.read_csv('gender_submission.csv')
    df1 = pd.read_csv('test.csv')
    df2 = pd.read_csv('train.csv')
    
    df01 = pd.merge(df0, df1  ,on = 'PassengerId', how='inner')
    
    df = pd.concat([df2,df01])
    df.index = range(df.shape[0])
    
    df.style.format('{:.2f')

    #1. How many people were going the titanic
    people_total = df.sort_values(by= 'PassengerId', ascending = 'False').nunique()
    print(f'How many people were going on the titanic : {people_total[0]} people' )
   
    #2. How many men and women survived?
    all_survived = sum((df['Survived']==1))
    men_survived = sum((df['Survived']==1) & (df['Sex']=='male'))
    women_survived = sum((df['Survived']==1) & (df['Sex']=='female'))
    
    print(f'How many survived : {all_survived}')
    print(f'How many men survived : {men_survived}')
    print(f'How many wome survived : {women_survived}')
    
if __name__ == '__main__':
    run()