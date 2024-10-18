#1
num: float = float(input('enter a number: '))

save: float = num
sum_digit: float = 0
ahadot: float = num - 10
print(num,"", end="")
while num >= 10:
    if num  % 10:
     num = num// 10
    print("-10.0", end="")
    print(f"{"=" if num > 10 else "= "}", end="")
    print(ahadot)
    break
else:
    ahadot: float = num * 10
    sum_digit = ahadot
    num = num // 10
    print("*10.0", end="")
    print (f" {"*" if num > 10 else "= "}", end="")
    print(sum_digit)

#2
x: float = float(input('give me a number:'))
a: float = float(input('give me a number:'))
b: float = float(input('give me a number:'))
sum1:float=x+a+b

for _ in range(3):
    if sum1 > 100 :
        sum1: float = x + a + b
        print(f"{sum1}")
        break
    if sum1 < 100:
        print(f"{sum1}The amount is less than 100")
        break

#In short:
print(f"{sum1} {"" if sum1 > 100 else "The amount is less than 100"}")
#3 bonus

#4
age: int = int(input('give me a number:'))
print(f"{age} {"" if age <0  or age < 120 else "Incorrect age"}")

#5
num_three_digit: int = int(input("My three digit number:"))
if 100 <= num_three_digit <= 999:
    num_three_digit= num_three_digit // 10 % 10
    print (f"{num_three_digit}")
