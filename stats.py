

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
    return(file_contents)

def get_num_words(text_from_book):
    words_from_book = text_from_book.split()
    num_words = len(words_from_book)
    return f"Found {num_words} total words"

def get_char_count(text_from_book):
    words_from_book = text_from_book.split()
    chars_in_book = {}
    for word in words_from_book:
        for char in word:
            lower_char = char.lower()
            if lower_char in chars_in_book:
                # print(f"{lower_char} value increase")
                chars_in_book[lower_char] = chars_in_book[lower_char] + 1
            else:
                # print(f"{lower_char} added")
                chars_in_book[lower_char] = 1
    # print(chars_in_book) 
    return(chars_in_book)

def sort_char_count(char_count):
    filtered_chars = []
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char in sorted_char_count:
        if char[0].isalpha():
            filtered_chars.append(char)
    return filtered_chars
    
def printable_sorted_char_count(sorted_char_count): 
    output = ""
    for char in sorted_char_count:
        output = output + f"{char[0]}: {char[1]}" + "\n"
    output = output[:-1]
    return(output)

