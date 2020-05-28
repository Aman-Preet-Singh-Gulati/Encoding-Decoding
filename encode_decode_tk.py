from tkinter import *
import tkinter.messagebox
import random
import time
import datetime


root = Tk()
root.geometry("950x520")
root.title(" CRYPTOcharm  (Encoding/decoding)")
icon = PhotoImage(file="cyber.png")
root.tk.call('wm','iconphoto',root._w, icon)
root.configure(background="black")


menubar = Menu(root)
root.config(menu=menubar)
subMenu = Menu(menubar,tearoff = 0)



def about_us():
    tkinter.messagebox.showinfo('About CryptoCHARM ','This is a application for encoding and decoding THE MESSAGE  \n\n Follow the steps to operate with this application EFFECTIVELY!\n\n1. Enter the MESSAGE which is to be encoded or decoded\n2. Enter the SECRET KEY\n3. Enter E for encoding message or D for decoding message in small alphabets\n4. Then click on OUTPUT BUTTON ,your result will be shown in result entry block ')

subMenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label="Help",menu=subMenu)
subMenu.add_command(label="About this app",command = about_us)



status = Label(root,text="Welcome to CRYPTOCHARM....",bd=1,relief=SUNKEN,anchor='w')
status.pack(side=BOTTOM,fill=X)



tops = Frame(root,width=1600, relief= SUNKEN,bg="black")
tops.pack(side=TOP)

f1= Frame(root, width=800,height=700, relief=SUNKEN,bg="black")
f1.pack(side=LEFT)

localtime= time.asctime(time.localtime(time.time()))


lblinfo = Label(tops, font=('arial black',40,'bold'), text="CryptoCHARM",fg="white",bd=10,anchor='w',bg="black")
lblinfo.grid(row=0, column=0)

lblinfo = Label(tops, font=('arial',20,'bold'),text=localtime,fg= "white",bd= 10,anchor='w',bg="black")
lblinfo.grid(row=1,column=0)

rand = StringVar()
msg = StringVar()
key = StringVar()
mode = StringVar()
result = StringVar()


def qExit():
    root.destroy()

def reset():
    rand.set("")
    msg.set("")
    key.set("")
    mode.set("")
    result.set("")



lblmsg = Label(f1, font=('arial',16,'bold'),text="Message :",bd=16, anchor='w',fg="white",bg="black")
lblmsg.grid(row=0,column=0)
txtmsg = Entry(f1,font=('arial',16,'bold'),textvariable= msg, bd=10, insertwidth= 4, bg="powder blue",justify='right')
txtmsg.grid(row=0,column=1)

lblkey =Label(f1, font=('arial',16,'bold'),text="Key :",bd=16,anchor='w',fg="white",bg="black")
lblkey.grid(row=1,column=0)

txtkey = Entry(f1, font=('arial',16,'bold'),textvariable= key,bd= 10, insertwidth =4, bg="powder blue",justify='right')
txtkey.grid(row=1,column=1)

lblmode = Label(f1, font=('arial',16,'bold'),text="Mode (e/d) :", bd=16, anchor='w',fg="white",bg="black")
lblmode.grid(row=0,column=2)

txtmode = Entry(f1, font=('arial',16,'bold'),textvariable= mode,bd= 10,insertwidth= 4,bg="powder blue",justify='right')
txtmode.grid(row=0,column=3)

lblservice = Label(f1, font=('arial',16,'bold'),text="Result :",bd= 16, anchor='w',pady=10,fg="white",bg="black")
lblservice.grid(row=1,column=2)

txtservice = Entry(f1,font= ('arial',16,'bold'),textvariable= result,bd= 10,insertwidth= 4,bg="powder blue",justify='right')
txtservice.grid(row=1,column=3)


import base64

def encode(key, clear):
    enc =[]
    for i in range(len(clear)):
        key_c= key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c))% 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
    status['text'] = "Message has been encoded !"

def decode(key,enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c= key[i % len(key)]
        dec_c = chr((256 + ord(enc[i])- ord(key_c)) % 256)
        dec.append(dec_c)
    return  "".join(dec)
    status ['text'] = "Message has been decoded !"

def ref():
    print('Message =',(msg.get()))
    clear = msg.get()
    k= key.get()
    m= mode.get()

    if (m=='e'):
        result.set(encode(k, clear))
    else:
        result.set(decode(k, clear))


btntotal = Button(f1,padx=16, pady=8, bd= 16, fg="white", font=('arial',16,'bold'),width=10,text="Output",bg="blue",command=ref).grid(row=11,column=1)

btnreset = Button(f1,padx=16, pady=8, bd= 16, fg="white", font=('arial',16,'bold'),width=10,text="Reset",bg="green",command=reset).grid(row=11,column=2)

btnexit = Button(f1,padx=16, pady=8, bd= 16, fg="white", font=('arial',16,'bold'),width=10,text="Exit",bg="red",command=qExit).grid(row=11,column=3)




root.mainloop()
