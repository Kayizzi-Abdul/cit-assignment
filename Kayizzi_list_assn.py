# 1  program to sum numbers in a list
list = []
x  =  int(input("Enter nummber of values"))
n = 1

while n <= x:
    value = int(input("enter value in list"))
    list.append(value)
    n += 1

sum = 0
for  item in range(0, len(list)):
    sum += list[item]
print(sum)

#number 2

list5 = ['abc', 'xyz', 'aba', '1221']
count = 0
for str in list5:
    if len(str) >= 2 and str[0] == str[-1]:
        count += 1
print(count)


 # number 3

fruits = ["apple", "banana", "melon", "banana", "cherry", "banana"]
duplicate = set()
dup = []

for fruit in fruits:
    if fruit not in duplicate:
        dup.append(fruit)
        duplicate.add(fruit)
    

print(f"{fruit} was removed from {duplicate}")


# number 4

list1 = ['red', 'green', 'white', 'black', 'pink', 'yelow']

del list1[0]
del list1[3:5]

print(list1)


#number 5

list2 = [k ** 2 for k in range(6)]
del list2[0:5]

print(list2)