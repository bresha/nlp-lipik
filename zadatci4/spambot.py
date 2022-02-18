import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
import string
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


df = pd.read_csv("spam.csv",encoding = "latin-1")
print(df.head())
print(df.shape)

print(sum(df.iloc[:, 2].notna()))
print(df.iloc[:, 2].unique())

print(sum(df.iloc[:, 3].notna()))
print(df.iloc[:, 3].unique())

print(sum(df.iloc[:, 4].notna()))
print(df.iloc[:, 4].unique())

df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
print(df.head())

df.columns = ["klasa", "poruke"]
print(df.head())

df['length'] = df['poruke'].apply(len)
print(df.head())

df.hist(column='length',by='klasa',bins=50, figsize=(15,6))
plt.show()

print(df.length.describe())

print(df[df['length']==910]['poruke'].iloc[0])

df = df.drop(["length"], axis=1)
print(df.head())

print(df.groupby('klasa').count())

label_counts = df.klasa.value_counts()
plt.figure(figsize = (12,6))
sns.barplot(label_counts.index, label_counts.values, alpha = 0.9)
plt.show()

print(df.groupby('klasa').describe())


def obrada_teksta(poruke):
    bez_interpunk = [znak for znak in poruke if znak not in string.punctuation]
    bez_interpunk = ''.join(bez_interpunk)

    bez_stop_rijeci = [rijec for rijec in bez_interpunk.split() if rijec.lower() not in stopwords.words('english')]
    
    return bez_stop_rijeci

df['poruke'] = df['poruke'].apply(obrada_teksta)
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(df['poruke'],df['klasa'],test_size=0.25)

pipeline = Pipeline([
    ('bow',CountVectorizer(analyzer=obrada_teksta)),
    ('tfidf',TfidfTransformer()), 
    ('classifier',MultinomialNB())
])

pipeline.fit(X_train,y_train)
predictions = pipeline.predict(X_test)

print(classification_report(y_test,predictions))