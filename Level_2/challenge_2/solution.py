input_1 = ([1, 2, 3, 4], 15)
input_2 = ([4, 3, 10, 2, 8], 12)

def solution(l, t):
  left, right = 0, 0
  mySum = l[0]
  
  while right < len(l):
    if mySum == t:
      return [left, right]
    elif mySum < t or left == right:
      right += 1
      if right == len(l):
        return [-1, -1]
      mySum += l[right]
    else:
      mySum -= l[left]
      left += 1

  return [-1, -1]

print(solution([4, 3, 10, 2, 8], 12))
print(solution([4], 4))
print(solution([1, 2, 3, 4], 15))