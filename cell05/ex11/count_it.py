#!/usr/bin/env python3
import sys

def main():
    # Get the number of parameters
    num_params = len(sys.argv) - 1  # Exclude the script name itself

    if num_params == 0:
        print("none")
    else:
        print(f"parameters: {num_params}")
        # Loop through each parameter and print its length
        for param in sys.argv[1:]:  # Skip the first argument (script name)
            print(f"{param}: {len(param)}")

if __name__ == "__main__":
    main()