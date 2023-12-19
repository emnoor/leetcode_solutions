class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        img2 = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                s = img[i][j]
                c = 1
                
                coordinates = [
                    (i-1, j-1), (i-1, j), (i-1, j+1),
                    (i, j-1), (i, j), (i, j+1),
                    (i+1, j-1), (i+1, j), (i+1, j+1),
                ]
                
                s = 0
                c = 0
                for ii, jj in coordinates:
                    if ii >=0 and ii < m and jj >=0 and jj < n:
                        s += img[ii][jj]
                        c += 1
                
                img2[i][j] = s // c
        
        return img2