'''
Write a Python program to convert radians to degrees.
Test Data:
Radian : .52
Expected Result : 29.781818181818185
'''

ANGLE_180 = 180
PI_VALUE = 3.14

radian = float(input("Radian: "))

result = (radian * 180) / PI_VALUE

result_with_decimals = int(result * 1000) / 1000.0

print(result_with_decimals)