def make_shifter(shift: int):
    """Higher-order function that creates and returns a pure character-shifting function."""
    def shift_char(char: str) -> str:
        if not char.isalpha():
            return char
            
        ascii_base = ord('A') if char.isupper() else ord('a')
        
        return chr(ascii_base + (ord(char) - ascii_base + shift) % 26)
        
    return shift_char

mode = input("Do you want to (encrypt) or (decrypt)? ").strip().lower()
text = input("Enter your message: ")
shift_amount = int(input("Enter the shift number: "))

if mode == "decrypt":
    shift_amount = -shift_amount

shifter = make_shifter(shift_amount)
output_text = "".join(map(shifter, text))

print(f"Output: {output_text}")
