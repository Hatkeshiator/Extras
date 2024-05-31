# goal: to make a quicksort algorithm
# quicksort: take the first/last (or a random) element as pivot. Everything smaller than the pivot goes to the left and bigger to the right
# and then we recursively quicksort the left and right. It works because each iteration puts the pivot in its sorted position.

listsize = int(input("How many numbers in your list? "))

def quicksort(alist):
    mylist = alist
    try:
        pivot = mylist[len(mylist)//2]

        right = []
        left = []

        for i in range(len(mylist)):

            if mylist[i] >= pivot:
                right.append(mylist[i])
            else:
                left.append(mylist[i])
        mylist = quicksort(left) + [pivot] + quicksort(right)

    except:
        if len(alist) <= 1:
            mylist = alist

    return mylist

mylist = [(x ** 2 % 395) - (x % 73) for x in range(listsize)]

print("Your input list is:  ", mylist)
print("The ordered list is: ", quicksort(mylist))