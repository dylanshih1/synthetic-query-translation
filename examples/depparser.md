## Keep syntactic heads or topic using a Dependency Parser 
Regardless of the order in which we pass args, depparser will always run first if specified. Dependency parser must run on a full sentence. We define syntactic heads as a parent of a group of words that depend on it. For example, `a quick brown fox` has the syntactic head `fox`. We define topic as the object or subject of a sentence. For example, `I eat apple` has the subject `I` and object `apple`. However, the topic will only be subject if object is none. 

### --synt_heads (-sh)
#### Keep syntactic heads only 
```console
foo@bar synthetic-query-translation % python3 src/main.py data/10verbose -sh

What advancements intelligence
create website scratch
What symptoms flu
Tell ways improve focus productivity
What rated restaurants city
change impact
What benefits meditation
recommend book Python programming
fix faucet
What ingredients interview
```

### --topic (-t)
#### Keep topic of the sentence (object or subject) 
```console
foo@bar synthetic-query-translation % python3 src/main.py data/10verbose -t

the latest advancements in artificial intelligence
a website from scratch
the symptoms of the flu ?
my focus and productivity
the top - rated restaurants in my city
biodiversity
the benefits of mindfulness meditation
a good book for learning Python programming
a leaking faucet
the key ingredients for a successful job interview
```

### Keep topic with remove determiners and punctuation 
```console
foo@bar synthetic-query-translation % python3 src/main.py data/10verbose -t -dl DET PUNCT

latest advancements in artificial intelligence
website from scratch
symptoms of flu
my focus and productivity
top rated restaurants in my city
biodiversity
benefits of mindfulness meditation
good book for learning Python programming
leaking faucet
key ingredients for successful job interview
```
