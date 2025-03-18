"""
Title: Simple Calculator (Skeleton Code)

Overview:
    This program will:
        1. Ask the user to choose an operation (add, subtract, multiply, divide).
        2. Ask the user for two numbers.
        3. Perform the chosen operation on those numbers.
        4. Print out the result.

Instructions:

PART 1: USER INPUT & IF/ELSE
    1) Prompt the user to choose an operation. 
       For simplicity, you could allow: "add", "subtract", "multiply", "divide".
       (Alternatively, you could let them type symbols like '+', '-', '*', '/'.)
    2) Prompt for two numbers (convert them to float or int).
    3) Use if/elif/else statements to decide which arithmetic operation to perform.
        - If the user typed "add" -> result = num1 + num2
        - If "subtract" -> result = num1 - num2
        - If "multiply" -> result = num1 * num2
        - If "divide" -> result = num1 / num2 (handle division by zero if you like)
    4) Print the result.

PART 2: DEFINE FUNCTIONS
    1) Convert your "input" logic into a function called get_operation_and_numbers().
       - This function should:
         a) Ask the user for an operation.
         b) Ask for two numbers.
         c) Return (operation, num1, num2).
    2) Convert your "perform operation" logic into a function called perform_calculation(operation, num1, num2).
       - This function should:
         a) Use if/elif/else to decide how to calculate the result.
         b) Return the result.
    3) Create a function display_result(result) that prints the result in a clear way.
    4) Write a main() function to tie it all together:
         - operation, num1, num2 = get_operation_and_numbers()
         - result = perform_calculation(operation, num1, num2)
         - display_result(result)
    5) Finally, add:

        if __name__ == "__main__":
            main()

    so the program runs when you execute the script.

HINTS:
    - Use input() to get user input, then convert to float() or int() as needed.
    - If you allow division, consider how you handle num2 == 0.
    - Use clear print statements to confirm what's happening (e.g., "You chose to add 2 and 3").
"""

# PART 1: USER INPUT & IF/ELSE

# TODO: Step 1: Prompt user for operation (e.g., operation = input("Choose an operation (add, subtract, multiply, divide): "))
# operation = ...

# TODO: Step 2: Prompt for two numbers (convert them to floats or ints).
# num1 = ...
# num2 = ...

# TODO: Step 3: Use if/elif/else to decide which operation to perform.
# result = None  # Initialize a variable to store the result
#
# if operation == "add":
#     result = ...
# elif operation == "subtract":
#     ...
# elif operation == "multiply":
#     ...
# elif operation == "divide":
#     # OPTIONAL: handle division by zero
#     ...
# else:
#     print("Invalid operation selected!")

# TODO: Step 4: Print the result (if it is valid and not None).
# print("Result:", ...)


# PART 2: DEFINE FUNCTIONS

# TODO: 1) Create a function get_operation_and_numbers():
#        - Prompt for operation, prompt for two numbers, return all three.
# def get_operation_and_numbers():
#     pass

# TODO: 2) Create a function perform_calculation(operation, num1, num2):
#        - Perform the chosen operation using if/elif/else, return the result.
# def perform_calculation(operation, num1, num2):
#     pass

# TODO: 3) Create a function display_result(result):
#        - Print the result in a clear way.
# def display_result(result):
#     pass

# TODO: 4) Write a main() function that ties everything together:
#           operation, num1, num2 = get_operation_and_numbers()
#           result = perform_calculation(operation, num1, num2)
#           display_result(result)
# def main():
#     pass

# TODO: 5) Add the if __name__ == "__main__": block here
# if __name__ == "__main__":
#     main()
