

def fn(v: int) -> int:
  denom = [100, 50, 10, 5, 1]
  res = {}
  for d in denom:
    res[d] = v // d
    v = v % d

  return res


print(fn(125))