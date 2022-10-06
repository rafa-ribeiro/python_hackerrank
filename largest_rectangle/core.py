#!/bin/python3

import os

"""
    Problem: https://www.hackerrank.com/challenges/largest-rectangle/problem
"""


#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#
def largestRectangle(h):
    max_area = 0
    area = 0
    stack = []
    i = 0
    while i < len(h):
        if len(stack) == 0 or h[stack[-1]] <= h[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if len(stack) == 0:
                area = h[top] * i
            else:
                area = h[top] * (i - stack[-1] - 1)

            if area > max_area:
                max_area = area

    while len(stack) > 0:
        top = stack.pop()
        if len(stack) == 0:
            area = h[top] * i
        else:
            area = h[top] * (i - stack[-1] - 1)

        if area > max_area:
            max_area = area

    return max_area


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
