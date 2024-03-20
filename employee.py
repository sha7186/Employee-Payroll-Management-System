
from tkinter import*
from tkinter import messagebox
import pymysql 
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title = Label(self.root,text="Employee Payroll Management System",font=("times new roman", 30 ,"bold"),bg="#262626",fg="white", anchor="w",padx=10).place(x=0,y=0,relwidth=1)


#  FRAME1

    #  Variables
        
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_experience=StringVar()
        self.var_proof_id=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
        
        
        
        

        
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)
        title2 = Label(Frame1,text="Employee Details",font=("times new roman", 20 ),bg="lightgray",fg="black", anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_code=Label(Frame1,text="Employee Code",font=("times new roman", 20 ),bg="white",fg="black").place(x=10,y=70)
        
        txt_code=Entry(Frame1,font=("times new roman", 15 ) ,textvariable=self.var_emp_code,bg="lightgray",fg="black").place(x=220,y=74,width=200)

        btn_search=Button(Frame1,text="Search",font=("times new roman", 20 ),bg="lightblue",fg="black").place(x=440,y=72,height=30)
       
        # ROW-1

        lbl_designation=Label(Frame1,text="Designation",font=("times new roman", 20 ),bg="white",fg="black").place(x=10,y=120)
        txt_designation=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_designation,bg="lightgray",fg="black").place(x=170,y=125,width=200)
        lbl_dob=Label(Frame1,text="D.O.B",font=("times new roman", 20 ),bg="white",fg="black").place(x=390,y=120)
        txt_dob=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_dob,bg="lightgray",fg="black").place(x=520,y=125)

        # ROW-2

        lbl_name=Label(Frame1,text="Name",font=("times new roman", 20 ),bg="white",fg="black").place(x=10,y=170)
        txt_name=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_name,bg="lightgray",fg="black").place(x=170,y=175,width=200)
        lbl_doj=Label(Frame1,text="D.O.J",font=("times new roman", 20 ),bg="white",fg="black").place(x=390,y=170)
        txt_doj=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_doj,bg="lightgray",fg="black").place(x=520,y=175)

        # ROW-3

        lbl_age=Label(Frame1,text="Age",font=("times new roman", 20 ),bg="white",fg="black").place(x=10,y=220)
        txt_age=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_age,bg="lightgray",fg="black").place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1,text="Experience",font=("times new roman", 20 ),bg="white",fg="black").place(x=390,y=220)
        txt_experience=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_experience,bg="lightgray",fg="black").place(x=520,y=225)

         # ROW-4
        
        lbl_gender=Label(Frame1,text="Gender",font=("times new roman", 20 ),bg="white",fg="black").place(x=10,y=270)
        txt_gender=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_gender,bg="lightgray",fg="black").place(x=170,y=275,width=200)
        lbl_proof=Label(Frame1,text="Proof ID",font=("times new roman", 20 ),bg="white",fg="black").place(x=390,y=270)
        txt_proof=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_proof_id,bg="lightgray",fg="black").place(x=520,y=275)

         # ROW-5
        
        lbl_email=Label(Frame1,text="Email",font=("times new roman", 20 ),bg="white",fg="black").place(x=10,y=320)
        txt_email=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_email,bg="lightgray",fg="black").place(x=170,y=325,width=200)
        lbl_contact=Label(Frame1,text="Contact",font=("times new roman", 20 ),bg="white",fg="black").place(x=390,y=320)
        txt_contact=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_contact,bg="lightgray",fg="black").place(x=520,y=325)

         # ROW-6
        
        lbl_location=Label(Frame1,text="Location",font=("times new roman", 20 ),bg="white",fg="black").place(x=10,y=370)
        txt_location=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_location,bg="lightgray",fg="black").place(x=170,y=375,width=200)
        lbl_status=Label(Frame1,text="Status",font=("times new roman", 20 ),bg="white",fg="black").place(x=390,y=370)
        txt_status=Entry(Frame1,font=("times new roman", 15 ),textvariable=self.var_status,bg="lightgray",fg="black").place(x=520,y=375)

         # ROW-7
        
        lbl_address=Label(Frame1,text="address",font=("times new roman", 20 ),bg="white",fg="black").place(x=10,y=422)
        self.txt_address=Text(Frame1,font=("times new roman", 15 ),bg="lightgray",fg="black")
        self.txt_address.place(x=170,y=425,width=550,height=150)
        




