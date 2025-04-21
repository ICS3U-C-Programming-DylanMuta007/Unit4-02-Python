#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : April 2025
# Calculates the factorial of the given number


def main():
    # Get user_numb as string
    user_numb_as_string = input("Input a positive integer: ")

    try:
        # Tries to convert the string into an integer
        user_numb_as_int = int(user_numb_as_string)

        # Checks if the user input is less than 0 or more than 100
        if user_numb_as_int < 0:
            print("\nPlease chose a positive integer")

        else:
            # Sets counter and sum to 0
            counter = 0
            factorial = 1

            # calculates the factorial of number while checking if counter is >= user number
            while True:
                # calculates the factorial of a number
                counter = counter + 1
                factorial = factorial * counter

                print(f"tracking {counter} time(s) though the loop")

                if counter >= user_numb_as_int:
                    break

            print(f"{user_numb_as_int}! = {factorial}")

    # If the user_input cant be converted prints the catch statement
    except ValueError:
        print("\nPlease input a number")


if __name__ == "__main__":
    main()
