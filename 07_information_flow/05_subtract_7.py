# Problem Statement
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.


def main():
    # User se number lena
    num: int = int(input("Enter a number: "))  # Input ko integer mein convert kar rahe hain
    num = subtract_seven(num)  # Subtract 7 from the entered number
    print("The result after subtracting 7 is: ", num)  # Result print karte hain

def subtract_seven(num):
    num = num - 7  # 7 ko num se subtract karte hain
    return num  # Updated num return karte hain

# This part is required to call the main function
if __name__ == '__main__':
    main()
