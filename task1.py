def upper_vowel(word):
    result = ""
    vowels = ["a", "e", "i", "o", "u"]
    for i in word:
        if i in vowels:
            result += i.upper()
        else:
            result += i

    return result

word = "aabbggdd"
print(upper_vowel(word))