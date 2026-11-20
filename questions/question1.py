
x = int ( input () )
# Calculate alpha ( x ) here
alpha = 0
factorial = 1
for i in range (1, x+1):
    factorial *= i 
    alpha += factorial

# Print the value of alpha ( x )
print ( alpha ) 