"""
Task:- There is an array of n integers. There are also 2 disjoint sets,A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0. For each i integer in the array, if i E A, you add 1 to your happiness.
If i E B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.
Input Format:- The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.
Output Format:- Output a single Integer, your total responses
"""
"""
    3 2
    1 5 3
    3 1
    5 7
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = list(map(int, input().split()))
ns = list(map(int, input().split()))
h = set(map(int, input().split()))
s = set(map(int, input().split()))
res = 0
for x in ns:
    if x in h:
        res += 1
    elif x in s:
        res -= 1
print(res)
