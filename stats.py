def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    letter_count = {}
    for t in text:
        t = t.lower()
        if t in letter_count:
            letter_count[t] += 1
        else:
            letter_count[t] = 1
    return letter_count

#Take a dictionary and break it into a list of dictionaries
def convert_to_list(items):
    dict_list = []
    for item in items:
        num = items[item]
        #Iterate through the dictionary and make each char/num its own value/pair dictionary
        char_dict = {
            "char": item,
            "num": num
        }
        dict_list.append(char_dict)
    return dict_list

def sort_on(items):
    return items["num"]