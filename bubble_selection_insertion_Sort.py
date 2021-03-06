import time
import random

'''Bubble Sort is basic sorting algorithm which sorts by
    comparing two consecutive elements in an array
    Space complexity: O(1)
    Time Complexity: O(n^2)    Best: O(n)'''

def swap(x, y):
    temp = x
    x = y
    y = temp
    return x,y

def bubble(B):
    size = len(B)
    for i in range(size):
        #in bubble sort with ascending order max element is sorted first
        #hence we dont need to reach size we an reach (size-1) - i
        for j in range(size-i-1):
            if (B[j]>B[j+1]):
                B[j],B[j+1]=swap(B[j],B[j+1])
    print 'Bubble sort:', B
#
# #Selection sort first finds min value
# # then we look in the array if we can find another value less than
# # current min. If we find another value to be ;ess then current min we swap these values
# Space complexity: O(1)
# Time Complexity: O(n^2)    Best: O(n^2)

def selection(A):
    size = len(A)
    for i in range (size):
        for j in range (i+1,size):
            if (A[i]>A[j]):
                A[i], A[j] = swap(A[i], A[j])
    print 'Selection Sort:',A

#Insertion sort is better then then bubble and selection sort
#Insertion sort looks at an element
# if we have only one element it is always sorted so we start with
# comparing 2 values first select first element
# compare if this element is greater then values in the array
# if it is smaller then a value insert at right position
# Space complexity: O(1)
# Time Complexity: O(n^2)    Best: O(n)

def insertion(A):
    size = len(A)
    for i in range(1, size):
        j = i-1
        temp = A[i]
        while j in range(0,size):
            if (temp<A[j]):
                A[j+1]=A[j]
                j-=1
            else: break
        A[j+1] = temp
    # print 'Insertion Sort:',A

#--------------------------------------------
# Entry point for program execution
bub = [3, 1, 9, 0, 12, 90, 45]
bubble(bub)

select = [3, 1, 9, 0, 12, 90, 45]
selection(select)

inArr = [3, 1, 9, 0, 12, 90, 45]
insertion(inArr)
print inArr

# get total time taken for insertion sort to sort x elements y times
start = time.time()
for j in range(10): # loop 100 times
    inArr = []
    for i in range(100): # elements in array
        inArr.append(random.randrange(0,1000))
    insertion(inArr)

end = time.time()
t_time =(end - start)
# print 'Insertion Sort: ', inArr
print 'Insertion time:',t_time