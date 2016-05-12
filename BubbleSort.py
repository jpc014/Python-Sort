'''
Created on May 5, 2016

@author: Juan

Python 3.5
'''
import random
class BubbleSort():
    '''
    implementation of Bubble sort
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def BubbleSort(self, array):
        '''
        Running time:
            Average O( (n^2) )
            Worst O( (n^2) )
        '''
        notDone = True
        
        while(notDone):
            notDone=False
            size = len(array)-1
            for i in range(0, size):
                if(array[i] > array[i+1]):
                    temp = array[i+1]
                    array[i+1] = array[i]
                    array[i] = temp
                    notDone=True
        return array
    
array = [random.randint(0,100000) for r in range(0,100)]
s = BubbleSort()

print(s.BubbleSort(array))