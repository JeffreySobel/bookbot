def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    list_of_dicts = dict_to_list(chars_dict)
    for item in list_of_dicts:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times.")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def sort_on(d):
    return d["num"]

def dict_to_list(chars_dict):
    list_of_dicts = []
    for i in chars_dict:
        list_of_dicts.append({"char" : i, "num" : chars_dict[i]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

main()
