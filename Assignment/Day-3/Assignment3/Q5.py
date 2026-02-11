def longest_word(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest

words = ["Rohan", "Shyamkant", "Kurumkar"]
print("Length of longest word:", longest_word(words))
