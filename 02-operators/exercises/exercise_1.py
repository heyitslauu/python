'''
Write a Python program to convert degrees to radians.
Note : The radian is the standard unit of angular measure, used in many areas of mathematics. 
An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle; one radian is just under 57.3 degrees (when the arc length is equal to the radius).

Test Case: 30
Result: 0.523

Test Case: 100
Result:  1.744
'''

PI_VALUE = 3.14
ANGLE_180 = 180


degree = int(input("Degree: "))

result = degree * (PI_VALUE/ANGLE_180)

result_with_decimals = int(result * 1000) / 1000.0

print(result_with_decimals)



