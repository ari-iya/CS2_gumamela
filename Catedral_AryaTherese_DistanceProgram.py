Python
import math

# Ask the user to enter the coordinates of the first point
point_x1 = (float(input("Enter the x1: ")))
point_x2 = (float(input("Enter the x2: ")))

# Ask the user to enter the coordinates of the second point
point_y1 = (float(input("Enter the y1: ")))
point_y2 = (float(input("Enter the y2: ")))

# Compute the distance using the distance formula
distance = math.sqrt(pow(point_x2-point_x1, 2))
point_a = pow(point_x2-point_x1, 2)
point_b = pow(point_y2-point_y1, 2)
result = point_a+point_b
distance = math.sqrt(result)

# Display the result rounded to two decimal places
print("The distance is", distance)
