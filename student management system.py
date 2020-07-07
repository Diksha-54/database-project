
# *************************** connection of database **************************************************************

def Connectdb():
    def submitdb():
        global con,mycursor
        host =hostval.get()
        user= userval.get()
        password= passwordval.get()
        try:
            con =pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror("Notification","Data is incorrect :please try again",parent=dbroot)
            return
        try:
            strr = "create database studentmanagementsystem1"
            mycursor.execute(strr)
            strr= "use studentmanagementsystem1"
            mycursor.execute(strr)
            strr = "create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30)," \
                   "address varchar(100),gender varchar(50),dob varchar(30),date varchar(30),time varchar(50))"
            mycursor.execute(strr)
            strr = "alter table studentdata1 modify column id int not null"
            mycursor.execute(strr)
            messagebox.showinfo("Notification", "database created and now you are connected to database....", parent=dbroot)
        except:
            strr = "use studentmanagementsystem1"
            mycursor.execute(strr)


            messagebox.showinfo("Notification","now you are connected to database....",parent=dbroot)
        dbroot.destroy()


    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry("470x200+800+150")
    dbroot.iconbitmap("Student icon.ico")
    dbroot.resizable(False,False)
    dbroot.config(bg="grey")



    #********************* connectdb labels *****************
    hostlabel= Label(dbroot,text=" Enter Host : ",bg="light blue",font=("bold",20),relief=GROOVE,borderwidth=3,width=13,anchor="w")
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text=" Enter User : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    userlabel.place(x=10, y=55)

    passwordlabel = Label(dbroot, text=" Enter Password : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    passwordlabel.place(x=10, y=100)
    #********************* connectdb entry *******************
    hostval=StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=("roman", 15, "bold"), bd=5, textvariable=hostval)
    hostentry.place(x=245,y=10)

    userentry = Entry(dbroot, font=("roman", 15, "bold"), bd=5, textvariable=userval)
    userentry.place(x=245, y=55)

    passwordentry = Entry(dbroot, font=("roman", 15, "bold"), bd=5, textvariable=passwordval)
    passwordentry.place(x=245, y=100)

    #******************* connectdb button *******************
    submitbutton= Button(dbroot,text="Submit",font=("chiller,20,bold"),width=20,height=2,bg="red",bd=5,
                         activebackground="blue",activeforeground="pink",command=submitdb)
    submitbutton.place(x=150,y=150)

    dbroot.mainloop()


#*********************************** add student function *************************************************************

