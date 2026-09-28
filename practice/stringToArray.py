def string_to_array(s):
    # your code here
#    return s.split(" ")

# print(string_to_array("I love arrays they are my favorite"))

# without using .split
    words = []
    word_left = " "
    
    for char in s:
        if char == " ":
            words.append(word_left)
            word_left = ""
        else:
            word_left += char
    words.append(word_left)
    return words

print(string_to_array("I love arrays they are my favorite"))