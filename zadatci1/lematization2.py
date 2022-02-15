import pandas as pd
from textblob import Word

text=['I like fishing','I eat fish','There are many fishes in pound', 'leaves and leaf']

df = pd.DataFrame({'text': text})
df['text'] = df['text'].apply(lambda x: " ".join([Word(word). lemmatize() for word in x.split()]))

print(df)
