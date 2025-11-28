
def get_num_words(text_from_book):
    words_from_book = text_from_book.split()
    num_words = len(words_from_book)
    print(f"Found {num_words} total words")

def get_character_count(text_from_book):

    words_from_book = text_from_book.split()
    characters_in_book = {}
    for word in words_from_book:
        for character in word:
            lower_character = character.lower()
            if lower_character in characters_in_book:
                # print(f"{lower_character} value increase")
                characters_in_book[lower_character] = characters_in_book[lower_character] + 1
            else:
                # print(f"{lower_character} added")
                characters_in_book[lower_character] = 1
    print(characters_in_book) 

