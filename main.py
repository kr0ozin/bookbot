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

def print_report(num, data):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    print(data)
    print("============= END ===============")

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    full_dict = char_count(text)
    dict_list = convert_to_list(full_dict)
    dict_list.sort(reverse = True, key = sort_on)
    report_data = generate_report(dict_list)
    print_report(num_words, report_data)

main()
