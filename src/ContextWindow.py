#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:21:45 2023

@author: dylanshih
"""
import numpy as np
import wordfreq

class ContextWindow:

    def __init__(self, sentences: list[str]):
        self.sentences = sentences
    
    
    def generate_zipf_probs(self, words):
        """
        Generate Zipf distribution probabilities for a list of words using wordfreq.
    
        Parameters:
        - words (list): List of words.
    
        Returns:
        - zipf_probs (list): Zipf distribution probabilities for each word.
        """
        zipf_probs = [wordfreq.zipf_frequency(word, 'en') for word in words]
        return zipf_probs / np.sum(zipf_probs)
    
    def find_rarest_word(self, words, zipf_probs):
        """
        Find the rarest word based on Zipf distribution probabilities.
    
        Parameters:
        - words (list): List of words.
        - zipf_probs (list): Zipf distribution probabilities for each word.
    
        Returns:
        - rarest_word (str): The rarest word.
        """
        rarest_index = np.argmin(zipf_probs)
        rarest_word = words[rarest_index]
        return rarest_word
    
    def create_context_window(self, sentence, target_word, window_size=2):
        """
        Create a context window around the target word in a given sentence.
    
        Parameters:
        - sentence (str): The input sentence.
        - target_word (str): The target word for which the context window is created.
        - window_size (int): The size of the context window.
    
        Returns:
        - context_window (list): A list containing words in the context window.
        """
        words = sentence.split()
        target_index = words.index(target_word)
        start_index = max(0, target_index - window_size)
        end_index = min(len(words), target_index + window_size + 1)
        context_window = words[start_index:end_index]
        return context_window
    
    def generate_sentence(self):
        filtered_sentences = []
        for sentence in self.sentences:
            words = sentence.split()
            zipf_probs = self.generate_zipf_probs(words)
            rarest_word = self.find_rarest_word(words, zipf_probs)
            context_window = self.create_context_window(sentence, rarest_word)
            filtered_sentences.append(" ".join(context_window))
        
        return filtered_sentences
    
if __name__ == "__main__":
    input_sentences = ["The quick brown fox jumps over the lazy dog.",
                 "A journey of a thousand miles begins with a single step.",
                 "To be or not to be, that is the question."]
    CW = ContextWindow(input_sentences)
    filtered_results = CW.generate_sentence()
    print(filtered_results)
    
# User inputs a list of sentences


