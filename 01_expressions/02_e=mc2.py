# Problem Statement
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!





# Define the speed of light as a constant (in meters per second)
C = 299792458  # Speed of light in m/s

def calculate_energy(mass):
    """
    Calculate energy using Einstein's mass-energy equivalence formula: E = m * C^2
    """
    return mass * C**2

def main():
    while True:
        try:
            # Ask user to enter mass in kg
            mass = float(input("Enter kilos of mass: "))

            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s\n")

            # Calculate energy
            energy = calculate_energy(mass)

            # Print result
            print(f"{energy} joules of energy!\n")

        except ValueError:
            print("Please enter a valid number for mass.")

        # Ask user if they want to continue
        choice = input("Do you want to enter another mass? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
