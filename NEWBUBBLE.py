# goal: to write a bubble sort function and have the user input a list to sort.
# bubble sort: you go through the list checking all adjacent pairs of elements and if one is out of sort then you swap them.
#     keep redoing it until the list is sorted.

from sort import issorted

listsize = int(input("How many numbers in your list? "))

# fn bubble
# param: a list
# output: input list with all elements sorted in ascending order

def bubble(mylist):

    while not issorted(mylist):

        for i in range(listsize-1):

            if mylist[i] > mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]

    return mylist

mylist = [(x ** 2 % 395) - (x % 73) for x in range(listsize)]

print("Your input list is:  ", mylist)
print("The ordered list is: ", bubble(mylist))