#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 21:49:54 2023

@author: dylanshih
"""

import spacy

nlp = spacy.load("en_core_web_sm")

class SRLLabel:
    def __init__(self, sentences: list[str]) -> None:
        self.sentences = sentences
        
        
    def allow_list(self, allowList):
        filtered_sentences = []
        for sentence in self.sentences:
            doc = nlp(sentence)
            filtered_tokens = [token.text for token in doc if token.pos_ in allowList]
            filtered_sentence = " ".join(filtered_tokens)
            filtered_sentences.append(filtered_sentence)
        return filtered_sentences
    
    def deny_list(self, denyList):
        filtered_sentences = []
        for sentence in self.sentences:
            doc = nlp(sentence)
            filtered_tokens = [token.text for token in doc if token.pos_ not in denyList]
            filtered_sentence = " ".join(filtered_tokens)
            filtered_sentences.append(filtered_sentence)
        return filtered_sentences
    
    def filter_sentences(self, allowList, denyList):
        self.allow_list(allowList)
        self.deny_list(denyList)
        

if __name__ == "__main__":
    input_sentences = [
        "What are the latest advancements in artificial intelligence?",
        "How do I create a website from scratch?",
        "What are the symptoms of the flu?"]
    srl = SRLLabel(input_sentences)
    print(srl.filter_sentences(["NOUN", "VERB", "ADJ"]))