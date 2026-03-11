n=int(input("Enter a number:"))

nlist=list(range(1,n+1))
print("Created list is ",nlist)

def print_odd():
    for i in nlist:
        if i%2 != 0:
            print(i,end=" ")

def print_even():
    for i in nlist:
        if i%2 == 0:
            print(i,end=" ")

def print_all():
    for i in nlist:
        print(i,end=" ")

