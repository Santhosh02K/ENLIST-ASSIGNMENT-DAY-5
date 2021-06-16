#1) write a program to create a list of n integer values and do the following
a = []

for i in range(0,25):
    a.append(i)
print(a)

#add an item into the list
a.append(30)
print(a)
#delete using function
del a[10]
print(a)
#store the largest num from the list
max_in_the_list = max(a)
print(max_in_the_list)
#store the smallest one in the list
min_in_the_list = min(a)
print(min_in_the_list)

#2)create a tuple and print the reverse of the tupled
tuple1 = (1,2,3,4,5,6,7)
print(tuple1)
reversing_tuple = reversed(tuple1)
print(tuple(reversing_tuple))

#3) create a tuple and convert tuple into list
tuple2 = (4,5,6,7,8,9)
print(tuple2)
list_tuple = list(tuple2)
print(list_tuple)
