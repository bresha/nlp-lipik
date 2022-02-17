import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt


wt_sentences = webtext.sents('firefox.txt')
wt_words = webtext.words('firefox.txt')

print(len(wt_sentences))
print(len(wt_words))

frequency_dist = nltk.FreqDist(wt_words)
print(frequency_dist.items())

sorted_frequency_dist = sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=False)
print(sorted_frequency_dist)

large_words = dict([(k,v) for k,v in frequency_dist.items() if len(k)>3])
print(large_words)

frequency_dist = FreqDist(large_words)
frequency_dist.plot(50)

wcloud = WordCloud().generate_from_frequencies(frequency_dist)

plt.imshow(wcloud)
plt.axis("off")
plt.show()