#  FRAME2
  #  variable    

        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_ctc=StringVar()
          
          

        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)

        title3 = Label(Frame2,text="Employee Salary",font=("times new roman", 20 ),bg="lightgray",fg="black", anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        lbl_month=Label(Frame2,text="Month",font=("times new roman", 18 ),bg="white",fg="black").place(x=10,y=60)
        txt_month=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_month,bg="lightgray",fg="black").place(x=90,y=62,width=100)
        
        lbl_year=Label(Frame2,text="Year",font=("times new roman", 18 ),bg="white",fg="black").place(x=210,y=60)
        txt_year=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_year,bg="lightgray",fg="black").place(x=270,y=62,width=100)
        
        lbl_salary=Label(Frame2,text="Salary",font=("times new roman", 18 ),bg="white",fg="black").place(x=380,y=60)
        txt_salary=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_salary,bg="lightgray",fg="black").place(x=450,y=62,width=100)
        

        # ROW-1

        lbl_totaldays=Label(Frame2,text="Total Days",font=("times new roman", 18 ),bg="white",fg="black").place(x=10,y=120)
        txt_totaldays=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_t_days,bg="lightgray",fg="black").place(x=170,y=125,width=100)
        lbl_absent=Label(Frame2,text="Absent",font=("times new roman", 18 ),bg="white",fg="black").place(x=300,y=120)
        txt_absent=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_absent,bg="lightgray",fg="black").place(x=420,y=125, width=120)

        # ROW-2

        lbl_medical=Label(Frame2,text="Medical",font=("times new roman", 18 ),bg="white",fg="black").place(x=10,y=150)
        txt_medical=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_medical,bg="lightgray",fg="black").place(x=170,y=155,width=100)
        lbl_pf=Label(Frame2,text="PF",font=("times new roman", 18 ),bg="white",fg="black").place(x=300,y=150)
        txt_pf=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_pf,bg="lightgray",fg="black").place(x=420,y=155, width=120)

        # ROW-2

        lbl_convence=Label(Frame2,text="Convence",font=("times new roman", 18 ),bg="white",fg="black").place(x=10,y=180)
        txt_convence=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_convence,bg="lightgray",fg="black").place(x=170,y=185,width=100)
        lbl_CTC=Label(Frame2,text="CTC",font=("times new roman", 18 ),bg="white",fg="black").place(x=300,y=180)
        txt_CTC=Entry(Frame2,font=("times new roman", 15 ),textvariable=self.var_ctc,bg="lightgray",fg="black").place(x=420,y=185, width=120)

        btn_calculate=Button(Frame2,text="Calculate",font=("times new roman", 20 ),bg="red",fg="black").place(x=150,y=240,height=30, width=120)
        btn_save=Button(Frame2,text="Save",font=("times new roman", 20 ),bg="blue",fg="black").place(x=285,y=240,height=30, width=120)
        btn_clear=Button(Frame2,text="Clear",font=("times new roman", 20 ),bg="green",fg="black").place(x=420,y=240,height=30, width=120)
        
       #  FRAME3
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=310)

        # calculater frame
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)

        def result():
                res=str(eval(self.var_operator))
                self.var_txt.set(res)
                self.var_operator=''

        def clear_cal():
             self.var_txt.set('')
             self.var_operator=''

             


        Cal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        Cal_Frame.place(x=2,y=2,width=247, height=300)

        txt_result=Entry(Cal_Frame,bg="lightgray",textvariable=self.var_txt, font=("times new roman",20, "bold"),justify=RIGHT).place(x=0,y=0,relwidth=1,height=50)

        # ROW-1

        btn_7=Button(Cal_Frame,text='7',command=lambda:btn_click(7),font=("times in roman",15,"bold")).place(x=0,y=52,width=60,height=60)
        btn_8=Button(Cal_Frame,text='8',command=lambda:btn_click(8),font=("times in roman",15,"bold")).place(x=61,y=52,width=60,height=60)
        btn_9=Button(Cal_Frame,text='9',command=lambda:btn_click(9),font=("times in roman",15,"bold")).place(x=122,y=52,width=60,height=60)
        btn_div=Button(Cal_Frame,text='/',command=lambda:btn_click('/'),font=("times in roman",15,"bold")).place(x=183,y=52,width=60,height=60)

         # ROW-2

        btn_4=Button(Cal_Frame,text='4',command=lambda:btn_click(4),font=("times in roman",15,"bold")).place(x=0,y=112,width=60,height=60)
        btn_5=Button(Cal_Frame,text='5',command=lambda:btn_click(5),font=("times in roman",15,"bold")).place(x=61,y=112,width=60,height=60)
        btn_6=Button(Cal_Frame,text='6',command=lambda:btn_click(6),font=("times in roman",15,"bold")).place(x=122,y=112,width=60,height=60)
        btn_multiply=Button(Cal_Frame,text='*',command=lambda:btn_click('*'),font=("times in roman",15,"bold")).place(x=183,y=112,width=60,height=60)

         # ROW-3

        btn_1=Button(Cal_Frame,text='1',command=lambda:btn_click(1),font=("times in roman",15,"bold")).place(x=0,y=172,width=60,height=60)
        btn_2=Button(Cal_Frame,text='2',command=lambda:btn_click(2),font=("times in roman",15,"bold")).place(x=61,y=172,width=60,height=60)
        btn_3=Button(Cal_Frame,text='3',command=lambda:btn_click(3),font=("times in roman",15,"bold")).place(x=122,y=172,width=60,height=60)
        btn_subs=Button(Cal_Frame,text='-',command=lambda:btn_click('-'),font=("times in roman",15,"bold")).place(x=183,y=172,width=60,height=60)

        # ROW-4

        btn_0=Button(Cal_Frame,text='0',command=lambda:btn_click(0),font=("times in roman",15,"bold")).place(x=0,y=232,width=60,height=60)
        btn_dot=Button(Cal_Frame,text='C',command=clear_cal,font=("times in roman",15,"bold")).place(x=61,y=232,width=60,height=60)
        btn_add=Button(Cal_Frame,text='+',command=lambda:btn_click('+'),font=("times in roman",15,"bold")).place(x=122,y=232,width=60,height=60)
        btn_equalsto=Button(Cal_Frame,text='=',command=result,font=("times in roman",15,"bold")).place(x=183,y=232,width=60,height=60)

        # salary frame

        sal_Frame=Frame(Frame3,bg="white",bd=2,relief=RIDGE)
        sal_Frame.place(x=251,y=2,width=300, height=300)
        title_sal = Label(sal_Frame,text="Salary Reciept",font=("times new roman", 20 ),bg="lightgray",fg="black", anchor="w",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2=Frame(sal_Frame,bg='white',bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)

        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(sal_Frame2,font=("times new roman",15),bg="lightgray",yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)

        btn_print=Button(sal_Frame,text="Print",font=("times new roman", 20 ),bg="yellow",fg="black").place(x=180,y=262,height=30, width=120)
        
        self.check_connection()

def add(self):
#      frame1 varoables
    print(self.var_emp_code.get(),
     self.var_designation.get(),
     self.var_name.get(),
     self.var_age.get(),
     self.var_gender.get(),
     self.var_email.get(),
     self.var_location.get(),
     self.var_dob.get(),
     self.var_doj.get(),
     self.var_experience.get(),
     self.var_proof_id.get(),
     self.var_contact.get(),
     self.var_status.get(),
        
     

#      frame2 variables
     self.var_month.get(),
     self.var_year.get(),
     self.var_salary.get(),
     self.var_t_days.get(),
     self.var_absent.get(),
     self.var_medical.get(),
     self.var_pf.get(),
     self.var_convence.get(),
     self.var_ctc.get(),
     self.txt_address.get('1.0,END')
               )
     
def calculate(self):
     if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_t_day.get()=='' or self.var_absent.get()=='' or self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_status.get()=='':
          messagebox.showerror('Error','All fields are required')
     else :
          # self.var
          #
          #
          per_day=int(self.var_salary.get())/int(self.var_t_days.get()) 
          work_day=int(self.var_t_days.get())/int(self.var_absent.get())    
          sal_=per_day*work_day
          deduct=int(self.var_medical.get())/int(self.var_pf.get()) 
          addition=int(self.var_convence.get())  
          net_sal=sal_-deduct+addition
          self.var_net_salary.set(str(round(net_sal,2)))


def check_connection(self): 
     try:
          print("connection")
        #   con=pymysql.connect(host='localhost',user='root',password='',db='EPMS')
        #   cur=con.curser()
        #   cur.execute("select * from emp_salary")
        #   rows=cur.fetchall()
        #   print(rows)

     except Exception as ex:
          messagebox.showerror("Error",f'Error due to: {str(ex)}')
# EmployeeSystem.check_connection()


root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
