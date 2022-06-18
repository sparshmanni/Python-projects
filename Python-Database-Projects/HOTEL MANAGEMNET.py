
#program of  hotel management                  
print("_____****HOTEL DOWNHILL****_____")
import mysql.connector


def name():
    while True:
        print("\n")
        print("-------------------------------------------------------------")
        name = input("ENTER YOUR NAME:")
        a = name.isdigit()
        if len(name) != 0 and a != True:
            return name

            break
        else:
            print("your name is invalid please input a valid name")
            print(" ")

def addr():
    while True:
        address = input("ENTER YOUR ADDRESS:")
        a = address.isdigit()
        if len(address) != 0 and a != True:
            return address
            break

        else:
            print("please enter valid input ")
        print(" ")

def contact():
    while True:
        mobile_no = input("ENTER YOUR CONTACT NO.:")
        if mobile_no.isdigit() == True and len(mobile_no) != 0 and len(mobile_no) == 10:
            return mobile_no
            break
        else:
            print("please enter valid input  ")
        print(" ")

def day():
    while True:
        no_of_days = input("ENTER NO. OF DAYS GUEST WANT TO STAY:")
        a = no_of_days.isdigit()
        if a == True and len(no_of_days) != 0:
            return no_of_days
            break
        else:
            print("please enter valid input ")

def check_in():
    while True:
        dte=input("ENTER CHECK-IN (dd-mm-yyyy)")
        if len(dte)!=0 and len(dte)==10:
            return dte
            break
        else:
            print("please enter valid input ")

def check_out():
    while True:
        dte1=input("ENTER CHECK-OUT (dd-mm-yyyy)")
        if len(dte1)!=0 and len(dte1)==10:
            return dte1
            break
        else:
            print("please enter valid input ")
#types of room
def roominfo():
        global bill
        print("\n")
        print("Choose rooms for your own comfort")
        print("---------------------------------------------------------------") 
        print("1-Non-AC Single Bed Room.............Rs 2000")
        print("---------------------------------------------------------------") 
        print("2-AC Single Bed Room.................Rs 4000")
        print("---------------------------------------------------------------") 
        print("3-Non-AC Double Bed Room.............Rs 3000")
        print("---------------------------------------------------------------") 
        print("4-AC Double Bed Room.................Rs 6000")
        print("---------------------------------------------------------------") 
        print("5-Top view Bed Room..................Rs 15,000")
        print("---------------------------------------------------------------") 
        print("6-King size Room.....................Rs 10,000")
        print("---------------------------------------------------------------") 
        print("7-children room......................Rs 9000")
        print("---------------------------------------------------------------") 
        print("\n")
        pr=int(input("**Enter your preference please**: "))
        nights=int(input("For how many nights do you want to stay:"))
        if(pr==1):
            print("You've selected Non-AC Single Bed Room")
            p=2000*nights
        elif(pr==2):
            print("You've selected AC Single Bed Room")
            p=4000*nights
        elif(pr==3):
            print("You've selected Non-AC Double Bed Room")
            p=3000*nights
        elif(pr==4):
            print("You've selected AC Double Bed Room")
            p=6000*nights
        elif(pr==5):
            print("You've selected Top view Bed Room")
            p=15000*nights
        elif(pr==6):
            print("You've selected King size room")
            p=10000*nights
        elif(pr==7):
            print("You've selected children room")
            p=9000*nights
        else:
            print("Please select a room")
        print("Your room rent is=",p,"\n")
        bill += p
        
      



