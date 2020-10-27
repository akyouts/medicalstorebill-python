from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from datetime import datetime
class Medic_soft:
    def __init__(self,root):
        self.name=StringVar()
        self.quantity=IntVar()
        self.price=DoubleVar()
        self.composition=StringVar()
        self.rackno=IntVar()
        self.columnno=IntVar()
        self.date=StringVar()
        self.ser_med=StringVar()
        self.ser=IntVar()
        self.customername=StringVar()
        self.customerno=IntVar()
        self.cuatomerage=IntVar()
        self.medlist=[]
        self.billprice=0
        #=====Heading
        self.heading=Label(root,text="Medical Store Management",font=("times new roman",30,"bold"),bg="black",fg="white")
        self.heading.pack(side=TOP,fill=BOTH)
        #=====Add medicine frame
        self.med=Frame(root,height=380,width=350,bd=5,background="grey")
        self.med.grid_propagate(0)
        self.med.place(x=10,y=55)
        self.med_name_lbl=Label(self.med,text="Medicine Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        self.med_name_lbl.grid(row=0,column=0,padx=5,pady=10)
        self.med_name_entry=Entry(self.med,font=("times new roman",15,"bold"),width=18,textvariable=self.name)
        self.med_name_entry.grid(row=0,column=1,padx=5,pady=10)
        self.med_quantity_lbl = Label(self.med, text="Quantity", font=("times new roman", 15, "bold"), bg="white",
                                  fg="black")
        self.med_quantity_lbl.grid(row=1, column=0, padx=5, pady=10,sticky="w")
        self.med_quantity_entry = Entry(self.med, font=("times new roman", 15, "bold"), width=5,textvariable=self.quantity)
        self.med_quantity_entry.grid(row=1, column=1, padx=5, pady=10,sticky="w")
        self.med_price_lbl = Label(self.med, text="Price in Rupees", font=("times new roman", 15, "bold"), bg="white",
                                      fg="black")
        self.med_price_lbl.grid(row=2, column=0, padx=5, pady=10, sticky="w")
        self.med_price_entry = Entry(self.med, font=("times new roman", 15, "bold"), width=5,textvariable=self.price)
        self.med_price_entry.grid(row=2, column=1, padx=5, pady=10, sticky="w")
        self.med_composition_lbl = Label(self.med, text="Composition", font=("times new roman", 15, "bold"),
                                   bg="white",
                                   fg="black")
        self.med_composition_lbl.grid(row=3, column=0, padx=5, pady=10, sticky="w")
        self.med_composition_entry = Entry(self.med, font=("times new roman", 15, "bold"), width=18,textvariable=self.composition)
        self.med_composition_entry.grid(row=3, column=1, padx=5, pady=10, sticky="w")
        self.med_rackno_lbl = Label(self.med, text="Rack Number", font=("times new roman", 15, "bold"),
                                         bg="white",
                                         fg="black")
        self.med_rackno_lbl.grid(row=4, column=0, padx=5, pady=10, sticky="w")
        self.med_rackno_entry = Entry(self.med, font=("times new roman", 15, "bold"), width=5,textvariable=self.rackno)
        self.med_rackno_entry.grid(row=4, column=1, padx=5, pady=10, sticky="w")
        self.med_columnno_lbl = Label(self.med, text="Column Number", font=("times new roman", 15, "bold"),
                                    bg="white",
                                    fg="black")
        self.med_columnno_lbl.grid(row=5, column=0, padx=5, pady=10, sticky="w")
        self.med_columnno_entry = Entry(self.med, font=("times new roman", 15, "bold"), width=5,textvariable=self.columnno)
        self.med_columnno_entry.grid(row=5, column=1, padx=5, pady=10, sticky="w")
        self.med_ex_lbl = Label(self.med, text="Expire Date", font=("times new roman", 15, "bold"),
                                      bg="white",
                                      fg="black")
        self.med_ex_lbl.grid(row=6, column=0, padx=5, pady=10, sticky="w")
        self.med_ex_entry = Entry(self.med, font=("times new roman", 15, "bold"), width=11,
                                        textvariable=self.date)
        self.med_ex_entry.grid(row=6, column=1, padx=5, pady=10, sticky="w")
        #==========Button Frame for information manupilation
        self.buttf=Frame(root,height=55,width=350,background="grey")
        self.buttf.grid_propagate(0)
        self.buttf.place(x=10,y=390)
        self.add_med=Button(self.buttf,text="ADD",font=('time new roman',10,'bold'),command=self.add_medi)
        self.add_med.grid(row=0,column=0,padx=2,pady=10)
        self.bill_med = Button(self.buttf, text="ADD TO BILL", font=('time new roman', 10, 'bold'),command=self.add_to_bill)
        self.bill_med.grid(row=0, column=1, padx=2, pady=10)
        self.delete_med = Button(self.buttf, text="DELETE", font=('time new roman', 10, 'bold'),command=self.delete_med)
        self.delete_med.grid(row=0, column=2, padx=2, pady=10)
        self.clear_med = Button(self.buttf, text="CLEAR", font=('time new roman', 10, 'bold'),command=self.clear)
        self.clear_med.grid(row=0, column=3, padx=2, pady=10)
        self.update_med = Button(self.buttf, text="UPDATE", font=('time new roman', 10, 'bold'),command=self.update)
        self.update_med.grid(row=0, column=4, padx=2, pady=10)
        #==============important info frame
        self.imp_info=Frame(root,height=250,width=350,background="grey")
        self.imp_info.grid_propagate(0)
        self.imp_info.place(x=10,y=448)
        self.imp_infolbl=Label(self.imp_info,text="Important Information:",font=("times new roman",20,"bold underline"),bg="grey")
        self.imp_infolbl.grid(row=0,column=0)
        #self.scrollinfo=Scrollbar(self.imp_info,orient=VERTICAL)
        self.imptxt=Text(self.imp_info,font=('times new roman',10),height=13,width=60,wrap=WORD)
        #self.scrollinfo.pack(side=RIGHT,fill=X)
        #self.scrollinfo.config(command=self.imptxt.yview)
        self.imptxt.grid(row=1,column=0)
        #==============detail frame
        self.detail_frame=Frame(root,height=640,width=975,background="grey")
        self.detail_frame.grid_propagate(0)
        self.detail_frame.place(x=370,y=55)
        self.search_by_lbl=Label(self.detail_frame,text="Search by:",font=('times new roman',20,'bold'),fg='black')
        self.search_by_lbl.grid(row=0,column=0,padx=10,pady=10)
        self.search_by_radio1=Radiobutton(self.detail_frame,text="Composition",value=1,variable=self.ser)
        self.search_by_radio2=Radiobutton(self.detail_frame,text="Name",value=2,variable=self.ser)
        self.search_by_radio1.grid(row=0,column=2,padx=10,pady=10,sticky="w")
        self.search_by_radio2.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        self.search_by_entry=Entry(self.detail_frame,font=("times new roman",10),textvariable=self.ser_med)
        self.search_by_entry.grid(row=0,column=4,padx=10,pady=10)
        self.search_button = Button(self.detail_frame, text="SEARCH",command=self.search)
        self.search_button.grid(row=0, column=5, padx=10, pady=10)
        self.show_button = Button(self.detail_frame, text="SHOW ALL",command=self.fetch_data)
        self.show_button.grid(row=0, column=6, padx=10, pady=10)
        self.billinglbl=Label(self.detail_frame,text="Billing Area",font=("times new Roman",25,"bold"))
        self.billinglbl.grid(row=0,column=8,padx=65)
        #========table frame
        self.table_frame=Frame(self.detail_frame,width=650,height=555,background="white")
        self.table_frame.place(x=10,y=70)
        self.table_frame.pack_propagate(0)
        self.scrolly = Scrollbar(self.table_frame, orient=VERTICAL)
        self.scrollx=Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.med_table=ttk.Treeview(self.table_frame,column=('name','composition','price_unit','quantity','expire_date','rackno','columnno'),show='headings',xscrollcommand=self.scrollx.set,yscrollcomman=self.scrolly.set)
        self.scrollx.pack(side=BOTTOM,fill=X)
        self.scrolly.pack(side=RIGHT,fill=Y)
        self.scrolly.config(command=self.med_table.yview)
        self.scrollx.config(command=self.med_table.xview)
        self.med_table.heading('name',text="NAME")
        self.med_table.heading('composition', text="COMPOSITION")
        self.med_table.heading('price_unit', text="PRICE/UNIT")
        self.med_table.heading('quantity', text="QUANTITY")
        self.med_table.heading('expire_date', text="EXPIRE DATE")
        self.med_table.heading('rackno', text="RACK NO.")
        self.med_table.heading('columnno', text="COLUMN NO.")
        self.med_table.pack(fill=BOTH,expand=1)
        self.med_table.place()
        self.med_table.bind('<ButtonRelease-1>',self.get_cur)
        #================biliing frame
        self.billing_frame=Frame(root,height=400,width=280)
        self.billing_frame.pack_propagate(0)
        self.billing_frame.place(x=1050,y=280)
        self.bill_lbl=Label(self.billing_frame,text="BILL",font=('times new roman',20,'bold'),relief=RAISED,bd=10)
        self.bill_lbl.pack(side=TOP,fill=X)
        self.txtscroll=Scrollbar(self.billing_frame,orient=VERTICAL)
        self.bill_text=Text(self.billing_frame,height=530,width=280,wrap=WORD,yscrollcommand=self.txtscroll.set)
        self.txtscroll.pack(side=RIGHT,fill=Y)
        self.txtscroll.config(command=self.bill_text.yview)
        self.bill_text.pack(fill=BOTH,expand=1)



        #==== billing details frame
        self.b=Frame(root,height=150,width=280,background="grey")
        self.b.grid_propagate(0)
        self.b.place(x=1050,y=125)
        self.cus_name=Label(self.b,text="Customer Name",font=('times new roman',10,'bold'))
        self.cus_name.grid(row=0,column=0,padx=10,pady=10)
        self.cusentry=Entry(self.b,font=('times new roman',10,'bold'),textvariable=self.customername)
        self.cusentry.grid(row=0,column=1)
        self.age_name = Label(self.b, text="Age", font=('times new roman', 10, 'bold'))
        self.age_name.grid(row=1, column=0, padx=10, pady=10,sticky='w')
        self.age=Spinbox(self.b,from_=1,to=100,font=("times new roman",10,'bold'),textvariable=self.cuatomerage)
        self.age.grid(row=1,column=1)
        self.mobile_name = Label(self.b, text="Phone:", font=('times new roman', 10, 'bold'))
        self.mobile_name.grid(row=2, column=0, padx=10, pady=10,sticky="w")
        self.mobileentry = Entry(self.b, font=('times new roman', 10, 'bold'),textvariable=self.customerno)
        self.mobileentry.grid(row=2, column=1)
        self.billgenbutt=Button(self.b,text='GENERATE BILL',command=self.bill_generate)
        self.billgenbutt.grid(row=3,column=0)
        self.billcenbutt = Button(self.b, text='CLEAR BILL',command=self.clear_bill)
        self.billcenbutt.grid(row=3, column=1)


    def add_medi(self):
        if self.name=="" or self.composition=="" or self.quantity==0 or self.date=="" or self.columnno==0 or self.rackno==0:
            messagebox.showerror('Error',"All fields are Required")
        else:
             try:
                 con = pymysql.connect(host='localhost', user='root', password='', database='medical')
                 cur = con.cursor()
                 cur.execute('INSERT INTO med values(%s,%s,%s,%s,%s,%s,%s)', (self.name.get(), self.composition.get(), self.price.get(), self.quantity.get(), self.date.get(),self.rackno.get(),self.columnno.get()))
                 con.commit()
                 con.close()
                 messagebox.showinfo("Success", "Medicine is added")
                 self.fetch_data()
             except pymysql.err.IntegrityError:
                 messagebox.showerror("Error", "This Medicine is already exist can only update or delete the data")

    def delete_med(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='medical')
        cur = con.cursor()
        cur.execute('DELETE FROM med WHERE name=%s',(self.name.get()))
        con.commit()
        con.close()
        self.fetch_data()
    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='medical')
        cur = con.cursor()
        cur.execute('SELECT * FROM med')
        rows=cur.fetchall()
        if len(rows)==0:
            messagebox.showerror("Sorry","No data found")
        else:
            self.med_table.delete(*self.med_table.get_children())
            for row in rows:
                self.med_table.insert('',END,values=row)


        con.commit()
        con.close()
    def search(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='medical')
        cur = con.cursor()
        value = self.ser_med.get()
        if self.ser == 2:
            cur.execute('SELECT * FROM med WHERE name ="'+(value)+'";')
        else:
            cur.execute('SELECT * FROM med WHERE compo = "'+(value)+'";')
        rows = cur.fetchall()
        if len(rows) == 0:
            messagebox.showerror("Sorry", "No data found")
        else:
            self.med_table.delete(*self.med_table.get_children())
            for row in rows:
                self.med_table.insert('', END, values=row)
    def get_cur(self,ev):
        cursor = self.med_table.focus()
        content = self.med_table.item(cursor)
        row = content['values']
        self.name.set(row[0])
        self.composition.set(row[1])
        self.price.set(row[2])
        self.quantity.set(row[3])
        self.date.set(row[4])
        self.rackno.set(row[5])
        self.columnno.set(row[6])
    def clear(self):
        self.name.set("")
        self.composition.set("")
        self.price.set(0.0)
        self.quantity.set(0)
        self.date.set("")
        self.rackno.set(0)
        self.columnno.set(0)
    def update(self):
        con= pymysql.connect(host='localhost',user='root',password='',database="medical")
        cur=con.cursor()

        cur.execute('UPDATE med SET name=%s,compo=%s,price=%s,quantity=%s,date=%s,rackno=%s,columnno=%s WHERE name=%s',(self.name.get(),self.composition.get(),self.price.get(),self.quantity.get(),self.date.get(),self.rackno.get(),self.columnno.get(),self.name.get()))
        con.commit()
        con.close()
    def bill_generate(self):
        if len(self.medlist )==0:
            messagebox.showerror("Sorry Can't able to generate bill","NO iteams added to bill")
        else:
            self.bill_text.delete('1.0', END)
            self.bill_text.insert(END, "********************************\n")
            self.bill_text.insert(END, "   Health City Medical Store   \n")
            self.bill_text.insert(END, "********************************\n")
            da = datetime.now().strftime("%d/%m/%y , %H:%M:%S")
            da = da.split(",")

            self.bill_text.insert(END, "Date:" + (da[0]) + "  ")
            self.bill_text.insert(END, "Time:" + (da[1]) + "  \n")
            self.bill_text.insert(END, "Name:" + str(self.customername.get()) + "  \n")
            self.bill_text.insert(END, "Age:" + str(self.cuatomerage.get()) + "  \n")
            self.bill_text.insert(END, "Phone no:" + str(self.customerno.get()) + "  \n")
            self.bill_text.insert(END, "********************************\n")
            z = 0
            for i in range(len(self.medlist)):
                r = self.medlist[i]
                self.bill_text.insert(END, r[0] + " " + str(r[1]) + " x " + str(r[2]) + "=" + str(r[3]) + "\n")
                z += r[3]
            self.bill_text.insert(END, "********************************\n")
            self.bill_text.insert(END, "********************TOTAL=" + str(z) + "\n")
            self.billprice += z
            self.medlist.clear()
    def clear_bill(self):
        self.bill_text.delete('1.0', END)
        self.customerno.set("")
        self.customername.set("")
        self.cuatomerage.set("")


    def add_to_bill(self):
        if self.name.get()=="" or self.quantity.get()==0 or self.price.get()==0:
            messagebox.showerror("ERROR","All feilds are required")
        else:
            a=[]
            a.append(self.name.get())
            a.append(self.quantity.get())
            a.append(self.price.get())
            x=self.price.get()*self.quantity.get()
            a.append(x)
            self.medlist.append(a)
            messagebox.showinfo("Success",str(len(self.medlist))+" items added to Bill")









root=Tk()
root.geometry("1366x768")
root.title("Soft Medic Store")
obj=Medic_soft(root)
root.mainloop()
