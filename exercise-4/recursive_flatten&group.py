def flatten(nested):
    """Flattens a deeply nested list recursively without any loops."""
    if not nested:
        return []
    head, *tail = nested
    if isinstance(head, list):
        return flatten(head) + flatten(tail)
    return [head] + flatten(tail)

def group_by(items, key_fn):
    """Groups items using a key function. Pure function using an internal loop."""
    grouped = {}
    for item in items:
        key = key_fn(item)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(item)
    return grouped

def combined(nested_words):
    """Combines flatten and group_by to organize words by their first letter."""
    flat_words = flatten(nested_words)
    return group_by(flat_words, lambda w: w[0] if w else "")

if __name__ == "__main__":
    print("Flatten:", flatten([1, [2, [3, [4]], 5]]))  
    standalone_group = group_by(["apple", "avocado", "banana"], lambda w: w[0])
    print("Group By:", standalone_group)  
    nested_input = [["apple", "avocado"], ["banana"], [["cherry"]]]
    print("Combined:", combined(nested_input))  