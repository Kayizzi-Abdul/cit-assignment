# No.1 printing the first 10 numbers using while loop

num = 0

while num <= 10:
    print(num)
    num += 1

# calculatinng the sum of given numbers

n = int(input("enter upperlimit"))
sum = 0
counter = 1

while counter <= n:
    sum += counter
    counter += 1
print(f"the sum is {sum}")


# multiplication table
x = int(input("number number"))
y = int(input("enter upper limit"))

for mult in range(1, y + 1, 1):
    print(f"{x} x {mult} = {x*mult}")

# display number fron -10 to 0 uding while loop

i = -10
while i <= 0:
    print(i)
    i += 1
    
