file = open("h.txt", 'r', encoding='utf-8')
file_of_words = open("list_of_words.txt", 'w', encoding='utf-8')
text = file.read()

splitted_text = set(text.split())
words = ''

for i in splitted_text:
    words += i + '\n'

file_of_words.write(words)


file.close()
file_of_words.close()
