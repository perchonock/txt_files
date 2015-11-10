import nltk

infile = open('www2.txt', 'r', encoding='utf8')
raw_text = infile.read()
sents = set(nltk.sent_tokenize(raw_text))
sents2 = []

for sent in sents:
    if '\n' in sent:
        s = sent.split('\n')
        sents2.extend(s)
    else:
        sents2.append(sent)

count = 0
# for sent2 in sents2:
#         print(sent2)
#         print('www')

for sent2 in sents2:
    if len(sent2) > 2 \
            and sent2[0].isupper() \
            and sent2[-1] == '.' \
            and ('ing ' in sent2) \
            and ('according to ' not in sent2)\
            and ('According to ' not in sent2):
        print(sent2)
        count +=1


print(len(sents2))
print(count)

infile.close()
