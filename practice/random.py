# GUESS WORD

# 1. IMPORT RANDOM
import random
import word

# 2. CREATE A LIST OF WORDS
list_of_words = word.guess     #calling the guess from word.py file

# 3. RANDOMLY SELECT A WORD FROM THE LIST
word = random.choice(list_of_words)

# 4. INITIALIZE ATTEMPT TO BE 5
attempt = 5

# 5. CREATE A LIST (result) CONTAINING UNDERSCORES DEPENDENT ON:
result = ["_"] * len(word)
print(result)

# 6. A WHILE LOOP THAT RUNS WHILE ATTEMPT IS GREATER THAN 5
while attempt > 0 and ("_" in result):

# 7. GUESS = INPUT A LETTER
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                result[i] = guess
        print("Correct guess!")
    else:
        attempt -= 1
        print("Incorrect guess. Attempts left:", attempt)
        