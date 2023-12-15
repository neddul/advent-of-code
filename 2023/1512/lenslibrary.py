with open("input.txt",'r') as f:     data = f.read()
data = data.split(',')

def my_hash(my_char, current_value):
    current_value += ord(my_char)
    current_value *= 17
    current_value = current_value % 256
    return current_value

def do_hash(string):
    current_value = 0
    for s in string:
        current_value = my_hash(s, current_value)
    return current_value

list_of_boxes = []
for _ in range(256):
    list_of_boxes.append([])

def add_or_sub(string):
    if string[-1].isdigit():
        return True
    return False

def boxes(string):
    if add_or_sub(string):
        #Add stuff to box
        lens_label = string[:-2]
        box_number = do_hash(lens_label)
        box_of_lenses = list_of_boxes[box_number]
        should_append = True
        for i in range(len(box_of_lenses)):
            if box_of_lenses[i][:-2] == lens_label:
                print("yahoo")
                #Replace lens
                list_of_boxes[box_number][i] = string[:-2] + " " + string[-1]
                should_append = False                

        if should_append:
            list_of_boxes[box_number].append(string[:-2] + " " + string[-1])
    else:
        lens_label = string[:-1]
        box_number = do_hash(lens_label)
        box_of_lenses = list_of_boxes[box_number]
        label_length = len(lens_label)
        for i in range(len(box_of_lenses)):
            if box_of_lenses[i][:label_length] == lens_label:
                list_of_boxes[box_number] = box_of_lenses[:i] + box_of_lenses[i+1:]
                break

def calc_boxes(list_of_boxes):
    my_sum = 0
    for i in range(len(list_of_boxes)):
        for j in range(len(list_of_boxes[i])):
            focal_length = int(list_of_boxes[i][j][-1])
            my_sum+= (i+1)*(j+1)*focal_length
    return my_sum

my_sum = 0
for d in data:
    my_sum+=do_hash(d)
    boxes(d)

print(f"P1: {my_sum}")
print(f"P2: {calc_boxes(list_of_boxes)}")