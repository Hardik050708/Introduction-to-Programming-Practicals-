# Practical 2 - Practice Question 10: BMI category

# Calculate BMI using kilograms and height in metres squared.
weight, height = 72, 1.75
bmi = weight / height ** 2

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.2f}\nCategory: {category}")