def addstudent():
    def submitadd():
        id= idval.get()
        name= nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime= time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = "insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(strr,(id, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel("Notifications","ID {} Name {} Added succesfully....and want to clean the form".format(id,name),parent=addSroot)
            if(res==True):
                idval.set(' ')
                nameval.set(' ')
                mobileval.set(' ')
                emailval.set(' ')
                addressval.set(' ')
                genderval.set(' ')
                dobval.set(' ')


        except:
            messagebox.showerror("Notifications","ID already exist try another id....",parent=addSroot)

        strr = "select * from studentdata1"
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)



    addSroot = Toplevel(master=DataEntryFrame)
    addSroot.grab_set()
    addSroot.geometry("450x450+140+170")
    addSroot.iconbitmap("Student icon.ico")
    addSroot.resizable(False, False)
    addSroot.config(bg="grey")
    #******************************* addstudent labels ********************
    idlabel = Label(addSroot, text=" Enter ID : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    idlabel.place(x=10, y=10)

    namelabel = Label(addSroot, text=" Enter Name : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    namelabel.place(x=10, y=60)

    mobilelabel = Label(addSroot, text=" Enter Mobile : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    mobilelabel.place(x=10, y=110)

    emaillabel = Label(addSroot, text=" Enter Email : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    emaillabel.place(x=10, y=160)

    addresslabel = Label(addSroot, text=" Enter Address: ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    addresslabel.place(x=10, y=210)

    genderlabel = Label(addSroot, text=" Enter Gender : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    genderlabel.place(x=10, y=260)

    doblabel = Label(addSroot, text=" Enter D.O.B : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    doblabel.place(x=10, y=310)
    #*********************** add student entry ***************
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()



    identry = Entry(addSroot, font=("roman", 15, "bold"), bd=5, textvariable=idval)
    identry.place(x=200, y=10)

    nameentry = Entry(addSroot, font=("roman", 15, "bold"), bd=5, textvariable=nameval)
    nameentry.place(x=200, y=60)

    mobileentry = Entry(addSroot, font=("roman", 15, "bold"), bd=5, textvariable=mobileval)
    mobileentry.place(x=200, y=110)

    emailentry = Entry(addSroot, font=("roman", 15, "bold"), bd=5, textvariable=emailval)
    emailentry.place(x=200, y=160)

    addressentry = Entry(addSroot, font=("roman", 15, "bold"), bd=5, textvariable=addressval)
    addressentry.place(x=200, y=210)

    genderentry = Entry(addSroot, font=("roman", 15, "bold"), bd=5, textvariable=genderval)
    genderentry.place(x=200, y=260)

    dobentry = Entry(addSroot, font=("roman", 15, "bold"), bd=5, textvariable=dobval)
    dobentry.place(x=200, y=310)
    #**************************** add student button ********************
    submitbutton = Button(addSroot, text="Submit", font=("chiller,30,bold"), width=20, height=2, bg="red", bd=5,
                          activebackground="blue", activeforeground="pink",command=submitadd)
    submitbutton.place(x=140, y=380)

    addSroot.mainloop()


#******************************************* search student function **********************************************

def searchstudent():
    def submitbutton():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id!=''):
            strr ="select *from studentdata1 where id=%s"
            mycursor.execute(strr,(id))
            datas=mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(name!= ''):
            strr = "select *from studentdata1 where name=%s"
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(mobile != ''):
            strr = "select *from studentdata1 where mobile=%s"
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(email != ''):
            strr = "select *from studentdata1 where email=%s"
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(address != ''):
            strr = "select *from studentdata1 where address=%s"
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(gender != ''):
            strr = "select *from studentdata1 where gender=%s"
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(dob != ''):
            strr = "select *from studentdata1 where dob=%s"
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = "select *from studentdata1 where addeddate=%s"
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)


    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry("450x450+140+170")
    searchroot.iconbitmap("Student icon.ico")
    searchroot.resizable(False, False)
    searchroot.config(bg="grey")
    #******************************* search student labels ********************
    idlabel = Label(searchroot, text=" Enter ID : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text=" Enter Name : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    namelabel.place(x=10, y=60)

    mobilelabel = Label(searchroot, text=" Enter Mobile : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    mobilelabel.place(x=10, y=110)

    emaillabel = Label(searchroot, text=" Enter Email : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    emaillabel.place(x=10, y=160)

    addresslabel = Label(searchroot, text=" Enter Address: ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    addresslabel.place(x=10, y=210)

    genderlabel = Label(searchroot, text=" Enter Gender : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    genderlabel.place(x=10, y=260)

    doblabel = Label(searchroot, text=" Enter D.O.B : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    doblabel.place(x=10, y=310)

    datelabel = Label(searchroot, text=" Enter Date : ", bg="light blue", font=("bold", 20), relief=GROOVE,
                     borderwidth=3,
                     width=13, anchor="w")
    datelabel.place(x=10, y=360)


    #*********************** search student entry ***************
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval =StringVar()


    identry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=idval)
    identry.place(x=200, y=10)

    nameentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=nameval)
    nameentry.place(x=200, y=60)

    mobileentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=mobileval)
    mobileentry.place(x=200, y=110)

    emailentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=emailval)
    emailentry.place(x=200, y=160)

    addressentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=addressval)
    addressentry.place(x=200, y=210)

    genderentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=genderval)
    genderentry.place(x=200, y=260)

    dobentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=dobval)
    dobentry.place(x=200, y=310)

    dateentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=dateval)
    dateentry.place(x=200, y=360)

    #**************************** add student button ********************
    submitbutton = Button(searchroot, text="Submit", font=("chiller,30,bold"), width=20, height=2, bg="red", bd=5,
                          activebackground="blue", activeforeground="pink",command=submitbutton)
    submitbutton.place(x=140, y=405)

    searchroot.mainloop()

#************************************ delete function ****************************************************************
def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content["values"][0]
    strr = "delete from studentdata1 where id=%s"
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo("Notifications","Id {} deleted successfully...".format(pp))
    strr = "select *from studentdata1"
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


#******************************************* update function **********************************************************
def updatestudent():
    def submitbutton():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = "update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s"
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo("Notification","Id {} modified successfully...".format(id),parent=updateroot)
        strr = "select *from studentdata1"
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)


    updateroot = Toplevel()
    updateroot.grab_set()
    updateroot.geometry("450x500+140+170")
    updateroot.iconbitmap("Student icon.ico")
    updateroot.resizable(False, False)
    updateroot.config(bg="grey")
    # ******************************* update student labels ********************
    idlabel = Label(updateroot, text=" Enter ID : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                    width=13, anchor="w")
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text=" Enter Name : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                      width=13, anchor="w")
    namelabel.place(x=10, y=60)

    mobilelabel = Label(updateroot, text=" Enter Mobile : ", bg="light blue", font=("bold", 20), relief=GROOVE,
                        borderwidth=3,
                        width=13, anchor="w")
    mobilelabel.place(x=10, y=110)

    emaillabel = Label(updateroot, text=" Enter Email : ", bg="light blue", font=("bold", 20), relief=GROOVE,
                       borderwidth=3,
                       width=13, anchor="w")
    emaillabel.place(x=10, y=160)

    addresslabel = Label(updateroot, text=" Enter Address: ", bg="light blue", font=("bold", 20), relief=GROOVE,
                         borderwidth=3,
                         width=13, anchor="w")
    addresslabel.place(x=10, y=210)

    genderlabel = Label(updateroot, text=" Enter Gender : ", bg="light blue", font=("bold", 20), relief=GROOVE,
                        borderwidth=3,
                        width=13, anchor="w")
    genderlabel.place(x=10, y=260)

    doblabel = Label(updateroot, text=" Enter D.O.B : ", bg="light blue", font=("bold", 20), relief=GROOVE, borderwidth=3,
                     width=13, anchor="w")
    doblabel.place(x=10, y=310)

    datelabel = Label(updateroot, text=" Enter Date : ", bg="light blue", font=("bold", 20), relief=GROOVE,
                      borderwidth=3,
                      width=13, anchor="w")
    datelabel.place(x=10, y=360)

    timelabel = Label(updateroot, text=" Enter Time : ", bg="light blue", font=("bold", 20), relief=GROOVE,
                      borderwidth=3,
                      width=13, anchor="w")
    timelabel.place(x=10, y=410)

    # *********************** update student entry ***************
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=idval)
    identry.place(x=200, y=10)

    nameentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=nameval)
    nameentry.place(x=200, y=60)

    mobileentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=mobileval)
    mobileentry.place(x=200, y=110)

    emailentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=emailval)
    emailentry.place(x=200, y=160)

    addressentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=addressval)
    addressentry.place(x=200, y=210)

    genderentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=genderval)
    genderentry.place(x=200, y=260)

    dobentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=dobval)
    dobentry.place(x=200, y=310)


    dateentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=dateval)
    dateentry.place(x=200, y=360)

    timeentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=timeval)
    timeentry.place(x=200, y=410)

    # **************************** update student button ********************
    submitbutton = Button(updateroot, text="Submit", font=("chiller,30,bold"), width=20, height=2, bg="red", bd=5,
                          activebackground="blue", activeforeground="pink", command=submitbutton)
    submitbutton.place(x=140, y=455)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content["values"]
    if(len(pp)!=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])


    updateroot.mainloop()

