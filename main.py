from tkinter import *
from tkinter import ttk
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("IIT Ashram")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="IIT Ashram",bd=10,relief=GROOVE,font=("times new roman",40,"bold","italic"),bg="white",fg="blue")
        title.pack(side=TOP,fill=X)


    #=======Manage Frame=====


        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#1560BD")
        Manage_Frame.place(x=20,y=100,width=450,height=560)


        m_title=Label(Manage_Frame,text="Manage Students",bg="#1560BD",fg="white",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=5)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="#1560BD",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=5,sticky="w")

        txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=FLAT)
        txt_Roll.grid(row=1,column=1,padx=5,pady=10,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="#1560BD",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=5,sticky="w")

        txt_name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=SUNKEN)
        txt_name.grid(row=2, column=1, padx=5, pady=10, sticky="w")

        lbl_Email = Label(Manage_Frame, text="E-Mail", bg="#1560BD", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=5, sticky="w")

        txt_Email = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, padx=5, pady=10, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="#1560BD", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=5, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,font=("times new roman", 13, "bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=5,pady=10)

        lbl_Contact = Label(Manage_Frame, text="Contact", bg="#1560BD", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=5, sticky="w")

        txt_Contact = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, padx=5, pady=10, sticky="w")

        lbl_Address = Label(Manage_Frame, text="Address", bg="#1560BD", fg="white",font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=6, column=0, pady=10, padx=5, sticky="w")

        txt_Address=Text(Manage_Frame,width=30,height=6,font=("",10))
        txt_Address.grid(row=6,column=1,pady=20,padx=5,sticky="w")

#============Button Frame=========

        btn_Frame = Frame(Manage_Frame,bd=0, relief=RIDGE, bg="#1560BD")
        btn_Frame.place(x=40,y=480, width=380)

        Addbtn=Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=5, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10).grid(row=0, column=1, padx=5, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10).grid(row=0, column=2, padx=5, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10).grid(row=0, column=3, padx=5, pady=10)


        # ======Detail Frame======

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#1560BD")
        Detail_Frame.place(x=500, y=100, width=800, height=560)

        lbl_search=Label(Detail_Frame, text="Search By:", bg="#1560BD", fg="white",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=5, sticky="w")
        combo_search = ttk.Combobox(Detail_Frame,width=10, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Roll", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=5, pady=10)

        txt_search = Entry(Detail_Frame, font=("times new roman", 10, "bold"), bd=4, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=5, pady=10, sticky="w")
        searchbtn = Button(Detail_Frame, text="Search", width=10,pady=5).grid(row=0, column=3, padx=5, pady=10)
        showallbtn = Button(Detail_Frame, text="Show all", width=10,pady=5).grid(row=0, column=4, padx=5, pady=10)

#=======Table frame======
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#1560BD")
        Table_Frame.place(x=10,y=70,width=760,height=480)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("Roll",text="Roll No.")
        Student_table.heading("Name", text="Name")
        Student_table.heading("Email", text="Email")
        Student_table.heading("Gender", text="Gender")
        Student_table.heading("Contact", text="Contact")
        Student_table.heading("Address", text="Address")
        Student_table["show"]='headings'
        Student_table.column("Roll",width=50)
        Student_table.column("Name", width=150)
        Student_table.column("Email", width=150)
        Student_table.column("Gender", width=100)
        Student_table.column("Contact", width=150)
        Student_table.column("Address", width=200)

        Student_table.pack(fill= BOTH,expand=1)

root=Tk()
ob=Student(root)
root.mainloop()
