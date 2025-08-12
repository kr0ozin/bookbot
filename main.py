from stats import word_count
from stats import char_count

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    print(char_count(text))



main()
