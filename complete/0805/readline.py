file = open('0805/sample.txt', 'r', encoding='UTF-8')
data = file.readlines()
for line in data:
    print(line, end='')
file.close()
