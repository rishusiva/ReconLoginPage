#importing the necessary modules
from tkinter import *
#from tkinter.ttk import *
from functools import partial

#declaring a function to validate login
def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	lbl = Label(tkWindow, text="Welcome!", font=("Arial",12,"bold"),bg="black",fg="green").pack()
	return

#intiializing the window
tkWindow = Tk()  
tkWindow.geometry('400x170')  
tkWindow.resizable(width=False,height=False)
tkWindow.configure(bg="black")
tkWindow.title('Recon Subsea Login Page')

TitleLabel = Label(tkWindow,text="Welcome to Recon Subsea Login Page!",font=("Segoe UI",14,"bold"),bg="black", fg="white").pack()

usernameLabel = Label(tkWindow, text="User Name",font=("Arial",10),bg="black", fg="white").pack()
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).pack()  

passwordLabel = Label(tkWindow,text="Password",font=("Arial",10),bg="black", fg="white").pack() 
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').pack()

validateLogin = partial(validateLogin, username, password)

loginButton = Button(tkWindow,text="Login", font=("Arial",13,"bold"),bg="green",fg="white", relief = RAISED, bd=6,command=validateLogin)
loginButton.pack()
tkWindow.iconbitmap('reconlogo.ico') 

tkWindow.mainloop()
