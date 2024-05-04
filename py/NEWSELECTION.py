# goal: sort using selection sort.
# selection sort: take the smallest unsorted element and place it just after the sorted portion. sorting here is in reference to the sorted list.

# input: n numbers
listsize = int(input("How many numbers in your list? "))

from sort import minimum
# min returns index of lowest value in the function

def selection(mylist):

    for i in range(listsize):
        sublist = mylist[i:]
        minindex = minimum(sublist) + i 
        # +i accounts for the fact that minimum is returning an index relative to i, where if i is the smallest element, it'll return 0
        mylist[i], mylist[minindex] = mylist[minindex], mylist[i]

    return mylist

mylist = [(x ** 2 % 395) - (x % 73) for x in range(listsize)]

print("Your input list is:  ", mylist)
print("The ordered list is: ", selection(mylist))