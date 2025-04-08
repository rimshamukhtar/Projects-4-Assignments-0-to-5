# Problem Statement
# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

# We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

# Here are two sample runs of the program, one for each return option (user input in bold italics):

# (Entered age is an adult age)

# How old is this person?: 35

# True

# (Entered age is not an adult age)

# How old is this person?: 7

# False


ADULT_AGE = 18  # U.S. legal adult age

def is_adult(age: int):
    if age >= ADULT_AGE:  # Check if age is 18 or older
        return True
    return False

def main():
    age = int(input("How old is this person?: "))  # Get user's age input
    print(is_adult(age))  # Check and print if the person is an adult or not

if __name__ == "__main__":  # Run the main function if the script is run directly
    main()
