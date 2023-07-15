username='Sreeja'
password='sreeja@2227'
c_name=input("enter your name:")
c_pass=str(input("enter your password:"))
if c_name==username and c_pass==password:
    print('1.deposit\n2.withdraw\n3.ministatement\n4.exit')
    amount=100000
    choice=int(input("enter your choice:"))
    if choice==1:
        dep=int(input("enter the amount:"))
        amount+=dep
        print("total amount:",amount)
    elif choice==2:
        withd=int(input("enter the amount:"))
        amount-=withd
        print("total amount:",amount)
    elif choice==3:
        print("-------ATM-----")
        print("username:",username)
        print("password:",password)
        print("total amount:",amount)
        print("thanks for visiting")
    else:
        exit
else:
    print("please enter correct details")
    
        
        
