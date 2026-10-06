# def count_words(words: list) -> dict[str, int]:
#     word_count = {}
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count

# def most_frequent(freq: dict[str, int]) -> str:
#     if not freq:
#         return None
#     max_word = max(freq, key=freq.get)
#     return max_word

# print(count_words(['Python', 'is', 'fun', ',', 'and', 'Python', 'is', 'powerful!']))
# print(most_frequent(count_words(['Python', 'is', 'fun', ',', 'and', 'Python', 'is', 'powerful!'])))

# Helper functions with zero side effects
def count_words(words: list[str]) -> dict[str, int]:
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def most_frequent(freq: dict[str, int]) -> str:
    best_word, max_count = "", -1
    for w, count in freq.items():
        if count > max_count:
            best_word, max_count = w, count
    return best_word

# Main Pipeline
text = "Python is fun, and Python is powerful!"

# Manual clean & split
cleaned = "".join([c for c in text.lower() if c not in ",.!?;:()\"'-"])
words = cleaned.split()

counts = count_words(words)
winner = most_frequent(counts)

print(f"Most frequent word: {winner} ({counts[winner]})")
