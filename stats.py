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