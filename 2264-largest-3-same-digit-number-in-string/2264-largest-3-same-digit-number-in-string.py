class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        answer = ""
        for i in range(len(num)-2) :
            if num[i] == num[i+1] and num[i+1] == num[i+2] :
                if answer == "" :
                    answer = num[i]*3
                elif int(num[i]) > int(answer[0]) :  
                    answer = num[i]*3
                
        return answer