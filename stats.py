def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    letter_count = {}
    for t in text:
        t.lower()
        letter_count[t] += 1
    return letter_count