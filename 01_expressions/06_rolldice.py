# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.



"""
🎲 Dice Rolling Simulator 🎲
----------------------------
Simulate rolling two dice, and print results of each
roll as well as their total.
"""

# 🧠 Import the random library to generate random numbers (like dice rolls!)
import random

# 🎯 Number of sides on each die (standard dice have 6 sides)
NUM_SIDES: int = 6

def main():
    # 🧪 (Optional) Set a seed for predictable results while testing
    # random.seed(1)

    # 🎲 Roll first die (1 to 6)
    die1: int = random.randint(1, NUM_SIDES)

    # 🎲 Roll second die (1 to 6)
    die2: int = random.randint(1, NUM_SIDES)

    # ➕ Add the two results to get the total
    total: int = die1 + die2

    # 🖨️ Print out all the results
    print("🎲 Dice have", NUM_SIDES, "sides each.")
    print("🎯 First die:", die1)
    print("🎯 Second die:", die2)
    print("✨ Total of two dice:", total)

# 🚀 This line ensures the main() function runs when the file is executed
if __name__ == '__main__':
    main()
