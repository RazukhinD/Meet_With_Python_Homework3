from decimal import Decimal as dcm
start_list=input('Введи числа через пробел:')
inital_list=start_list.split()
print(inital_list)
temp_list=[]
for item in inital_list:
    k=dcm(item)%1
    print(k)
    temp_list.append(k)
min=1
max=0
for numbers in temp_list:
    if numbers!=0:
        if numbers<min:
            min=numbers
    if numbers>max:
        max=numbers
diff=max-min
print(f'Разница между максимальным и минимальным значением дробной части элементов={diff}')
