#!/usr/bin/env python3
import sys

# Check if exactly one parameter was passed (excluding the script name)
if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")