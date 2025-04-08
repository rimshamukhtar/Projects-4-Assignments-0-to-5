# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.



import random

NUM_SIDES = 6

def roll_dice():
  """
    Simulates rolling two dice and prints their total
    """
  die1 = random.randint(1, NUM_SIDES) # Removed extra indent and changed := to =
  die2 = random.randint(1, NUM_SIDES) # Removed extra indent and changed : to =
  print(f"Die 1: {die1}")
  print(f"Die 2: {die2}")
  total = die1 + die2
  print(f"Total of two dice: {total}")

def main(): # Removed extra indent
  die1 : int = 10
  print("die1 in main() start as:" + str(die1))
  roll_dice()
  roll_dice()
  roll_dice()
  print("die1 in main() is:" + str(die1))

if __name__ == "__main__":
  main()