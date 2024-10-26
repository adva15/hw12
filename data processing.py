#11
num: int = int(input('enter a number: '))
SENTINEL: int=0
sum_digit_negatives: int = 1

print(num, ': ', end="")
while True:
    num: int = int(input('enter a negatives number: '))
    if num < 0:
       num+=1
       sum_digit_negatives %= 10
       sum_digit_negatives //= 10
       continue
    if num > 0:
        break
    print(f"average = {sum_digit_negatives}")
print(sum_digit_negatives)


#12
list_10: list[int] = []
for _ in range(1,10+1):
    list_10.append(_)
print(list_10[::-1])
#13
SENTINEL: int = 0
count=0
prime=1

while True:
    num: int = int(input('give me a number:'))
    if num == SENTINEL:
        break
    if num >1 :
        prime=1
        count += 0
    for i in range(2,int(num**0.5+1)):
        if num % i == 0:
            prime=0
            break
        if prime:
            count +=1
    print(f"the amount of prime numbers are {count}")

#14
while True:
    grade1: int = int(input("grade1:"))
    grade2: int = int(input("grade2:"))
    grade3: int = int(input("grade3:"))
    grade4: int = int(input("grade4:"))
    grade5: int = int(input("grade5:"))

    avg_grades = (grade1 + grade2 + grade3+grade4+grade5) / 5
    digits_count:int = 0
    if 0<= grade1 <= 100 and 0<= grade2 <= 100 and 0<= grade3 <= 100 and grade4 <= 100 and 0 <= grade5 <= 100 \
        and avg_grades // 5 :
        break
    if digits_count == 0:
            digits_count = 1
    else:
        while avg_grades > 0:
              digits_count += 1
              num = avg_grades // 5
        print(f"{digits_count} {"+ " if avg_grades // 5 else "= "}", end="")
print(digits_count)
print(avg_grades)

#15
num1: int = int(input("number 1 for division:"))
num2: int = int(input("number 2 for division:"))

sum_division: int = 0

if num1 > 0 and num2 >0 :
    sum_division: int = num1+num2 // 10
    sum_division += sum_division
    sum_division = sum_division // 10
print(num1, '// ', f"{num2}","=", end="")
print(sum_division)

#BONUS:
#16
num: int = int(input('enter a tree-numbers: '))

save: int = num
ahadot:int=0
sum_digit: int = 0

print(num, ': ', end="")

if  num >0:
    ahadot: int = num % 10
    sum_digit += ahadot
    num = num // 10
    print (f"{sum_digit}+{ahadot} {"+ " if num > 0 else "= "}", end="")
    print(sum_digit)
    print("The number is not divisible by 3")
else:
    print(sum_digit)
    print("The number is divisible by 3")


#17
text_string:str=str(input("enter a text string:"))
hello=None
if text_string == "hello":
    print(f"The answer does not change")
else:
    print(f"The reverse answer is {text_string[::-1]}")