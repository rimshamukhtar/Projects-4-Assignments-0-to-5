# Problem Statement
# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

def is_odd(value: int):
    return value % 2 == 1  # Returns True if number is odd

def main():
    for i in range(10, 20):  # Loop from 10 to 19
        if is_odd(i):
            print(i, "odd")
        else:
            print(i, "even")

if __name__ == '__main__':
    main()
