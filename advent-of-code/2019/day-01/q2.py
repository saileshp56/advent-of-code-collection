mylist = []
file_name = 'input.txt'
summation = 0


f = open(file_name, 'r')
file_data = f.read()
input_text_block = file_data.strip().split('\n')
for line in input_text_block:
        innerSum = int(line)//3 - 2
        current = innerSum
        while current > 0:
                temp = current//3 - 2
                current = temp
                if(temp > 0):
                        innerSum += temp
        summation+= innerSum

print(summation)