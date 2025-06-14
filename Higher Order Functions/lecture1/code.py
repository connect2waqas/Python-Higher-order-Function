# Lambda functions:

# adding through lambda function:

addition = lambda a,b: (a+" "+b)
print(f"The addition is: {addition("hello","word!")}")


squaring = lambda x : x**2
print(f"The of number is : {squaring(4)}")

is_even_odd = lambda x : "even" if x % 2==0 else "odd"
print(is_even_odd(5))

even = lambda x : x % 2==0
print(even(4))

uppercase = lambda s: s.upper()
print(uppercase(input("enter a string: ")))

reversing = lambda s : s[::-1]

print(reversing("Hello"))

