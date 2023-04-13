mylist = []
file_name = 'input.txt'

depth = 0
width = 0
aim = 0
f = open(file_name, 'r')
file_data = f.read()
input_text_block = file_data.strip().split('\n')
for line in input_text_block:
        temp = line.split()
        if(temp[0] == 'up'):
                aim -= int(temp[1])


        elif(temp[0] == 'down'):
                aim += int(temp[1])


        elif(temp[0] == 'forward'):
                width += int(temp[1])
                depth += aim*int(temp[1])



print(depth, width, depth * width)