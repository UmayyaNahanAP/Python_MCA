d1={0:1,1:2,2:3}
d2={3:4,4:5}
d={}
print("Dictionary 1 :")
print(d1)
print("Dictionary 2 :")
print(d2)
print("New dictionary after concatination :")
for i in(d1,d2):
    d.update(i)
print(d)
