# Filter() function as higher order functions:


# numbers = [20,3,40,5,60,70,9,80]
# filtered = filter(lambda x : x%2==0,sorted(numbers))
# print(list(filtered))

# print(list(filter(lambda num: num%2!=0,[20,30,23,43,23,65,75,43,12,])))

string = "ihtishameo"
vowels = ['a','e','o','i','u']
# def vowel(ch):
#     if ch in string:
#         return True

# filtered = list(filter(vowel,vowels))
# print(filtered)
# print(filtered)

# filtered = list(filter(lambda ch : ch in sorted("ihtishamuieo"),['a','e','o','i','u']))
# print(filtered)

# names = ["waqas","ihtisham","roman","shahab","shantanu"]

# def finding_length(name):
#     return f"{name} : {len(name)}"

# mapping = list(map(finding_length,names))
# print(mapping)
# through short hands if-else :

# nums = [5,3,8,11,6]
# map_obj = map(lambda x: x**2 if x%2!=0 else x**3,nums)
# print(map_obj)


