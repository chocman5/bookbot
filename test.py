import sys

args = sys.argv

def argument_check():
    if len(args) != 2:
        print("Usage: python 3 main.py <path_to_book>")
        sys.exit(1)

def main():
    test = argument_check()
    print("you got out")
    print(len(args))
    checker = input()

main()