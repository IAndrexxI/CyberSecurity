keys=[(1, 9, 4), (4, 2, 8), (4, 8, 3), (7, 1, 5), (8, 10, 1)]
with open("g:/Il mio Drive/UNIPD Andrea/CyberSecurity/Challenges 3/1_valley_of_fear/book.txt", "r") as book:
    text=book.read()
    paragraphs=[p.split("\n") for p in text.split("\n\n")]
    words=list(map(lambda p: list(map(lambda s: s.split(" "), p)), paragraphs))
    flag=' '.join(words[key[0]-1][key[1]-1][key[2]-1] for key in keys)
print(flag)