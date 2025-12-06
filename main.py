import sys

from stats import get_book_text

from stats import get_number_of_words_in_text

from stats import get_character_counts

from stats import sort_character_counts_dictionary_greatest_to_least

def main():

    if len(sys.argv) < 2:

        print("Usage: python3 main.py <path_to_book>")

        sys.exit(1)

    else:
    
        book = sys.argv[1]
    
        book_text = get_book_text(book)

        number_of_words_in_text = get_number_of_words_in_text(book_text)

        character_counts_dictionary = get_character_counts(book_text)

        character_list = sort_character_counts_dictionary_greatest_to_least(character_counts_dictionary)

        print("============ BOOKBOT ============")

        print("Analyzing book found at books/frankenstein.txt...")

        print("----------- Word Count ----------")

        print(f"Found {number_of_words_in_text} total words")

        print("--------- Character Count -------")

        for object in character_list:
            
            character = object["Character"]

            count = object["Count"]

            if character.isalpha():

                print(f"{character}: {count}")

        print("============= END ===============")

main()