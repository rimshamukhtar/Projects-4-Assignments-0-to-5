# Problem Statement
# Write a function that takes two numbers and finds the average between the two.

def average(a: float, b: float):
    """
    Returns the number which is halfway between a and b
    """
    sum = a + b
    return sum / 2

def main():
    # User se inputs lena
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    # Average calculate karna
    avg = average(a, b)
    
    # Result print karna
    print("The average is:", avg)

if __name__ == '__main__':
    main()
