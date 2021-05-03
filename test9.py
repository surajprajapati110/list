li=[23,4,5,34,67,1,2,3,8,9]
size=len(li)
for x in range (size):
    for y  in range (x+1,size):
        if li [x]>li[y]:
            t=li[y]
            li[y]=li[x]
            li[x]=t
print(li)
