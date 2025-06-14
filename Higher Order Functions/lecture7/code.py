# Reduce as higher order function:
import functools
# nums = [5,8,9,10,11,12,13]

# def logic(a,b):
#     return a + b 

# reduce_obj = functools.reduce(logic,nums)
# print(reduce_obj)

# nums = [5,8,9,10,11,12,13]

# reduce_obj = functools.reduce(lambda x , y : x + y,nums)
# print(reduce_obj)

# reduce_obj = functools.reduce(lambda x,y: x+y ,[5,8,9,10,11,12,13] )
# print(reduce_obj)

nums = [5,8,9,10,11,12,13]

def max1(a,b):
    if a > b:
        return a
    else:
        return b
    
reduce_obj = functools.reduce(max1,nums)
print(reduce_obj)