f = open("gt.txt","r")
lines = f.readlines()

newfile = open("corrected_gt.txt","w")
counter =0
array=[]
print(lines[0])
for i in range(len(lines)):
    x,y= lines[i].split(" ")
    x,y= float(x),float(y)
    array.append([x,y])
    if(counter%4 == 3):
        print(array)
        sum_x=0
        sum_y=0
        for j in array:
            sum_x+=j[0]
            sum_y+=j[1]
        
        newfile.write(str(sum_x/4)+" "+str(sum_y/4)+"\n")
        print(sum_x/4)
        array=[]
        
    counter+=1
        
        
        