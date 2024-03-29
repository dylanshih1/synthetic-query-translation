import stanza

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')

class DependencyParser: 
    """A dependency parser for English with capacity to keep syntactic heads."""

    def __init__(self, sentences: list[str]) -> None:
        """Create dependency parser for the given sentences."""
        self.sentences = sentences
        self.taggers = [nlp(sent) for sent in self.sentences]

    def keep_heads(self) -> None:
        """Keep syntactic heads in order that they appear"""
        for i, tagger in enumerate(self.taggers): 
            head_indices = set()
            valid_words = []
            for sent in tagger.sentences: 
                for word in sent.words:
                    if word.head != 0:
                        head_indices.add(word.head-1)
                for index in sorted(head_indices):
                    valid_words.append(sent.words[index].text)
            self.sentences[i] = ' '.join(valid_words)
    
    def keep_topic(self) -> None:
        for i, tagger in enumerate(self.taggers): 
            word_ids = set()
            queue = []
            for sent in tagger.sentences: 
                for word in sent.words:
                    if word.deprel == 'nsubj':
                        queue.append(word.id)
                        word_ids.add(word.id)
                    if word.deprel == 'obj':
                        if len(queue) != 0:
                            queue.pop()        # pop off nsubj
                            word_ids.pop()
                        queue.append(word.id)
                        word_ids.add(word.id)
                # queue either has nsubj or obj root 
                assert len(queue) == 1
                # get all words dependent on root
                while queue:
                    word = queue.pop(0)
                    for child in sent.words:
                        if child.head == word:
                            queue.append(child.id)
                            word_ids.add(child.id)
            valid_words = [sent.words[index-1].text for index in sorted(word_ids)]
            self.sentences[i] = ' '.join(valid_words)

    def get_sentences(self) -> list[str]:
        """Return the transofrmed sentences."""
        return self.sentences