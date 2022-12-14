class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        dic={'type':0,'color':1,'name':2}
        cnt=0
        for i in items:
            if i[dic[ruleKey]]==ruleValue:
                cnt+=1
        return cnt
    
    ##another sol
        # typee=[]
        # color=[]
        # name=[]
        # count=0
        # for i in range(len(items)):
        #     typee.append(items[i][0])
        #     color.append(items[i][1])
        #     name.append(items[i][2])
        # if ruleKey==typee:
        #     return typee.count(ruleValue)
        # elif ruleKey == "color":
        #     return color.count(ruleValue)
        # elif ruleKey == "name":
        #     return name.count(ruleValue)