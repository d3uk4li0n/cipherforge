import sys 
from colorama import Fore

def capitalize(word):
    return word.capitalize()

def upper(word):
    return word.upper()

def rev_word(word):
    return word[::-1]
    
def add_digits(word):
    for i in range(1, 10000001):
        yield f"{word}{i}"

## replaces letters with look-alike numbers
def replace_letters_digits(word):
    ret_list = []
    lowercase_dict = {"i":1, "z":2, "e":3,"a": 4, "s":5, "b":8, "o":0}
    uppercase_dict = {"I":1, "Z":2, "E":3,"A": 4, "S":5, "B":8, "O":0}

    for i in word:
        for key_l in lowercase_dict:
            for key_u in uppercase_dict:
                if i == key_l:
                    word = word.replace(i, str(lowercase_dict[key_l]))
                    ret_list.append(word)
                if i == key_u:
                    word = word.replace(i, str(uppercase_dict[key_u]))
                    ret_list.append(word)
    return set(ret_list)

## makes 2 words combinations
def combine_multiple_words(*words, comb=4):
    ret_list = []
    for i in range(comb):
        curword = words[0]
        ret_list.append(words[0] + words[i+(i+1)])
        ret_list.append(words[i+1] + words[0])
        i += 1
    return set(ret_list)

def patterns(word):
    return [
        f"{word}123",
        f"{word}2024",
        f"{word}!",
        f"{word}@123",
        f"{word.capitalize()}123"
    ]

# write_to_file(patterns(s), file)
def write_to_file(generator, file):
    with open(file, "a") as f:
        for item in generator:
            f.write(item + "\n")

## TODO add generate_wordlist function

def generate_wordlist(words):
    for word in words:
        yield word
        yield word.capitalize()
        yield word.upper()

        yield from patterns(word)
        yield from replace_letters_digits(word)

        for other in words:
            if other != word:
                yield f"{word}{other}"
                yield f"{word}_{other}"

'''
if __name__ == "__main__":
    ## TODO add functions that tackle option for minimum and maximum length
    min_length = int(input(f"{Fore.BLUE}[?] (Optional) Minimum length: "))
    max_length = int(input(f"{Fore.BLUE}[?] (Optional) Maximum length: "))
    add_words = input(f"{Fore.BLUE}[?] (Optional) Do you want to combine words [Y/n]: ") ## makes 2 words combinations
    if add_words == "Y" or add_words == "y":
        add_how_many_words = input(f"{Fore.BLUE}[?] How many words do you want to combine [2]: ")
    file = input(f"{Fore.BLUE}[?] (Optional) output (default: cf_wordlist.txt): ")
    source = input(f"{Fore.BLUE}[?] Insert word list (separated by comma): ").split(", ")
    for s in source:
        write_to_file([s], file)
        write_to_file(patterns(s), file)
        write_to_file(add_digits(s), file)
'''
