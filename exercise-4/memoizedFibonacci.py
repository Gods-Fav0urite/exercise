def memoize(func):
    cache = {}  

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def count_ways(n):
    if n <= 1:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)

if __name__ == "__main__":
    import time

    print("--- Testing Fibonacci (n=35) ---")
    start_fib = time.perf_counter()
    fib_res = fib(35)
    end_fib = time.perf_counter()
    
    print(f"fib(35) Result: {fib_res}")
    print(f"Execution Time: {(end_fib - start_fib) * 1000:.4f} ms (almost instant!)")

    print("\n--- Testing Stair Climbing Generalization (n=35) ---")
    start_stairs = time.perf_counter()
    stairs_res = count_ways(35)
    end_stairs = time.perf_counter()
    
    print(f"count_ways(35) Result: {stairs_res}")
    print(f"Execution Time:     {(end_stairs - start_stairs) * 1000:.4f} ms")
