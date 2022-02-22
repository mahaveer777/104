import csv
with open("data.csv") as f:
  reader=csv.reader(f)
  filedata=list(reader)
filedata.pop(0)
newdata=[]
for x in range(len(filedata)):
  weight=filedata[x][2]
  newdata.append(float(weight))
print(newdata)  
total=0
for y in newdata:
  total=total+y
print(total)  
meandata=total/len(newdata)
print("mean--->"+str(meandata))
