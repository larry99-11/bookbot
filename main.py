def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_count = get_book_text_word_connt(book_path)

    chars_dictionary = text_from_book(book_text)
    # then get the dictionary and sort it in a list
    chars_sorted_list = chars_dictionary_to_sorted_list(chars_dictionary)


    print(f"-- begin report of: {book_path} --")
    print(f"{book_count} words found in the document")
    print()

    print("book dictionary:", chars_dictionary)


    #####
    print(f"--- Begin report of: {book_path} ---")
    print(f"{book_count} Words found in the document")

    # Now we have to convert the dictionary of 

def chars_dictionary_to_sorted_list(nums_chars_dict):
    sorted_list = []

    for character in nums_chars_dict:
        sorted_list.append({"char": character, "num": nums_chars_dict[character]})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_book_text_word_connt(path):
    with open(path) as f:

        file_contents = f.read()

        # this line is using the split function that will store the data in an array
        word_count = len(file_contents.split())

    return word_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["num"]

def text_from_book(text):

    string_dictionary = {}
    for string in text:
        convert_to_lowercase = string.lower()

        if convert_to_lowercase in string_dictionary:
            string_dictionary[convert_to_lowercase] +=1
        else:
            string_dictionary[convert_to_lowercase] = 1

    return string_dictionary



    
main()