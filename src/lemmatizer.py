import stanza
nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma')

class Lemmatizer:
    def __init__(self, sentences: list[str]) -> None:
        """Create lemmatizer for the given sentences.""" 
        self.sentences = sentences
        self.taggers = [nlp(sent) for sent in self.sentences]

    def to_lemma(self, conversion_types: Optional[list[str]]) -> None:
        """Convert words to their lemma form. 

        Arguments: 
        conversion_types -- the parts of speech to be converted to lemma form. 
            If not specified, all words will be converted.
        """

        for i, tagger in enumerate(self.taggers):
            lemmas = []
            for sent in tagger.sentences:
                for word in sent.words:
                    if conversion_types != []:
                        if word.upos in conversion_types:
                            lemmas.append(word.lemma)
                        else:
                            lemmas.append(word)
                    else:    
                        lemmas.append(word.lemma)
            self.sentences[i] = ' '.join(lemmas)
    
    def get_sentences(self) -> list[str]:
        """Return the transformed sentences."""
        return self.sentences

    

