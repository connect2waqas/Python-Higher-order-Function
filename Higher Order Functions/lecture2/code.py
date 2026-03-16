# Small Project: Designing a calculator:

operation ={
    "-" : lambda a , b : a - b,
    "+" : lambda a , b : a + b,
    "*" : lambda a , b : a * b,
    "/" : lambda a , b : a / b
}

num1 = float(input("enter a number: "))
operator = input('enter a operator: ')
num2 = float(input("enter another number: "))

print(f"Result: {operation[operator](num1,num2)}")

import pandas as pd
people = [
    { "name": "Alice", "age": 15},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 50}
]
adults = list(filter(lambda x : x["age"] >=18, people))
df = pd.DataFrame(adults)
output_data = df.to_csv("output.csv")
print(output_data)
# Temperature Converter:

c_to_f = lambda c : (c * 9 / 5) + 32
print(c_to_f(34))

def greeting():
    import datetime
    current_hour = datetime.datetime.now().hour
    greeting_rule = {
        "morning": lambda: "Good Morning!",
        "afternoon" : lambda: "Good afternoon!",
        "evening"  : lambda: "Good evening!"
    }
    if 5 <= current_hour < 12:
        greet = greeting_rule["morning"]
    elif 12 <= current_hour < 17:
        greet =  greeting_rule["afternoon"]
    else:
        greet = greeting_rule["evening"]
    return greet
greet_1 = greeting()
print(greet_1)
