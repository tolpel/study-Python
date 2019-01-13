def search4vowels(word):
    """入力された単語内の母音を表示する。"""
    vowels = set('aiueo')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

"""git-krakenからあげてみた """
