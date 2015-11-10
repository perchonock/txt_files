inf = open("test_en.txt", 'r', encoding="utf8")
ngrams = open("list_of_words_without_freq.txt", 'r', encoding="utf8")
ouf = open("outfile.txt", 'w', encoding="utf8")

phrases_dict = {}

for line in ngrams:
    phrases_dict[line.strip()] = 0

print(phrases_dict)

for line in inf:
    for phrase in phrases_dict:
        if phrase.lower() in line.strip().lower():
            phrases_dict[phrase] +=1

for key, value in phrases_dict.items():
    s = key + "\t" + str(value) + "\n"
    ouf.write(s)

print(phrases_dict)

inf.close()
ngrams.close()
ouf.close()
