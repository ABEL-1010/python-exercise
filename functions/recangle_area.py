def average(*args):
    return sum(args) / len(args)

print(average(1,2,3,4,5,6,7,5,4,2))

x = 5
print(id(x))

def global_modify():
    global x;
    x = "abel"
    print(f'x is {x}')
    print(id(x))

global_modify()
