def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            raise ValueError("Input must be non-negative")
        result = factorial(num)
        print(f"The factorial of {num} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

