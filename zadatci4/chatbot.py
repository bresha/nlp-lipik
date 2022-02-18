from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def generate_response(sentence):
    input_vector = bow_vectorizer.transform([sentence])
    print(input_vector)
    predict = classifier.predict(input_vector)
    print(predict)
    index = int(predict[0])
    print (index)
    return answers[index-1]

def start_chat():
    while True:
        user_response = input()
        if user_response=="exit":
            break
        else:    
            reply = generate_response(user_response)+"\n"
            print(reply)
    return


labels = []
questions = []
for line in open('pitanja.txt', encoding="utf8"):
    labels.append(line.strip().split(" ")[-1])
    questions.append(" ".join(line.strip().split(" ")[:-1]))
answers = []
for line in open('odgovori.txt', encoding="utf8"):
    answers.append(line.strip())

bow_vectorizer = CountVectorizer()
training_vectors = bow_vectorizer.fit_transform(questions)

classifier = MultinomialNB()
classifier.fit(training_vectors, labels)

start_chat()