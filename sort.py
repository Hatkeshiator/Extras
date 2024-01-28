# sortedto: 
# param is a list
# returns an int; index of first unsorted element
# if return == length of list, list is sorted

def sortedto(mylist):

    upto = len(mylist)

    for i in range(len(mylist)-1):

        if mylist[i] > mylist[i+1]:
            upto = i+1
            break
    
    return upto

def spsortedto(mylist):
    
    ref = sorted(mylist)

    for i in range(len(mylist)):
        if mylist[i] != ref[i]:
            upto = i
            break
    
    return upto

def issorted(mylist):
    
    # return mylist == sorted(mylist)
    
    var = True
    
    if sortedto(mylist) < len(mylist):
        var = False

    if len(mylist) <= 1:
        var = True
    
    return var


def minimum(mylist):
    
    minindex = 0

    for i in range(len(mylist)):
        
        if mylist[minindex] > mylist[i]:
            minindex = i
    
    return minindex

def maximum(mylist):
    
    maxindex = 0

    for i in range(len(mylist)):

        if mylist[maxindex] <= mylist[i]:
            maxindex = i

    return maxindex