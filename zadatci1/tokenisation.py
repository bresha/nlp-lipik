import pandas as pd
from textblob import TextBlob

text = ['Arfiticial inteligence is intelligence demonstrated by machines',
        'Leading AI textboks define the field as the study of intelligent agents',
        'AI applications include advanced web search engines',
        'Artificial intelligence was founded as an academic discipline in 1956',
        'various sub-fields of AI research are centered around particular goals.']

df = pd.DataFrame({'text': text})

print(TextBlob(df['text'][3]).words)