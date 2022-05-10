# a=[[1,2,3,4,5],[1,1,2,3,4,5,5],[1496,3]]
# i=0
# # sum=0
# while i<len(a):
#     j=0
#     # sum=0
#     k=a[i][j]
#     while j<len(a[i]):
#         if a[i][j]>k:
#             k=a[i][j]
#             # sum=sum+1
#         j=j+1
#     i=i+1
#     print(k)


# a=[[1,2,3,4,5],[1,1,2,3,4,5,5],[1496,3]]
# # i=0
# b=[0]
# i=0
# while i<len(a):
#     if a[i]>b:
#         b=a[i]
#     i=i+1
# print(b)    

a=[[2,5,6],[7,8,9],[12,16,11]]
i=0
sum=0
while i<len(a):
    j=0
    d=0
    while j<len(a[i]):
        d=d+a[i][j]
        j=j+1
    sum=sum+d
    i=i+1
print(sum)