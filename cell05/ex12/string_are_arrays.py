#!/usr/bin/env python3
import sys

def main():
    # Check if exactly one parameter is passed
    if len(sys.argv) != 2:
        print("none")
        return
    
    # Retrieve the parameter (the input string)
    input_string = sys.argv[1]
    
    # Count occurrences of 'z'
    count_z = input_string.lower().count('z')  # Handle case insensitive

    # Display 'z' for each occurrence of 'z'
    if count_z > 0:
        print("z" * count_z)
    else:
        print("none")

if __name__ == "__main__":
    main()