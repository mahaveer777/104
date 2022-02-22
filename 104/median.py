import csv
with open("data.csv") as f:
  reader=csv.reader(f)
  filedata=list(reader)
filedata.pop(0)
newdata=[]
for x in range(len(filedata)):
  weight=filedata[x][2]
  newdata.append(float(weight))
total=0
newdata.sort()
print(newdata) 
n=len(newdata)
if(n%2==0):
  median1=float(newdata[n//2])
  median2=float(newdata[n//2 - 1 ])
  median=(median1+median2)/2
else:
  median=float(newdata[n//2])  
print("median--->"+str(median))  