# Practical 9 - Practice Question 2: BMI function

# Return both the numeric BMI and its threshold-based category.
def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive.")
    bmi = weight / height ** 2
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

bmi, category = calculate_bmi(72, 1.75)
print(f"BMI: {bmi:.2f}\nCategory: {category}")
