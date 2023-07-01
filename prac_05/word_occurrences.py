"""
Word Occurrences
Estimate: 25 minutes
Actual:    minutes
"""

text = input("Enter your text: ")
words = text.split()
unique_words = set(words)
word_to_frequency = {}

for word in unique_words:
    word_to_frequency[word] = words.count(word)

max_length = max(len(word) for word in unique_words)
for key in word_to_frequency:
    print(f"{key:{max_length}} = {word_to_frequency[key]}")
