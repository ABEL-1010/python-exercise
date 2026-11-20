def maximum(val1, val2, val3):
    max_val = val1
    if val2 > max_val:
        max_val = val2
    if val3 > max_val:
        max_val = val3
    return max_val
print(maximum( 123, 124, 125))
print(maximum("blue", "red", "green"))


def max_of_infinity(*args):
    if not args:
        return None
    
    max_val = args[0]

    for val in args:
        if val > max_val:
            max_val = val

        
    return max_val

print(max_of_infinity(1,2,3,4,5,6,7,8,9,0,11,22,33,53))
print(max_of_infinity())