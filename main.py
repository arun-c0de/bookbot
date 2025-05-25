import sys
from stats import get_num_words
from stats import character_counter
from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    book_path = sys.argv[1]
    book_string = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    num_words = get_num_words(book_string)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    character_dict = character_counter(book_string)
    sorted_char_count = sorted_list(character_dict)
    print("--------- Character Count -------")
    for i in sorted_char_count:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
