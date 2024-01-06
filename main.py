file_brodsky = 'brodsky.txt'
file = open(file_brodsky, mode='r')
file_content = file.read()
file.close()
print(file_content)

print('*' * 30)

with open('brodskySkyros.txt', 'r') as f:
    print(f.read())
f.close()
