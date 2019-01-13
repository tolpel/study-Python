vowels = ['a','i','u','e','o']
word = input("単語を入力してください。母音を探します。")

found = {}

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k,v in sorted(found.items()):
    print(k,'の出現回数は', v,'回。')
