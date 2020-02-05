from tkinter import *
import time
def times():
  current_time=time.strftime("%H:%M:%S")
  clock.config(text=current_time)
  clock.after(1000,times)
root=Tk()
root.geometry("500x250")
clock=Label(root,font="time 50 bold",bg="orange")
clock.grid(row=2,column=2,pady=25,padx=100)
times()

heading=Label(root,text="DIGITAL CLOCK",font="times 26 bold",fg="red",bg="black")
heading.grid(row=0,column=2)
root.config(bg="black")

nota=Label(root,text=" hours   minutes   seconds   ",font="times 15 bold",fg="white",bg="black")
nota.grid(row=3,column=2)



root.mainloop()
