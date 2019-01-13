phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.remove("D")
plist.remove("'")

for letter in plist:
    if letter in plist:
        plist.pop()
        print(plist)

plist.remove(" ")

plist.insert(2, " ")
plist.insert(4, "a")

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
