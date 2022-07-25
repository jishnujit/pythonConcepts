# Write a program to compute the frequency of the words from the input. The output should output after
# sorting the key alphanumerically.
from itertools import count

sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
sentence_list = sorted(sentence.split(" "))
word_count_dict = {word: sentence_list.count(word) for word in sentence_list}
print(word_count_dict)
print(sorted.__doc__)