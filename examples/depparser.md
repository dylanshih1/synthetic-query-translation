## Keep syntactic heads in a sentence
Regardless of the order in which we pass args, depparser will always run first if specified. Dependency parser must run on a full sentence. We define syntactic heads as a parent of a group of words that depend on it. For example, `a quick brown fox` has the syntactic head `fox`. 

### --depparser (-dp)
#### Delete determiners and punctuation 
```console
foo@bar synthetic-query-translation % python3 src/main.py data/10verbose -dp

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
