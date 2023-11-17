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
        
        
    
    def filter_sentences(self):
        filtered_sentences = []
        for sentence in self.sentences:
            doc = nlp(sentence)
            filtered_tokens = [token.text for token in doc if token.pos_ in {"NOUN", "VERB", "ADJ"} or token.ent_type_]
            filtered_sentence = " ".join(filtered_tokens)
            filtered_sentences.append(filtered_sentence)
        return filtered_sentences
