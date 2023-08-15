# Calculate BMI

weight =  float(input("Enter your weight in kg:"))
height_m =  float(input("Enter your height in m:"))
height_cm = float(input("Enter your height in cm:"))

# Define the BMI function
def BMI():
    if weight and height_m:
        BMI_kg_m = weight / (height_m ** 2)  # Corrected the formula and added parentheses
        return BMI_kg_m  # Return the calculated BMI
        
    elif weight and height_cm:
        BMI_kg_cm = (weight / (height_cm **2))*10000
        return BMI_kg_cm
    
# Define for weight class
def Scale():
    bmi = BMI()
    if bmi < 18.5:
        return ("You are under weight")
    elif 18.5 <= bmi < 24.9:
        return ("Congratulations ! You have a Healthy Weight")
    elif 25.0 <= bmi < 29.9:
        print ("You are overweight")
    else:
        return("You are obese, please loss your weight to improve your health")
        
print ("Your BMI is:",BMI())
print ("Your weight calss is",Scale())
    