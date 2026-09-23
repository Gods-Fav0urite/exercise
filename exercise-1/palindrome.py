# name = "level"
# reversed_name = ""
# for char in name:
#     reversed_name = char + reversed_name
# print(name == reversed_name)

word = "level" 
left = 0
right = len(word) - 1
palindrome = True

for left in range(len(word) // 2):
    if word[left] != word[right - left]:
        palindrome = False
        break

if palindrome:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
