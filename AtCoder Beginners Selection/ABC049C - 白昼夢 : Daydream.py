word = input()
 
word =word.replace("eraser", "X")
word = word.replace("erase", "X")
word = word.replace("dreamer", "X")
word = word.replace("dream", "X")
 
word =word.replace("X", "")
 
if word == "":
  print("YES")
else:
  print("NO")