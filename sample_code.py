#!/usr/bin/env python3
"""
Sample Python file for Git practice.

This is a simple Python program that demonstrates basic Python concepts.
You don't need to understand everything - just use this file to practice Git!

What this program does:
- Creates a list of names
- Says hello to each person
- Says goodbye to each person
"""

# A "function" is a reusable piece of code that does one thing.
# Here's a function that creates a greeting message.
# When you call greet("Alice"), it returns "Hello, Alice!"

def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


# This is another function that says goodbye.
def farewell(name):
    """Return a farewell message for the given name."""
    return f"Goodbye, {name}! See you soon."


# This is the main function - it's the entry point of our program.
# When you run this file, Python starts here.
def main():
    # A "list" is a collection of items in order.
    # Here we create a list of three names.
    names = ["Alice", "Bob", "Charlie"]

    # Print a header for the greetings section
    print("=== Greetings ===")

    # A "for loop" repeats code for each item in a list.
    # This loop prints a greeting for each name in our list.
    for name in names:
        print(greet(name))

    # Print a blank line and a header for the farewells section
    print("\n=== Farewells ===")

    # Another loop for farewells
    for name in names:
        print(farewell(name))


# This special line says "if this file is run directly, start here".
# It tells Python to run the main() function when you execute this file.
if __name__ == "__main__":
    main()
