# 1. Get user configuration inputs
mode = input("Do you want to (encrypt) or (decrypt)? ").strip().lower()
text = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

# If decrypting, we reverse the shift direction
if mode == "decrypt":
    shift = -shift

result = []

# 2. Process each character in the message
for char in text:
    if char.isalpha():
        # Check if the character is uppercase or lowercase to set the proper ASCII base
        ascii_base = ord('A') if char.isupper() else ord('a')
        
        # Calculate zero-indexed position (0-25), apply the shift with wrap-around, and convert back
        original_pos = ord(char) - ascii_base
        new_pos = (original_pos + shift) % 26
        new_char = chr(ascii_base + new_pos)
        
        result.append(new_char)
    else:
        # Preserve non-alphabetical characters exactly as they are
        result.append(char)

# 3. Combine into the final string and print
output_text = "".join(result)
print(f"Output: {output_text}")
