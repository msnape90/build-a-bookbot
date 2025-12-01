from stats import get_num_words,  get_book_text
from stats import get_character_count

def main():

    book_location = "books/frankenstein.txt"

    main_header = "============ BOOKBOT ============"
    main_footer = "============= END ===============" 
    word_count_header = "----------- Word Count ----------"
    char_count_header = "--------- Character Count -------"

    book_text = get_book_text(book_location)

    analyze_statement = f"Analyzing book found at {book_location}..."
    word_count_statement = get_num_words(book_text)

    char_count = get_character_count(book_text)

    print(f"{main_header}\n{analyze_statement}\n{word_count_header}\n{word_count_statement}\n{char_count_header}\n{main_footer}")


main()
