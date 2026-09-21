palindrome_word = input("Enter a word: ")
length = len(palindrome_word)
is_palindrome = True

for i in range(length // 2):
    if palindrome_word[i] != palindrome_word[length - 1 - i]:
        is_palindrome = False

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")   