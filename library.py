from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox

class Library:

    def __init__(self,root):
        self.root=root
        self.root.title("Libray Management Systems")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="powder blue")

        MType=StringVar()
        Ref=StringVar()
        Firstname=StringVar()
        surname=StringVar()
        Address=StringVar()
        MobileNo=StringVar()
        BookID=StringVar()
        BookTitle=StringVar()
        DateBorrowed=StringVar()
        DateDue=StringVar()
        SellingPrice=StringVar()
        LateReturnFine=StringVar()
        Prescription=StringVar()

        def iReset():
            MType.set("")
            Ref.set("")
            Firstname.set("")
            surname.set("")
            Address.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            LateReturnFine.set("")
            self.txtFrameDetail.delete("1.0",END)
            self.txtDisplayR.delete("1.0",END)
            
        def iDelete():    
            iReset()
            self.txtDisplayR.delete("1.0",END)

        def iExit():
            iExit= tkinter.messagebox.askyesno ("Library Management System","confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return
        def iDisplayData():
            self.txtFrameDetail.insert(END,"\t"+MType.get()+"\t"+Ref.get()+"\t\t"+Firstname.get()+"\t\t"+surname.get()+"\t\t"
                                       +Address.get()+"\t\t"+BookTitle.get()+"\t\t"+DateBorrowed.get()+"\t")
            #iReceipt()
        def iReceipt():
            self.txtDisplayR.insert(END,"Member Type:  \t\t" +MType.get() + "\n")
            self.txtDisplayR.insert(END,"Ref No:  \t\t" +  Ref.get() + "\n")
            self.txtDisplayR.insert(END,"Firstname:  \t\t" +   Firstname.get() + "\n")
            self.txtDisplayR.insert(END,"surname:  \t\t" +surname.get() + "\n")
            self.txtDisplayR.insert(END,"Address:  \t\t" +Address.get() + "\n")
            self.txtDisplayR.insert(END,"MobileNo:  \t\t" +MobileNo.get() + "\n")
            self.txtDisplayR.insert(END,"BookID:  \t\t" + BookID.get() + "\n")
            self.txtDisplayR.insert(END,"Book Title:  \t\t" +BookTitle.get() + "\n")
            self.txtDisplayR.insert(END,"DateBorrowed:  \t\t" + DateBorrowed.get() + "\n")
#==========================================================================framework====================================================================================
        MainFrame =Frame(self.root)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,width=1350,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle = Label(TitleFrame,width = 39,font=('arial',40,'bold'),text="\tLibrary Managment Systems\t",padx=12)
        self.lblTitle.grid()

        ButtonFrame= Frame(MainFrame,bd =20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail=Frame(MainFrame,bd=20,width=1350, height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20, width= 1300 ,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800,height=300, padx=20, relief=RIDGE,font=("arial",12,"bold"),
                                   text="Library membership Info:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT= LabelFrame(DataFrame , bd=10, width=450,height=300,padx=20 , relief=RIDGE ,font=("arial",12,"bold"),
                                   text="book details:")
        DataFrameRIGHT.pack(side=RIGHT)
#===============================================================================================================================================================

        self.lblMemberType= Label(DataFrameLEFT, font=("arial",12,"bold"), text="Member type:",padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)

        self.cboMemberType=ttk.Combobox(DataFrameLEFT,state="readonly",textvariable= MType,
                                        font=("arial",12,"bold"), width=23)
        self.cboMemberType['value']=("","student",'lecturer')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1)

        self.lblBookID=Label(DataFrameLEFT, font=("arial",12,"bold"), text="BookID",padx=2,pady=2)
        self.lblBookID.grid(row=0,column=2,sticky=W)
        self.txtBookID=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=BookID, width=25)
        self.txtBookID.grid(row=0,column=3)

        self.lblRef=Label(DataFrameLEFT, font=("arial",12,"bold"), text="Reference No:",padx=2,pady=2)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.txtRef=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=Ref, width=25)
        self.txtRef.grid(row=1,column=1)

        self.lblBookTitle=Label(DataFrameLEFT, font=("arial",12,"bold"), text="BookTitle:",padx=2,pady=2)
        self.lblBookTitle.grid(row=1,column=2,sticky=W)
        self.txtBookTitle=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=BookTitle, width=25)
        self.txtBookTitle.grid(row=1,column=3)

        self.lblFirstname=Label(DataFrameLEFT, font=("arial",12,"bold"), text="Firstname:",padx=2,pady=2)
        self.lblFirstname.grid(row=2,column=0,sticky=W)
        self.txtFirstname=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=Firstname, width=25)
        self.txtFirstname.grid(row=2,column=1)

        self.lblDateBorrowed=Label(DataFrameLEFT, font=("arial",12,"bold"), text="Data Borrowed:",padx=2,pady=2)
        self.lblDateBorrowed.grid(row=2,column=2,sticky=W)
        self.txtDateBorrowed=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable= DateBorrowed ,width=25)
        self.txtDateBorrowed.grid(row=2,column=3)

        self.lblsurname=Label(DataFrameLEFT, font=("arial",12,"bold"), text="surname:",padx=2,pady=2)
        self.lblsurname.grid(row=3,column=0,sticky=W)
        self.txtsurname=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=surname, width=25)
        self.txtsurname.grid(row=3,column=1)

        self.lblDateDue=Label(DataFrameLEFT, font=("arial",12,"bold"), text="Date Due:",padx=2,pady=2)
        self.lblDateDue.grid(row=3,column=2,sticky=W)
        self.txtDateDue=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=DateDue, width=25)
        self.txtDateDue.grid(row=3,column=3)

        self.lblAddress=Label(DataFrameLEFT, font=("arial",12,"bold"), text="Address:",padx=2,pady=2)
        self.lblAddress.grid(row=4,column=0,sticky=W)
        self.txtAddress=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=Address ,width=25)
        self.txtAddress.grid(row=4,column=1)

        self.lblLateReturnFine=Label(DataFrameLEFT, font=("arial",12,"bold"), text="Late Return Fine:",padx=2,pady=2)
        self.lblLateReturnFine.grid(row=4,column=2,sticky=W)
        self.txtLateReturnFine=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=LateReturnFine ,width=25)
        self.txtLateReturnFine.grid(row=4,column=3)

        self.lblMobileNo=Label(DataFrameLEFT, font=("arial",12,"bold"), text="MobileNo:",padx=2,pady=2)
        self.lblMobileNo.grid(row=5,column=0,sticky=W)
        self.txtMobileNo=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=MobileNo, width=25)
        self.txtMobileNo.grid(row=5,column=1)

        self.lblSellingPrice=Label(DataFrameLEFT, font=("arial",12,"bold"), text="Selling Price:",padx=2,pady=2)
        self.lblSellingPrice.grid(row=5,column=2,sticky=W)
        self.txtSellingPrice=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=SellingPrice, width=25)
        self.txtSellingPrice.grid(row=5,column=3)
        #======================================================widget===================================================================
        self.txtDisplayR=Text(DataFrameRIGHT,font=("arial",12,"bold"), width=32, height=13 ,padx=8,pady=20)
        self.txtDisplayR.grid(row=0,column=2)
        #=======================================================listbox==================================================================
    
        ListOfBooks=['Story of My Life','Three Mans in a Boat','The Great Gateby','The Secret Garden','Alice Adventure',
                     'Goodnight Moon','The Borrowers','Harry Potter Series','Black Beauty','James and Giant Peach']
        def SelectedBook(evt):
            values=str(booklist.get(booklist.curselection()))
            print(values)
            w = values

            if (w =='Story of My Life' ):
                BookID.set("ISBN 7458796554")
                BookTitle.set("Hellen Keller")
                LateReturnFine.set("Rs 20")
                SellingPrice.set("Rs 500")
                iReceipt()
                
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
            elif (w =='Three Mans in a Boat' ):
                BookID.set("ISBN 7478466784")
                BookTitle.set("Three friends and a dog")
                LateReturnFine.set("Rs 16")
                SellingPrice.set("Rs 120")
                iReceipt()
                
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
            elif (w =='The Great Gateby'):
                BookID.set("ISBN 7478466444")
                BookTitle.set("The Gateby")
                LateReturnFine.set("Rs 10")
                SellingPrice.set("Rs 400")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
            elif (w =='The Secret Garden' ):
                BookID.set("ISBN 7478466999")
                BookTitle.set("Beauty of Nature")
                LateReturnFine.set("Rs 15")
                SellingPrice.set("Rs 350")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
            elif (w =='Alice Adventure' ):
                BookID.set("ISBN 7478466000")
                BookTitle.set("WonderLand")
                LateReturnFine.set("Rs 20")
                SellingPrice.set("Rs 360")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
            elif (w =='Goodnight Moon' ):
                BookID.set("ISBN 7478409666")
                BookTitle.set("Goodnight Moon")
                LateReturnFine.set("Rs 10")
                SellingPrice.set("Rs 540")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
            elif (w =='The Borrowers' ):
                BookID.set("ISBN 7478466444")
                BookTitle.set("The Borrower")
                LateReturnFine.set("Rs 7")
                SellingPrice.set("Rs 560")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)      
            elif (w ==' Harry Potter Series' ):
                BookID.set("ISBN 7478678333")
                BookTitle.set("Magical World")
                LateReturnFine.set("Rs 50")
                SellingPrice.set("Rs 960")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
            elif (w =='Black Beauty' ):
                BookID.set("ISBN 7678423111")
                BookTitle.set("Fairy Tales")
                LateReturnFine.set("Rs 12")
                SellingPrice.set("Rs 360")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
            elif (w =='James and Giant Peach' ):
                BookID.set("ISBN 7478465778")
                BookTitle.set(" Huge")
                LateReturnFine.set("Rs 10")
                SellingPrice.set("Rs 160")
                iReceipt()
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=7)
                d3=(d1 + d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                
        booklist = Listbox(DataFrameRIGHT, width=20, height=12,font=('arial',12,'bold'))
        booklist.bind('<<ListboxSelect>>',SelectedBook)
        booklist.grid(row=0,column=0,padx=8)
        
        for items in ListOfBooks:
            booklist.insert(END,items)
            
 #=====================================================label=========================================================================   
        self.lblLabel = Label(FrameDetail, font =('arial',10,'bold'),pady=8,
             text="Member Type\t\t  Reference No\t  Firstname\t surname\t Address\t\t Book Title\t\t  Date Borrowed")
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail=Text(FrameDetail,font=("arial",12,"bold"), width=121, height=4 ,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)

        
 #=========================================================Button=====================================================================
        
        self.btnDisplayData=Button(ButtonFrame, text='Display Data', font=("arial",12,"bold"),width=30,bd=4,
                                   command=iDisplayData)
        self.btnDisplayData.grid(row=0,column=0)
       
        self.btnDelete=Button(ButtonFrame, text='Delete', font=("arial",12,"bold"),width=30,bd=4,command= iDelete)
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame, text='Reset', font=("arial",12,"bold"),width=30,bd=4, command =iReset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame, text='Exit', font=("arial",12,"bold"),width=30,bd=4, command=iExit)
        self.btnExit.grid(row=0,column=3)
    

if __name__=="__main__":
    root =Tk()
    application= Library(root)
    root.mainloop()
