from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repos=0
time=None

   


window=Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50,bg=YELLOW)


def timer(count):
    min=math.floor(count/60)
    sec=count%60
    if sec<10:
       sec=f"0{sec}"
    c.itemconfig(change,text=f"{min}:{sec}")
    if count>0:
     global time
     time=window.after(1000,timer,count-1)
    else:
      timer_start()
def timer_start():    
   global repos
   repos+=1
   if repos==1 or repos==3 or repos==5 or repos==7:
    timer(WORK_MIN*60)
    l.config(text="WORK",fg=GREEN)
   elif repos==2 or repos==4 or repos==6:
     timer(SHORT_BREAK_MIN*60)
     l.config(text="BREAK",fg=PINK)
   else:
     timer(LONG_BREAK_MIN*60)
     l.config(text="BREAK",fg=RED)
def reset_timer():
    window.after_cancel(time)  
    l.config(text="Timer",fg=GREEN)  
    c.itemconfig(change,text="00:00")
    global repos
    repos=0       
t="✔"
l=Label(text="Timer",fg=GREEN,font=(FONT_NAME,35),bg=YELLOW)
l.grid(column=1,row=0,)
l2=Label(text=t,fg=GREEN,bg=YELLOW)
l2.grid(column=1,row=4)
c=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
t=PhotoImage(file="tomato.png")
c.create_image(100,112,image=t)
L3=Button(text="Start",bg=YELLOW,command=timer_start)
L3.grid(column=0,row=4)
l4=Button(text="reset",bg=YELLOW,command=reset_timer)
l4.grid(column=2,row=4)
change=c.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
c.grid(column=1,row=1)
window.mainloop()