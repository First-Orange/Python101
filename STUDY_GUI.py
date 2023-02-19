from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('600x400')

L1 = Label(GUI,text='ทดลองปุ่มทั้ง 3 แบบ',font=('Angsana New',30),fg='blue')
L1.place(x=180,y=20)
#################################################
def Button1():
    text = 'X111X'
    messagebox.showerror('ERROR',text)

FB1 = Frame(GUI)
FB1.place(x=250,y=80)
B1 = ttk.Button(FB1,text='ปุ่มที่1',command=Button1)
B1.pack(ipadx=10,ipady=10)

#################################################
def Button2():
    text = 'X222X'
    messagebox.showinfo('Information',text)

FB2 = Frame(GUI)
FB2.place(x=250,y=140)
B2 = ttk.Button(FB1,text='ปุ่มที่2',command=Button2)
B2.pack(ipadx=10,ipady=10)

#################################################
def Button3():
    text = 'X333X'
    messagebox.showwarning('Warning',text)

FB3 = Frame(GUI)
FB3.place(x=250,y=200)
B3 = ttk.Button(FB1,text='ปุ่มที่3',command=Button3)
B3.pack(ipadx=10,ipady=10)

#################################################
GUI.mainloop()
