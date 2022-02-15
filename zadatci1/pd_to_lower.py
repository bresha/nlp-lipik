import pandas as pd

text = ['Artificial intelligence is intelligence demonstrated by machines', 
        'Leading AI textbooks define the field as the study of intelligent agents', 
        'AI applications include advanced web search engines', 
        'Artificial intelligence was founded as an academic discipline in 1956', 
        'various sub-fields of AI research are centered around particular goals.']

df = pd.DataFrame({'text': text})

df['text'] = df['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))

print(df)