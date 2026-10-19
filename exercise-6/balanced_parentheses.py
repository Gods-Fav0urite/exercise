def is_balanced(text_string):
    stack = []
    
    for char in text_string:
      
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return "Not balanced (mismatched type)"
            
            last = stack.pop()
            if (char == ")" and last != "(") or \
               (char == "]" and last != "[") or \
               (char == "}" and last != "{"):
                return "Not balanced (wrong order)"

    return "Balanced" if not stack else "Not balanced (unclosed)"

tests = ["(a + b) * [c - d]", "(a + b)]", "((a + b)", "[(a + b) * {c - d}]", "([)]"]
for t in tests:
    print(f"Input: \"{t}\" → {is_balanced(t)}")
