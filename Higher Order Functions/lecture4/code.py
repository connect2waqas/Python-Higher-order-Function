# Here we have to study lambda functions with if-else statements:

# short hand if-else:
# num1 = 10
# num2 = 20
# print(num1 if num1 >= num2 else num2)

# printing maximum values through if-else short in lambda functions:

# mix1 = lambda x,y: x if x>=y else y
# print(mix1(4,5))
# iife in python:

# we cannot we used IIFE in normal python functions but we can do it with lambda functions:

# result = (lambda x,y: x+y)(4,9)
# print(result)

# greet = (lambda:print("Hello from IIFE"))()
# print(greet)

# with multiple line of code IIfE

# person = (
#     lambda:(
#         print("Hello How are you!"),
#         print("Yes I am Fine!")
#     )
# )()
# print(person)
# words = ["apple", "cat", "dog", "elephant"]
# filtered = filter(lambda x: len(x) > 3, words)
# capitalized = map(lambda x: x.upper(), filtered)
# print(list(capitalized))  # Output: ['APPLE', 'ELEPHANT']

# words = ["apple","cat","dog","elephant","cheery","laptop"]
# filtered = filter(lambda x : len(x)>3, words)
# upper = map(lambda s: s.upper(),filtered)
# print(list(upper))

# numbers = [1,2,3,4,90,4,3,5,6,7]
# filtered = filter(lambda x: x%2==0,numbers)
# square = map(lambda x: x**2,filtered)
# print(list(square))


# inputs = ["123", "45a", "678", "9b"]

# filtered = filter(lambda x:x.isdigit(),inputs)
# number = map(lambda s: eval(s),filtered)
# print(list(number))