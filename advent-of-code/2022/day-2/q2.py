def part1(c1, c2):
        if((c1 == 'A' and c2 =='X' )or (c1 == 'B' and c2 =='Y' )or (c1 == 'C' and c2 =='Z' )):
                if(c1 == 'A'):
                        return 4
                elif(c1 == 'B'):
                        return 5
                elif(c1 == 'C'):
                        return 6
        elif(c1 == 'A' and c2 == 'Y'):
                return 8
        elif(c1 == 'A' and c2 == 'Z'):
                return 3
        elif(c1 == 'B' and c2 == 'X'):
                return 1
        elif(c1 == 'B' and c2 == 'Z'):
                return 9
        elif(c1 == 'C' and c2 == 'X'):
                return 7
        elif(c1 == 'C' and c2 == 'Y'):
                return 2
        else:
                print("strange input")
                return 0

def part2(c1, c2):
        if (c1 == 'A' and c2 == 'Y'):
                return 4
        elif (c1 == 'A' and c2 == 'Z'):
                return 8
        elif(c1 == 'A' and c2 == 'X'):
                return 3
        if (c1 == 'B' and c2 == 'Y'):
                return 5
        elif (c1 == 'B' and c2 == 'Z'):
                return 9
        elif(c1 == 'B' and c2 == 'X'):
                return 1
        if (c1 == 'C' and c2 == 'Y'):
                return 6
        elif (c1 == 'C' and c2 == 'Z'):
                return 7
        elif(c1 == 'C' and c2 == 'X'):
                return 2

mylist = []
file_name = 'input.txt'



f = open(file_name, 'r')
file_data = f.read()
input_text_block = file_data.strip().split('\n')
summation = 0


for line in input_text_block:
        stuff = line.split(' ')
        print(stuff[0], stuff[1])
        summation += part2(stuff[0], stuff[1])





print(summation)