#****************************************** show function ********************************************************
def showstudent():
    strr = "select *from studentdata1"
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

#****************************************** export function ********************************************************
def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg =studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content["values"]
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),\
        gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
        dd = ["Id","Name","Mobile","Email","Address","Gender","D.O.B","Added Date","Added Time"]
        df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
        paths = r'{}.csv'.format(ff)
        df.to_csv(paths,index=False)
        messagebox.showinfo("Notification","Student data is saved {}".format(paths))


#************************************** exit student function ********************************************************
def exitstudent():
    res=messagebox.askokcancel("notification","do you want to exit?")
    if(res==True):
        root.destroy()



#************************************************** tick slider*******************************************************
def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%Y")
    clock.config(text="Date : "+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)

#************************************ introslider ******************************************************************
import random
color=["red","blue","pink","gold","green","orange","grey","brown","yellow"]
def introlabelcolortick():
    fg = random.choice(color)
    SliderLabel.config(fg=fg)
    SliderLabel.after(50,introlabelcolortick)

def introlabeltick():#SLIDER FUNCTION
    global count,text
    if(count>=len(ss)):
        count= 0
        text= ""
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200,introlabeltick)
#**********************************************************************
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
import time #time module
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql


root=Tk()
root.title("Student Management System")
root.config(bg='sky blue')
root.geometry("1174x700+200+50")
root.iconbitmap("Student icon.ico")
root.resizable(False,False)#cant change the width and height now.

