import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def delete_stopwords(sentences: list[str]) -> list[str]:
    