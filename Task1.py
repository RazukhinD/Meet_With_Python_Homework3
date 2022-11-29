import random
numbers=int(input('Введи число N длинну списка: '))
initial_list=[]
for number in range(numbers):
    number=random.randint(0,100)
    initial_list.append(number)
print (initial_list)
k=-1
multiply=[]
i=0
while i<numbers/2:
    multiply.append(initial_list[i]*initial_list[k])
    i+=1
    k-=1
print(multiply)
