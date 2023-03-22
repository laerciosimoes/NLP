
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

with open('sample_text.txt', encoding='utf-8') as f:
    paragraph = f.read()

    sentences = nltk.sent_tokenize(paragraph)
    stemmer = PorterStemmer()

    for item in sentences:
        words = nltk.word_tokenize(item)
        words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
        print(' '.join(words))
