#convert list to set
l=[1,2,3,4,5,6]
s=set(l)
print(s)

#add
s={1,2,3,4,5}
s.add(45)
print(s)
print()
#pop
s={2,34,5,6,7}
print(s.pop())
print(s)
print()
# #remove
s={2,34,5,6,7}
s.remove(2)
print(s)
print()
# #clear
s={2,34,5,6,7}
s.clear()
print(s)
print()
# #discard
s={2,34,5,6,7}
s.discard(5)
print(s)
print()
#update
s={2,34,5,6,7}
l=[32,33,45]
s.update(l)
print(s) 