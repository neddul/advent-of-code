with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

game_sum = 0

for row in rows:
    game_id = row.split(':')
    items = game_id[1].split(';')
    info = []
    for item in items:
        item = [a.split() for a in item.split(',')]
        info.append(item)

    valid_game = True
    for item_set in info:
        for item in item_set:
            bag = {'red' : 12, 'green' : 13, 'blue' : 14}
            bag[item[1]] -= int(item[0])
            if bag[item[1]] < 0:
                valid_game = False            

    
    game_id = game_id[0][5:]
    if valid_game:
        game_sum += int(game_id)



print(game_sum)
