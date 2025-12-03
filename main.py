def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
        
    print(word_count(file_contents))
    print_report(dict_to_lst(char_count(file_contents)), book_path)


def word_count(file_txt):
    words_lst = file_txt.split()
    return len(words_lst)


def char_count(file_txt):
    char_dict = {}
    for i in file_txt:
        lower = i.lower()
        if lower not in char_dict:
            char_dict[lower] = 1
        else:
            char_dict[lower] += 1
    return char_dict


def dict_to_lst(dict):
    char_lst = []
    for keys, values in dict.items():
        char_lst.append({'keys': keys, 'values': values})
    return char_lst


def print_report(char_lst, book_path):
    print(f"--- Begin report of {book_path} ---")
    char_lst.sort(reverse = True, key = sort_on)
    for char_dict in char_lst:
        if char_dict['keys'].isalpha():
            print(f"The '{char_dict['keys']}' was found {char_dict['values']} times")

    print('-- End Report --')
    



def sort_on(char_lst):
    return char_lst['values']


def get_text(path):
    with open(path) as contents:
        return contents.read()


main()