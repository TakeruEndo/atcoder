f = int(input())

m = [500,100,50,10,5,1]
f = 1000 - f
ans_ = 0
for i in m:
  n = f // i
  ans_ += n
  f = f - n*i
  
print(ans_)

