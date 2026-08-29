#Program to Find the Square Root

n = int(input("Enter a number: "))
sqrt = n ** 0.5
print("The square root of", n, "is", sqrt)

# Calculate the Area and Perimeter of Triangle and Circle

    #Triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
perimeter_triangle = base + height + (base**2 + height**2)**0.5
print("Area of the triangle is:", area_triangle)
print("Perimeter of the triangle is:", perimeter_triangle)

    #Circle
radius = float(input("Enter the radius of the circle: "))
area_circle = 3.14159 * radius ** 2
circumference_circle = 2 * 3.14159 * radius
print("Area of the circle is:", area_circle)
print("Circumference of the circle is:", circumference_circle) 

#Solve a Quadratic Equation

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))           
if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:   
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        print("The roots are real and different.")
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("The roots are real and the same.")
        print("Root:", root)
    else:
        real_part = -b / (2 * a)
        imaginary_part = (abs(discriminant) ** 0.5) / (2 * a)
        print("The roots are complex and different.")
        print("Root 1:", complex(real_part, imaginary_part))
        print("Root 2:", complex(real_part, -imaginary_part))   

#Swap Two Variables
a = input("Enter the first variable: ")
b = input("Enter the second variable: ")
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)

#Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")

#Convert kilometers to miles
kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometers is equal to {miles} miles.")