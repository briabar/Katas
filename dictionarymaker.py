def func(n,m):
  dictionary = {}
  for i in range(0,len(n)):
    dictionary[n[i]] = m[i]
  return dictionary

n = ["alice", "Bob"]
m = [20, 45]

print(func(n,m))
