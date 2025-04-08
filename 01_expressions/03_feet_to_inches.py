# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.



def feet_to_inches(feet):
    """
    Convert feet to inches.
    1 foot = 12 inches.
    """
    return feet * 12

def main():
    while True:
        try:
            # Ask user for input in feet
            feet = float(input("Enter length in feet: "))

            # Convert feet to inches
            inches = feet_to_inches(feet)

            # Print result
            print(f"{feet} {'foot' if feet == 1 else 'feet'} is equal to {inches} inches.\n")

        except ValueError:
            print("Please enter a valid number for feet.")

        # Ask user if they want to continue
        choice = input("Do you want to convert another value? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
