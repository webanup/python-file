l=[]
while True:
    b=int(input('''
                1 enqueue element
                2 dequeue element
                3 rear
                4 front
                5 exit:-'''))
    if b==1:
        n=input("enter the value:-")
        l.append(n)
        print(l)
    if b==2:
        # n=input("enter the value:-")
        del l[-1]
        print(l)
    if b==3:
        
        print(l[0])
        print(l)
    if b==4:
        print(l[-1])
        print(l)
    if b==5:
        break;  