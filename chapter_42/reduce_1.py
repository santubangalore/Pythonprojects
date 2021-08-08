from functools import reduce

def add_all(a,b):
    return a+b


nums= [3,2,4,5,7,9.11,6,8]

evens=list(filter(lambda n:n%2==0,nums))

# map lambda function, adds 2 to each element of evens
doubles= list(map(lambda n:n*2,evens))


sum= reduce(add_all,doubles)

print(sum)
