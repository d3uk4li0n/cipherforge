import sys 
from colorama import Fore

def capitalize(word):
    return word.capitalize()

def upper(word):
    return word.upper()

def rev_word(word):
    return word[::-1]

def leet(word):
    mapping = {
        "a": ["4", "@"],
        "e": ["3"],
        "i": ["1"],
        "o": ["0"],
        "s": ["5", "$"]
    }

    yield word
    for i, char in enumerate(word):
        if char.lower() in mapping:
            for repl in mapping[char.lower()]:
                yield word[:i] + repl + word[i+1:]

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

def write_to_file(generator, file):
    with open(file, "w") as f:
        for item in generator:
            f.write(item + "\n")

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

gen = generate_wordlist(source)
write_to_file(gen, file)

def main():
    parser = argparse.ArgumentParser(description="Custom Wordlist Generator (Cybersecurity Tool)")

    parser.add_argument("--words", required=True,
                        help="Comma-separated words (eg john,doe,company)")
    parser.add_argument("--min", type=int, default=0,
                        help="Minimum length")
    parser.add_argument("--max", type=int, default=999,
                        help="Maximum length")
    parser.add_argument("--output", default="wordlist.txt",
                        help="Output file")

    args = parser.parse_args()

    words = args.words.split(",")

    gen = generate_wordlist(words, args.min, args.max)
    write_to_file(gen, args.output)

    print(f"[+] Wordlist saved to {args.output}")

if __name__ == "__main__":
    main()
