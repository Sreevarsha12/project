# sum of elements

n=[1,2,3,4,5]
print(sum(n))

# duplicate

a=[1,2,3,4,2,5,3,6,1]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i,end=' ')

# list is empty

a=[]
if not a:
    print("the list is empty")

# average

n=[2,4,5,6,8]
sum=sum(n)
avg=sum/len(n)
print("average is:")
print(avg) 

