import nltk

with open('sample_text.txt', encoding='utf-8') as f:
    paragraph = f.read()

    sentences = nltk.sent_tokenize(paragraph)

    words = nltk.word_tokenize(paragraph)
    print("Words:")
    print("-------------------")
    for item in words:
        print(item)
