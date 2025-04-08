# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it r
# emoves until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main()
#  function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])  # Access first element using index 0



def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()               # Get list from user
    get_first_element(lst)        # Print first element

if __name__ == '__main__':
    main()
