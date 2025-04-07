def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        num_words = len(words)
        print(f"Found {num_words} total words")
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
    
    return char_count

def sort_on(dict):
    return dict["count"]  

def sort_characters_by_count(char_count):
    # Create a list to hold dictionaries
    chars_list = []
    
    # For each character in the character count dictionary
    for char, count in char_count.items():
        # Create a dictionary for this character and its count
        char_dict = {"character": char, "count": count}
        # Add the dictionary to our list
        chars_list.append(char_dict)
    
    # Sort the list by count (greatest to least)
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

def print_characters(char_list):
     for char_dict in char_list:
        character = char_dict["character"]
        count = char_dict["count"]
        
        if character.isalpha():
            print(f"{character}: {count}")