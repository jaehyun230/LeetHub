class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        answer = [[0]*len(img[0]) for i in range(len(img))]
        
        mx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        my = [1, 0, -1, 1, 0, -1, 1, 0, -1]
        
        for i in range (len(img)) :
            
            for j in range(len(img[i])) :
                number = 0
                for k in range(9) :
                    
                    if 0<= i+mx[k] < len(img) and 0 <= j+my[k] < len(img[i]) :
                        print(mx[k], my[k])
                        number +=1
                        answer[i][j] += img[i+mx[k]][j+my[k]]
                
                
                answer[i][j] = answer[i][j]//number
                    
        
        
        return answer