from stats import get_num_words
from stats import count_characters

def main():
    file_contents = get_num_words()
    count_characters(file_contents)

main()