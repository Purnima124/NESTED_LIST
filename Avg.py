marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
i=0
while i<len(marks):
    sum=0
    a=0
    s=0
    while a<len(marks[i]):
        s=s+(marks[i][a])
        a=a+1
    sum=sum+s
    b=sum//len(marks[i])
    i=i+1
    print("avg=",b)
