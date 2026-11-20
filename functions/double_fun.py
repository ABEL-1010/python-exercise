def double_print(x):
    print(x * 2)

def double_return(x):
    return x * 2

a = double_print(5)
b = double_return(5)
print(a, b)
print(double_return(double_return(3)))