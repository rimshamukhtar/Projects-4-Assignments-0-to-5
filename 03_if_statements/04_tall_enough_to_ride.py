# Problem Statement
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)

MINIMUM_HEIGHT: int = 50

def tall_enough_extension():
    print("🎢 Welcome to the Rollercoaster Ride Checker!")
    print(f"Minimum required height to ride: {MINIMUM_HEIGHT} units\n")

    while True:
        height_input = input("Enter your height (or press Enter to exit): ")

        if height_input == "":
            print("\n👋 Exiting... Thank you for visiting!")
            break

        try:
            height = float(height_input)  # Convert to number
            
            if height < 0:
                print("⚠️ Height cannot be negative. Try again.\n")
            elif height >= MINIMUM_HEIGHT:
                print("✅ You're tall enough to ride!\n")
            else:
                print("❌ You're not tall enough to ride, but maybe next year!\n")

        except ValueError:
            print("❗ Invalid input! Please enter a number (e.g. 150.5).\n")
if __name__ == '__main__':
    tall_enough_extension()
