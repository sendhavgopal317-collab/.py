'''.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found'''
s=input("")
i=len(s)-1
count1=0
count2=0
secl=""
vis=""
l=""

while i>=0:
    ch=s[i]
    if ch  not in vis:
        count=s.count(ch)
        if count>count1:
            count2=count1
            secl=l
            count1=count
            l=ch
        elif count>=count2 and count!=count1:
            count2=count
            secl=ch
        vis=vis+ch
    i=i-1
print("s second highest is -",count2," ",secl)
print("leargest is -", count1," ", l)



   