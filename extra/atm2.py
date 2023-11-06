#New and improved
#Algorithm
#If remainder of 50 = 0, turn into 50's and 100's
#Else remove a 20 until it is divisable by 50 or out of money.

def withdraw(amount: int) -> [int]:
	money_left = amount
	hundreds = 0
	fifties = 0
	twenties = 0

	while money_left > 0:
		if money_left % 50 == 0 and money_left > 0: #Is the money divisable by 50? 
			fifties = money_left // 50 #If so, find out how many fifties you got
			money_left = 0	
		else:
			money_left -= 20
			if money_left >= 0:
				twenties += 1
				
	hundreds = fifties // 2 #if there are more than 2 fifties, turn every other extra fifty into a 100
	fifties = fifties - 2*hundreds #remove 50's
	return [hundreds, fifties, twenties]


if withdraw(40) == [0, 0, 2]:
	print("40 test true")
if withdraw(60) == [0, 0, 3]:
	print("60 test true")
if withdraw(230) == [1, 1, 4]:
	print("230 test true")
if withdraw(250) == [2, 1, 0]:
	print("250 test true")
if withdraw(260) == [2, 0, 3]:
	print("260 test true")
if withdraw(70) == [0, 1, 1]:
	print("70 test true")
