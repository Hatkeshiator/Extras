# goal: to sort elements using insertion sort.
# insertion sort: take the first unsorted element and slide it backward through the sorted portion until it fits.

from Extras.py.sorting.sort import sortedto # returns index of first unsorted element of an array e.g. stdto([1,5,4,2,3]) == 2

listsize = int(input("How many numbers in your list? "))

def insertion(mylist):

    while sortedto(mylist) != listsize:
        start = sortedto(mylist)

        for i in range(start, 1, -1): # iterate backward from first unsorted element
            if mylist[i-1] > mylist[i]:
                mylist[i], mylist[i-1] = mylist[i-1], mylist[i]
            else:
                break

        if start == 1:
            mylist[0], mylist[1] = mylist[1], mylist[0]

    return mylist

mylist = [(x ** 2 % 395) - (x % 73) for x in range(listsize)]

print("Your input list is:  ", mylist)
print("The ordered list is: ", insertion(mylist))