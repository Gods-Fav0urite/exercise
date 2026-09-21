def word_frequencies(sentence):
    word_counts = {}
    
    punctuation = "!.,;?\"()[]{}':"
    
    words = sentence.lower().split()
    
    for word in words:
        word = word.strip(punctuation)
        
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
                
    return word_counts


sample_text = "python is fun and python is powerful!"
results = word_frequencies(sample_text)

for word, count in results.items():
    print(f"{word}: {count}")
