import re
mylist = []
file_name = 'input.txt'
summation = 0

list1 = ['N', 'Q', 'L', 'S', 'C', 'Z', 'P', 'T']
list2 = ['G', 'C', 'H', 'V', 'T', 'P', 'L']
list3 = ['F', 'Z', 'C', 'D']
list4 = ['C', 'V', 'M', 'L', 'D', 'T', 'W', 'G']
list5 = ['C', 'W', 'P']
list6 = ['Z', 'S', 'T', 'C', 'D', 'J', 'F', 'P']
list7 = ['D', 'B', 'G', 'W', 'V']
list8 = ['W', 'H', 'Q', 'S', 'J', 'N']
list9 = ['V', 'L', 'S', 'F', 'Q', 'C', 'R']
list1.reverse()
list2.reverse()
list3.reverse()
list4.reverse()
list5.reverse()
list6.reverse()
list7.reverse()
list8.reverse()
list9.reverse()
templist = []
templist.append(list1)
templist.append(list2)
templist.append(list3)
templist.append(list4)
templist.append(list5)
templist.append(list6)
templist.append(list7)
templist.append(list8)
templist.append(list9)

# templist = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
f = open(file_name, 'r')
file_data = f.read()
input_text_block = file_data.strip().split('\n')
print(templist)

for line in input_text_block:
        #int(line.split('move')[1].split('from')[0])
        match = re.findall(r'\d+', line)
        templist2 = []
        for num in range(int(match[0])):

                templist2.append(templist[int(match[1]) - 1].pop())


        templist2.reverse()

        for item in templist2:
                templist[int(match[2]) - 1].append(item)
        print(templist)


for list in templist:
        print(list[-1])
print(templist, "final")