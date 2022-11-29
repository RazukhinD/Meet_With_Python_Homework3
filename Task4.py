size=int(input('Введи длину списка негафибаначчи'))
fib_list=[]
fib_list.append(1)
fib_list.append(0)
print(fib_list)
i=2
k=-2
j=0
while j<=size-2:
    fib_list.append(fib_list[i-2+j]+fib_list[i-1+j])
    fib_list.insert(0,fib_list[i+k+1]-fib_list[i+k])
    i+=1
    k-=1
    j+=1
fib_list.append(fib_list[i-2+j]+fib_list[i-1+j])
print(fib_list)

# fib1=0
# fib2=1
# print(fib1, fib2, end=' ')
# for i in range(2, size+1):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

