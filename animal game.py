import random
l=["snake","dog","ant"]
'''
snake vs dog -> dog win
snake vs ant -> snake win 
ant vs dog -> ant win
'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''game start
                          1 yes
                          2 no|exit
                          
                          '''))  
    if uc == 1:
        
        for a in range(1,6):
            userinput=int(input('''
                                1 snake
                                2 dog
                                3 ant
                                '''))
            if userinput==1:
                uchoice="snack"
            elif userinput==2:
                uchoice="dog"
            elif userinput==3:
                uchoice="ant"
            cchoice=random.choice(l)
            print(uchoice)
            print(cchoice)
            
            if cchoice==uchoice:
                print("computer value",cchoice)
                print("user value",uchoice)
                print("game draw") 
                ucount=ucount+1
                ccount=ccount+1
                 
       
            
        ucount=ucount+1
        ccount=ccount+1
    elif uchoice==("snake"and cchoice=="dog")or(uchoice=="ant"and cchoice=="snake")or(uchoice=="dog"and cchoice=="ant"):
        print("you win")
        print("computer value",cchoice)
        print("user value",cchoice)
        ucount=ucount+1
        
    else:
        print("computer win")
        print("computer value",cchoice)
        print("user value",cchoice)
        ccount=ccount+1
        
    if ucount==ccount:
        print("game draw")
        print("user score",ucount)
        print("computer score,ccount")
        
    elif ucount>ccount:
        print("you win")
        print("user score",ucount)
        print("computer score",ccount)
    
    else:
         print("computer win")
         print("user score",ucount)
         print("computer score",ccount)
         
                        
        
            
           
            
                            