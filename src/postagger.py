import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')

class POSTagger: 
    """A part-of-speech tagger for English with capacity to remove words of a given type."""

    def __init__(self, sentences: list[str]) -> None:
        """Create tagger for the given sentences."""
        self.sentences = sentences
        self.taggers = [nlp(sent) for sent in self.sentences]

    def remove_types(self, types: list[str]) -> None:
        """Remove words of specified types"""
        for i, tagger in enumerate(self.taggers): 
            valid_words = []
            for sent in tagger.sentences: 
                for word in sent.words:
                    if word.upos not in types:
                        valid_words.append(word.text)
            self.sentences[i] = ' '.join(valid_words)
    
    def keep_types(self, types: list[str]) -> None:
        """Keep words of specified types"""
        for i, tagger in enumerate(self.taggers): 
            valid_words = []
            for sent in tagger.sentences: 
                for word in sent.words:
                    if word.upos in types:
                        valid_words.append(word.text)
            self.sentences[i] = ' '.join(valid_words)
    
    def get_sentences(self) -> list[str]:
        """Return the transofrmed sentences."""
        return self.sentences