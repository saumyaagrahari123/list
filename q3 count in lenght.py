# Write a code, that counts the numbers between 20 and 40 and then print its count.

numbers=[50, 40, 23, 70, 56, 22, 25, 10, 7]
length = len(numbers)
s = 0
num_between40_20=0
while s<length:
    num = numbers[s]
    if num<40 and num>20:
        num_between40_20+=1
    s+=1
print(num_between40_20)


