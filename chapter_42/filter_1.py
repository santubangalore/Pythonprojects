
def is_even(n):
    if n%2==0:
        return True
    else:
        return False

nums=[3,2,6,7,8,9,11,13]


evens = list(filter(is_even,nums))

print(evens)
        
