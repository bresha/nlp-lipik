import pandas as pd
from nltk.stem.lancaster import LancasterStemmer

text=['I like fishing','I eat fish','There are many fishes in pound']

df = pd.DataFrame({'text': text})

st = LancasterStemmer()

df['text'] = df['text'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

print(df)
