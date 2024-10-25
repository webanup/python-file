#delete
l=[10,20,30,40,50,60]
del l[1]
print(l)

print()

#pop
l=[10,20,30,40,50,60]
l.pop(4)
print(l)
print()

#remove
l=[10,20,30,40,50,60]
l.remove(30)
print(l)
print()

#clear
l=[10,20,30,40,50,60]
l.clear()
print(l)
print()

#update
l=[10,20,30,40,50,60]
l[0]=34
print(l)
print()
#append
l=[10,20,30,40,50,60]
n=[12,2,34]
l.append(n)
print(l)
#extend
l=[10,20,30,40,50,60]
n=[12,12,12,12]
l.extend(n)
print(l)
print()

#count
l=[10,20,30,40,50,60,10]
a=l.count(10)
print(a)
print()
#max

l=[10,20,30,40,50,60]
a=max(l)
print(a)

#min
l=[10,20,30,40,50,60]
a=min(l)
print(a)
print()
    
#sort
l=[10,20,30,40,50,60,34,31]
l.sort()
print(l)
print()

#reverse
l=[10,20,30,40,50,60]
l.reverse()
print(l)
print()
#index

l=[10,20,30,40,50,60]
l.index(30)
print(l)
