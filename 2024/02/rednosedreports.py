with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def test_row(my_list):
    is_d = False
    is_i = False
    succ = True
    for i in range(len(my_list)-1):
        if succ:
            if my_list[i] != my_list[i+1] and abs(my_list[i] - my_list[i+1]) <= 3:
                if my_list[i] < my_list[i+1] and not is_d: # 1 2 3 4
                    is_i = True
                elif my_list[i] > my_list[i+1] and not is_i: # 4 3 2 1
                    is_d = True
                else:
                    succ = False
            else:
                succ = False
        else:
            break  
    return succ

def check_row(my_list, p2):
    res = True
    succ = test_row(my_list)

    if succ: return res

    if p2:
        for i in range(len(my_list)):
            my_row = my_list.copy()
            my_row.pop(i)

            succ = test_row(my_row)
            if succ: return res
    
    res = False
    return res
    
sum_p1 = 0
sum_p2 = 0

for row in rows:
    current_row = [int(x) for x in row.split()]
    if check_row(current_row, False):
        sum_p1+=1
    if check_row(current_row, True):
        sum_p2+=1

print(sum_p1)
print(sum_p2)
        