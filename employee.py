import os
import tempfile
import time
from tkinter import *
from tkinter import font, messagebox, ttk
from tkinter.font import BOLD

import pymysql
from fpdf import FPDF
from tkcalendar import *


class empolyee_payroll:
    def __init__(self,root):
        self.root=root

        app_width=1370
        app_height=800

        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()

        x=(screen_width/2)-(app_width/2)
        y=(screen_height/2)-(app_height/2)

        self.root.title("Employee Payroll Management")
        self.root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.root.config(bg='white')
        self.root.resizable(False,False)
        
        title=Label(self.root,text='Employee Payroll Management System',font=('Times New Roman',40,BOLD),bg='gold',fg='Black',anchor='w',padx=5).place(x=0,y=0,relwidth=1)
        btn_employe=Button(self.root,text="All Employee Details",command=self.employee_frame,font=("times new roman",15,BOLD),fg="black",bg='white',padx=5).place(x=1150,y=15)

        f1=Frame(self.root,bd=5,relief=RIDGE,bg='light cyan')
        f1.place(x=5,y=70,width=730,height=690)
        f2=Frame(self.root,bd=5,relief=RIDGE,bg='light cyan')
        f2.place(x=760,y=70,width=600,height=350)
        f3=Frame(self.root,bd=5,relief=RIDGE,bg='light cyan')
        f3.place(x=760,y=450,width=600,height=310)
        #====== frame 1(f1) ===============#
        title2=Label(f1,text='Employee Details',font=("Times new roman",30,BOLD),bg='deep sky blue',padx=5,fg='black',anchor='w')
        title2.place(x=0,y=0,relwidth=1)
        
        #=========== design in frame 1(f1) button========= #

        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_email_id=StringVar()
        self.var_contact_no=StringVar()
        self.var_doj=StringVar()
        self.var_gender=StringVar()
        self.var_exp=StringVar()
        self.var_designation=StringVar()
        self.var_age=StringVar()
        self.var_id_proof=StringVar()
        self.var_address=StringVar()
        self.var_status=StringVar()

        options_gender=["Male",
                        "Female",
                        "Not to say"]
        self.var_gender.set(options_gender[2])

        self.pdf=FPDF()
        self.pdf.add_page()
        self.pdf.set_font('times new roman',15)
        

        emp_id=Label(f1,text="Employee id",font=('Times New Roman',18),fg='black',bg='light cyan').place(x=5,y=70)
        self.txt_id=Entry(f1,font=('times new roman',15),textvariable=self.var_id,bg='white',fg='black',bd=2,justify='center')
        self.txt_id.place(x=180,y=70)
        btn_search=Button(f1,text='search',font=('times new roman',14,BOLD),bg='yellow',fg='black',bd=2)
        btn_search.bind("<Return>",self.search)
        btn_search.bind("<Button-1>",self.search)
        btn_search.place(x=400,y=70)

        #============ row 1(f1)===========================#
        emp_name=Label(f1,text="Employee Name",font=('times new roman',18),fg='black',bg='light cyan').place(x=5,y=125)
        txt_name=Entry(f1,font=('times new roman',15),textvariable=self.var_name,fg='black',bg='white',bd=2,justify='center').place(x=180,y=125,width=190)
        
        emp_dob=Label(f1,text='D.O.B',font=('times new roman',18),fg='black',bg='light cyan').place(x=430,y=125)
        txt_dob=Entry(f1,font=('times new roman',15),textvariable=self.var_dob,fg='black',bg='white',bd=2,justify='center').place(x=510,y=125,width=190)
        dob=Label(f1,text="YYYY / MM / DD",font=(10),fg="black",bg="light cyan").place(x=550,y=158)
        #===============row 2 (f1)=======================#
        emp_email_id=Label(f1,text='Email id',font=('times new roman',18),fg='black',bg='light cyan').place(x=5,y=185)
        emp_email_id=Entry(f1,font=('times new roman',15),textvariable=self.var_email_id,fg='black',bg='white',bd=2,justify='center').place(x=180,y=185,width=190)

        emp_contact_no=Label(f1,text='Contact No',font=('times new roman',18),fg='black',bg='light cyan').place(x=390,y=185)
        self.txt_contact_no=Entry(f1,font=('times new roman',15),textvariable=self.var_contact_no,fg='black',bg='white',bd=2,justify='center')
        self.txt_contact_no.place(x=510,y=185,width=190)
        
        #=================row 3 (f1)======================#
        emp_doj=Label(f1,text='D.O.J',font=('times new roman',18),fg='black',bg='light cyan').place(x=5,y=240)
        txt_doj=Entry(f1,font=('times new roman',15),textvariable=self.var_doj,fg='black',bg='white',bd=2,justify='center').place(x=180,y=240,width=190)
        
        date_entry=Label(f1,text="YYYY / MM / DD",font=(10),fg="black",bg="lightcyan")
        date_entry.place(x=220,y=274)
        
        emp_Gender=Label(f1,text='Gender',font=('times new roman',18),fg='black',bg='light cyan').place(x=410,y=250)
        self.txt_Gender=OptionMenu(f1,self.var_gender,*options_gender)
        self.txt_Gender.place(x=510,y=250,width=190) 

        #==================row 4 (f1)======================#
        emp_exp=Label(f1,text='Experience',font=('times new roman',18),fg='black',bg='light cyan').place(x=5,y=300)
        txt_exp=Entry(f1,font=('times new roman',15),textvariable=self.var_exp,fg='black',bg='white',bd=2,justify='center').place(x=180,y=300,width=190)

        emp_designation=Label(f1,text='Designation',font=('times new roman',18),fg='black',bg='light cyan').place(x=385,y=300)
        txt_designation=Entry(f1,font=('times new roman',15),textvariable=self.var_designation,fg='black',bg='white',bd=2,justify='center').place(x=510,y=300,width=190)

        #====================row 5(f1)=====================#
        emp_id_proof=Label(f1,text='ID Proof',font=('times new roman',18),fg='black',bg='light cyan').place(x=5,y=350)
        txt_id_proof=Entry(f1,font=('times new roman',15),textvariable=self.var_id_proof,fg='black',bg='white',bd=2,justify='center').place(x=180,y=350,width=190)

        emp_age=Label(f1,text='Age',font=('times new roman',18),fg='black',bg='light cyan').place(x=420,y=350)
        txt_age=Entry(f1,font=('times new roman',15),textvariable=self.var_age,fg='black',bg='white',bd=2,justify='center').place(x=510,y=350,width=190)

        #======================== row 6(f1)================#
        emp_status=Label(f1,text='Status',font=('times new roman',18),bg='light cyan',fg='black').place(x=5,y=400)
        txt_status=Entry(f1,font=('times new roman',15),bg='white',fg='black',bd=2,justify='center',textvariable=self.var_status).place(x=180,y=400)

        #=======================row 7(f1)=================#
        emp_address=Label(f1,text='Address',font=('times new roman',18),bg='light cyan',fg='black').place(x=5,y=480)
        self.txt_address=Text(f1,font=('times new roman',18),bg='white',fg='black',bd=2)
        self.txt_address.place(x=180,y=480,width=450,height=120)
         
        #====================frame 2 works start(f2)=======#
        title3=Label(f2,text='Employee Salary details',font=("Times new roman",22,BOLD),bg='deep sky blue',padx=5,fg='black',anchor='w')
        title3.place(x=0,y=0,relwidth=1)

        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_basic_sal=StringVar()
        self.var_days=StringVar()
        self.var_absents=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_conveyance=StringVar()
        self.var_net_salary=StringVar()

        #===================row 1(f2)==================#

        sal_month=Label(f2,text='Month',font=('times new roman',18),fg='black',bg='light cyan').place(x=5,y=50)
        txt_month=Entry(f2,font=('times new roman',12),textvariable=self.var_month,fg='black',bg='white').place(x=90,y=53,width=100)
        
        sal_year=Label(f2,text='Year',font=('times new roman',18),fg='black',bg='light cyan').place(x=200,y=50)
        txt_year=Entry(f2,font=('times new roman',12),textvariable=self.var_year,fg='black',bg='white').place(x=260,y=53,width=100)
        
        sal_sal=Label(f2,text='Basic Salary',font=('times new roman',18),fg='black',bg='light cyan').place(x=365,y=50)
        txt_sal=Entry(f2,font=('times new roman',12),textvariable=self.var_basic_sal,fg='black',bg='white').place(x=495,y=53,width=95)

        #================row 2 (f2)====================#

        sal_days=Label(f2,text='Total days',font=('times new roman',18),bg='light cyan',fg='black').place(x=5,y=100)
        txt_days=Entry(f2,font=('times new roman',12),textvariable=self.var_days,bg='white',fg='black').place(x=115,y=102,width=150)
        
        sal_absents=Label(f2,text='Absents',font=('times new roman',18),bg='light cyan',fg='black').place(x=280,y=100)
        txt_days=Entry(f2,font=('times new roman',12),textvariable=self.var_absents,bg='white',fg='black').place(x=400,y=102,width=150)

        #==============row 3 (f2)===================#

        sal_medical=Label(f2,text='Medical',font=('times new roman',18),bg='light cyan',fg='black').place(x=5,y=150)
        txt_medical=Entry(f2,font=('times new roman',12),textvariable=self.var_medical,bg='white',fg='black').place(x=100,y=152,width=150)
        
        sal_pf=Label(f2,text='Provident Fund',font=('times new roman',18),bg='light cyan',fg='black').place(x=240,y=150)
        txt_pf=Entry(f2,font=('times new roman',12),textvariable=self.var_pf,bg='white',fg='black').place(x=400,y=150,width=150)

        #===============row 4 (f2)=============#

        sal_conveyance=Label(f2,text='conveyance',font=('times new roman',16),bg='light cyan',fg='black').place(x=5,y=200)
        txt_conveyance=Entry(f2,font=('times new roman',12),textvariable=self.var_conveyance,bg='white',fg='black').place(x=115,y=202,width=150)
        
        sal_Net_salary=Label(f2,text='Net Salary',font=('times new roman',18),bg='light cyan',fg='black').place(x=270,y=200)
        txt_Net_salary=Entry(f2,font=('times new roman',12),textvariable=self.var_net_salary,bg='white',fg='black').place(x=400,y=202,width=150)

        #=============buttons (f2) ===========#

        btn_cal=Button(f2,text='Calculate',font=('times new roman',18,BOLD),bg='dark orange',fg='black',bd=2)
        btn_cal.bind("<Return>",self.cal)
        btn_cal.bind("<Button-1>",self.cal)
        btn_cal.place(x=70,y=250,h=30, w=100)

        self.btn_add=Button(f2,text='Save',command=self.add,font=('times new roman',18,BOLD),bg='yellow',fg='black',bd=2)
        self.btn_add.bind("<Return>",self.add)
        self.btn_add.bind("<Button-1>",self.add)
        self.btn_add.place(x=180,y=250,h=30,w=100)

        btn_clear=Button(f2,text='Clear',font=('times new roman',18,BOLD),bg='light steel blue',fg='black',bd=2)
        btn_clear.bind("<Return>",self.clear)
        btn_clear.bind("<Button-1>",self.clear)
        btn_clear.place(x=290,y=250,h=30,w=100)
        
        self.btn_update=Button(f2,text='Update',state=DISABLED,font=('times new roman',18,BOLD),bg='Light green',fg='black',bd=2)
        self.btn_update.bind("<Return>",self.update)
        self.btn_update.bind("<Button-1>",self.update)
        self.btn_update.place(x=400,y=250,h=30,w=100) 
        
        self.btn_delete=Button(f2,text='Delete',state=DISABLED,font=('times new roman',18,BOLD),bg='Red',fg='black',bd=2)
        self.btn_delete.bind("<Return>",self.delete)
        self.btn_delete.bind("<Button-1>",self.delete)
        self.btn_delete.place(x=250,y=300,h=30,w=100)

        #============frame 3 wrok start from here===========#
        self.var_txt=StringVar()
        self.var_opertor=''
        
        def btn_click(num):
            self.var_opertor=self.var_opertor+str(num)
            self.var_txt.set(self.var_opertor)

        def result():
            res=str(eval(self.var_opertor))
            self.var_txt.set(res)
            self.var_opertor=""
        def clear(event):
            self.var_txt.set('')
            self.var_opertor=""
        

        
        cal_frame=Frame(f3,bg='light cyan',bd=2,relief=RIDGE)
        cal_frame.place(x=5,y=2,width=249,height=295)

        text_frame=Entry(cal_frame,font=('times new roman',15),bg='white',textvariable=self.var_txt,fg='black',justify=RIGHT).place(x=0,y=0,relwidth=1,height=40)
        
        #==============row 1 buttons======================#

        btn_7=Button(cal_frame,text='7',command=lambda:btn_click(7),font=('times new roman',15,BOLD)).place(x=0,y=42,w=61,h=61)
        btn_8=Button(cal_frame,text='8',command=lambda:btn_click(8),font=('times new roman',15,BOLD)).place(x=61,y=42,w=61,h=61)
        btn_9=Button(cal_frame,text='9',command=lambda:btn_click(9),font=('times new roman',15,BOLD)).place(x=122,y=42,w=61,h=61)
        btn_divide =Button(cal_frame,text='/',command=lambda:btn_click('/'),font=('times new roman',15,BOLD)).place(x=183,y=42,w=61,h=61)

        #====================row 2 buttons==============#

        btn_4=Button(cal_frame,text='4',command=lambda:btn_click(4),font=('times new roman',15,BOLD)).place(x=0,y=102,w=61,h=61)
        btn_5=Button(cal_frame,text='5',command=lambda:btn_click(5),font=('times new roman',15,BOLD)).place(x=61,y=102,w=61,h=61)
        btn_6=Button(cal_frame,text='6',command=lambda:btn_click(6),font=('times new roman',15,BOLD)).place(x=122,y=102,w=61,h=61)
        btn_multiply =Button(cal_frame,command=lambda:btn_click('*'),text='*',font=('times new roman',15,BOLD)).place(x=183,y=102,w=61,h=61)

        #====================row 3 button=================#

        btn_1=Button(cal_frame,text='1',command=lambda:btn_click(1),font=('times new roman',15,BOLD)).place(x=0,y=162,w=61,h=61)
        btn_2=Button(cal_frame,text='2',command=lambda:btn_click(2),font=('times new roman',15,BOLD)).place(x=61,y=162,w=61,h=61)
        btn_3=Button(cal_frame,text='3',command=lambda:btn_click(3),font=('times new roman',15,BOLD)).place(x=122,y=162,w=61,h=61)
        btn_subtract=Button(cal_frame,text='-',command=lambda:btn_click('-'),font=('times new roman',15,BOLD)).place(x=183,y=162,w=61,h=61)

        #======================row 4 buttons ==============#

        btn_0=Button(cal_frame,text='0',command=lambda:btn_click(0),font=('times new roman',15,BOLD)).place(x=0,y=222,w=61,h=61)
        btn_dot=Button(cal_frame,text='.',command=lambda:btn_click('.'),font=('times new roman',15,BOLD)).place(x=61,y=222,w=61,h=61)
        btn_add=Button(cal_frame,text='+',command=lambda:btn_click('+'),font=('times new roman',15,BOLD)).place(x=122,y=222,w=61,h=61)
        btn_equal=Button(cal_frame,text='=',command=result,font=('times new roman',15,BOLD)).place(x=183,y=222,w=61,h=61)
        #btn_clr=Button(f3,command=clear,text='C',font=('times new roman',15,BOLD)).place(x=255,y=230,w=61,h=61)

        #======================== Salary frame f3 print receipt ================#

        sal_receipt=Frame(f3,bg='light cyan',bd=2,relief=RIDGE)
        sal_receipt.place(x=260,y=2,w=330,h=295)

        title4=Label(sal_receipt,text='Pay Slip',font=("Times new roman",20,BOLD),bg='deep sky blue',padx=10,fg='black',anchor='center')
        title4.place(x=0,y=0,relwidth=1)

        sal_receipt_frame=Frame(sal_receipt,bg='white',relief=RIDGE)
        sal_receipt_frame.place(x=0,y=40,relwidth=1,height=200)

        self.receipt_frame= f'''\t AZURE, COMPANY \n\r          Address:KOTESHWAR DAM,\n\tBUSINESS UNITED, floor4
--------------------------------------------------
Employee ID\t\t:
Employee Name\t\t:
Salary of year\t\t: MM-YYYY
Generated on \t\t: DD-MM-YYYY
--------------------------------------------------
Total days\t\t: DD
Total present\t\t: DD  
Total Absent\t\t: DD
conveyance\t\t: RS----
Medical\t\t: RS----  
Provident Fund\t\t: RS----  
Gross payement\t\t: Rs----
Net Salary\t\t: RS----
--------------------------------------------------
'''
        
        scroll_b=Scrollbar(sal_receipt_frame,orient=VERTICAL)
        scroll_b.pack(fill=Y,side=RIGHT)
        
        self.txt_salary_receipt=Text(sal_receipt_frame,font=('times new roman',14),bg='lightyellow',yscrollcommand=scroll_b.set)
        self.txt_salary_receipt.pack(fill=BOTH,expand=1)
        scroll_b.config(command=self.txt_salary_receipt.yview)

        self.txt_salary_receipt.insert(END,self.receipt_frame)

        self.btn_print=Button(sal_receipt,state=DISABLED,text='Print receipt',command=self.print_receipt,font=('times new roman',18,BOLD),bg='deep sky blue',fg='black',bd=2)
        self.btn_print.place(x=80,y=242)



        self.check_connection()
    
    #============================== All Function def from here =====================================#
    def search(self,event):
        
        try:

            con=pymysql.connect(host='localhost',user='root',password='',db='employee_management_system')
            cur=con.cursor()
            cur.execute('select * from emp_salary where emp_id=%s',(self.var_id.get()))
            row=cur.fetchone()
                #print(rows)
            if row==None:
                
                messagebox.showerror("Error","Please Enter proper Employee ID",parent=self.root)
                
            else:
                #cur.execute("INSERT INTO emp_salary VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",)
                print(row)
                self.var_id.set(row[0])
                self.var_name.set(row[1])
                self.var_dob.set(row[2])
                self.var_email_id.set(row[3])
                self.var_contact_no.set(row[4])
                self.var_doj.set(row[5])
                self.var_gender.set(row[6])
                self.var_exp.set(row[7])
                self.var_designation.set(row[8])
                self.var_id_proof.set(row[9])
                self.var_age.set(row[10])
                self.var_status.set(row[11])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[12])
                self.var_month.set(row[13])
                self.var_year.set(row[14])
                self.var_basic_sal.set(row[15])
                self.var_days.set(row[16])
                self.var_absents.set(row[17])                        
                self.var_medical.set(row[18])
                self.var_pf.set(row[19])
                self.var_conveyance.set(row[20])
                self.var_net_salary.set(row[21])
                file_receipt_folder=open('Salary_receipt/'+str(row[22]),'r')
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_receipt_folder:
                    self.txt_salary_receipt.insert(END,i)
                file_receipt_folder.close()
                
                self.btn_add.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.btn_delete.config(state=NORMAL)
                self.txt_id.config(state='readonly')
                self.btn_print.config(state=NORMAL)
                
                    
        
        except EXCEPTION as e:

            messagebox.showerror('error'f'error due to:{str(e)}')
    def clear(self,event):
        self.btn_add.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.txt_id.config(state=NORMAL)
        self.btn_print.config(state=DISABLED) 
        self.var_id.set("")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_email_id.set("")
        self.var_contact_no.set("")
        self.var_doj.set("")
        self.var_gender.set("")
        self.var_exp.set("")
        self.var_designation.set("")
        self.var_id_proof.set("")
        self.var_age.set("")
        self.var_status.set("")
        self.txt_address.delete("1.0",END)
        self.var_month.set("")
        self.var_year.set("")
        self.var_basic_sal.set("")
        self.var_days.set("")
        self.var_absents.set("")                        
        self.var_medical.set("")
        self.var_pf.set("")
        self.var_conveyance.set("")
        self.var_net_salary.set("")
        self.txt_salary_receipt.delete('1.0',END)
        self.txt_salary_receipt.insert(END,self.receipt_frame)
                

            
    def delete(self,event):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Employee ID must be Required!")
        else:
            
            try:

                con=pymysql.connect(host='localhost',user='root',password='',db='employee_management_system')
                cur=con.cursor()
                cur.execute('select * from emp_salary where emp_id=%s',(self.var_id.get()))
                row=cur.fetchone()
                    #print(rows)
                if row==None:
                    
                    messagebox.showerror("Error","Please Enter proper Employee ID",parent=self.root)
                    
                else:
                    option_box=messagebox.askyesno('Confirm',"Do you Really want to Delete")
                    if option_box==TRUE:
                        cur.execute('DELETE FROM emp_salary WHERE emp_id=%s',(self.var_id.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee ID has Successfully deleted from our Records",parent=self.root)
                    self.clear(event=self.clear)                  
            except EXCEPTION as e:
                messagebox.showerror('error'f'error due to:{str(e)}')
        

    def cal(self,event):
        try:
            if self.var_month.get()=='' or self.var_year.get()=='' or self.var_basic_sal.get()=='' or self.var_days.get()=='' or self.var_absents.get()=='' or self.var_medical.get()=='' or self.var_pf.get()=='' or self.var_conveyance.get()=='':
                messagebox.showerror("Erorr","All field are required here!")
            else:
                per_day=int(self.var_basic_sal.get())/int(self.var_days.get())
                work_day=int(self.var_days.get())-int(self.var_absents.get())
                sal_salary=per_day*work_day
                deduct=int(self.var_medical.get())+int(self.var_pf.get())
                addition=int(self.var_conveyance.get())
                net_sal=sal_salary+addition
                self.var_net_salary.set(str(round(net_sal,2)))
                receipt_frame= f'''\t Azure company, mumbai \n \tAddress: Phoniex market city, floor4
    --------------------------------------------------
    Employee ID\t\t:{self.var_id.get()}
    Employee Name\t\t:{self.var_name.get()}
    Salary of Month\t\t:{self.var_month.get()}-{self.var_year.get()}
    Generated on \t\t: {str(time.strftime('%d / %m / %Y'))}
    --------------------------------------------------
    Total days\t\t: {self.var_days.get()}
    Total present\t\t: {str(int(self.var_days.get())-int(self.var_absents.get()))}  
    Total Absent\t\t: {self.var_absents.get()}
    conveyance\t\t: {self.var_conveyance.get()}
    Medical\t\t: {self.var_medical.get()} 
    Provident Fund\t\t: {self.var_pf.get()} 
    Gross payement\t\t: {self.var_basic_sal.get()}
    Net Salary\t\t: {self.var_net_salary.get()}
    --------------------------------------------------
    '''         
                self.txt_salary_receipt.delete('1.0',END)
                self.txt_salary_receipt.insert(END,receipt_frame)
        except ValueError:
            messagebox.showerror("Error","Enter proper digits or number characters are not allowed")    

    
    def add(self,event):

        if self.var_id.get()=="" or self.var_id_proof.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror('Error','Please enter all the required fields')
        elif len(self.var_contact_no.get())!=10:
            messagebox.showerror("Error","Please Enter proper phone number")
        
        else:
        
            try:

                con=pymysql.connect(host='localhost',user='root',password='',db='employee_management_system')
                cur=con.cursor()
                cur.execute('select * from emp_salary where emp_id=%s',(self.var_id.get()))
                row=cur.fetchone()
                #print(rows)
                if row!=None:

                    messagebox.showerror("Error","This employee id has already in our record",parent=self.root)
                
                else:
                    cur.execute("INSERT INTO emp_salary VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_id.get(),
                        self.var_name.get(),
                        self.var_dob.get(),
                        self.var_email_id.get(),
                        self.var_contact_no.get(),
                        self.var_doj.get(),
                        self.var_gender.get(),
                        self.var_exp.get(),
                        self.var_designation.get(),
                        self.var_id_proof.get(),
                        self.var_age.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_basic_sal.get(),
                        self.var_days.get(),
                        self.var_absents.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_conveyance.get(),
                        self.var_net_salary.get(),
                        self.var_id.get()+'.txt'
                    )
                    )
                    con.commit()
                    con.close()
                    file_receipt_folder=open('Salary_receipt/'+str(self.var_id.get())+'.txt','w')
                    file_receipt_folder.write(self.txt_salary_receipt.get('1.0',END))
                    file_receipt_folder.close()
                    txtfile=open('Salary_receipt/'+str(self.var_id.get())+'.txt','r')
                    for x in txtfile:
                        self.pdf.cell(200,10,txt=x,ln=1,align='c')
                    self.pdf.output('Salary_receipt/'+str(self.var_id.get())+'.pdf')
                    messagebox.showinfo("succees","record has been added")
                    self.btn_print.config(state=NORMAL)

            except EXCEPTION as e:
                messagebox.showerror('error',f'error due to:{str(e)}')
    def update(self,event):
        
        if self.var_id.get()=="" or self.var_id_proof.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror('Erorr','All details are Mandatory')
        elif len(self.var_contact_no.get())!=10:
            messagebox.showerror("Error","Please enter proper phone number")
        
        else:
        
            try:

                con=pymysql.connect(host='localhost',user='root',password='',db='employee_management_system')
                cur=con.cursor()
                cur.execute('select * from emp_salary where emp_id=%s',(self.var_id.get()))
                row=cur.fetchone()
                #print(rows)
                if row==None:

                    messagebox.showerror("Error","This employee id is invalid try with different employee id",parent=self.root)
                
                else:
                    cur.execute("UPDATE emp_salary SET emp_name=%s, emp_dob=%s, emp_email_id=%s, emp_contactno=%s, emp_doj=%s, emp_gender=%s, emp_experience=%s, emp_designation=%s, emp_id_proof=%s, emp_age=%s, emp_status=%s, emp_address=%s, emp_month=%s, emp_year=%s, emp_basic_salary=%s, emp_totaldays=%s, emp_absents=%s, emp_medical=%s, emp_pf=%s, emp_conveyance=%s, emp_netsalary=%s, emp_salary_receipt=%s WHERE emp_id=%s",
                    (
                        self.var_name.get(),
                        self.var_dob.get(),
                        self.var_email_id.get(),
                        self.var_contact_no.get(),
                        self.var_doj.get(),
                        self.var_gender.get(),
                        self.var_exp.get(),
                        self.var_designation.get(),
                        self.var_id_proof.get(),
                        self.var_age.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_basic_sal.get(),
                        self.var_days.get(),
                        self.var_absents.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_conveyance.get(),
                        self.var_net_salary.get(),
                        self.var_id.get()+'.txt',
                        self.var_id.get()
                    )
                    )
                    con.commit()
                    con.close()
                    file_receipt_folder=open('Salary_receipt/'+str(self.var_id.get())+'.txt','w')
                    file_receipt_folder.write(self.txt_salary_receipt.get('1.0',END))
                    file_receipt_folder.close()
                    messagebox.showinfo("succees","Record has Updated Successfully")
                    self.btn_print.config(state=NORMAL)

            except EXCEPTION as e:
                messagebox.showerror('error',f'error due to:{str(e)}')
    
    
        
        
    
    def check_connection(self):
        try:

            con=pymysql.connect(host='localhost',user='root',password='',db='employee_management_system')
            cur=con.cursor()
            cur.execute('select * from emp_salary')
            rows=cur.fetchall()
            print(rows)


        except EXCEPTION as e:
            messagebox.showerror('error',f'error due to:{str(e)}')
    
    def print_receipt(self):
        file_receipt=tempfile.mktemp(".txt")
        open(file_receipt,'w').write(self.txt_salary_receipt.get('1.0',END))
        os.startfile(file_receipt,'print')

    
    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='employee_management_system')
            cur=con.cursor()
            cur.execute('select * from emp_salary')
            rows=cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())

            for row in rows:
                self.employee_tree.insert('',END,value=row)
            con.close()
        except EXCEPTION as e:
            messagebox.showerror('error',f'error due to:{str(e)}')
    
    def employee_frame(self):
        self.root2=Toplevel(self.root)

        app_width=900
        app_height=500

        screen_width=self.root2.winfo_screenwidth()
        screen_height=self.root2.winfo_screenheight()

        x=(screen_width/2)-(app_width/2)
        y=(screen_height/2)-(app_height/2)

        self.root2.title("Employee Payroll Management")
        self.root2.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.root2.config(bg='white')
        self.root2.resizable(True,True)
        
        title=Label(self.root2,text='All Employee details',font=('Times New Roman',20,BOLD),bg='gold',fg='Black',anchor='w',padx=5).pack(fill=X,side=TOP)
        self.root2.focus_force()
        
        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)


        self.employee_tree=ttk.Treeview(self.root2,columns=("emp_id","emp_name", "emp_dob", "emp_email_id", "emp_contactno", "emp_doj", "emp_gender", "emp_experience", "emp_designation", "emp_id_proof", "emp_age", "emp_status", "emp_address", "emp_month", "emp_year", "emp_basic_salary", "emp_totaldays", "emp_absents", "emp_medical", "emp_pf", "emp_conveyance", "emp_netsalary", "emp_salary_receipt"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('emp_id',text='Eid')
        self.employee_tree.heading('emp_name',text='Name')
        self.employee_tree.heading('emp_dob',text='Date of Birth')
        self.employee_tree.heading('emp_email_id',text='Email Id')
        self.employee_tree.heading('emp_contactno',text='Contact no')
        self.employee_tree.heading('emp_doj',text='Date of Joining')
        self.employee_tree.heading('emp_gender',text='Gender')
        self.employee_tree.heading('emp_experience',text='Experience')
        self.employee_tree.heading('emp_designation',text='Designation')
        self.employee_tree.heading('emp_id_proof',text='Id proof')
        self.employee_tree.heading('emp_age',text='Age')
        self.employee_tree.heading('emp_status',text='Status')
        self.employee_tree.heading('emp_address',text='Address')
        self.employee_tree.heading('emp_month',text='Month')
        self.employee_tree.heading('emp_year',text='Year')
        self.employee_tree.heading('emp_basic_salary',text='Basic Salary')
        self.employee_tree.heading('emp_totaldays',text='Total days')
        self.employee_tree.heading('emp_absents',text='Absent')
        self.employee_tree.heading('emp_medical',text='Medical')
        self.employee_tree.heading('emp_pf',text='Provident fund')
        self.employee_tree.heading('emp_conveyance',text='Conveyance')
        self.employee_tree.heading('emp_netsalary',text='Netsalary')
        self.employee_tree.heading('emp_salary_receipt',text='salary receipt')
        self.employee_tree["show"]='headings'

        self.employee_tree.column('emp_id',width=150)
        self.employee_tree.column('emp_name',width=150)
        self.employee_tree.column('emp_dob',width=150)
        self.employee_tree.column('emp_email_id',width=150)
        self.employee_tree.column('emp_contactno',width=150)
        self.employee_tree.column('emp_doj',width=150)
        self.employee_tree.column('emp_gender',width=150)
        self.employee_tree.column('emp_experience',width=150)
        self.employee_tree.column('emp_designation',width=150)
        self.employee_tree.column('emp_id_proof',width=150)
        self.employee_tree.column('emp_age',width=150)
        self.employee_tree.column('emp_status',width=150)
        self.employee_tree.column('emp_address',width=150)
        self.employee_tree.column('emp_month',width=150)
        self.employee_tree.column('emp_year',width=150)
        self.employee_tree.column('emp_basic_salary',width=150)
        self.employee_tree.column('emp_totaldays',width=150)
        self.employee_tree.column('emp_absents',width=150)
        self.employee_tree.column('emp_medical',width=150)
        self.employee_tree.column('emp_pf',width=150)
        self.employee_tree.column('emp_conveyance',width=150)
        self.employee_tree.column('emp_netsalary',width=150)
        self.employee_tree.column('emp_salary_receipt',width=150)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
        
        
        self.root2.mainloop()


root=Tk()
emp=empolyee_payroll(root)
root.mainloop()

