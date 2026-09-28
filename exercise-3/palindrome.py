def is_palindrome(text):
    left = 0
    right = len(text) - 1
    
    while left < right:
        
        while left < right and not text[left].isalnum():
            left += 1
            
        while left < right and not text[right].isalnum():
            right -= 1
            
        if text[left].lower() != text[right].lower():
            return "Not a palindrome"
            
        left += 1
        right -= 1
        
    return "Palindrome"

print(is_palindrome("Was it a car or a cat I saw?"))  
print(is_palindrome("Hello, World!"))                
