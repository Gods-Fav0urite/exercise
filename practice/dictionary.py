arr = [
        {"you": "us"}, 
       [1, 2, 3], 
       3, 
       4, 
       5, 6, 6, 6
    ]

print(arr)

dictionary = {
    'apple': 3,
    'mangos': 5,
    "orange": 6
}

#list
#pop, append, extend, remove

popped = arr.pop()
print(popped)
print(arr)
arr.append([8, 9, 10])
print(arr)

arr.extend([8, 9, 10])
print(arr)

arr.remove([1, 2, 3])
print(arr)

print(arr.count(6))