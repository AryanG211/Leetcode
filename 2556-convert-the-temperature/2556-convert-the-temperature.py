class Solution(object):
    def convertTemperature(self, celsius):
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 +32.00
        return [Kelvin , Fahrenheit]

celsius = 39.23
sol = Solution()
result = sol.convertTemperature(celsius)
print(result)
        