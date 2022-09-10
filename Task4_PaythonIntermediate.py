




names=['mahmoud','farida','ali','hassan','mahmoud','khaled','taha']
transformedList=[]
for name in names:
    transformedList.append(name.upper())
    print(name)
print(transformedList)    
print('@'*30)
###################
listComprehension=[x.upper() for x in names]
print(listComprehension)
print('@'*30)
####################
def myUpper(text):
    return f'{text.upper()}'
for y in map(myUpper,names):
    print(y)
print(list(map(myUpper,names))) 
print('@'*30)
####################
for y in map(lambda text : f'{text.upper()}' , names):
    print(y)
  
print('#'*50)
#########################################################################
for name in names :
    if 'a' in name :
        print(name)
print('@'*30)
####################
def findA(nameWithA):
    return 'a'in nameWithA
x =list( filter(findA,names))
print(x)
print('@'*30)
####################
c=[name for name in names if 'a' in name ]
print(c)
print('#'*50)
#########################################################################
tList=[]
for x in names :
    if x.startswith('t'):
        print(x)
tList.append(x)    
print(tList)    
print('@'*30)
####################
tcomprehension=[x for x in names if x.startswith('t')  ]
print(tcomprehension)
print('@'*30)
####################
def myT(startswitht):
    return startswitht.startswith('t')
newTlist=filter(myT,names)
print(list(newTlist))   
print('@'*30)
####################
for v in filter(lambda startswitht : startswitht.startswith('t'),names ) :
    print(v)
print('#'*50)
#########################################################################
for name in names:
    if name.count('a')>=2:
        print(name)
print('@'*30)
####################
def find2A(name2A):
    return name2A.count('a')>= 2 
retuned2A=filter(find2A,names)   
print(list(retuned2A)) 
print('@'*30)
####################
e=[g for g in names if g.count('a')>=2 ]
print(e)
for g in filter(lambda name2A : name2A.count('a')>=2,names):
    print(g)
#########################################################################
a,*b =[5,6,9,4,3 ]
print(a)
print(b)
print('@'*30)

*a,b =[5,6,9,4,3 ]
print(a)
print(b)
print('@'*30)

a,b,*_ =[5,6,9,4,3 ]
print(a)
print(b)
