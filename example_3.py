#modulus operator example

def main():
    number = int(input("Enter an integer: "))

    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

def is_even(n):
        return True if n % 2 == 0:
    
main()