# function(add 2 numbers)

def add(a,b):
    return(a+b)
x=int(input("enter first number"))
y=int(input("enter second number"))
print(add(x,y))

#small anonymous fn

x=lambda a,b:a+b
print(x(4,3))

#exception handling

try:
  a=8
  b=0
  print(a/b)
except:
  print("division error")
finally:
  print("i am finally")

#file handling

file=open("new.txt",'w')
content=file.write("new file")
print(content)
file.close()