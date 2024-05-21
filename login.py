from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import*
import sqlite3
from tkinter import messagebox
import os
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        #self.root.focus_force()
        #===================BG COLOR===============================
        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl=Label(self.root,bg="#031F3C",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,width=1)
        #======================Frames==============================
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)


        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="EMAIL ADDRESS",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=350,height=35)
        

        pass_=Label(login_frame,text="PASSWORD",font=("times new roman",18,"bold"),bg="white",fg="gray").place(x=250,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=250,y=280,width=350,height=35)

        btn_reg=Button(login_frame,cursor="hand2",command=self.register_window,text="Register new Account",font=("times new roman",14),bg="white",bd=0,fg="#800857").place(x=250,y=320)

        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roman",20,"bold"),fg="white",bg="#800857",cursor="hand2").place(x=250,y=380,width=180,height=40)

        
        #=====================Clock================================
        #self.lbl=Label(self.root,bg="white",bd=0)
        #self.lbl.place(x=90,y=120,height=450,width=350)
    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to {str(es)}",parent=self.root)

        

if __name__=="__main__":
    root=Tk()
    obj=Login_window(root)
    root.mainloop()