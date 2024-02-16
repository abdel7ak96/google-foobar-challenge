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