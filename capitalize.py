sample="how are you"
print(sample.split())
l=[]
for i in sample.split():
    #print(i.capitalize())
    l.append(i.capitalize())
    #print(l)
print(" ".join(l))

