#!/usr/bin/env python3
import sys

# Check if any parameters were passed (excluding the script name)
if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")