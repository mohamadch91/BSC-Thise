
#  open file
import random


for j in range(1,2981):
    f= open ("errors//"+str(j)+".txt","w")
    for i in range (35):
        r=random.random()/100
        f.write(str((i*3/100)+r))
        f.write("\n")
    for i in range (35):
        r=random.random()
        f.write(str((0.1+r)))
        f.write("\n")
    for i in range (35):
        r=random.random()/100
        f.write(str((i*3/100)+r))
        f.write("\n")  
    for i in range (35):
        r=random.random()
        f.write(str((0.3+r)))
        f.write("\n")
        
  