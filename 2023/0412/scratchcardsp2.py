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
    a = a[0].split(' ')
    winning_cards.append(a)
    b = x[1].split(' ')

    your_cards.append(b)


winning_cards = [[int(x) for x in a if x.isdigit()] for a in winning_cards]
your_cards = [[int(x) for x in a if x.isdigit()] for a in your_cards]
number_of_cards = [1 for x in range(len(winning_cards))]
    
list_of_all_cards = []

score = 0
i= 0

for w, m, x in zip(winning_cards, your_cards, number_of_cards):
    for _ in range(x):     
        winning_numbers = 0
        for number in m:
            if number in w:
                winning_numbers +=1

        if winning_numbers > 0:
            for j in range(winning_numbers):
                number_of_cards[j+i+1] +=1
    i +=1
    
print(sum(number_of_cards))