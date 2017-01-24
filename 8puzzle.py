num_array = list()
num = input("Enter how many elements you want:")
print( 'Enter numbers in array: ')
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))
print( 'ARRAY: ',num_array)
count = 0
iteration = 0
while(num_array != num_array.sort()):

    if num_array[0] == 0:
        num_array[0] = num_array[1]
        num_array[1] = 0
        count+=1
        print(count, num_array)
    if num_array[1] == 0:
        num_array[1] = num_array[2]
        num_array[2] = 0
        count+=1
        print(count, num_array)
    if num_array[2] == 0:
        num_array[2] = num_array[5]
        num_array[5] = 0
        count+=1
        print(count, num_array)
    if num_array[3] == 0:
        num_array[3] = num_array[4]
        num_array[4] = 0
        count+=1
        print(count,num_array)
    if num_array[4] == 0:
        num_array[4] = num_array[5]
        num_array[5] = 0
        count+=1
        print(count, num_array)
    if num_array[5] == 0:
        num_array[5] = num_array[8]
        num_array[8] = 0
        count+=1
        print(count, num_array)
    if num_array[6] == 0:
        num_array[6] = num_array[7]
        num_array[7] = 0
        count+=1
        print(count, num_array)
    if num_array[7] == 0:
        num_array[7] = num_array[8]
        num_array[8] = 0
        count+=1
        print(count, num_array)
    if num_array[8] == 0:
        num_array[8] = num_array[7]
        num_array[7] = 0
        count+=1
        print(count, num_array)
    iteration+=1

print(num_array)
print(count)
print(iteration)
