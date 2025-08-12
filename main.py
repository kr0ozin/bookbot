import sys
from stats import word_count
from stats import char_count
from stats import sort_on
from stats import convert_to_list

def get_book_text(file):
    with open(file) as f:
        return f.read()
    
def generate_report(dict):
    report = ""
    for d in dict:
        if d["char"].isalpha():
            report += d["char"] + ": " + str(d["num"]) + "\n"
    return report

def print_report(num, data, book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    print(data)
    print("============= END ===============")

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    text = get_book_text(path_to_book)
    num_words = word_count(text)
    full_dict = char_count(text)
    dict_list = convert_to_list(full_dict)
    dict_list.sort(reverse = True, key = sort_on)
    report_data = generate_report(dict_list)
    print_report(num_words, report_data,path_to_book)

main()
