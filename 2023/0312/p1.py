with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def get_neighbors(x,y, arr, diagonals=False):
    neighbors = []
    len_cols = len(arr[0]) - 1
    len_rows = len(arr) - 1
    if diagonals:
        for dy in range(-1,2):
            for dx in range(-1,2):
                if x+dx < 0 or x+dx > len_cols or y+dy < 0 or y+dy > len_rows or (dx == 0 and dy == 0):
                    continue
                else:
                    neighbors.append((x+dx, y+dy))
    else:
        if x + 1 < len_cols:
            neighbors.append((x+1, y))
        if x - 1 >= 0:
            neighbors.append((x-1, y))
        if y + 1 < len_rows:
            neighbors.append((x, y+1))
        if y - 1 >= 0:
            neighbors.append((x, y-1))

    return neighbors
numbers = []
summ = 0

my_list_of_strings = []
for y in range(len(rows)):
    number_list = []
    indices = []
    
    number = ""
    row = rows[y]
    use_number = False
    my_strings = list(rows[y])
    # print(len(my_strings))
    print(len(row))
    for x in range(len(row)):
        if row[x].isdigit():
            number+=row[x]
            indices.append(x)
            if not use_number:
                neighbors = get_neighbors(y, x, rows, diagonals=True)
                if y == 74 and x > 120:
                    print(x)
                    print(neighbors)
                for n, m in neighbors:                    
                    if not rows[n][m].isalpha() and not rows[n][m].isdigit() and not rows[n][m] == '.':
                        use_number = True
            print(number)
        else:
            if not use_number:
                number = ""
                indices = []
                continue
            else:
                use_number = False
                for x in indices:
                    my_strings[x] = '.'
                indices = []
                numbers.append(int(number))
                number_list.append(int(number))
                summ += int(number)
                number = ""

    if len(number) > 0 and use_number:        
        use_number = False
        for x in indices:
            my_strings[x] = '.'
        indices = []
        numbers.append(int(number))
        number_list.append(int(number))
        summ += int(number)
        number = ""
    
        
    a = ''.join(my_strings)
    my_list_of_strings.append(a)
    print("")
    print(f"{y} - {number_list}")
    print("")

    
with open('input_copy.txt', 'w') as file:
    # Write each string to a new line in the file
    for string in my_list_of_strings:
        file.write(string + '\n')


print(summ)
            