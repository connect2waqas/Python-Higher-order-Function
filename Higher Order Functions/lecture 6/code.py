# map() and filter() function:

# nums = [10,20,30,40,50,60,70]
# numeric = [1,2,3,4,5,6,7]
# bonus = [1,2,3,4,5,6,7]

# def logic(n):
#     return n + 1

# through lambda function:
# map_obj = list(map(lambda x ,y,z: (x + 1 + y)*z,nums,numeric,bonus))
# map_obj = list(map(logic,nums))
# print(map_obj)

# laptops = {"Hp":55000,"Lenove":60000,"Sony":65000,"Apple":80000}
# budget = int(input("enter your budget: "))
# def logic(ele):
#     if laptops[ele] <= budget:
#         return True
#     else:
#         return False

# filtered_obj = list(filter(logic,laptops))
# print(filtered_obj)