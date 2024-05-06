
def get_book_text_word_connt(path):
    with open(path) as f:

        file_contents = f.read()

        # this line is using the split function that will store the data in an array
        word_count = len(file_contents.split())

    return word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def text_from_book(text):

    string_dictionary = {}
    for string in text:
        convert_to_lowercase = string.lower()

        if convert_to_lowercase in string_dictionary:
            string_dictionary[convert_to_lowercase] +=1
        else:
            string_dictionary[convert_to_lowercase] = 1

    return string_dictionary

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_count = get_book_text_word_connt(book_path)

    chars_dictionary = text_from_book(book_text)
    print("Word count:", book_count)
    print("book dictionary:", chars_dictionary)

    
main()