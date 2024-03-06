#Calculate BMI
weight = input("Enter your weight in KG : ")
height = input("Enter your height in Metres : ")

weight_in_float = float(weight)
height_in_float = float(height)

bmi = weight_in_float/height_in_float**2
bmi_in_int = int(bmi)
print("Your BMI is : " + str(bmi_in_int))
