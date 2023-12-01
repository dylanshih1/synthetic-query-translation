import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

stopwords = set(stopwords.words('english'))

def delete_stopwords(sentences: list[str]) -> list[str]:
    non_stopwords = []
    for sentence in sentences:
        new_sentence = []
        for word in sentence.split():
            if word.lower() not in stopwords:
                new_sentence.append(word)
        non_stopwords.append(' '.join(new_sentence))
    return non_stopwords
