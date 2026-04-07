import argparse

def capitalize(word):
    return word.capitalize()

def upper(word):
    return word.upper()

def rev_word(word):
    return word[::-1]


def patterns(word):
    return [
        f"{word}123",
        f"{word}2024",
        f"{word}!",
        f"{word}@123",
        f"{word.capitalize()}123"
    ]


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


def add_digits(word, max_num=100):
    for i in range(max_num):
        yield f"{word}{i}"

def generate_wordlist(words, min_len=0, max_len=999):
    seen = set()

    for word in words:
        # base transformations
        candidates = [
            word,
            capitalize(word),
            upper(word),
            rev_word(word)
        ]

        # patterns
        candidates.extend(patterns(word))

        # leetspeak
        candidates.extend(leet(word))

        # combinations
        for other in words:
            if other != word:
                candidates.append(f"{word}{other}")
                candidates.append(f"{word}_{other}")

        # digits (controlled)
        candidates.extend(add_digits(word))

        # filtering + deduplication
        for candidate in candidates:
            if candidate not in seen and min_len <= len(candidate) <= max_len:
                seen.add(candidate)
                yield candidate

def write_to_file(generator, file):
    with open(file, "w") as f:
        for item in generator:
            f.write(item + "\n")

def main():
    parser = argparse.ArgumentParser(
        description="Custom Wordlist Generator (Dictionary Attack Tool)"
    )

    parser.add_argument(
        "--words",
        required=True,
        help="Comma-separated words (e.g. john,doe,company)"
    )

    parser.add_argument(
        "--min",
        type=int,
        default=0,
        help="Minimum password length"
    )

    parser.add_argument(
        "--max",
        type=int,
        default=999,
        help="Maximum password length"
    )

    parser.add_argument(
        "--output",
        default="wordlist.txt",
        help="Output file"
    )

    args = parser.parse_args()

    words = [w.strip() for w in args.words.split(",") if w.strip()]

    gen = generate_wordlist(words, args.min, args.max)
    write_to_file(gen, args.output)

    print(f"[+] Wordlist saved to {args.output}")

if __name__ == "__main__":
    main()
