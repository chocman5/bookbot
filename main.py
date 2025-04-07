#python 3

from stats import *
import sys

args = sys.argv

def header(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

def argument_check():
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():

    argument_check()

    # Set variables
    book_path = args[1]

    # Header Text 
    header(book_path)
    print ("----------- Word Count ----------") # display formating

    # prints and returns number of words
    file_contents = get_num_words(book_path) 

    print("--------- Character Count -------")
    char_count = count_characters(file_contents) # builds directory of characters
    char_list = sort_characters_by_count(char_count) #builds list of directories. Sorts by count

    print_characters(char_list)

    print("============= END ===============")

main()