height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height1 = float(height)
weight1 = float(weight)
print("Your Body Mass Index (BMI) is: " + str(int(weight1 / (height1 * height1))))