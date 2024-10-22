import os
os.chdir('C:\\Users\\khleb\\Desktop')
with open('1.txt', encoding='utf-8') as f:
    count = 0
    for i in f.read():
        if i.isupper():
            count += 1
    print(count)
