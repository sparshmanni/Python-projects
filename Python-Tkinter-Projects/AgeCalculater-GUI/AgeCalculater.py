import datetime
import tkinter as tk
from PIL import Image,ImageTk
 
window=tk.Tk()
window.title("Age_Cal_App")
 
name = tk.Label(text = "Name")
name.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
month = tk.Label(text = "Month")
month.grid(column=0,row=3)
date = tk.Label(text = "Day")
date.grid(column=0,row=4)
 
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)
 
def getInput():
    name=nameEntry.get()
    monkey = Person(name, datetime.date(int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())))
     
    textArea = tk.Text(master=window,height=10,width=25)
    textArea.grid(column=1,row=6)
    answer = " Heyy {monkey}!!!. You are {age} years old!!! ".format(monkey=name, age=monkey.age())
    textArea.insert(tk.END,answer)
 
button=tk.Button(window,text="Calculate Age",command=getInput,bg="pink")
button.grid(column=1,row=5)
 
class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
     
from PIL import Image,ImageTk  #import the PIL library to our code
image = Image.open('app_image.png' )     #specify the path of the image
image.thumbnail((200,200),Image.ANTIALIAS)    #100,100 is the resolution
#ANTIALIAS helps to deal some problems while using images
photo= ImageTk.PhotoImage(image)   #converts the image to a tkinter image
label_image= tk.Label(image=photo)  #stores the image in a label
label_image.grid(column=1,row=0)    #Puts it in a grid
 
window.mainloop()
