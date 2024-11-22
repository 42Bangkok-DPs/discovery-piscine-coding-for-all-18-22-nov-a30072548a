#!/usr/bin/env python3

def main():
    # Prompt the user for a number
    number = int(input("Enter a number:\n"))

    # Display the multiplication table for the given number
    for i in range(10):
        print(f"{i} x {number} = {i * number}")

if __name__ == "__main__":
    main()