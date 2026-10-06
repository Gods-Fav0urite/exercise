def count_words(words: list) -> dict[str, int]:
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def most_frequent(freq: dict[str, int]) -> str:
    if not freq:
        return None
    max_word = max(freq, key=freq.get)
    return max_word

print(count_words(['Python', 'is', 'fun', ',', 'and', 'Python', 'is', 'powerful!']))
print(most_frequent(count_words(['Python', 'is', 'fun', ',', 'and', 'Python', 'is', 'powerful!'])))