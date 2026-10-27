def process_sentence(sentence):
    capitalized_chars = []
    is_new_word = True
    
    for char in sentence:
        if char == ' ':
            capitalized_chars.append(char)
            is_new_word = True
        else:
            if is_new_word:
                if 'a' <= char <= 'z':
                    char = chr(ord(char) - 32)
                is_new_word = False
            capitalized_chars.append(char)
            
    capitalized_str = "".join(capitalized_chars)
    no_spaces_chars = []
    for char in capitalized_str:
        if char != ' ':
            no_spaces_chars.append(char)
            
    no_spaces_str = "".join(no_spaces_chars)
    
    return capitalized_str, no_spaces_str
input_text = input("Enter a sentence to process: ")
cap_result, no_space_result = process_sentence(input_text)

# print(f"Input:       \"{input_text}\"")
print(f"Capitalized: \"{cap_result}\"")
print(f"No Spaces:   \"{no_space_result}\"")
