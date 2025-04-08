# Problem Statement
# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Here's two sample runs of the program (user input in bold italics):

# Enter a fruit: pear

# This fruit is in stock! Here is how many:

# 1000

# Enter a fruit: lychee

# This fruit is not in stock.

def main():
    # User se fruit ka naam lena
    fruit : str = input("Enter a fruit: ")
    
    # Fruit ka stock check karna
    stock = num_in_stock(fruit)
    
    # Agar stock 0 hai, toh fruit available nahi hai
    if stock == 0:
        print("This fruit is not in stock.")
    else:
        # Agar stock 0 se zyada hai, toh fruit ka stock print karna
        print("This fruit is in stock! Here is how many:")
        print(stock)

# Function to check fruit stock
def num_in_stock(fruit):
    """
    This function returns the number of fruit Sophia has in stock.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        # Fruit stock mein nahi hai
        return 0

# Code ko run karne ka tareeqa
if __name__ == '__main__':
    main()
