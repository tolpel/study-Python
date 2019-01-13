vowels = ['a','i','u','e','o']
word = input("単語を入力してください。母音を探します。")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
