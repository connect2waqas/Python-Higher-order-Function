# here we have to study  the lambda and map() combinally..

# numbers = [1,2,3,4,5,6,7]
# squared = list(map(lambda x : x ** 2 ,numbers))
# print(squared)

# def squaring(x):
#     return x**2

# squared = list(map(squaring,numbers))
# print(squared)


# Converting String to uppercase:

words = ["hello","welcome","data science","artificial intelligence"]

# uppercase = list(map(lambda s : s.upper(),words))

# print(uppercase)

# resversing = list(map(lambda s : s[::-1],words))

# print(resversing)

# lengths = [5,10,15]
# widths = [3,6,9]

# areas = list(map(lambda l,w : w*l,lengths,widths))
# print(areas)

# numeric_strings = ["10", "20", "30"]  
# numbers = list(map(lambda s: int(s), numeric_strings))  
# print(numbers)  # Output: [10, 20, 30]  

# numeric_strings = ["10","20","30"]
# numbers = list(map(lambda s: eval(s),numeric_strings))
# print(numbers)

# Project 2: String Prefixer:

# words = ["user","system","AI"]

# prefix = tuple(list(map(lambda s : "say_"+ s, words)))

# print(prefix)

# Lists of unequal lengths will stop at the shortest  
# sums = list(map(lambda x, y: x + y, [1, 2],[4,7]))  


# Nesting lambda functions:

# One Method:

# def outer():
#    return lambda x,y: x+y
# add = outer()
# print(add(4,5))

# Another Method:

outer = lambda:lambda x,y: x + y
add = outer()
print(add(4,5)) # this is nested lambda function.

