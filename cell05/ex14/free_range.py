#!/usr/bin/env python3
import sys

def main():
    # Check if the number of parameters is not equal to 2
    if len(sys.argv) != 3:
        print("none")
        return

    # Retrieve the parameters
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("none")
        return

    # Construct a list of numbers in the specified range (inclusive)
    number_range = list(range(start, end + 1))

    # Display the list
    print(number_range)

if __name__ == "__main__":
    main()