mylist = []
file_name = 'input.txt'
summation = 0

skip = False
f = open(file_name, 'r')
file_data = f.read()
input_text_block = file_data.strip().split('\n')
for line in input_text_block:
        skip = False
        templist = []
        for char in line[:len(line)//2]:
                templist.append(char)
        for char in line[len(line) // 2:]:
                if char in templist:
                        print("duplicate was ", char)
                        if char.islower():
                                summation += ord(char) - 96
                                print("adding ", ord(char) - 96)
                        else:
                                summation += ord(char) - 38
                                print("adding ", ord(char) - 38)

                        skip = True
                if skip:
                        break

print(summation)