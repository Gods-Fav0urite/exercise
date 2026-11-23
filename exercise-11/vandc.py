def count_letters(text):
    vowels = consonants = 0

    for ch in text.lower():
        if "a" <= ch <= "z":
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return (vowels, consonants)

print(count_letters("Hello, World 123"))