mylist = []
file_name = 'input.txt'
summation = 0

skip = False
f = open(file_name, 'r')
file_data = f.read()
input_text_block = file_data.strip().split('\n')
subList = [input_text_block[n:n+3] for n in range(0, len(input_text_block), 3)]
print(subList)

duplicates = []
templist = []
templist2 = []
counter = 0
for element in subList:
        counter = 0
        templist.clear()
        templist2.clear()
        print(element, " <-")
        for line in element:
                for char in line:
                        if counter == 0:
                                print("appending ", char)
                                templist.append(char)
                        elif counter == 1:
                                templist2.append(char)
                        else:
                                if char in templist and char in templist2 and counter == 2:
                                        duplicates.append(char)
                                        break
                counter += 1
                print(duplicates, " duplicates")






for char in duplicates:
        if char.islower():
                summation += ord(char) - 96
                print("adding ", ord(char) - 96)
        else:
                summation += ord(char) - 38
                print("adding ", ord(char) - 38)



print(summation)