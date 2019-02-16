n = [19,12,18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i = 0
while i < len(n):
  j = i+1
  while j < len(n):
    if n[i] == n[j]:
      del(n[j])
    j=j+1
  i = i+1
print n
