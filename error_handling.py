# Handling errors in code is a common part of programming
# There are 2 main types of errors in programming compilation and runtime
# Given that Python does not have a compilation step, only runtime errors can occur

# Errors can be discovered either statically - static inspection/analysis of code or dynamically by running program

# Here is an error of using a variable that does not exist made by programmer
# Static inspection is able to catch these kinds of errors - and IDE like PyCharm will inform about them
# print(non_existent_variable)

# Here is an error when a user inputs an unexpected value - in this case not a number
# Static inspection is not able to catch this error - all user related errors have to be discovered by programmers/testers
# age = int(input("Enter your age: "))

# Errors can be caught by try/except blocks
# Basic use is: let error happen in the try block, handle expected error types in except blocks and use finally to clean up resources

# Example: let user input their age and do various calculations with it
print("Start")

while True:
    user_age = input("Input your age: ")

    # In this block we expect that some error may happen
    # This block should be as small as possible
    try:
        user_age_as_int = int(user_age)

        print(f"In ten years you are going to be: {10 + user_age_as_int}")
        print(f"How many years until retirement: {65 - user_age_as_int}")

        print(f"100 divided by your age: {100 / user_age_as_int}")

        break
    # Here we are catching ValueError which we know may occur, and we want to handle it
    except ValueError as err:
        print(f"Please input number! Full error: {err}")
    # Here we are catching ZeroDivisionError which we know may occur, and we want to handle it
    except ZeroDivisionError:
        print("Age cannot be zero")
    # Here we are catching any other errors with a universal clause - this is not recommended as means we don't know what went wrong
    except Exception as err:
        print(f"Something went wrong: {err}")
    # This block is executed regardless of whether an exception was raised or not
    # This block is mostly used to clean up resources
    finally:
        print("Inside finally")

print("After error handling")
