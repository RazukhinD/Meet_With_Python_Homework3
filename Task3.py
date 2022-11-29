number=int(input('Введи число которое надо преобразовать в двоичное:'))
new_number=''
while number>0:
    new_number = str(number%2)+new_number
    number=number//2
print(new_number)

