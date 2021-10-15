"""
Task:- Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the
average of all the plants with distinct heights in her greenhouse.
Formula used: Average = Sum of Distinct heightd/Total number of Distinct Heights
Input Format:- The first line contains the integer,N , the size of arr.
The second line contains the N space-separated integers,arr[i]
"""

"""
    10
    161 182 161 154 176 170 167 171 170 174
"""


def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
