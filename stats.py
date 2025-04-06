def get_num_words():
    with open("/home/lochie/workspace/github.com/chocman5/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        print(f"{num_words} words found in the document")
        return file_contents

def count_characters(text):

    # Make empty list of characters 
    char_count = {}
    
    text = text.lower()
    characters = list(text)
    for character in characters:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    
    print(char_count)