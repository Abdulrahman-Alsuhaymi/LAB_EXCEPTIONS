def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + b)#b is not defined(name error)
        print("The operation is successful")
    except NameError:
        print("variable is not defined.")


additoin(10, 20)