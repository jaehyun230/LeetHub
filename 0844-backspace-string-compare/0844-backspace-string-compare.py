class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        
        temp = []
        for i in s :
            if i != "#" :
                temp.append(i)
            
            if i == "#" and temp :
                temp.pop()
        
        temp2 = []
        for i in t :
            if i != "#" :
                temp2.append(i)
            
            if i == "#" and temp2 :
                temp2.pop()
        
        if temp == temp2 :
            return True
        else :
            return False
       
            