import random
numbers=int(input('Введи число N длинну списка в котором считаем сумму на нечетных позициях '))
initial_list=[]
for number in range(numbers):
    number=random.randint(0,100)
    initial_list.append(number)
print (initial_list)
sum=0
for index in range(len(initial_list)):
    if index%2==1:
        sum+=initial_list[index]
print(f'сумма нечетных индесов данного массива: {sum}')