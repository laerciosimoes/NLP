import nltk

with open('sample_text.txt', encoding='utf-8') as f:
    paragraph = f.read()

    sentences = nltk.sent_tokenize(paragraph)
    print("Sentences:")
    print("-------------------")
    for item in sentences:
        print(item)
