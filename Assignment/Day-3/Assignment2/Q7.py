def long_words(words, length):
    result = []
    for word in words:
        if len(word) > length:
            result.append(word)
    return result


words = input("Enter words: ").split()
length = int(input("Enter length: "))

print("Words longer than", length, "are:", long_words(words, length))
