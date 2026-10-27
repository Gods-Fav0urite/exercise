def roman_to_int(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    i = 0
    n = len(s)
    
    while i < n:
        if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
            total += roman_map[s[i + 1]] - roman_map[s[i]]
            i += 2  
        else:
            total += roman_map[s[i]]
            i += 1  
            
    return total

print(roman_to_int("III"))      
print(roman_to_int("LVIII"))    
print(roman_to_int("MCMXCIV"))  
