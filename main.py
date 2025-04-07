#python 3

from stats import get_num_words
from stats import count_characters
from stats import sort_characters_by_count
from stats import print_characters

def header(path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")


def main():

    # Set variables

    book_path = "books/frankenstein.txt"

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