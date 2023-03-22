import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


with open('sample_text.txt', encoding='utf-8') as f:
    paragraph = f.read()


    ps = PorterStemmer()
    wordnet=WordNetLemmatizer()
    sentences = nltk.sent_tokenize(paragraph)
    corpus = []
    for item in sentences:
        review = re.sub('[^a-zA-Z]', ' ', item)
        review = review.lower()
        review = review.split()
        review = [wordnet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
        review = ' '.join(review)
        print(review) 
        corpus.append(review)

    # Creating the TF-IDF model
    cv = TfidfVectorizer()
    X = cv.fit_transform(corpus).toarray()
    print(corpus)
    print(X)