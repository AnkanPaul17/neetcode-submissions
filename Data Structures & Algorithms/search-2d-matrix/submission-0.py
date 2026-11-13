class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r_low = 0
        r_high = len(matrix) - 1

        while r_low <= r_high:
            r_mid = (r_low + r_high) // 2

            if target < matrix[r_mid][0]:
                r_high = r_mid - 1
            elif target > matrix[r_mid][-1]:
                r_low = r_mid + 1
            else:
                c_low = 0
                c_high = len(matrix[0]) - 1

                while c_low <= c_high:
                    c_mid = (c_low + c_high) // 2

                    if matrix[r_mid][c_mid] == target:
                        return True
                    elif matrix[r_mid][c_mid] < target:
                        c_low = c_mid + 1
                    else:
                        c_high = c_mid - 1

                return False

        return False