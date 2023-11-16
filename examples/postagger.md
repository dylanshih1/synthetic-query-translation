## Delete or keep word types in a sentence using POS tagger 
See https://universaldependencies.org/u/pos/ for accepted word types. You may use both allowlist and denylist in one command, but order matters!

### Denylist (-dl / --denylist) 
#### Delete determiners and punctuation 
```console
foo@bar synthetic-query-translation % python3 src/main.py data/10verbose -dl DET PUNCT

What are latest advancements in artificial intelligence
How do I create website from scratch
What are symptoms of flu
Tell me best ways to improve my focus and productivity
What are top rated restaurants in my city
How does climate change impact biodiversity
What are benefits of mindfulness meditation
Can you recommend good book for learning Python programming
How do I fix leaking faucet
What are key ingredients for successful job interview
```

#### Delete determiners, punctuation, auxiliary, and coordinating conjunction
```console
foo@bar synthetic-query-translation % python3 src/main.py data/10verbose -dl DET PUNCT AUX CCONJ

What latest advancements in artificial intelligence
How I create website from scratch
What symptoms of flu
Tell me best ways to improve my focus productivity
What top rated restaurants in my city
How climate change impact biodiversity
What benefits of mindfulness meditation
you recommend good book for learning Python programming
How I fix leaking faucet
What key ingredients for successful job interview
```

### Allowlist (-al / --allowlist) 
#### Keep nouns and verbs 
```console
foo@bar synthetic-query-translation % python3 src/main.py data/10verbose -al VERB NOUN

advancements intelligence
create website scratch
symptoms flu
Tell ways improve focus productivity
rated restaurants city
climate change impact biodiversity
benefits mindfulness meditation
recommend book learning programming
fix leaking faucet
ingredients job interview
```

#### Keep nouns, verns, numeral, adjective, and particle
```console
foo@bar synthetic-query-translation % python3 src/main.py data/10verbose -al VERB NOUN NUM ADJ PART

latest advancements artificial intelligence
create website scratch
symptoms flu
Tell best ways to improve focus productivity
top rated restaurants city
climate change impact biodiversity
benefits mindfulness meditation
recommend good book learning programming
fix leaking faucet
key ingredients successful job interview
```