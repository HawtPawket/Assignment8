# Task 1: Start
# Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.
# Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.


try:
    originalServings = int(input("How many servings is the recipe was designed for: "))
    if originalServings > 0:
        print(f"Your recipe is made for {originalServings} servings.")
    else:
        print("Number must be positive. ")

except ValueError:
    print("Value must be a number")

# Task 2: Quantity Calculation
# Calculate the adjustment factor by dividing the desired servings by the original servings.
# Use a 'try' block to catch any arithmetic errors that may occur during the calculation.

try:
    desiredServings = int(input("How many servings would you like to make? "))
    if desiredServings > 0:
        print(f"You would like to make {desiredServings} servings. ")
    else:
        print("Servings must be a positive number. ")
    adjustment = desiredServings / originalServings
    
    print(f"The adjustment factor is {adjustment}.")
except ValueError:
    print("Value must be a number. ")



# Task 3: Serving Success
# If the calculation is successful, display the adjusted recipe quantities to the user.
# Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.

finally:
    print("Thank you for using The Recipe Ratio Adjuster! Enjoy your cooking!")