from multiprocessing.sharedctypes import Value
from tkinter import * #importing everything from tkinter(made to use powerful GUI applications)
from tkinter import ttk #Tkinter provides the ttk package that is used to style the widget's property and its look and feel
from PIL import Image,ImageTk
from pip import main #py -m pip install pillow
import random

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0") #to take full window size
        self.root.title("Shop Billing Software")

        #================Variables=============================

        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.billno=StringVar()
      
        z=random.randint(1000,9990)
        self.billno.set(z)

        #self.search=StringVar()
        self.c_email=StringVar()
        self.searchbill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.taxinput=StringVar()
        self.total=StringVar()

        #Product categories list

        self.category=["select options","clothing","Lifestyle","Mobiles"]

        #subcatclothing

        self.subcatclothing=["Shirt","T-Shirt","pant"]
        self.pant=["Levis","Roadster","Mufti","Spykar"]
        self.price_levis=3000
        self.price_mufti=4000
        self.price_spykar=5000
        self.price_roadster=5000

        self.Shirt=["Peter England","Louis Phillips","park avenue"]
        self.price_peter=2100
        self.price_phillips=4000
        self.price_parkavenue=3100

        self.Tshirt=["Roadster","polo","jack&Jones"]
        self.price_road=2000
        self.price_polo=4000
        self.price_jj=8000

        self.subcatlifestyle=["Bath soap","Face cream","hair oil"]
        self.bathsoap=["Lux","Dove","Lifeboy","wildstone"]
        self.price_Lux=40
        self.price_Dove=60
        self.price_Lifeboy=70
        self.price_wildstone=50

        self.facecream=["Nivea","Boroplus","Fairnlovely","vicco","Olay","Glamup"]
        self.price_nivea=200
        self.price_boroplus=300
        self.price_fairnlovely=400
        self.price_vicco=250
        self.price_olay=150
        self.price_glamup=800

        self.hairoil=["coconut","Indulekha","patanjali"]
        self.price_coconut=150
        self.price_Indulekha=600
        self.price_patanjali=220

        self.subcatmobiles=["Iphone","samsung","xiome","OnePlus"]

        self.Iphone=['IphoneX','Iphone_11','Iphone_12']
        self.price_IphoneX=70000
        self.price_Iphone_11=60000
        self.price_Iphone_12=80000

        self.samsung=["samsung_8","samsung_A30","samsung_F50"]
        self.price_samsung_8=20000
        self.price_samsung_A30=19000
        self.price_samsung_F50=30000

        self.xiome=["Realme_narzo","Realme_8i","Realme_9"]
        self.price_Realme_narzo=20000
        self.price_Realme_8i=19000
        self.price_Realme_9=15000

        self.oneplus=["oneplus_9","oneplus_8","oneplus_10"]
        self.price_oneplus_9=40000
        self.price_oneplus_8=30000
        self.price_oneplus_10=20000


        #IMAGE 1

        img=Image.open("images/BS0.jpg")
        img=img.resize((450,200),Image.ANTIALIAS) #antialias helps to convert high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img) #self helps to make class variable

        lbl_img=Label(self.root,image=self.photoimg) #we want to show the image on the window with the help of the label
        lbl_img.place(x=0,y=0,width=450,height=200)

       #IMAGE 2


        img_1=Image.open("images/BS1.png")
        img_1=img_1.resize((450,200),Image.ANTIALIAS) #antialias helps to convert high level image to low level image
        self.photoimg_1=ImageTk.PhotoImage(img_1) #self helps to make class variable

        lbl_img_1=Label(self.root,image=self.photoimg_1) #we want to show the image on the window with the help of the label
        lbl_img_1.place(x=450,y=0,width=450,height=200)


        #IMAGE 3

        img_2=Image.open("images/BS2.jpg")
        img_2=img_2.resize((450,200),Image.ANTIALIAS) #antialias helps to convert high level image to low level image
        self.photoimg_2=ImageTk.PhotoImage(img_2) #self helps to make class variable

        lbl_img_2=Label(self.root,image=self.photoimg_2) #we want to show the image on the window with the help of the label
        lbl_img_2.place(x=900,y=0,width=460,height=200)


        lbl_title=Label(self.root,text="A SHOP BILLING SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        lbl_title.place(x=0,y=200,width=1430,height=35)


        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=235,width=1360,height=460)


        #Customer LabelFrame

        cust_Frame=LabelFrame(Main_frame,text="Customer",font=("times new roman",12,"bold"),bg="white",fg="red")
        cust_Frame.place(x=10,y=5,width=310,height=130)

        self.lbl_mob=Label(cust_Frame,text="Mobile No.",font=("times new roman",11,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(cust_Frame,font=("times new roman",11,"bold"),textvariable=self.c_phone,width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lbl_Custname=Label(cust_Frame,text="Name",font=("times new roman",11,"bold"),bg="white",bd=4)
        self.lbl_Custname.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(cust_Frame,font=("times new roman",11,"bold"),textvariable=self.c_name,width=24)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.lbl_Emailid=Label(cust_Frame,text="Email-Id",font=("times new roman",11,"bold"),bg="white",bd=4)
        self.lbl_Emailid.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmailid=ttk.Entry(cust_Frame,font=("times new roman",11,"bold"),textvariable=self.c_email,width=24)
        self.txtEmailid.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        #Product LabelFrame

        product_Frame=LabelFrame(Main_frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        product_Frame.place(x=330,y=5,width=560,height=130)

        #category

        self.lblCategory=Label(product_Frame,text="Select category",font=("times new roman",11,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_category=ttk.Combobox(product_Frame,value=self.category,font=("times new roman",10,"bold"),width=24,state="readonly")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_category.bind("<<ComboboxSelected>>",self.categories)


        # middle image frame

        Middle_Frame=Frame(Main_frame,bg="white")
        Middle_Frame.place(x=310,y=150,width=570,height=200)

        img_10=Image.open("images/BS3.jpg")
        img_10=img_10.resize((310,200),Image.ANTIALIAS) #antialias helps to convert high level image to low level image
        self.photoimg_10=ImageTk.PhotoImage(img_10) #self helps to make class variable

        lbl_img_10=Label(Middle_Frame,image=self.photoimg_10) #we want to show the image on the window with the help of the label
        lbl_img_10.place(x=10,y=10,width=570,height=200)

        img_11=Image.open("images/BS3.jpg")
        img_11=img_11.resize((600,320),Image.ANTIALIAS) #antialias helps to convert high level image to low level image
        self.photoimg_11=ImageTk.PhotoImage(img_11) #self helps to make class variable

        lbl_img_11=Label(Middle_Frame,image=self.photoimg_11) #we want to show the image on the window with the help of the label
        lbl_img_11.place(x=10,y=10,width=570,height=200)
        
        #SubCategory

        self.lbl_Subcategory=Label(product_Frame,font=("times new roman",11,"bold"),bg="white",text="Sub category",bd=4)
        self.lbl_Subcategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.combo_Subcategory=ttk.Combobox(product_Frame,state="readonly",value=[""],font=("times new roman",10,"bold"),width=24)
        self.combo_Subcategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combo_Subcategory.bind("<<ComboboxSelected>>",self.product_add)

        #Product Name

        self.lbl_prodname=Label(product_Frame,font=("times new roman",11,"bold"),bg="white",text="Product name",bd=4)
        self.lbl_prodname.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.combo_prodname=ttk.Combobox(product_Frame,state="readonly",font=("times new roman",10,"bold"),textvariable=self.product,width=24)
        self.combo_prodname.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.combo_prodname.bind("<<ComboboxSelected>>",self.price)

        #Price

        self.lblprice=Label(product_Frame,font=("times new roman",11,"bold"),bg="white",text="Price",bd=4)
        self.lblprice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.comboprice=ttk.Combobox(product_Frame,state="readonly",textvariable=self.prices,font=("times new roman",10,"bold"),width=17)
        self.comboprice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        #Quantity

        self.lblQty=Label(product_Frame,text="Quantity",font=("times new roman",11,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.comboQty=ttk.Combobox(product_Frame,state="readonly",textvariable=self.qty,font=("times new roman",10,"bold"),width=17)
        self.comboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        #search Area

        Search_Frame=Frame(Main_frame,bd=2,bg="white")
        Search_Frame.place(x=900,y=10,width=500,height=35)


        self.lblbill=Label(Search_Frame,text="Bill Number",font=("times new roman",11,"bold"),bg="orangered",fg="white")
        self.lblbill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,font=("times new roman",11,"bold"),textvariable=self.searchbill,width=30)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=3)

        self.Btnsearch=Button(Search_Frame,width=9,text="Search",font=("times new roman",10,'bold'),bg="orangered",fg="white",cursor="hand2")
        self.Btnsearch.grid(row=0,column=2)

        #Right Frame Bill Area

        RightLabelFrame=LabelFrame(Main_frame,text="Bill_Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=900,y=45,width=435,height=395)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="Blue",font=("times new roman",11,"bold"))#because we want to use text field as global only, not as functions
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #Bill Counter LabelFrame

        Bottom_Frame=LabelFrame(Main_frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=180,width=300,height=140)

        
        #Buttons LabelFrame

        Buttons_Frame=LabelFrame(Main_frame,font=("times new roman",12,"bold"),bg="white",fg="red")
        Buttons_Frame.place(x=0,y=370,width=890,height=70)

        # Sub Total

        self.lblSubtotal=Label(Bottom_Frame,text="Sub Total",font=("times new roman",11,"bold"),bg="white",bd=4)
        self.lblSubtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntySubtotal=ttk.Entry(Bottom_Frame,font=("times new roman",10,"bold"),width=21)
        self.EntySubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        #tax

        self.lbltax=Label(Bottom_Frame,text=" Gov Tax",font=("times new roman",11,"bold"),bg="white",bd=4)
        self.lbltax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=("times new roman",10,"bold"),width=21)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

            #total Amount

        self.lblAmount=Label(Bottom_Frame,text=" Total Amount",font=("times new roman",11,"bold"),bg="white",bd=4)
        self.lblAmount.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txt_Amount=ttk.Entry(Bottom_Frame,font=("times new roman",10,"bold"),width=21)
        self.txt_Amount.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # 6 buttons styling

        self.BtnAddtocart=Button(Buttons_Frame,height=3,width=15,text="Add to Cart",font=("times new roman",11,'bold'),bg="orangered",fg="white",cursor="hand2")
        self.BtnAddtocart.grid(row=0,column=0)

        self.genbill=Button(Buttons_Frame,height=3,width=15,text="Generate Bill",font=("times new roman",11,'bold'),bg="orangered",fg="white",cursor="hand2")
        self.genbill.grid(row=0,column=1)

        self.Btnsave=Button(Buttons_Frame,height=3,width=15,text="Save Bill",font=("times new roman",11,'bold'),bg="orangered",fg="white",cursor="hand2")
        self.Btnsave.grid(row=0,column=2)

        self.Btnprint=Button(Buttons_Frame,height=3,width=16,text="Print",font=("times new roman",11,'bold'),bg="orangered",fg="white",cursor="hand2")
        self.Btnprint.grid(row=0,column=3)

        self.Btnclear=Button(Buttons_Frame,height=3,width=15,text="Clear",font=("times new roman",11,'bold'),bg="orangered",fg="white",cursor="hand2")
        self.Btnclear.grid(row=0,column=4)

        self.BtnExit=Button(Buttons_Frame,height=3,width=16,text="Exit",font=("times new roman",11,'bold'),bg="orangered",fg="white",cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()


    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,f"\t Welcome to Tuteja's Mini Mall")
        self.textarea.insert(END,f"\n\n Bill Number:{self.billno.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Customer Phone:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,"\n ============================================")
        self.textarea.insert(END,"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n ============================================")


    def categories(self,event=""):
        if self.combo_category.get()=="clothing":
           self.combo_Subcategory.config(value=self.subcatclothing)
           self.combo_Subcategory.current(0)

        if self.combo_category.get()=="Lifestyle":
           self.combo_Subcategory.config(value=self.subcatlifestyle)
           self.combo_Subcategory.current(0)

        if self.combo_category.get()=="Mobiles":
           self.combo_Subcategory.config(value=self.subcatmobiles)
           self.combo_Subcategory.current(0)

    def product_add(self,event=""):
        if self.combo_Subcategory.get()=="pant":
            self.combo_prodname.config(value=self.pant)
            self.combo_prodname.current(0)

        if self.combo_Subcategory.get()=="Shirt":
            self.combo_prodname.config(value=self.Shirt)
            self.combo_prodname.current(0)

        if self.combo_Subcategory.get()=="T-Shirt":
            self.combo_prodname.config(value=self.Tshirt)
            self.combo_prodname.current(0)

            #Lifestyle

        if self.combo_Subcategory.get()=="Bath soap":
            self.combo_prodname.config(value=self.bathsoap)
            self.combo_prodname.current(0)

        if self.combo_Subcategory.get()=="Face cream":
            self.combo_prodname.config(value=self.facecream)
            self.combo_prodname.current(0)

        if self.combo_Subcategory.get()=="hair oil":
            self.combo_prodname.config(value=self.hairoil)
            self.combo_prodname.current(0)

        #Mobiles

        if self.combo_Subcategory.get()=="Iphone":
            self.combo_prodname.config(value=self.Iphone)
            self.combo_prodname.current(0)

        if self.combo_Subcategory.get()=="samsung":
            self.combo_prodname.config(value=self.samsung)
            self.combo_prodname.current(0)

        if self.combo_Subcategory.get()=="xiome":
            self.combo_prodname.config(value=self.xiome)
            self.combo_prodname.current(0)

        if self.combo_Subcategory.get()=="OnePlus":
            self.combo_prodname.config(value=self.oneplus)
            self.combo_prodname.current(0)

    def price(self,event=""):

        #Pant

        if self.combo_prodname.get()=="Levis":
            self.comboprice.config(value=self.price_levis)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="Roadster":
            self.comboprice.config(value=self.price_roadster)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="Mufti":
            self.comboprice.config(value=self.price_mufti)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="Spykar":
            self.comboprice.config(value=self.price_spykar)
            self.comboprice.current(0)
            self.qty.set(1)

        #T-Shirt

        if self.combo_prodname.get()=="Roadster":
            self.comboprice.config(value=self.price_road)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="polo":
            self.comboprice.config(value=self.price_polo)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="jack&Jones":
            self.comboprice.config(value=self.price_jj)
            self.comboprice.current(0)
            self.qty.set(1)

          #Shirt

        
        if self.combo_prodname.get()=="Peter England":
            self.comboprice.config(value=self.price_peter)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="Louis Phillips":
            self.comboprice.config(value=self.price_phillips)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="park avenue":
            self.comboprice.config(value=self.price_parkavenue)
            self.comboprice.current(0)
            self.qty.set(1)

        #Bath Soap

        
        if self.combo_prodname.get()=="Lux":
            self.comboprice.config(value=self.price_Lux)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="Dove":
            self.comboprice.config(value=self.price_Dove)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="Lifeboy":
            self.comboprice.config(value=self.price_Lifeboy)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="wildstone":
            self.comboprice.config(value=self.price_wildstone)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname=="Nivea":
            self.comboprice.config(value=self.price_nivea)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="Boroplus":
            self.comboprice.config(value=self.price_boroplus)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="Fairnlovely":
            self.comboprice.config(value=self.price_fairnlovely)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="vicco":
            self.comboprice.config(value=self.price_vicco)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="Olay":
            self.comboprice.config(value=self.price_olay)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="Glamup":
            self.comboprice.config(value=self.price_glamup)
            self.comboprice.current(0)
            self.qty.set(1)

            #Hair Oil

        if self.combo_prodname.get()=="coconut":
            self.comboprice.config(value=self.price_coconut)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="Indulekha":
            self.comboprice.config(value=self.price_Indulekha)
            self.comboprice.current(0)
            self.qty.set(1)

        if self.combo_prodname.get()=="patanjali":
            self.comboprice.config(value=self.price_patanjali)
            self.comboprice.current(0)
            self.qty.set(1)

            #Iphone

        
        if self.combo_prodname.get()=="IphoneX":
            self.comboprice.config(value=self.price_IphoneX)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="Iphone_11":
            self.comboprice.config(value=self.price_Iphone_11)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="Iphone_12":
            self.comboprice.config(value=self.price_Iphone_12)
            self.comboprice.current(0)
            self.qty.set(1)

            #Samsung

        
        if self.combo_prodname.get()=="samsung_8":
            self.comboprice.config(value=self.price_samsung_8)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="samsung_A30":
            self.comboprice.config(value=self.price_samsung_A30)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="samsung_F50":
            self.comboprice.config(value=self.price_samsung_F50)
            self.comboprice.current(0)
            self.qty.set(1)

            #Xiome

        
        if self.combo_prodname.get()=="Realme_narzo":
            self.comboprice.config(value=self.price_Realme_narzo)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="Realme_8i":
            self.comboprice.config(value=self.price_Realme_8i)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="Realme_9":
            self.comboprice.config(value=self.price_Realme_9)
            self.comboprice.current(0)
            self.qty.set(1)

         #One Plus
            
        if self.combo_prodname.get()=="oneplus_9":
            self.comboprice.config(value=self.price_oneplus_9)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="oneplus_8":
            self.comboprice.config(value=self.price_oneplus_8)
            self.comboprice.current(0)
            self.qty.set(1)

        
        if self.combo_prodname.get()=="oneplus_10":
            self.comboprice.config(value=self.price_oneplus_10)
            self.comboprice.current(0)
            self.qty.set(1)

     




        



















if __name__=='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
