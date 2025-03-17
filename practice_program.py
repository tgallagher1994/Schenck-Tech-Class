"""
Title: Number Analyzer (Skeleton Code)

Overview:
    1. Ask the user how many numbers they want to enter.
    2. Collect that many numbers (using a for loop).
    3. Determine how many of them are positive, negative, or zero (using if/else).
    4. (Later) Refactor the code into functions for clarity.

INSTRUCTIONS:

PART 1: LOOPS AND INPUT
    - Prompt the user: "How many numbers do you want to enter?"
    - Convert the response to an integer (e.g., count).
    - Create an empty list (e.g., numbers = []).
    - Use a for loop (e.g., for i in range(count)) to:
        > Prompt the user: "Enter a number:"
        > Convert the input to an integer
        > Append it to the list.

PART 2: IF/ELSE
    - Initialize three counters: positive_count, negative_count, zero_count = 0, 0, 0
    - Loop over the list of numbers:
        > If a number is greater than 0, increment positive_count
        > Else if it is less than 0, increment negative_count
        > Otherwise, increment zero_count (this covers zero)
    - Print out the results for each category.

PART 3: DEFINE FUNCTIONS
    - Move the "collect numbers" logic into a function called get_numbers().
    - Move the "analyze numbers" logic into a function called analyze_numbers().
    - Write a display_results() function that prints the counts in a readable way.
    - Write a main() function that calls those three functions in order.
    - At the bottom, call main() using the following code:

        if __name__ == "__main__":
            main()
"""

# ===== PART 1: LOOPS AND INPUT =====
# TODO: Prompt the user for how many numbers they want to enter.
#       Convert it to an integer and store it in a variable named 'count'.

# e.g. 
# count = ...

# TODO: Create an empty list to store the numbers.

# e.g. 
# numbers = ...

# TODO: Use a for loop to collect 'count' numbers from the user.
#       Convert each input to an integer and append to 'numbers'.

# e.g. 
# for i in range(count):
#     num = ...
#     numbers.append(...)

# ===== PART 2: IF/ELSE =====
# TODO: Initialize three counters: positive_count, negative_count, zero_count

# positive_count = 0
# negative_count = 0
# zero_count = 0

# TODO: Loop over 'numbers'. For each 'n':
#       If n > 0, increment positive_count
#       Else if n < 0, increment negative_count
#       Else, increment zero_count (covers zero)

# e.g.
# for n in numbers:
#     if ...
#         ...
#     elif ...
#         ...
#     else:
#         ...

# TODO: Print the results:
# print("Positive:", positive_count)
# print("Negative:", negative_count)
# print("Zero:", zero_count)

# ===== PART 3: DEFINE FUNCTIONS =====

# TODO: 1. Convert the code from PART 1 into a function get_numbers() that returns the list of numbers.

# def get_numbers():
#     # 1. Prompt user for count
#     # 2. Create empty list
#     # 3. Collect numbers in a loop
#     # 4. Return the list
#     pass

# TODO: 2. Convert the code from PART 2 into a function analyze_numbers(numbers)
#         that returns (positive_count, negative_count, zero_count).

# def analyze_numbers(numbers):
#     pass

# TODO: 3. Write a function display_results(positive_count, negative_count, zero_count)
#         that prints the result in a nice format.

# def display_results(positive_count, negative_count, zero_count):
#     pass

# TODO: 4. Write a main() function that ties it all together:
#     numbers = get_numbers()
#     p_count, n_count, z_count = analyze_numbers(numbers)
#     display_results(p_count, n_count, z_count)

# def main():
#     pass

# TODO: 5. At the bottom, call main() if the script is run directly:
# if __name__ == "__main__":
#     main()

# END OF SKELETON
