"""
Word Occurrences
Estimate: 25 minutes
Actual:   45 minutes
"""

text = input("Enter your text: ")
words = text.split()
unique_words = set(words)
word_to_frequency = {}

# Adds values to the dictionary for each unique word from the user input
for word in unique_words:
    word_to_frequency[word] = words.count(word)

word_to_frequency = dict(sorted(word_to_frequency.items()))  # Sorts the dictionary by alphabetical order

max_length = max(len(word) for word in unique_words)  # Sets the max length to the length of the longest word

# Prints the word and frequency for each word in the dictionary
for key in word_to_frequency:
    print(f"{key:{max_length}} = {word_to_frequency[key]}")
