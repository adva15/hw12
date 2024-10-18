#6
natural_num_n:int=int(input("natural number n:"))
for _ in range(natural_num_n, 0 ,-1):
    print(_," ",end="")
print()
#7
num1:int=int(input("number 1:"))
num2:int=int(input("number 2:"))

for numbers in range(num1-1,num2):
    if numbers % 2:
        numbers+=1
        print("",numbers,end="")
print()

for numbers in range(num1,):
    if numbers % 3 or  numbers % 5:
        numbers+=1
        print("",numbers,end="")
#8

