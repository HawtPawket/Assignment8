# Task 1: Start
# Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.
# Ensure that your program only accepts numerical input and provides a friendly error message if 
# the user enters something that can't be converted to a number.

# Task 2: Temperature Conversion
# Write a function that converts the Fahrenheit temperature to Celsius.
# Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

# Task 3: User Experience
# Implement an else block that prints the converted temperature in a user-friendly format.
# Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed 
# regardless of whether an exception was caught or not.

def fahreneitToCelsius():
    try:
        fahreneit = float(input("Please enter the temperature in F° that you would like to be converted to C°:  "))
        celsius = (fahreneit - 32) * 5/9
    except ValueError:
        print("Please enter only numbers.")
    else:
        print(f"The converted temperature is {celsius}°")
    finally:
        print("Thank you for using the weather forecast application!")
fahreneitToCelsius()