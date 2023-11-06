def withdraw(amount: int) -> [int]:
    #Check if it is divisable by 100 with rest 0
    if amount % 100 == 0:
      hundreds = amount/100
      return [int(hundreds), 0 ,0]
    if amount % 50 == 0:
      money_left = amount
      hundreds = money_left // 100
      return [hundreds, 1, 0] #If it is divisable by 50 then it's always going be x hundreds and 1 50, otherwise just return in hundres in linse 6
    if amount % 20 == 0:
      money_left = amount
      hundreds = money_left // 100
      money_left = money_left - hundreds*100
      twenties = int(money_left/20)
      return [hundreds, 0, twenties]
    
    if amount >= 70 and amount <=130:
      money_left = amount
      twenties = 0
      while money_left > 50:
        twenties +=1
        money_left = money_left - 20
      
      return [0, 1, twenties]
      
    
    money_left = amount
    hundreds = money_left // 100
    if hundreds > 1:
      hundreds -= 1 #Need atleast 110 to even out with 50's and 20's
    money_left = money_left - hundreds*100
    
    twenties = 0
    while money_left > 50:
      twenties +=1
      money_left = money_left - 20
      
    if twenties > 5:
      twenties -= 5
      hundreds +=1
      
    

    return[hundreds, 1, twenties]


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