#******************************************** FRAMES *******************************************************************

##*************************** dataentry frame  ****************************************
DataEntryFrame = Frame(root,bg="light grey",relief=GROOVE,borderwidth=5)#detalentry frame
DataEntryFrame.place(x=10,y=85,width=500,height=600)

frontlabel =Label(DataEntryFrame,text="**********************Welcome**********************",width=30,font=("arial",22,"bold"),bg="light grey")
frontlabel.pack(side=TOP,expand=True)
#BUTTON
addbtn = Button(DataEntryFrame,text="1. Add Student",width=17,font=("chiller", 30, "bold"),bd=6,bg="pink",
                activebackground="yellow",activeforeground="red",relief=RIDGE,command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text="2. Search Student",width=17,font=("chiller", 30, "bold"),bd=6,bg="pink",
                activebackground="yellow",activeforeground="red",relief=RIDGE,command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text="3. Delete Student",width=17,font=("chiller", 30, "bold"),bd=6,bg="pink",
                activebackground="yellow",activeforeground="red",relief=RIDGE,command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text="4. Update Student",width=17,font=("chiller", 30, "bold"),bd=6,bg="pink",
                activebackground="yellow",activeforeground="red",relief=RIDGE,command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text="5. Show All",width=17,font=("chiller", 30, "bold"),bd=6,bg="pink",
                activebackground="yellow",activeforeground="red",relief=RIDGE,command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text="6. Export Data",width=17,font=("chiller", 30, "bold"),bd=6,bg="pink",
                activebackground="yellow",activeforeground="red",relief=RIDGE,command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text="7. Exit",width=17,font=("chiller", 30, "bold"),bd=6,bg="pink",
                activebackground="yellow",activeforeground="red",relief=RIDGE,command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


##*************************** show frame intro **********************************************

ShowDataFrame = Frame(root,bg="light grey",relief=GROOVE,borderwidth=5)#showdetail frame
ShowDataFrame.place(x=530,y=85,width=634,height=600)

##*********************** show data frame **********************************************************************
style= ttk.Style()
style.configure("Treeview.heading",font=("italic",50),fg="blue",bg="red")
style.configure("Treeview.heading",font=("times new roman",20,"bold"),fg="black",bg="cyan")

scroll_x= Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y= Scrollbar(ShowDataFrame,orient=VERTICAL)

studenttable =Treeview(ShowDataFrame,columns=("Id","Name","Mobile No","Email","Address","Gender","D.O.B","Added Date","Added Time")
                                              ,yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading("Id",text="Id")
studenttable.heading("Name",text="Name")
studenttable.heading("Mobile No",text="Mobile No")
studenttable.heading("Email",text="Email")
studenttable.heading("Address",text="Address")
studenttable.heading("Gender",text="Gender")
studenttable.heading("D.O.B",text="D.O.B")
studenttable.heading("Added Date",text="Added Date")
studenttable.heading("Added Time",text="Added Time")
studenttable["show"]="headings"
studenttable.column("Id",width=100)
studenttable.column("Name",width=200)
studenttable.column("Mobile No",width=200)
studenttable.column("Email",width=300)
studenttable.column("Address",width=200)
studenttable.column("Gender",width=100)
studenttable.column("D.O.B",width=150)
studenttable.column("Added Date",width=150)
studenttable.column("Added Time",width=150)
studenttable.column("Id",width=100)



studenttable.pack(fill=BOTH,expand=1)

#********************************************************** SLIDER *****************************************************
ss="Welcome To Student Management System"
count=0
text=""
#####################################
SliderLabel = Label(root,text=ss,font=("chiller",30),relief=RIDGE,borderwidth=4,width=35,bg="light blue")
SliderLabel.place(x=250,y=0)
introlabeltick()#calling function introlabelticks
introlabelcolortick()#calling color function
#***************************************************** slider-CLOCK ****************************************************

clock=Label(root,font=("times",14,"bold"),relief=RIDGE,borderwidth=4,bg="light blue")
clock.place(x=0,y=0)
tick()#calling function ticks

#************************************** connect to database ************************************************************

connectbutton= Button(root,text="Connect To Database",width=16,height=2,font=("chiller",20,"italic bold"),relief=RIDGE, borderwidth=9,bg="green",
                     activebackground="blue",activeforeground="red",command=Connectdb)#??????????
connectbutton.place(x=960,y=0)


root.mainloop()

