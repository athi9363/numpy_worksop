#write a program to find the sum of digits of a given number'
n=int(input("no:"))
def sum(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total

print(sum(n))
