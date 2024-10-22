
WORD_A = 65
words_dict = {key: chr(value) for key, value in enumerate(
    range(WORD_A, WORD_A + 26)
)}

print(words_dict)

letters = 'helllo'

for key, value in words_dict.items():
    if value.lower() in letters:
        print(key, end='')
        if letters.count(value.lower()) > 1:
            for i in range(letters.count(value.lower()) - 1):
                print(key, end='')
