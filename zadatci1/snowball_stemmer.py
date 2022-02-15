import pandas as pd
from nltk.stem.snowball import SnowballStemmer

text=['I like fishing','I eat fish','There are many fishes in pound']

df = pd.DataFrame({'text': text})

st = SnowballStemmer('english')

df['text'] = df['text'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))

print(df)
