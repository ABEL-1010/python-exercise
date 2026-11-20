x = int ( input (" Enter a number: ") )
# Calculate the sum here
total = 0
for i in range (1, x+1):
    for j in range (1, i+1):
        total += j


# Print the value of the sum
print ( total )