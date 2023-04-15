import  matplotlib.pyplot as plt 
import math 
f= open("erros.txt")
x=[]
y=[]
for i in range (72):
    x.append(i)
    y.append(math.log(float(f.readline())))

plt.plot(x,y)
plt.show()