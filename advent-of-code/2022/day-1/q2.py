mylist = []
file_name = 'input.txt'
summation = 0


f = open(file_name, 'r')
file_data = f.read()
input_text_block = file_data.strip().split('\n')
highest = 0
summation = 0
mylist = []
for line in input_text_block:
        if(line != ''):
                summation += int(line)
        elif(line == ''):
                mylist.append(summation)
                summation = 0

print(mylist)
mylist.sort()
print(mylist)