file = open("input.txt")
readings = file.readlines()
file.close()

readings = [s.strip() for s in readings]

def remove_binary(list_of_binary, index, bit): #Takes a list of binary strings and adds the string of binary depending on if the bit in the stream is 0 or 1 depending on input
    filtered_list = []
    for stream in list_of_binary:
        if stream[index] != bit:
            filtered_list.append(stream)
    return filtered_list

def count_occurances(list_of_binary_streams, index):
    ones = 0
    zeroes = 0
    for stream_of_binary in list_of_binary_streams:
        if stream_of_binary[index] == "1":
            ones += 1
        else:
            zeroes +=1
    return ones, zeroes

def o2(list_of_binary, index):
    if len(list_of_binary) == 1:
        return list_of_binary[0]
    ones, zeroes = count_occurances(list_of_binary, index)

    if ones >= zeroes:
        return o2(remove_binary(list_of_binary, index, "0"), index+1)
    else:
        return o2(remove_binary(list_of_binary, index, "1"), index+1)

def co2(list_of_binary, index):
    if len(list_of_binary) == 1:
        return list_of_binary[0]
    ones, zeroes = count_occurances(list_of_binary, index)

    if ones >= zeroes:
        return co2(remove_binary(list_of_binary, index, "1"), index+1)
    else:
        return co2(remove_binary(list_of_binary, index, "0"), index+1)


oxygen = o2(readings, 0) #Strings with binary
carbon = co2(readings, 0)

oxygen = int(oxygen, 2) #Turns string of binary to decimal
carbon = int(carbon, 2)


life_support_rating = oxygen*carbon
print(life_support_rating)