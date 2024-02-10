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

## returns list with permuted words capitalized and uppercased
def caps_perms(permutes):
    ret_list = []
    for p in permutes:
        ret_list.append(upper(p))
        ret_list.append(capitalize(p))
    return ret_list 

def write_to_file(data, file="cf_wordlist.txt"):
    try:
        with open(file, "w+") as f:
            f.write(data)
    except Exception as e:
        print(f"{Fore.RED}Exception occurred, could not write to file {file}")
    file.close()
    print(f"{Fore.GREEN}[+] Wordlist ready at: {file}")

if __name__ == "__main__":
    file = input(f"{Fore.BLUE}[?] (Optional) output (default: cf_wordlist.txt): ")
    source = input(f"{Fore.BLUE}[?] Insert word list (separated by comma): ").split(", ")
    for s in source:
      print(capitalize(s))
      print(upper(s))
      print(permute_all(s))
      print(rev_word(s)) 
      print(add_digits(s))
      print(caps_perms(s))
