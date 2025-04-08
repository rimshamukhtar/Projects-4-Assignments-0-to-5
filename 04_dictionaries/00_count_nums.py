# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.


def get_user_numbers():
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("⚠️ Please enter a valid number.")
    return user_numbers

def count_nums(num_lst):
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict

def print_counts(num_dict):
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

def main():
    print("📊 Number Frequency Counter 📊\n(Leave input blank to finish)")
    user_numbers = get_user_numbers()
    if user_numbers:
        num_dict = count_nums(user_numbers)
        print("\n🔁 Frequency of Each Number:")
        print_counts(num_dict)
    else:
        print("❌ No numbers were entered.")

if __name__ == '__main__':
    main()
