#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
'''
Demonstration of sorting and searching technique in a single program!

Sorting algo used:   Quick Sort
Searching algo used: Binary Search

© Pranshu Ranakoti 2019
'''
#===================PROGRAM STARTS===================
#import the randint function
from random import randint

#Pretty Printing
class bcolors:
    HEADER= '\033[35m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NOFORMAT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#Create a random array
def createRandomArray(size=20, max=100):
    return [randint(0, max) for _ in range(size)]

def createUserArray():
    global arr
    arr = []
    nElements = int(input("Enter the number of elements: "))
    for i in range(0,nElements):
        elements=int(input("Element at index {}: ".format(i)))
        arr.append(elements)

print(f"{bcolors.HEADER}{bcolors.BOLD}Quick Sort and Binary Search Python3 implementation\n{bcolors.NOFORMAT}")

#=================Quick Sort=================
def quickSort(arr):

    if len(arr)<=1: return arr #if the array has less than or equal to 1 element, its already sorted!
    smaller, equal, greater = [],[],[] #create auxiliary arrays for sorting the elements
    pivot = arr[randint(0,len(arr)-1)] #select a random pivot to decrease the chances of getting one sided cases

#The pivot in action
    for current in arr:
        if current<pivot:    smaller.append(current)
        elif current==pivot: equal.append(current)
        else:                greater.append(current)
#return the combined list of elements, the 'equal' list is already sorted
    return quickSort(smaller)+equal+quickSort(greater)

#===============Binary Search==================
def binarySearch(arr,valSearch):
    #if the array has 0 elements, or has only 1 element and its not the required element, return false
    if len(arr)==0 or (len(arr)==1 and arr[0]!=valSearch):
        return "No such value found!"

    #divide the array into 2 parts
    mid=arr[int(len(arr)/2)]

    #if the mid element is the required number, return that
    if valSearch==mid: return "\n{} found at index {}".format(valSearch, sortedArr.index(valSearch))
    #if the required number is less than mid, search the first half
    if valSearch<mid: return binarySearch(arr[:int(len(arr)/2)], valSearch)
    #if the required number is greater than mid, search the second half
    if valSearch>mid: return binarySearch(arr[int(len(arr)/2+1):], valSearch)

arrType=int(input("Press 1 for custom array or 2 for randomly generated array: "))

if arrType==1:
    arr=None
    createUserArray()
    print("Unsorted Array: ", arr)
    sortedArr = quickSort(arr)
    print("Sorted Array:   ", sortedArr)
    valSearch = int(input("\nInput the number to be searched: "))
    print(binarySearch(sortedArr,valSearch))

    print("\n Benchmark is not yet supported on User Defined Arrays...\n Create a pull request if you've implemented it! Thanks!")
if arrType==2:
    print ("Generating a random array!\n")
    arr = createRandomArray()
    print("Unsorted Array: ", arr)
    sortedArr = quickSort(arr)
    print("Sorted Array:   ", sortedArr)
    valSearch = int(input("\nInput the number to be searched: "))
    print(binarySearch(sortedArr,valSearch))

    #==============Benchmark Sort and valSearch=============(Optional Code)
    print ('\nRunning benchmarks for sorting and searching algos!')
    from time import time
    times = {'Sort':[], 'Search':[]}
    n = [10,100,1000,10000,100000]
    samples = 5

    for size in n:
        tot_time = 0.0
        for _ in range (samples):
            arr = createRandomArray(size,size)
            t0 = time()
            sortedArr = quickSort(arr)
            t1 = time()
            tot_time += (t1-t0)
        times['Sort'].append(tot_time/float(samples))

        tot_time = 0.0
        for _ in range (samples):
            arr = createRandomArray(size,size)
            t0 = time()
            sortedArr = binarySearch(arr, valSearch)
            t1 = time()
            tot_time += (t1-t0)
        times['Search'].append(tot_time/float(samples))

    print ('\n')
    print(20*"="+"\n")
    print ("Sample\tQuick Sort"+"\nSize")
    print (20*"_")
    for i,size in enumerate(n):
        print ("{0:d}\t{1:f}".format(size,times['Sort'][i]))
    print ('\n')
    print(25*"="+"\n")
    print ("Sample\tBinary Search"+"\nSize")
    print (25*"_")
    for i,size in enumerate(n):
        print ("{0:d}\t{1:f}".format(size,times['Search'][i]))

#===================PROGRAM ENDS===================
