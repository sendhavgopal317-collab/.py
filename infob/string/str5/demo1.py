'''1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc'''



n=input("enter input").lower()
alpha=""
for ch in n:
        if ch==" ":
            pass
        else:
         f=0
         for x in alpha:
            if x==ch:
             f=1
             n[x]=n[i]
             break
         if f==0:
            alpha=alpha+ch
print(alpha)