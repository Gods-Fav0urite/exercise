word1 = "Triangle"
word2 = "integral"

# 1. Convert both words to lowercase
w1 = word1.lower()
w2 = word2.lower()

# 2. Anagrams must have the exact same length
if len(w1) != len(w2):
    is_anagram = False
else:
    # 3. Build frequency map for word 1 manually
    counts1 = {}
    for char in w1:
        if char in counts1:
            counts1[char] += 1
        else:
            counts1[char] = 1
            
    # 4. Build frequency map for word 2 manually
    counts2 = {}
    for char in w2:
        if char in counts2:
            counts2[char] += 1
        else:
            counts2[char] = 1
            
    # 5. Compare the two frequency maps manually
    is_anagram = True
    for char in counts1:
        if char not in counts2 or counts1[char] != counts2[char]:
            is_anagram = False
            break

# Print the final result
if is_anagram:
    print("Output: Anagram")
else:
    print("Output: Not an anagram")
