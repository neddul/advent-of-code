with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

cards = []
for x in rows:
    cards.append(x.split(' | '))


winning_cards = []
your_cards = []
for x in cards:
    a = x[0].split(': ')
    a = a[1:]
    a = a[0].split()
    winning_cards.append(a)
    b = x[1].split()

    your_cards.append(b)


winning_cards = [[int(x) for x in a if x.isdigit()] for a in winning_cards]
your_cards = [[int(x) for x in a if x.isdigit()] for a in your_cards]


score = 0
for w, m in zip(winning_cards, your_cards):
    winning_numbers = 0
    for number in m:
        if number in w:
            print(number)
            winning_numbers +=1
    print()
    if winning_numbers > 0:
        points = 2**(winning_numbers-1)
        score+=points

print(score)