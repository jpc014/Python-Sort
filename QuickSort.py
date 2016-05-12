'''
Created on May 5, 2016

@author: Juan

Python 3.5
'''
import random
class QuickSort(object):
    '''
    implementation of a Quick sort
    running time
        average: O(n Log(n))
        worst  : O(n^2)
    '''
    
    def __init__(self):
        '''
        Constructor
        '''

    def partition(self, S, pivot):
        #partition sequence S so that items <pivot are in partition L and items >pivot are in partion R
        L = []
        R = []
        for i in S:
            if i < pivot:
                L.append(i)
            else:
                R.append(i)
        return L, R
    
    def quickSort(self, S):
        # Input: sequence S with n elements
        # Output: Sorted sequence S
        if(len(S) > 1):
            pivot_index = int(len(S) / 2)
            
            pivot = S.pop(pivot_index)
            L,R = self.partition(S,pivot)
            L = self.quickSort(L)
            R = self.quickSort(R)
            
            pivot = [pivot]
            return L + pivot + R
        else:
            return S
        
q = QuickSort()
toSort = [random.randint(0,100000) for r in range(0,10000)]

print(q.quickSort(toSort))    
        