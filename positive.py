list1=[]
n=int(input("print no of elem in list"))
i=0
while i<n:
    ele=int(input())
    list1.append(ele)
    i=i+1
print("input:list1=",list1)
print("output:")
for i in list1:
    if i>0:
        print(i)
