def fizzbuzz_plus(n):
    rules = [(3, "Fizz"), (5, "Buzz"), (7, "Bazz")]
    result = []
    for i in range(1, n + 1):
        word = ""
        for divisor, text in rules:
            if i % divisor == 0:
                word += text
        result.append(word or str(i))
    return result

print(fizzbuzz_plus(15))




