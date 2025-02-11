def sum(n):
  return n*(n+1)/2

#space complexity = 1

def arraysum(a):
  sum = 0
  for i in a:
    sum = sum + i
  return (sum)

a = [12,3,4,5]
arraysum(a)

#space complexity = n
# with the array the space will also increase
