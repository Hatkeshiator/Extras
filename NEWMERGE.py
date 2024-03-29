# goitre: make a merge sort
# marge simpson: you halve the list into two roughly equal sublists and keep doing that until each leaf is a 1-list
# then you merge lists, knowing that each of the pairs of lists you're merging is itself sorted
# so you use an algorithm that relies on that. Make a new list, and compare the first elements of each list. 
# whichever is lower gets moved to the new list. Repeat until one of the lists is empty, then append the rest of the other list to
# the new list.

listsize = int(input("How many numbers in your list? "))

from sort import issorted

def mergelists(list1, list2):
    
    merged = []
    i = 0

    while len(list1) != 0 and len(list2) != 0:
        
        if list1[0] <= list2[0]:
            merged.append(list1[0])
            del list1[0]
        
        else:
            merged.append(list2[0])
            del list2[0]
        
        i += 1
    
    merged += list1 + list2

    return merged

def merge(mylist):

    merged = mylist

    if not issorted(mylist):

        half = len(mylist) // 2

        left = mylist[:half]
        right = mylist[half:]

        merged = mergelists(merge(left), merge(right))

    return merged

mylist = [(x ** 2 % 395) - (x % 73) for x in range(listsize)]

print("Your input list is:  ", mylist)
print("The ordered list is: ", merge(mylist))