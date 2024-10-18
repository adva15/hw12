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

#8
num_n:int=int(input("positive number n:"))

for number in range(num_n+1):
    if number % 3==0 or number % 5==0:
        num_n = number // 3 or number // 5
        print("",number,end="")
#9
num_n7:int=int(input("number n*7:"))

for number in range(num_n7+1):
    if number %7==0:
        print("",number,end="")