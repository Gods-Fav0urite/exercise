def compose(f, g):
    """Returns a function that computes f(g(x))."""
    return lambda x: f(g(x))

def pipe(*funcs):
    """Returns a function that applies functions sequentially from left to right."""
    def wrapper(x):
        result = x
        for func in funcs:
            result = func(result)
        return result
    return wrapper

def strip_whitespace(s: str) -> str:
    return s.strip()


def lowercase(s: str) -> str:
    return s.lower()


def remove_vowels(s: str) -> str:
    vowels = "aeiou"
    return "".join(char for char in s if char not in vowels)
