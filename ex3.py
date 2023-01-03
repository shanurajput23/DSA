max=int(input("enter the mumber:"))
odd_numbers=[]
for i in range (1,max):
    if i%2==1:
        odd_numbers.append(i)
print("odd numbers:",odd_numbers)
