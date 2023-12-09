with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
rows = [x.split() for x in rows]
rows = [[int(x) for x in row] for row in rows]

def diff_row(my_list):
    diff_list = []
    for i in range(len(my_list)-1):
        diff_list.append(my_list[i+1] - my_list[i]) 
    return diff_list

def check_rows(my_list):
    for x in my_list:
        if x != 0:
            return False
    return True

p1 = 0
p2 = 0
for row in rows:
    temp_diff_list = [row]
    while not check_rows(temp_diff_list[0]):
        new_row = diff_row(temp_diff_list[0])
        temp_diff_list = [new_row] + temp_diff_list
    
    for i in range(len(temp_diff_list) - 1):
        temp_diff_list[i+1].append(temp_diff_list[i][-1] + temp_diff_list[i+1][-1])
        temp_diff_list[i+1].insert(0, temp_diff_list[i+1][0] - temp_diff_list[i][0])
   
    p1+= temp_diff_list[-1][-1]
    p2+= temp_diff_list[-1][0]
        
print(f"Part 1 {p1}")
print(f"Part 2 {p2}")