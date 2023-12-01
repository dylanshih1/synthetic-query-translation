#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:13:53 2023

@author: dylanshih
"""
import argparse
import wordfreq

class PruneTopN:
    def __init__(self, sentences, n = 15):
        self.sentences = sentences
        self.n = n
        self.word_list = set(wordfreq.top_n_list('en', self.n))
        
    
    def delete_top_words_from_sentence(self, sentence):
        # Tokenize the sentence into words
        words = sentence.split()
    
        # Remove the top common words from the original sentence
        filtered_sentence = ' '.join(word for word in words if word.lower() not in self.word_list)
    
        return filtered_sentence
    
    def delete_top_words_from_sentences(self):
        return [self.delete_top_words_from_sentence(sentence) for sentence in self.sentences]
    
if __name__ == "__main__":
    input_sentences = [
    "What are the latest advancements in artificial intelligence?",
    "How do I create a website from scratch?",
    "What are the symptoms of the flu?"

    ]
    
    Prune = PruneTopN(input_sentences, 15)
    new_sentences = Prune.delete_top_words_from_sentences()
    print(new_sentences)

