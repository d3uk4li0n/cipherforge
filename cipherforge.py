import sys 
from itertools import permutations
from colorama import Fore

def capitalize(word):
    return word.capitalize()

def upper(word):
    return word.upper()

def permute_all(word):
    return ["".join(w) for w in permutations(word)]

def rev_word(word):
    return word[::-1]
    
## add digits from 1 to 1000000
def add_digits(word):
    ret_list = []
    for i in range(1, 10000001):
        ret_list.append(word + str(i))
    return ret_list
    
if __name__ == "__main__":
    file = input(f"{Fore.BLUE}[?] (Optional) output (default: cf_wordlist.txt): ")
    source = input(f"{Fore.BLUE}[?] Insert word list (separated by comma): ").split(", ")
    for s in source:
      print(capitalize(s))
      print(upper(s))
      print(permute_all(s))
      print(rev_word(s)) 
      print(add_digits(s))
