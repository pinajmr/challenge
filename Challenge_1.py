import pandas as pd
import numpy as np
import re

def run():
    #Preprocessing
    df0 = pd.read_csv('gender_submission.csv')
    df1 = pd.read_csv('test.csv')
    df2 = pd.read_csv('train.csv')

    df01 = pd.merge(df0,df1,on = 'PassengerId', how='inner')

    df = pd.concat([df2,df01])
    df.index = range(df.shape[0])

    df.style.format('{:.2f')

    df.to_csv('titanic.csv',index = False)

    df.convert_dtypes().dtypes
    df[['Survived','Sex']] = df[['Survived','Sex']].astype('category')
    df[['Female','Male']] = pd.get_dummies(df['Sex'])
    df[['Death','Live']] = pd.get_dummies(df['Survived'])
    df.rename(columns = {'Name':'Full Name'}, inplace = True)

    df1 = df.copy(deep=True)
    df1.drop(['Pclass','PassengerId','SibSp','Parch','Ticket','Cabin','Sex','Embarked'], axis = 1 ,inplace = True)

    #1. How many people were going the titanic
    people_total = df.nunique()
    print(f'\n How many people were going on the titanic : {people_total[0]} people \n' )

    #2. How many men and women survived?
    #Men
    survived_men = df1.query('(Male == 1) & (Survived	== 1)').count()[0]
    print(f' How many men survived ? : {survived_men} men \n')
    #Women
    survived_women = df1.query('(Female == 1) & (Survived == 1)').count()[0]
    print(f' How many women survived ? : {survived_women} women \n')

    #3.Top 10 ages that  more survived and the top 10 age that not survived
    df_top1= df1.copy(deep = True)
    df_top1.drop(['Survived','Full Name', 'Fare','Female','Male','Death'], axis = 1, inplace = True)
    df_top_survived = df_top1.groupby(by=['Age']).sum().sort_values(by='Live', ascending=False).head(10)
    print('\n What\'s  the top of age survived ? \n')
    print(df_top_survived)

    df_top2= df1.copy(deep = True)
    df_top2.drop(['Survived','Full Name', 'Fare','Female','Male','Live'], axis = 1, inplace = True)
    df_top_death = df_top2.groupby(by=['Age']).sum().sort_values(by='Death', ascending = False).head(10)
    print('\n What\'s  the top of age death ? \n')
    print(df_top_death)


    #4.How many positions or titles were going on the titanic?
    f = open('titanic.csv','r')
    pattern = re.compile(r' ([\w]{1,})\.')
    df_title = []
    for line in f:
        res = pattern.search(line)
        if res:
            df_title.append(res.group(0))

    f.close()
    df_title = pd.DataFrame(df_title)
    df_title.columns = ['Titles']
    df_title = df_title.drop_duplicates()
    df_title.index = range(df_title.shape[0])
    print('\n Positions or titles were going on the Titanic \n')
    print(df_title)

    #5.How much summary the valor tickets in USD ?
    value = df1.apply(lambda x: x['Fare'], axis =1).sum() * 4.886
    print(f'\n Summary the valors of tickets with fee 4.886  $ {value:,.2f} USD \n')


if __name__ == '__main__':
    run()


