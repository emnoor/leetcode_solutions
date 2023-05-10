class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            matrix.append([0] * n)

        np = n - 1
        direction = 0  # 0: right, 1: down, 2: left, 3: up
        i = 0
        j = 0

        for k in range(n * n):
            matrix[i][j] = k + 1
            match direction:
                case 0:
                    if j == np or matrix[i][j + 1] != 0:
                        i += 1
                        direction = 1
                    else:
                        j += 1
                case 1:
                    if i == np or matrix[i + 1][j] != 0:
                        j -= 1
                        direction = 2
                    else:
                        i += 1
                case 2:
                    if j == 0 or matrix[i][j - 1] != 0:
                        i -= 1
                        direction = 3
                    else:
                        j -= 1
                case 3:
                    if matrix[i - 1][j] != 0:
                        j += 1
                        direction = 0
                    else:
                        i -= 1

        return matrix