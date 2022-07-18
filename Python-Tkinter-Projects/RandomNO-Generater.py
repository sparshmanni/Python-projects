from tkinter import *
import random


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    ## you can change the range by changing the value in below ##
    R=random.randint(1,500)
    if text=="Generate":
        scvalue.set(R)
        screen.update
    elif text=="EXIT":
        quit()
    else:
        scvalue.set("Button is'nt assigned!!")
        screen.update
        
      


root = Tk()
root.geometry("640x900")
root.title("Random no.Genrater by Sparsh")
sf=Frame(root,width=10,height=100)


main=Frame(root,highlightthickness=2,highlightbackground="blue")
scvalue = StringVar()
scvalue.set("")
screen = Entry(sf,textvar=scvalue,font="ROBOTO 40 bold")
screen.pack(fill=X,ipadx=5,pady=20,padx=250)
sf.pack(padx=5,pady=150)


f=Frame(root)


b=Button(f,text="_",padx=15,pady=10,font="ludida 35 bold",background="grey")
b.bind("<Button-1>",click)
b.pack(side="left",padx=5,pady=5)

b=Button(f,text="Generate",padx=15,pady=10,font="ludida 35 bold",)
b.bind("<Button-1>",click)
b.pack(side="left",padx=5,pady=5)

b=Button(f,text="EXIT",padx=15,pady=10,font="ludida 35 bold",background="red")
b.bind("<Button-1>",click)
b.pack(side="left",padx=5,pady=5)
f.pack()
main.pack()


f.pack()
main.pack()
