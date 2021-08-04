

def sum (a, *b):
    c=a
    #fetch all values from tuple b

    for i in b:
        c= c+i

    print(c)
    

sum (5,4,34,76)
