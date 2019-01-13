vowels = set('aiueo')

word = input("単語を入力してください。母音を探します。")

found = vowels.intersection(set(word))

for vowel in found:
    print(found)
