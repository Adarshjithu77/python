import mysql.connector

con =mysql.connector.connect(
    host="localhost",
    user="jithu",
    password="jithu123",
    port=3306,
    database="jithu"
)

cur =con.cursor()
con.autocommit =True

cur.execute("create table User(user text,password text)")


import tkinter

win = tkinter.Tk()
win.title("synnefo")
win.geometry("500x500")
win.minsize(500,500)
win.maxsize(500,500)
win.configure(bg="black")

def Login():
    user = entry1.get()
    password = entry2.get()
    print(user)
    print(password)
def Register():
    user = entry1.get()
    password = entry2.get()
    print(user)
    print(password)
label1 = tkinter.Label(win,text="Username",bg="black",fg="white")
# label1.pack()#centre akn vndi
label1.place(x=100,y=45)#crct position place chyn vndi
# label1.grid(row=5,column=0)#rows columns vech kodkn vndi

entry1 = tkinter.Entry(win)
entry1.place(x=200,y=45)

label2 = tkinter.Label(win,text="Password",bg="black",fg="white")
label2.place(x=100,y=100)

entry2 = tkinter.Entry(win)
entry2.place(x=200,y=100)

btn = tkinter.Button(win,text="Login",bg="black",fg="white",activebackground="black",activeforeground="white",padx=20,pady=10,command=Login)
btn.place(x=150,y=150)

btn1= tkinter.Button(win,text="Register",bg="black",fg="white",activebackground="black",activeforeground="white",padx=20,pady=10,command=Register)
btn1.place(x=250,y=150)

win.mainloop()