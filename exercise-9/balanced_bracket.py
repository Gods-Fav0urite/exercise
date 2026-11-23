# THE GOAL OF THIs QUESTION IS TO CHHECK IF THE BRACKETS IN THE STRINGS ARE PROPERLY BALANCED & NESTED.
# EVERY OPENED BRACKET ((,[,{) MUST HHAVE A CORRESPONDING CLOSED BRACKET (),],}). 

def is_balanced(text: str) -> bool:
    stack_dict = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    stack = []

    for char in text:
        if char in stack_dict.values():
            stack.append(char)
        elif char in stack_dict:
            if not stack or stack.pop() != stack_dict[char]:
                return False

    return not stack  

def max_depth(text: str) -> int:
    current_depth = 0
    max_depth = 0

    for char in text:
        if char in "({[":
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char in ")}]":
            current_depth -= 1

    return max_depth

if __name__ == "__main__":
    print(is_balanced("(a + b) * [c - d]") ) 
    print(is_balanced("{[()]}") )       
    print(is_balanced("([)]") )              
    print(is_balanced("((") )                
    print(is_balanced("}{") )                
    print(is_balanced("") )