"""8. Weather Monitoring System

A weather monitoring system classifies the weather condition based on temperature:

* Below 0°C → Freezing
* 0°C to 20°C → Cold
* 21°C to 35°C → Warm
* Above 35°C → Hot

Write a Python program to classify the weather.

Input:
Enter temperature: 38

Output:
Weather Condition: Hot"""

w = int(input("Enter the Weather :"))
if w < 0 :
	print("Freezing")
elif 0 <= w <= 20:
	print("Cold")
elif 21 <= w <= 35:
	print("Warm")
else :
	print("Hot")
