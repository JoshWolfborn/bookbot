def get_book_text(book):

    with open(book) as f:

        text = f.read()

    return text

def get_number_of_words_in_text(text):

    number_of_words = len(text.split())

    return number_of_words

def get_character_counts(text):

    text = text.lower()
    
    character_counts_dictionary = {}

    for character in text:

        if character in character_counts_dictionary:

            character_counts_dictionary[character] += 1

        else:

            character_counts_dictionary[character] = 1

    return character_counts_dictionary

def sort_on(count):

    return count["Count"]

def sort_character_counts_dictionary_greatest_to_least(character_counts_dictionary):

    character_list = []

    for character, count in character_counts_dictionary.items():

        character_list.append({"Character": character, "Count": count})

    character_list.sort(reverse=True, key=sort_on)
    
    return character_list