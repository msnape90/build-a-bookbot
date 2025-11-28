from stats import get_num_words
from stats import get_character_count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    get_num_words(book_text)
    get_character_count(book_text)

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return(file_contents)

main()
