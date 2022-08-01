from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1700x900+0+0")
        

    #=================variable========================
        self.var_email=StringVar()
        self.var_pass=StringVar()

        # background image
        bg = Image.open(r"images\bg.webp")
        bg= bg.resize((1550, 800), Image.ANTIALIAS)
        self.photobg = ImageTk.PhotoImage(bg)

        bg_lbl = Label(self.root, image=self.photobg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

         # frame
        frame = Frame(bg_lbl, bd=2, bg="black")
        frame.place(x=580, y=170, width=400, height=550)

        #login image
        img1 = Image.open(r"images\login.webp")
        img1= img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(self.root, image=self.photoimage1,bg="black",borderwidth=0)
        lbl_img1.place(x=735, y=180, width=100, height=100)

        # title
        get_str = Label(frame, text="Get Started", font=("Times new roman", 20,"bold"), fg="white",bg="black")
        get_str.place(x=135, y=110)

        #username
        username = Label(frame, text="Username", font=("Times new roman", 15,"bold"), fg="white",bg="black")
        username.place(x=100, y=175)

        #username_txt
        self.txt_user= ttk.Entry(frame,textvariable=self.var_email, font=("arial", 12, "bold"))
        self.txt_user.place(x=60,y=200,width=270)

         #passowrd
        passsword = Label(frame, text="Password", font=("Times new roman", 15,"bold"), fg="white",bg="black")
        passsword.place(x=100, y=250)

        #password txt
        self.txt_password= ttk.Entry(frame,textvariable=self.var_pass, font=("arial", 12, "bold"),show="*")
        self.txt_password.place(x=60,y=275,width=270)

        #=======================icon images=====================

        #userimage
        img2 = Image.open(r"images\user.webp")
        img2= img2.resize((30,30), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(self.root, image=self.photoimage2,bg="black",borderwidth=0)
        lbl_img2.place(x=650, y=342, width=30, height=30)

        #password icon
        img3 = Image.open(r"images\password.webp")
        img3= img3.resize((30,30), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(self.root, image=self.photoimage3,bg="black",borderwidth=0)
        lbl_img3.place(x=650, y=418, width=30, height=30)

        #=================================Login button=======================
        login_btn =Button(frame,command=self.login, text="LogIn", font=("arial", 15, "bold"),bd=3,relief=RIDGE,bg="Red", fg="white",activebackground="red",activeforeground="white",cursor="hand2")
        login_btn.place(x=145, y=350,width=120,height=35)

         #=================================Register button=======================
        register_btn =Button(frame,command=self.register_window,text="New User Registration", font=("arial", 10, "bold"),borderwidth=0,bg="black", fg="white",activebackground="black",cursor="hand2")
        register_btn.place(x=35, y=420,width=140)

        #=================================forget password button=======================
        forget_btn =Button(frame,command=self.forgot_password_window,text="Forget Password", font=("arial", 10, "bold"),borderwidth=0,bg="black", fg="white",activebackground="black",cursor="hand2")
        forget_btn.place(x=18, y=450,width=140)

    #=====================register window defination========================
    def register_window(self):
        self.register_window=Toplevel(self.root)
        self.app=Register(self.register_window)

    def login(self):
        if self.txt_user.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","Field can't be left empty")
        elif self.txt_user.get()=="prajjal" or self.txt_password.get()=="Admin@123":
            messagebox.showinfo("Success","Welcome to Admin Panel")

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Admin@123", database="registration")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                self.var_email.get(),
                                                                self.var_pass.get()
                     ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Credentials, Try again!!!")
            else:
                open_main=messagebox.askyesno("Message","Do you want to continue")
                if open_main>0:
                    self.Student_window=Toplevel(self.root)
                    self.app=Student(self.Student_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

#==========================================reset password function====================
    def reset_pass(self):
        if self.Security_Ques.get()=="Select":
            messagebox.showerror("Error","Please Select an Option",parent=self.root2)
        elif self.Security_Ans.get()=="":
            messagebox.showerror("Error","Please Enter the Answer to Change Password",parent=self.root2)
        elif self.new_pass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password to proceed futher",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Admin@123", database="registration")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and securityQ=%s and securityA=%s",(
                                                                self.var_email.get(),#username
                                                                self.Security_Ques.get(),
                                                                self.Security_Ans.get()
                     ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Credentials",parent=self.root2)
            else:
                my_cursor.execute("update register set password=%s where email=%s",(
                                                            self.new_pass.get(),
                                                            self.var_email.get(),
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Password Changed Successfully, Please login",parent=self.root2)
                self.root2.destroy()





    def forgot_password_window(self):
        if self.txt_user.get()=="":
            messagebox.showerror("Error","Please Enter the User Name to reset password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Admin@123", database="registration")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from register where email=%s",
                                                      (self.txt_user.get(),
                ))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Enter the Valid User Name")
                else:
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("435x550+550+170")

                     # frame
                    frame = Frame(self.root2, bd=2, bg="black")
                    frame.place(x=0, y=0, width=435, height=550)

                    #password reset login image
                    root2_img1 = Image.open(r"images\login.webp")
                    root2_img1=root2_img1.resize((100, 100), Image.ANTIALIAS)
                    self.root2_photoimage1 = ImageTk.PhotoImage(root2_img1)

                    root2_img1 = Label(self.root2, image=self.root2_photoimage1 ,bg="black",borderwidth=0)
                    root2_img1.place(x=155, y=10, width=100, height=100)
                    
                    #password reset label
                    l = Label(frame,text="Forget Password",font=("arial",20,"bold"),fg="red",bg="black",borderwidth=0)
                    l.place(x=0, y=120, relwidth=1)

                    #Select Security_Ques label entry
                    Security_Ques = Label(frame, text="Select Security Ques", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
                    Security_Ques.place(x=95, y=170)

                    #Select Security Ques entry field
                    self.Security_Ques = ttk.Combobox(frame,font=("arial", 12, "bold"), width=17, state="readonly")
                    self.Security_Ques["value"] = ("Select", "Your pet name","Favourite Book", "Favourite Place", "Nick name", "Person Close to you")
                    self.Security_Ques.current(0)
                    self.Security_Ques.place(x=95,y=210,width=250)
                
                    #Security_Ans label entry
                    Security_Ans = Label(frame, text="Security Answer",font=("Times new roman", 20,"bold"), fg="orange",bg="black")
                    Security_Ans.place(x=95, y=250)

                    #Security Answerentry field
                    self.Security_Ans= ttk.Entry(frame, font=("arial", 20, "bold"))
                    self.Security_Ans.place(x=95,y=290,width=250)
                    
                    #New PassWord label entry
                    new_pass = Label(frame, text="New Password",font=("Times new roman", 20,"bold"), fg="orange",bg="black")
                    new_pass.place(x=95, y=335)

                    #New PassWord entry field
                    self.new_pass= ttk.Entry(frame, font=("arial", 20, "bold"),show="*")
                    self.new_pass.place(x=95,y=370,width=250)

                    #=================================reset button=======================
                    reset = Button(frame,command=self.reset_pass,text="Reset", font=("arial", 15, "bold"),bd=3,relief=RIDGE,bg="Green", fg="white",activebackground="red",activeforeground="white",cursor="hand2")
                    reset.place(x=150, y=450,width=120,height=35)

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1700x900+0+0")

        #=====================Variables=======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()

        # background image
        bg = Image.open(r"images\bg.webp")
        bg= bg.resize((1550, 800), Image.ANTIALIAS)
        self.photobg = ImageTk.PhotoImage(bg)

        bg_lbl = Label(self.root, image=self.photobg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #===================left image============================
        img1 = Image.open(r"images\reg.jpg")
        img1= img1.resize((460, 550), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(self.root, image=self.photoimg1)
        lbl_img1.place(x=50, y=102, width=460, height=550)

        #main frame
        frame = Frame(bg_lbl, bd=2, bg="black")
        frame.place(x=505, y=100, width=800, height=550)

        #register label
        register_lbl = Label(frame, text="Register Here", font=("Times new roman", 20,"bold"), fg="white",bg="black")
        register_lbl.place(x=350, y=20)

        #first name label entry
        fname = Label(frame, text="First Name", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
        fname.place(x=50, y=100)

        #firstname entry field
        self.fname_entry= ttk.Entry(frame,textvariable=self.var_fname, font=("arial", 20, "bold"))
        self.fname_entry.place(x=50,y=135,width=250)

        #last name label entry
        lname = Label(frame, text="Last Name", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
        lname.place(x=450, y=100)

        #last name entry field
        self.lname_entry= ttk.Entry(frame,textvariable=self.var_lname, font=("arial", 20, "bold"))
        self.lname_entry.place(x=450,y=135,width=250)


        #contact label entry
        contact = Label(frame, text="Contact No", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
        contact.place(x=50, y=180)

        #contact entry field
        self.contact_entry= ttk.Entry(frame,textvariable=self.var_contact, font=("arial", 20, "bold"))
        self.contact_entry.place(x=50,y=215,width=250)

        #email label entry
        email = Label(frame, text="Email", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
        email.place(x=450, y=180)

        #email entry field
        self.email_entry= ttk.Entry(frame,textvariable=self.var_email, font=("arial", 20, "bold"))
        self.email_entry.place(x=450,y=215,width=250)

        #password label entry
        password = Label(frame, text="Password", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
        password.place(x=50, y=255)

        #password entry field
        self.password_entry= ttk.Entry(frame,textvariable=self.var_pass, font=("arial", 20, "bold"),show="*")
        self.password_entry.place(x=50,y=290,width=250)

        #confirm password label entry
        cnf_password = Label(frame, text="Confirm Password", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
        cnf_password.place(x=450, y=255)

        #confirm password entry field
        self.cnf_password_entry= ttk.Entry(frame,textvariable=self.var_confpass, font=("arial", 20, "bold"),show="*")
        self.cnf_password_entry.place(x=450,y=290,width=250)


        #Select Security_Ques label entry
        Security_Ques = Label(frame, text="Select Security Ques", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
        Security_Ques.place(x=50, y=330)

        #Select Security Ques entry field
        self.Security_Ques = ttk.Combobox(frame,textvariable=self.var_securityQ, font=("arial", 12, "bold"), width=17, state="readonly")
        self.Security_Ques["value"] = ("Select", "Your pet name","Favourite Book", "Favourite Place", "Nick name", "Person Close to you")
        self.Security_Ques.current(0)
        self.Security_Ques.place(x=50,y=370,width=250)
       
        #Security_Ans label entry
        Security_Ans = Label(frame, text="Security Answer", font=("Times new roman", 20,"bold"), fg="orange",bg="black")
        Security_Ans.place(x=450, y=330)

        #Security Answerentry field
        self.Security_Ans= ttk.Entry(frame,textvariable=self.var_securityA, font=("arial", 20, "bold"))
        self.Security_Ans.place(x=450,y=370,width=250)

        #check button label
        check_btn_lbl = Label(frame, text="I Agree To the Terms & Conditions", font=("Times new roman",12,"bold"), fg="white",bg="black")
        check_btn_lbl.place(x=73, y=420)
        #====================check button===============
        check_btn= Checkbutton(frame,variable=self.var_check,font=("arial",12,"bold"),onvalue=1,offvalue=0,borderwidth=0, bg="black", fg="black",activebackground="black",activeforeground="white",cursor="hand2")
        check_btn.place(x=48,y=420)

        #========buttons==========
        register_btn =Button(frame,command=self.register_data, text="Register Now", font=("arial", 15, "bold"),bd=3,relief=RIDGE,bg="Red", fg="white",activebackground="red",activeforeground="white",cursor="hand2")
        register_btn.place(x=90, y=470,width=150,height=40)

        #========buttons==========
        login_btn =Button(frame,command=self.return_login, text="LogIn Now", font=("arial", 15, "bold"),bd=3,relief=RIDGE,bg="Red", fg="white",activebackground="red",activeforeground="white",cursor="hand2")
        login_btn.place(x=500, y=470,width=150,height=40)

      #function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="":
            messagebox.showerror("Error","Fields can't be left empty")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please check the Botton to Agree")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Admin@123", database="registration")
                my_cursor = conn.cursor()
                query=("select * from register where email =%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","User already exists, Please try another email")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                self.var_fname.get(),
                                self.var_lname.get(),
                                self.var_contact.get(),
                                self.var_email.get(),
                                self.var_securityQ.get(),
                                self.var_securityA.get(),
                                self.var_pass.get(),
                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Data has been added!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
    def return_login(self):
        self.root.destroy()

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x900+0+0")
        self.root.title("HOSTEL MANAGEMENT SYSTEM CGEC")
        

        # Variables
        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_batch = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_address = StringVar()

        #search variable
        self.var_Search_field = StringVar()
        self.var_Search = StringVar()

        # 1st image
        img1 = Image.open(r"images\img1.jpg")
        img1 = img1.resize((1530, 120), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img1)

        self.btn_1 = Button(self.root, image=self.photoimg_1, cursor="hand2")
        self.btn_1.place(x=0, y=0, width=1530, height=120)

        # background image
        img4 = Image.open(r"images\img4.jpg")
        img4 = img4.resize((1530, 700), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img4)

        bg_lbl = Label(self.root, image=self.photoimg_4, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=120, width=1530, height=710)

        # title
        lbl_title = Label(bg_lbl, text="WELCOME TO HOSTEL MANAGEMENT SYSTEM CGEC", font=(
            "Times new roman", 30), fg="red")
        lbl_title.place(x=0, y=0, width=1530, height=50)

        # frame
        Manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        Manage_frame.place(x=20, y=60, width=1490, height=590)

        # left frame
        DataLeftFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information", font=(
            "Times new roman", 15, "bold"), fg="red", bg="white")
        DataLeftFrame.place(x=10, y=10, width=700, height=570)

        # head image
        img2 = Image.open(r"images\img2.jpg")
        img2 = img2.resize((120, 120), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img2)

        self.btn_2 = Button(
            DataLeftFrame, image=self.photoimg_2, cursor="hand2")
        self.btn_2.place(x=280, y=0, width=120, height=120)

        # Course field
        std_lbl_info_Frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Course information", font=(
            "Times new roman", 15, "bold"), fg="red", bg="white")
        std_lbl_info_Frame.place(x=0, y=120, width=680, height=120)

        # Department Label
        lbl_dept = Label(std_lbl_info_Frame, text="Department", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_dept.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        # departments
        Combo_dep = ttk.Combobox(std_lbl_info_Frame, textvariable=self.var_dep, font=(
            "arial", 12, "bold"), width=17, state="readonly")
        Combo_dep["value"] = ("Select Department", "CSE",
                              "ECE", "EE", "ME", "CE")
        Combo_dep.current(0)
        Combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Year Label
        lbl_Year = Label(std_lbl_info_Frame, text="Year", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_Year.grid(row=0, column=2, padx=20, pady=10, sticky=W)

        # Year
        Combo_year = ttk.Combobox(std_lbl_info_Frame, textvariable=self.var_year, font=(
            "arial", 12, "bold"), width=17, state="readonly")
        Combo_year["value"] = ("Select Year", "1st", "2nd", "3rd", "4th")
        Combo_year.current(0)
        Combo_year.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Sem Label
        lbl_sem = Label(std_lbl_info_Frame, text="Semester", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_sem.grid(row=1, column=0, padx=2, pady=10, sticky=W)

        # Sem
        Combo_sem = ttk.Combobox(std_lbl_info_Frame, textvariable=self.var_sem, font=(
            "arial", 12, "bold"), width=17, state="readonly")
        Combo_sem["value"] = ("Select Semester", "1st",
                              "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        Combo_sem.current(0)
        Combo_sem.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # batch Label
        lbl_batch = Label(std_lbl_info_Frame, text="Batch", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_batch.grid(row=1, column=2, padx=20, pady=10, sticky=W)

        # batch
        Combo_batch = ttk.Combobox(std_lbl_info_Frame, textvariable=self.var_batch, font=(
            "arial", 12, "bold"), width=17, state="readonly")
        Combo_batch["value"] = (
            "Select Batch", "2019-2023", "2020-2024", "2021-2025", "2022-2026")
        Combo_batch.current(0)
        Combo_batch.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Student field
        std_lbl_student_Frame = LabelFrame(DataLeftFrame, bd=4, relief=RIDGE, padx=2, text="Student information", font=(
            "Times new roman", 15, "bold"), fg="red", bg="white")
        std_lbl_student_Frame.place(x=0, y=240, width=680, height=220)

        # student_idLabel
        lbl_id = Label(std_lbl_student_Frame, text="Student ID:",
                       font=("arial", 12, "bold"), fg="Black", bg="white")
        lbl_id.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        id_entry = ttk.Entry(std_lbl_student_Frame, textvariable=self.var_std_id, font=(
            "arial", 12, "bold"), width=22)
        id_entry.grid(row=0, column=1, sticky=W, padx=2, pady=7)

        # name Label
        lbl_name = Label(std_lbl_student_Frame, text="Student Name:", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_name.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        txt_name = ttk.Entry(std_lbl_student_Frame, textvariable=self.var_std_name, font=(
            "arial", 12, "bold"), width=22)
        txt_name.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        # rollno Label
        lbl_roll = Label(std_lbl_student_Frame, text="Student Roll", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_roll.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        txt_roll = ttk.Entry(std_lbl_student_Frame, textvariable=self.var_roll, font=(
            "arial", 12, "bold"), width=22)
        txt_roll.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # Gender Label
        lbl_gender = Label(std_lbl_student_Frame, text="Gender:", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_gender.grid(row=1, column=2, padx=5, pady=10, sticky=W)

        Combo_txt_gender = ttk.Combobox(std_lbl_student_Frame, textvariable=self.var_gender, font=(
            "arial", 12, "bold"), width=20, state="readonly")
        Combo_txt_gender["value"] = (
            "Select Gender", "Male", "Fe-male", "Other")
        Combo_txt_gender.current(0)
        Combo_txt_gender.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Phone Label
        lbl_phone = Label(std_lbl_student_Frame, text="Phone No:", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_phone.grid(row=2, column=0, padx=5, pady=10, sticky=W)

        txt_phone = ttk.Entry(std_lbl_student_Frame, textvariable=self.var_phone, font=(
            "arial", 12, "bold"), width=22)
        txt_phone.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # Email Label
        lbl_email = Label(std_lbl_student_Frame, text="Email-id:",
                          font=("arial", 12, "bold"), fg="Black", bg="white")
        lbl_email.grid(row=2, column=2, padx=5, pady=10, sticky=W)

        txt_email = ttk.Entry(std_lbl_student_Frame, textvariable=self.var_email, font=(
            "arial", 12, "bold"), width=22)
        txt_email.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # DOB Label
        lbl_dob = Label(std_lbl_student_Frame, text="DOB:", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_dob.grid(row=3, column=0, padx=5, pady=10, sticky=W)

        txt_dob = ttk.Entry(std_lbl_student_Frame, textvariable=self.var_dob, font=(
            "arial", 12, "bold"), width=22)
        txt_dob.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        # address Label
        lbl_address = Label(std_lbl_student_Frame, text="Address:", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        lbl_address.grid(row=3, column=2, padx=5, pady=10, sticky=W)

        txt_address = ttk.Entry(std_lbl_student_Frame, textvariable=self.var_address, font=(
            "arial", 12, "bold"), width=22)
        txt_address.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        # button frame
        btn_frame = Frame(DataLeftFrame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=480, width=680, height=40)

        btn_Add = Button(btn_frame, text="Save", command=self.add_data, font=(
            "arial", 12, "bold"), width=16, bg="Green", fg="white", cursor="hand2")
        btn_Add.grid(row=0, column=0, padx=2)

        btn_update = Button(btn_frame, text="Update",command=self.update_data, font=(
            "arial", 12, "bold"), width=16, bg="orange", fg="white", cursor="hand2")
        btn_update.grid(row=0, column=1, padx=2)

        btn_delete = Button(btn_frame, text="Delete",command=self.delete_data, font=(
            "arial", 12, "bold"), width=16, bg="Red", fg="white", cursor="hand2")
        btn_delete.grid(row=0, column=2, padx=2)

        btn_reset = Button(btn_frame, text="Reset",command=self.reset_data, font=(
            "arial", 12, "bold"), width=16, bg="blue", fg="white", cursor="hand2")
        btn_reset.grid(row=0, column=3, padx=2)

        # right frame
        DataRightFrame = LabelFrame(Manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Details", font=(
            "Times new roman", 15, "bold"), fg="red", bg="white")
        DataRightFrame.place(x=720, y=10, width=755, height=570)

        # head image
        img3 = Image.open(r"images\img3.jpg")
        img3 = img3.resize((120, 120), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img3)

        self.btn_3 = Button(
            DataRightFrame, image=self.photoimg_3, cursor="hand2")
        self.btn_3.place(x=280, y=0, width=120, height=120)

        # search frame
        SearchFrame = LabelFrame(DataRightFrame, bd=4, relief=RIDGE, padx=2, text="Search Student Information", font=(
            "Times new roman", 15, "bold"), fg="red", bg="white")
        SearchFrame.place(x=0, y=120, width=740, height=80)
        
        #search label
        search_by = Label(SearchFrame, text="Search By:", font=(
            "arial", 12, "bold"), fg="Black", bg="white")
        search_by.grid(row=0, column=0, padx=2, sticky=W)

        #search field
        Combo_txt_search = ttk.Combobox(SearchFrame,textvariable=self.var_Search_field,font=("arial", 12, "bold"), width=18, state="readonly")
        Combo_txt_search["value"] = ("Select Options", "Roll", "Phone", "Student_Id")
        Combo_txt_search.current(0)
        Combo_txt_search.grid(row=0, column=1, padx=2, sticky=W)

        txt_search = ttk.Entry(SearchFrame,textvariable=self.var_Search,font=(
            "arial", 12, "bold"), width=18)
        txt_search.grid(row=0, column=2, sticky=W, padx=2, pady=10)

        btn_search = Button(SearchFrame, text="Search",command=self.search_data, font=(
            "arial", 12, "bold"), width=12, bg="orange", fg="white", cursor="hand2")
        btn_search.grid(row=0, column=3, padx=2)

        btn_ShowAll = Button(SearchFrame, text="Show All",command=self.fetch_data, font=(
            "arial", 12, "bold"), width=12, bg="Blue", fg="white", cursor="hand2")
        btn_ShowAll.grid(row=0, column=4, padx=2)

        # =================================Table and Scroll bar======================================
        table_frame = Frame(DataRightFrame, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=0, y=210, width=740, height=320)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("dep", "year", "sem", "batch", "student_id", "name", "roll",
                                          "gender", "phone", "email", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("student_id", text="Student Id")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("address", text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("batch", width=100)
        self.student_table.column("student_id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_data)
        self.fetch_data()

    def add_data(self):
        if(self.var_std_name.get() == "" or self.var_year.get() == "" or self.var_roll.get() == ""):
            messagebox.showerror("Error", "Field can not be left blank")
        elif(self.var_email.get() == ""):
            messagebox.showwarning("Warning", "Email is not entered")
        elif(self.var_phone.get() == ""):
            messagebox.showwarning("Warning", "Phone Number is not entered")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Admin@123", database="hostel_management_system")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_batch.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_dob.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Sucess", "Data has been added!", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    # data fetch from database

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Admin@123", database="hostel_management_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get data
    def get_data(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]
        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_sem.set(data[2]),
        self.var_batch.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_email.set(data[9]),
        self.var_dob.set(data[10]),
        self.var_address.set(data[11])

    # update the data
    def update_data(self):
        if(self.var_std_name.get() == "" or self.var_phone.get() == "" or self.var_year.get() == "" or self.var_roll.get() == ""):
            messagebox.showerror("Error", "Field can not be left blank")
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Are you sure you want to Update the Data", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Admin@123", database="hostel_management_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update Student set dep=%s, year=%s, semester=%s, batch=%s, name=%s, roll=%s, gender=%s, phone=%s, email=%s, dob=%s, address=%s where student_id=%s", (
                        self.var_dep.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_batch.get(),
                        self.var_std_name.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_std_id.get(),
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo(
                    "Success", "Data is updated", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To:{str(es)}", parent=self.root)

    #delete data
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Field left blank")
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure you want to delete the data")
                if Delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Admin@123", database="hostel_management_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("delete from Student where student_id=%s",(
                                                            self.var_std_id.get(),
                    ))
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Data has been Deleted",parent=self.root)
            except Exception as es:
                 messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #reset
    def reset_data(self):
              self.var_dep.set("Select Department"),
              self.var_year.set("Select Year"),
              self.var_sem.set("Select Semester"),
              self.var_batch.set("Select Batch"),
              self.var_std_id.set(""),
              self.var_std_name.set(""),
              self.var_roll.set(""),
              self.var_gender.set("Select Gender"),
              self.var_phone.set(""),
              self.var_email.set(""),
              self.var_dob.set(""),
              self.var_address.set(""),
    
    #search
    def search_data(self):
        if self.var_Search_field.get()=="" or self.var_Search.get()=="":
            messagebox.showerror("Error","Please Select an Option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Admin@123", database="hostel_management_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select  *from Student where "+str(self.var_Search_field.get())+" LIKE '%"+str(self.var_Search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                 messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

if __name__ == "__main__":
    main()