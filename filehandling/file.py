#file = open('data.txt', 'a')
#ontent = '\n This is a third line'
#file.write(content)
#file.close()
with open('datareadlines.txt', 'r') as file:
     lines = file.readlines()

for line in lines:
     print(line)

