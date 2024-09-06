from tkinter import *
from tkinter import messagebox
import random
import json
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

def generate():
 l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 n=['1','2','3','4','5','6','7','8','9','10']
 s=['@','$','%','&','#','^']
 password=[]
 n1=random.randint(8,10)
 n2=random.randint(2,4)
 n3=random.randint(2,4)
 new=[random.choice(l) for _ in range(n1)]
 new2=[random.choice(n) for _ in range(n2)]
 new3=[random.choice(s) for _ in range(n3)]
 password=new+new2+new3
 random.shuffle(password)
 ch="".join(password)
 p.insert(0,ch)

 
def save():
    data={web.get():{"email":e.get(),"password":p.get()}}
    if len(web.get())==0 or len(e.get())==0:
      messagebox.showerror(title="Error",message="Please fill all the fields")
    else:
      try:  
       file = open("data.json", "r")
       d=json.load(file)
      except: 
       file=open("data.json","w")
       json.dump(data,file,indent=4)
      else:
        d.update(data)
        file=open("data.json","w")
        json.dump(d,file,indent=4)
      finally: 
       web.delete(0,END)
       p.delete(0,END)
   
def find_password():
    website=web.get()
    file=open("data.json")
    d=json.load(file)
    if website in d:
      email=d[web.get()]["email"]
      password=d[web.get()]["password"]
      messagebox.showinfo(title="data",message=f"Email:{email} \nPassword:{password}")
    else:
      messagebox.showerror(title="Error",message="No data found")

window=Tk()
window.config(padx=20,pady=20)
window.title("Password Manager")
c=Canvas(width=200,height=200)
img=PhotoImage(file="logo.png")
c.create_image(100,100,image=img)
c.grid(column=1,row=0)
wesite=Label(text="Website:",font=(FONT_NAME,20,"bold"))
wesite.grid(column=0,row=1)
web=Entry(width=35)
web.grid(column=1,row=1)
email=Label(text="Email/Username:",font=(FONT_NAME,20,"bold"))
email.grid(column=0,row=2)
e=Entry(width=35)
e.insert(0,"abc@gmail.com")
e.grid(column=1,row=2)
password=Label(text="Password:",font=(FONT_NAME,20,"bold"))
password.grid(column=0,row=3)
p=Entry(width=25)
p.grid(column=1,row=3)
b=Button(text="generate password",command=generate)
b.grid(column=2,row=3)
b=Button(text="search",command=find_password)
b.grid(column=2,row=1)
add=Button(text="ADD",width=20,command=save)
add.grid(column=1,row=4)
window.mainloop()