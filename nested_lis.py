max=[[4,3,5,2,1],[7,5,8,4,3],[10,9,20,5,3]]
i=0
while i<len(max):
    j=0
    k=max[i][j]
    while j <len(max[i]):
        if max[i][j]>k:
            k=max[i][j]
        j=j+1
    i=i+1
    print(k)

# max=[2,4,5],[4,5,6],[2,1,6],[4,8,9]
# i=0
# while i<len(max):
#     j=0
#     k=max[i][j]
#     while j <len(max[i]):
#         if max[i][j]>k:
#             k=max[i][j]
#         j=j+1
#     i=i+1
#     print(k)


# a=[12,14,86,87,88,91]
# n=[]
# i=0
# b=a[0]
# while i<len(a):
#     if a[i]>b :
#         k=a[-i]
#         n.append(k)
#     i=i+1
# print()
