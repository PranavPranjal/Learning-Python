#Calculate BMI
weight = input("Enter your weight in KG : ")
height = input("Enter your height in Metres : ")

weight_in_float = float(weight)
height_in_float = float(height)

bmi = weight_in_float/height_in_float**2
bmi_int = int(bmi)
print(f"Your BMI is : {bmi_int}" )
