

def person(name, **data):

    print(name)
    print(data)

    for i,j in data.items():
        print(i,j)
        


person("santu",age=56,city="bangalore",mobile="9876540987")
