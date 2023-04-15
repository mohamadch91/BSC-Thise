
#  open file
import random

f= open ("erros.txt","w")

for i in range (18):
    r=random.random()/100
    f.write(str((i*3/100)+r))
    f.write("\n")
for i in range (18):
    r=random.random()
    f.write(str((0.3+r)))
    f.write("\n")

for i in range (18):
    r=random.random()
    f.write(str((0.3+r)))
    f.write("\n")
    
for i in range (18):
    r=random.random()/100
    f.write(str((i*3/100)+r))
    f.write("\n")  