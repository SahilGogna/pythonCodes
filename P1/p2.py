def collatz(number):
   if number%2:
       print('odd')
       return 1
   else:
       print('even')

result = 0
while result!=1:
    num = input()
    try:
       new = int(num)
       result = collatz(new)
    except:
       print('please enter a number')
    
