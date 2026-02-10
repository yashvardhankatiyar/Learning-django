nums = [1,2 ,3]
a = list(map(lambda a : a*a, nums))
b = reduce(lambda a,b : a+ b, nums)
print(a)