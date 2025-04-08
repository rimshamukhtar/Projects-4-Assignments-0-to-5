# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    # Test cases
    print(in_range(5, 1, 10))   # Output: True, because 5 is between 1 and 10 (inclusive)
    print(in_range(15, 1, 10))  # Output: False, because 15 is greater than 10
    print(in_range(7, 5, 10))   # Output: True, because 7 is between 5 and 10 (inclusive)
    print(in_range(1, 1, 10))   # Output: True, because 1 is equal to the low value 1
    print(in_range(10, 1, 10))  # Output: True, because 10 is equal to the high value 10

if __name__ == '__main__':
    main()
