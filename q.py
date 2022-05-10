# a=[1,2,3,4,5,6]
# b=[2,3,1,0,6,7]
# y=[]
# i=0
# while i<len(a):
    # k=a[i]
    # if k not in b:
        # y.append(k)
    # i=i+1
# print(y)
# 

a=[-1,-2,-3,-4,-5,0]
i=0
n=a[i]
while i<len(a):
    if a[i]>n:
        n=a[i]
    i=i+1
print(n)