#hotel menu
def menu():
    global bill
    print("\n")
    print("-------------------------***HOTEL***-----------------------------")
    print("----------------------------MENU---------------------------------")
    print()
    print("1-water.....................................................RS 25")
    print("2-tea.......................................................RS 50")
    print("3-soft drink................................................RS 100")
    print("4-cold coffee...............................................RS 110")
    print("5-breakfast.................................................RS 250")
    print("6-lunch.....................................................RS 300")
    print("7-dinner....................................................RS 250")
    print("8-choclate sandwich.........................................RS 40")
    print("9-tripple layer sandwich....................................RS 80")
    print("10-watershots...............................................RS 30")
    print("11-oreo shake...............................................RS 100")
    print("12-Burger...................................................RS 49")
    print("13-choclate puding..........................................RS 150")
    print("14-ice cream................................................RS 90")
    print("15-red & white sauce pasta..................................RS 1300")
    print("16-dosa.....................................................RS 100")
    print("17-pizza....................................................RS 190")
    print("18-punjabithali.............................................RS 450")
    print("19-vegthali.................................................RS 400")
    print("20-brownie..................................................RS 60")
    print("21-cup cake.................................................RS 70")
    print("22-pie......................................................RS 100")
    print("23-salad....................................................RS 90")
    print("24-gym lover salad..........................................RS 150")
    print("25-cheese chilly............................................RS 350")
    print("26-champ....................................................RS 250")

            
    print("\n")        
    print("***If you want to have our delicious food then enter items***")
    menu=int(input("Enter your choice : "))
    if(menu==1):
        print("You have ordered water")
        a=int(input("enter number of bottles?? "))
        b=10*a
        print("Price of water bottles is: ",b)
    elif(menu==2):
        print("You have ordered tea")
        a=int(input("enter how many cups you want?? "))
        b=7*a
        print("Price of tea is: ",b)
    elif(menu==3):
        print("You have ordered Coca cola")
        a=int(input("enter how many bottles you want??(60ml) "))
        b=60*a
        print("Price of Coca cola is: ",b)
    elif(menu==4):
        print("You have ordered cold coffee")
        a=int(input("enter how many cups you want?? "))
        b=100*a
        print("Price of cold coffee is: ",b)
    elif(menu==5):
        print("You have ordered breakfast")
        a=int(input("enter how many times you have ordered it?? "))
        b=250*a
        print("Price of breakfast is: ",b)
    elif(menu==6):
        print("You have ordered lunch")
        a=int(input("enter how many times you have ordered it?? "))
        b=300*a
        print("Prive of lunch is: ",b)
    elif(menu==7):
        print("You have ordered dinner")
        a=int(input("enter how many times you have ordered it?? "))
        b=250*a
        print("Price of dinner is: ",b)
    elif(menu==8):
        print("You have ordered choclate sandwich")
        a=int(input("enter quantity?? "))
        b=20*a
        print("Price of choclate sandwich is: ",b)
    elif(menu==9):
        print("You have ordered tripple layer sandwich")
        a=int(input("enter quantity?? "))
        b=40*a
        print("Price of tripple layer sandwich is: ",b)
    elif(menu==10):
        print("You have ordered watershots")
        a=int(input("enter quantity?? "))
        b=30*a
        print("Price of watershots is: ",b)
    elif(menu==11):
        print("You have ordered oreo shake")
        a=int(input("enter quantity?? "))
        b=75*a
        print("Price of oreo shake is: ",b)
    elif(menu==12):
        print("You have ordered burger")
        a=int(input("enter quantity?? "))
        b=35*a
        print("Price of  burger is: ",b)
    elif(menu==13):
        print("You have ordered choclate puding")
        a=int(input("enter quantity?? "))
        b=20*a
        print("Price of choclate puding: ",b)
    elif(menu==14):
        print("You have ordered icecream")
        a=int(input("enter quantity?? "))
        b=60*a
        print("Price of icecream: ",b)
    elif(menu==15):
        print("You have ordered red & white sauce pasta ")
        a=int(input("enter quantity?? "))
        b=30*a
        print("Price of red & white sauce pasta is: ",b)
    elif(menu==16):
        print("you have ordered dosa")
        a=int(input("enter quantity?? "))
        b=100*a
        print("Price of dosa is: ",b)
    elif(menu==17):
        print("You have ordered pizza")
        a=int(input("enter quantity?? "))
        b=90*a
        print("Price of pizza is: ",b)
    elif(menu==18):
        print("You have ordered punjabi thali")
        a=int(input("enter quantity?? "))
        b=110*a
        print("Price of punjabi thali is: ",b)
    elif(menu==19):
        print("You have ordered veg thali")
        a=int(input("enter quantity?? "))
        b=150*a
        print("Price of veg thali is: ",b)
    elif(menu==20):
        print("You have ordered brownie")
        a=int(input("enter quantity?? "))
        b=30*a
        print("Price of brownie is: ",b)
    elif(menu==21):
        print("You have ordered cup cake")
        a=int(input("enter how many pieces you've ordered?? "))
        b=20*a
        print("Price of cup cake is: ",b)
    elif(menu==22):
        print("You have ordered pie")
        a=int(input("enter how many pieces you've ordered?? "))
        b=20*a
        print("Price of pie is: ",b)
    elif(menu==23):
        print("You have ordered salad")
        a=int(input("enter quantity?? "))
        b=20*a
        print("Price of salad is: ",b)
    elif(menu==21):
        print("You have ordered gym lover salad")
        a=int(input("enter quantity?? "))
        b=20*a
        print("Price of gym lover salad is: ",b)
    elif(menu==21):
        print("You have ordered cheese chilly")
        a=int(input("enter quantity?? "))
        b=20*a
        print("Price of cheese chilly is: ",b)
    elif(menu==21):
        print("You have ordered champ")
        a=int(input("enter quantity?? "))
        b=20*a
        print("Price of champ is: ",b)
    else:
        print("please choose a item")
   
    bill+=b

#billing
def billing():
    global bill
    print("\n\n --------------------------------")
    print("		 Hotel DOWNHILLS")
    print(" --------------------------------")
    print("			 Bill")
    print(" --------------------------------")
    print("         Total Amount : ",bill)
    print(" --------------------------------")
    print("		 Thank You")
    print("		 Visit Again :)")       
    print(" --------------------------------\n")   
    
    

def myhotel():
    mydb=mysql.connector.connect(host="localhost",password="",user="root",database="myhotel")
    cursor=mydb.cursor()
    print()
    print("Enter 1: FOR BOOKING: ")
    print("Enter 2: Room Info: ")
    print("Enter 3: To View Menu: ")
    print("Enter 4: Bill: ")
    print("Enter 5: to Exit ")
    print()
    pr=int(input("Enter your choice : "))
    if(pr==1):
        nme = name()
        address = addr()
        contact()
        dte = check_in()
        dte1 = check_out()
        cursor.execute("insert into customer_data values ('{}','{}','{}','{}')".format(nme,address,dte,dte1))
        mydb.commit()
    elif(pr==2):
        roominfo()
    elif(pr==3):
        menu()
    elif(pr==4):
        billing()
    elif(pr==5):
        print("Exiting the application")
        quit()
    else:
        print("please enter your preference")
    while(pr<9):
        myhotel()

        
bill=0
mydb=mysql.connector.connect(host="localhost",password="",user="root")
cursor=mydb.cursor()
cursor.execute("create database if not exists myhotel")
cursor.execute("use myhotel")
sql="create table if not exists customer_data(name varchar(30),address varchar(40),check_in_date date,check_out_date date)"
cursor.execute(sql)

sql1="create table if not exists room(roomno int(5),roomtype varchar(50),price int(5))"
cursor=mydb.cursor()
cursor.execute(sql1)
sql="create table if not exists resturentmenu(orderno int(5),item varchar(50),price int(5))"
cursor=mydb.cursor()
cursor.execute(sql)
mydb.commit()



myhotel()











