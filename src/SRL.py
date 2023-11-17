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

if __name__ == "__main__":
    input_sentences = [
        "Dylan likes chocolate.",
        "The second sentence contains some named entities like New York and John.",
        "The third sentence has multiple verbs and adjectives."
    ]

    SRL = SRLLabel(input_sentences)
    filtered_results = SRL.filter_sentences()
    print(filtered_results)

    # Print or use the filtered results as needed
    for original, filtered in zip(input_sentences, filtered_results):
        print("Original Sentence:", original)
        print("Filtered Sentence:", filtered)
        print("\n")
