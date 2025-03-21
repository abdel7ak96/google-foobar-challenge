# Challenge 1: The cake is not a lie!
## Challenge description
Commander Lambda has had an incredibly successful week: the first test of the LAMBCHOP doomsday device was completed AND Lambda set a new personal high score in Tetris. To celebrate, the Commander ordered cake for everyone -- even the lowliest of minions! But competition among minions is fierce, and if you don't cut exactly equal slices of cake for everyone you'll get in big trouble.

The cake is round, and decorated with M&Ms in a circle around the edge. But while the rest of the cake is uniform, the M&Ms are not: there are multiple colors, and every minion must get exactly the same sequence of M&Ms. Commander Lambda hates waste and will not tolerate any leftovers, so you also want to make sure you can serve the entire cake.

To help you best cut the cake, you have turned the sequence of colors of the M&Ms on the cake into a string: each possible letter (between a and z) corresponds to a unique color, and the sequence of M&Ms is given clockwise (the decorations form a circle around the outer edge of the cake).

Write a function called solution(s) that, given a non-empty string less than 200 characters in length describing the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without leaving any leftovers.

### Languages

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

### Test cases

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

#### Python cases
```python
Input:
solution.solution("abccbaabccba")
Output:
    2

Input:
solution.solution("abcabcabcabc")
Output:
    4
```

#### Java cases
```java
Input:
Solution.solution("abccbaabccba")
Output:
    2

Input:
Solution.solution("abcabcabcabc")
Output:
    4
```

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.

## Solution
```python
input_1 = "abccbaabccba" # 2
input_2 = "abcabcabcabc" # 4
input_3 = "abcabcabcabcabcabcabcabc" # 8
input_4 = "aaaaaaa" #7
input_5 = "ababababab" #5

def Solution(s):
  for i in range(1, (len(s) / 2) + 1):
    if s[0:i] * (len(s) / i) == s:
      return len(s) / i
  return 1
  
print(Solution(input_5))
```

## Success screen
![Success screen](./Web%20capture_11-5-2023_43951_foobar.withgoogle.com.jpeg)