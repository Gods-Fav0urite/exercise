text = "Python is fun, and Python is powerful!"

# 1. Normalize to lowercase
lowercase_text = text.lower()

# 2. Manually strip punctuation without re or string.punctuation
cleaned_text = ""
punctuation_to_remove = ",.!?;:()\"'-"

for char in lowercase_text:
    if char not in punctuation_to_remove:
        cleaned_text += char

# Split the cleaned text into a list of words
words = cleaned_text.split()

# 3. Count frequencies manually into a dictionary
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# 4. Find the most frequent word without using max() or sorting
most_frequent_word = None
highest_count = -1

for word, count in word_counts.items():
    if count > highest_count:
        highest_count = count
        most_frequent_word = word

# Print the final result
print(f"Most frequent word: {most_frequent_word} ({highest_count})")
