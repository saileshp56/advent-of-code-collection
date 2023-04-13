mylist = []
file_name = 'input.txt'
summation = 0


f = open(file_name, 'r')
file_data = f.read()
input_text_block = file_data.strip().split('\n')
for line in input_text_block:
        summation += int(line)//3 -2

print(summation)