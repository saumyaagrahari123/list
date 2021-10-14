friends_list=["Jija","Bhavana","Alima","Pragati","Aditi","Saumya","Fatima"]
# print(friends_list[2])
# print(friends_list[-2])
#[]-represent index (0,1,2,3,4,5,6,)
# negative index-(-1,-2,-3,-4,-5,-6,-7)

# print(friends_list[8])
# Index Error: list index out of range.
# friends_list[2]="Mahi"
# print(friends_list)

# friends_list[8]="jaya"
# print(friends_list)
# IndexError: list assignment index out of range


i = 65
while i <=69:
    print(" ",end=" ")
    a = 65
    while a <= i:
        print(chr(i),end=" ")
        a +=1
    i+=1
    print()
    print()