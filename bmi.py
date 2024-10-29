def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    print("Calculated BMI = " + str(bmi))
    
    # Classify BMI
    if bmi < 18.5:
        classification = -1  # Underweight
    elif 18.5 <= bmi < 25:
        classification = 0   # Normal weight
    else:
        classification = 1   # Overweight
    
    # Print classification as -1, 0, or 1
    print("Classification = " + str(classification))
    
    # Return both BMI and classification
    return bmi, classification

# Get user input for height and weight
try:
    height = float(input("Please enter your height in meters: "))
    weight = float(input("Please enter your weight in kg: "))
    
    # Calculate and display BMI and classification
    bmi_value, classification = calculate_bmi(height, weight)
    print(f"Your BMI is: {bmi_value:.2f}")
    print("Classification (Underweight: -1, Normal weight: 0, Overweight: 1):", classification)

except ValueError:
    print("Error: Please enter valid numbers for height and weight.")