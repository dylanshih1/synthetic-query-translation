import stanza
nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')
from typing import Optional

class Lemmatizer:
    def __init__(self, sentences: list[str]) -> None:
        """Create lemmatizer for the given sentences.""" 
        self.sentences = sentences
        self.taggers = [nlp(sent) for sent in self.sentences]

    def convert_all(self) -> None:
        """Convert all words to their lemma form."""
        for i, tagger in enumerate(self.taggers):
            lemmas = []
            for sent in tagger.sentences:
                for word in sent.words:
                    lemmas.append(word.lemma)
            self.sentences[i] = ' '.join(lemmas)

    def convert_types(self, conversion_types: list[str]) -> None:
        """Convert words of specified types to their lemma form."""
        for i, tagger in enumerate(self.taggers):
            lemmas = []
            for sent in tagger.sentences:
                for word in sent.words:
                    if word.upos in conversion_types:
                        lemmas.append(word.lemma)
                    else:
                        lemmas.append(word.text)
            self.sentences[i] = ' '.join(lemmas)
    
    def get_sentences(self) -> list[str]:
        """Return the transformed sentences."""
        return self.sentences

    

