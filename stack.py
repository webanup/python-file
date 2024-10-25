l=[]
while True:
    b=int(input('''
                1 push element
                2 pop element
                3 peek element
                4 display stack
                5 exit:-'''))
    if b==1:
        n=input("enter the value:-")
        l.append(n)
        print(l)
    if b==2:
        # n=input("enter the value:-")
        p=l.pop()
        print(p)
        print(l)
    if b==3:
        q=l[-1]
        print(q)
        print(l)
    if b==4:
        print(l)
      
    if b==5:
        break;        
            
          
        