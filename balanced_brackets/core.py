# !/bin/python3

import os

"""
    Problem: https://www.hackerrank.com/challenges/balanced-brackets/problem
"""

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

OPENS = {'{', '[', '('}

BRACKET_PAIRS = {
    '}': '{',
    ']': '[',
    ')': '(',
}


def is_open(bracket: str):
    return bracket in OPENS


def is_pair(open_bracket: str, close_bracket: str):
    close_bracket_pair = BRACKET_PAIRS[close_bracket]
    return open_bracket == close_bracket_pair


def isBalanced(s):
    stack = []
    for bracket in s:
        if is_open(bracket):
            stack.append(bracket)
        elif len(stack) > 0:
            prev_bracket = stack.pop()
            matched = is_pair(prev_bracket, bracket)
            if not matched:
                return 'NO'
        else:
            return 'NO'

    return 'YES' if len(stack) == 0 else 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
