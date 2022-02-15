import pandas as pd
import nltk
from nltk.corpus import stopwords

text = ['Artificial intelligence is intelligence demonstrated by machines', 
        'Leading AI textbooks define the field as the study of intelligent agents', 
        'AI applications include advanced web search engines', 
        'Artificial intelligence was founded as an academic discipline in 1956', 
        'various sub-fields of AI research are centered around particular goals.']

df = pd.DataFrame({'text': text})

df['text'] = df['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))

stop = stopwords.words('english')

df['text'] = df['text'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

print(df['text'])