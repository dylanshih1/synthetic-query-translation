#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:34:59 2023

@author: dylanshih
"""
import random
import string

class NoiseInjection:
    def __init__(self, sentences):
        self.sentences = sentences
        
    def inject_noise(self, sentence, noise_prob):
        noisy_sentence = list(sentence)
    
        for i, char in enumerate(noisy_sentence):
            # Introduce noise with a certain probability
            if random.uniform(0, 1) < noise_prob:
                # Randomly choose the type of noise
                noise_type = random.choice(['misspelling', 'miscapitalization', 'grammar'])
    
                if noise_type == 'misspelling':
                    # Replace a character with a random one
                    noisy_sentence[i] = random.choice(string.ascii_letters + string.punctuation + string.digits)
                
                elif noise_type == 'miscapitalization':
                    # Toggle the capitalization of a letter
                    noisy_sentence[i] = char.upper() if char.islower() else char.lower()
    
                elif noise_type == 'grammar':
                    # Introduce common grammar mistakes
                    if char.isalpha():
                        noisy_sentence[i] = random.choice(['', 's', 'es'])
    
        return ''.join(noisy_sentence)
    
    def inject_noise_to_sentences(self, noise_prob_per_sentence=0.5, noise_prob=0.2):
        noisy_sentences = []
        for sentence in self.sentences:
            if random.uniform(0, 1) < noise_prob_per_sentence:
                noisy_sentences.append(self.inject_noise(sentence, noise_prob))
            else:
                noisy_sentences.append(sentence)
                
        return noisy_sentences
    
if __name__ == "__main__":
    input_sentences = [
        "This is a sample sentence.",
        "Python is a powerful programming language.",
        "Machine learning is changing the world."
    ]

    noise_prob_per_sentence = 0.3  # Probability of injecting noise into each sentence
    noise_prob = 0.1  # Probability of introducing noise within a sentence
    
    noise = NoiseInjection(input_sentences)
    noisy_sentences = noise.inject_noise_to_sentences(noise_prob_per_sentence, noise_prob)

    for original, noisy in zip(input_sentences, noisy_sentences):
        print("Original Sentence:", original)
        print("Noisy Sentence:", noisy)
        print("\n")

    

        