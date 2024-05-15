def sortedto(mylist: list[int]) -> int:

    upto = len(mylist)

    for i in range(len(mylist)-1):
        if mylist[i] > mylist[i+1]:
            upto = i+1
            break

    return upto

def issorted(mylist):

    # return mylist == sorted(mylist)

    return sortedto(mylist) == len(mylist)


def minimum(mylist):

    minindex = 0

    for i in range(len(mylist)):

        if mylist[minindex] > mylist[i]:
            minindex = i

    return (minindex, mylist[minindex])

def maximum(mylist):

    maxindex = 0

    for i in range(len(mylist)):

        if mylist[maxindex] <= mylist[i]:
            maxindex = i

    return (maxindex, mylist[maxindex])
