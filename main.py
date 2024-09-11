def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_words(text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)

main()