file = open('0805/sample.txt', 'r', encoding='UTF-8')
for line in file:
    print(line, end='')
file.close()
