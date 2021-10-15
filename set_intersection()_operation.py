"""
Task:- You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
and the other set is subscribed to the French newspaper. The same student could be in both sets.
Your task is to find the total number of students who have subscribed to at least one newspaper.
Input Format:- The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.
Output Format:- Output the total number of students who have subscriptions to both English and French newspapers.
"""
"""
    9
    1 2 3 4 5 6 7 8 9
    9
    10 1 2 3 11 21 55 6 8
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
num1 = int(input())
setA = set(map(int, input().split()))
num2 = int(input())
setB = set(map(int, input().split()))

print(len(setA.intersection(setB)))