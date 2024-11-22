#!/usr/bin/env python3
import sys

def main():
    # Get the list of parameters, excluding the script name
    params = sys.argv[1:]

    # Check if there are no parameters
    if len(params) == 0:
        print("none")
        return
    # Loop through each parameter and process it
    for param in params:
        if not param.endswith("ism"):
            print(param + "ism")

if __name__ == "__main__":
    main()