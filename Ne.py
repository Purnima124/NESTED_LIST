# Code likho jo iss list mein se maximum dhund kar ke print kare.
 
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 

# Iss list ke liye aapke program ka output 70 hona chaiye.
# ans:-
# num=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# i=0
# b=num[0]
# while i<len(num):   
#     if num[i]>b:
#         b=num[i]
#     i=i+1
# print(b)



marks=[78,76,94,86,88],[11,71,18,65,76],[15,45,78,52,40]
i=0
while i<len(marks):
    sum=0
    a=0
    s=0
    while a<len(marks[i]):
        s=s+marks[i][a]
        a=a+1
        sum=sum+s
        avg=sum//a
    i=i+1

print(marks,"avg","count")


# name=["a","n","a","t","n","a","x","u","g","a","x","a"]
# i=0
# n=[]
# while i<len(name):
#     b=0
#     count=0
#     a=[]
#     while b<len(name):
#         if name[i]==name[b]:
#             count=count+i
#         b=b+i
#     a.append(name)
#     a.append(name)
#     if a not in n:
#         n.append(a)
#     i=i+1            


