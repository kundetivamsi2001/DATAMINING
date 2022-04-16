import math
p1=[[1,3],[4,5],[6,8],[6,5]]
p2=[[8,9],[5,6],[3,6],[3,4]]
d=0
print("MANHATTEN DISTANCES ARE:")

for i in range(len(p1)):
               for j in range(len(p1[i])-1):
                              d=d+abs((p2[i][j]-p1[i][j])+(p2[i][j+1]-p1[i][j+1]))
                              print(d)
                              d=0

        
