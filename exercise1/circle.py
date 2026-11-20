"""Calculate and display a circle's diameter, circumference, and area."""

radius = int(input("Enter the radius of the circle: "))
PIE = 3.14159

diameter = 2 * radius
circumference = 2 * PIE * radius
area = PIE * radius ** 2

print(f"diameter = {diameter}\ncircumference = {circumference}\narea = {area}")
