

a =10

def something():
    global a
    a=15

    print("in the func",a)

something()

print("outside",a)
