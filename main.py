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

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    report_output = '''============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------\nFound ''' + str(num_words) + " total words\n--------- Character Count -------\n"
    full_dict = char_count(text)
    dict_list = convert_to_list(full_dict)
    dict_list.sort(reverse = True, key = sort_on)
    report_output += generate_report(dict_list)
    print(report_output)

main()
