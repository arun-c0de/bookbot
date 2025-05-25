def get_num_words(book_string):
    return len(book_string.split())

def character_counter(book_string):
    char_count = dict()
    book_string = book_string.lower()
    for character in book_string:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sorted_list(character_dict):
    sorted_char_count = []
    for key in character_dict:
        sorted_char_count.append({"char": key, "num": character_dict[key]})
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count
