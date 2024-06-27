def analyze_sentence(sentence):
    words = sentence.split()
    num_words = len(words)
    num_captial= sum(1 for c in sentence if c.isupper())
    num_small = sum(1                                                                                                                                                                                                                                                                    for c in sentence if c.islower())
    num_digit = sum()




