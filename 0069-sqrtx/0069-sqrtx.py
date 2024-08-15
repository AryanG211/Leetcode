class Solution(object):
    def mySqrt(self, x):
        left , right = 1 , x
        if (0 < x < 2):
            return x
        else:
            while left <= right:
                mid = (left + right)//2
                M_square = mid * mid
                if M_square == x:
                    return mid
                elif M_square > x:
                    right = mid -1
                    
                else:
                    left = mid + 1 

            return right
        
x = 16
sol= Solution()
result = sol.mySqrt(x)
print(result)        