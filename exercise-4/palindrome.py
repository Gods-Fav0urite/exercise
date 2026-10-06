
def is_letter(ch: str) -> bool:
    """Returns True if the character is an alphanumeric letter, False otherwise."""
    code = ord(ch)
    return (
        (65 <= code <= 90) or  
        (97 <= code <= 122) or  
        (48 <= code <= 57)      
    )

def is_palindrome(text: str) -> bool:
    """Determines if a sentence is a palindrome using two pointers moving inward."""
    left = 0
    right = len(text) - 1

    while left < right:
        if not is_letter(text[left]):
            left += 1
            continue
        if not is_letter(text[right]):
            right -= 1
            continue

        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True

input_1 = "Was it a car or a cat I saw?"
input_2 = "Hello, World!"

print(f"Input: {input_1} → Output:", "Palindrome" if is_palindrome(input_1) else "Not a palindrome")
print(f"Input: {input_2} → Output:", "Palindrome" if is_palindrome(input_2) else "Not a palindrome")
