class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashmap= {}
        for i in range(len(list1)):   
            hashmap[list1[i]] = i
        
        res = []

        minsum = float("inf")   
        
        for j in range(len(list2)):   
            if list2[j] in hashmap:
                Sum = j + hashmap[list2[j]]    
                
                if Sum < minsum:  
                    minsum = Sum
                    res = []
                    res.append(list2[j])
                elif Sum == minsum:    
                    res.append(list2[j])
        return res