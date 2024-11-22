#!/usr/bin/env python3
def main():
    try:
        # Accept user input and convert it to a number
        num = int(input("Enter a number less than 25: "))
        
        # Check if the number is greater than 25
        if num > 25:
            print("Error")
        else:
            # Loop from the input number up to 25
            for i in range(num, 26):
                print(f"Inside the loop, my variable is {i}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()