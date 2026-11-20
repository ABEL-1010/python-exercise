"""first funtion"""


def about_local_var(x):
    y = 5
    x += y
    return x
x = 10
y = 20
print(f"x = {x}, y = {y} and function call: {about_local_var(x)}")
print(f'after function call x: {x} and y: {y}')
