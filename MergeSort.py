'''
Created on May 5, 2016

@author: Juan

Python 3.5
'''
import random
class MergeSort(object):
    '''
    implementation of a Merge sort
    Running time:O( ( nlogn)  
    '''
    def __init__(self):
        '''
        Constructor
        '''

    def merge(self,S1,S2):
        #merge S1 and S2 in order to generate one merged sorted sequence S
        S=[]
        S1_index = 0
        S2_index = 0

        for i in S1:     
            notDone = True
            
            while notDone:
                if (S2_index < len(S2)):
                    if(i < S2[S2_index]):
                        S.append(i)
                        S1_index += 1
                        notDone=False
                    else:
                        S.append(S2[S2_index])
                        S2_index += 1
                else:
                    S.append(i)
                    S1_index += 1
                    notDone=False
        
        while S2_index < len(S2):
            S.append(S2[S2_index])
            S2_index += 1
        
        return S.copy()
        
    def MergeSort(self,S):
        #Input: Sequence S with n elements
        #Output: sorted sequence S
        if(len(S) > 1):
            half = int(len(S) / 2)
            S1 = S[0:half]
            S2 = S[half:]
                    
            return self.merge(self.MergeSort(S1),self.MergeSort(S2.copy()))
        else:
            return S.copy()

array = [random.randint(0,1000) for r in range(0,1000)]
s = MergeSort()

print(s.MergeSort(array))