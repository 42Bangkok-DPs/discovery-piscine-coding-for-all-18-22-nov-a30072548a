#!/usr/bin/env python3
import sys

# Check if there are fewer than two parameters
if len(sys.argv) < 3:
    print("none")
else:
    # Display the parameters in reverse order
    for param in reversed(sys.argv[1:]):
        print(param)