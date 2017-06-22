# -*- coding: utf-8 -*- #


def selectionSort(alist):
    for i in range(len(alist)):
        least = i
        leastValue = alist[i]
        for j in range(i+1, len(alist)):
            if alist[j]<leastValue:
                least = j;
                leastValue = alist[j]
        
        tmp = alist[i]
        alist[i] = alist[least]
        alist[least] = tmp
        
list1 = [7,9,5,1,8]
selectionSort(list1)
print(list1)