import sys
from stats import get_num_words,  get_book_text, printable_sorted_char_count, sort_char_count
from stats import get_char_count

def main():
    arguments = sys.argv
    try:
        book_location = arguments[1]
        print_report(book_location)
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def print_report(book_location):
    if book_location == None:
        print("Please provide the relative location of the book you would like a report on")
    main_header = "============ BOOKBOT ============"
    main_footer = "============= END ===============" 
    word_count_header = "----------- Word Count ----------"
    char_count_header = "--------- Character Count -------"

    book_text = get_book_text(book_location)

    analyze_statement = f"Analyzing book found at {book_location}..."
    word_count_statement = get_num_words(book_text)

    char_count = get_char_count(book_text)

    sorted_char_count = sort_char_count(char_count)

    Psorted_char_count = printable_sorted_char_count(sorted_char_count)

    print(f"{main_header}\n{analyze_statement}\n{word_count_header}\n{word_count_statement}\n{char_count_header}\n{Psorted_char_count}\n{main_footer}")

main()
