def fizzbuzz_plus(n):
    rules = [(3, "Fizz"), (5, "Buzz"), (7, "Bazz")]
    result = []
    for i in range(1, n + 1):
        word = []
        for divisor, text in rules:
            if i % divisor == 0:
                word.append(text)
        result.append(''.join(word) or str(i))
    return result

print(fizzbuzz_plus(0))




