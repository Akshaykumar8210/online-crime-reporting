from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class criminal:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1366x678+0+0')
        
        self.root.title('ONLINE CRIMINAL REPORTING SYSTEM')

        lbl__title=Label(self.root,text='ONLINE CRIMINAL REPORTING SYSTEM SOFTWARE',font=('times new roman',30,'bold'),bg='black',fg='gold')
        lbl__title.place(x=0,y=0,width=1366,height=80)
        #ncr logo
        
        img__logo=img__logo.resize((60,60),Image.ANTIALIAS)
        self.photo__logo=ImageTk.PhotoImage(img__logo)
        
        self.logo=Label(self.root,image=self.photo__logo)
        self.logo.place(x=80,y=5,width=60,height=60)
        
        #img__Frame
        img__frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img__frame.place(x=0,y=80,width=1366,height=135)
      
        img1=Image.open('images/police.png')
        img1=img1.resize((440,130),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        
        self.img__1=Label(img__frame,image=self.photo1)
        self.img__1.place(x=0,y=0,width=400,height=130)
        
        
        ##2set
        img__2=Image.open('images/img2.png')
        img__2=img__2.resize((600,150),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img__2)
        
        self.img__2=Label(img__frame,image=self.photo2)
        self.img__2.place(x=400,y=0,width=300,height=130)
        
        #3set
        img__3=Image.open('images/img7.png')
        img__3=img__3.resize((800,150),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img__3)
        
        self.img__3=Label(img__frame,image=self.photo3)
        self.img__3.place(x=590,y=0,width=600,height=130)
        
        #4set
        img__4=Image.open('images/img9.png')
        img__4=img__4.resize((1000,200),Image.ANTIALIAS)
        self.photo4=ImageTk.PhotoImage(img__4)
        
        self.img__4=Label(img__frame,image=self.photo4)
        self.img__4.place(x=1000,y=0,width=900,height=130)
        
        #Main frame
        Main__frame=Frame(self.root,bd=2,relief=RIDGE,bg='yellow')
        Main__frame.place(x=0,y=220,width=1380,height=560)
        
        
        #Upper frame
        upper__frame=LabelFrame(Main__frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION ',font=('times new roman',15,'bold'),fg='red',bg='white')
        upper__frame.place(x=10,y=0,width=1340,height=560)
  
                
        #Labels Entry
        #Case id
        caseid=Label(upper__frame,text='Case ID',font=('arial',11,'bold'),bg='blue')
        caseid.grid(row=0,column=0,padx=2,sticky=W)
        
        caseentry=ttk.Entry(upper__frame,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)
         
        #Criminal No
        lbl__criminal__no=Label(upper__frame,font=("arial",12,"bold"),text="Criminal No:",bg="white")
        lbl__criminal__no.grid(row=0,column=2,sticky=W,padx=2,pady=7)
        
        txt__criminal__no=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__criminal__no.grid(row=0,column=3,sticky=W,padx=2,pady=7)
        
         #CRIMINAL Name
        lbl__Name=Label(upper__frame,font=("arial",12,"bold"),text="Criminal Name:",bg="white")
        lbl__Name.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        txt__Name=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__Name.grid(row=1,column=1,sticky=W,padx=2,pady=7)
        
        
        #Nick Name
        lbl__nickname=Label(upper__frame,font=("arial",12,"bold"),text="Nick Name:",bg="white")
        lbl__nickname.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        txt__Name=ttk.Entry(upper__frame,width=22,font=('arial',11,'bold'))
        txt__Name.grid(row=1,column=3,sticky=W,padx=2,pady=7)
        
        #Arrest Date
        lbl__arrestDate=Label(upper__frame,font=("arial",12,"bold"),text="Arres Date:",bg="white")
        lbl__arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        txt__Name=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__Name.grid(row=2,column=1,sticky=W,padx=2,pady=7)
         
        #Date of crime
        lbl__dateofcrime=Label(upper__frame,font=("arial",12,"bold"),text="Date Of Crime:",bg="white")
        lbl__dateofcrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        txt__Name=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__Name.grid(row=2,column=3,sticky=W,padx=2,pady=7)
         
        #Address
        lbl__address=Label(upper__frame,font=("arial",12,"bold"),text="Address:",bg="white")
        lbl__address.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        txt__Name=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__Name.grid(row=3,column=1,sticky=W,padx=2,pady=7)
         
        #Age
        lbl__age=Label(upper__frame,font=("arial",12,"bold"),text="Age:",bg="white")
        lbl__age.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        txt__age=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__age.grid(row=3,column=3,sticky=W,padx=2,pady=7)
         
        #Occupution
        lbl__occuputin=Label(upper__frame,font=("arial",12,"bold"),text="Occupution:",bg="white")
        lbl__occuputin.grid(row=4,column=0,sticky=W,padx=2,pady=7)
       
        txt__occupution=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__occupution.grid(row=4,column=1,sticky=W,padx=2,pady=7)
      
         
        #birthMark
        lbl__birthMark=Label(upper__frame,font=("arial",12,"bold"),text="Birth Mark:",bg="white")
        lbl__birthMark.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        txt__Name=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__Name.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        
        #Crime TYpe
        lbl__crimeType=Label(upper__frame,font=("arial",12,"bold"),text="Crime Type:",bg="blue")
        lbl__crimeType.grid(row=0,column=4,sticky=W,padx=2,pady=7)
        
        txt__Name=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__Name.grid(row=0,column=5,sticky=W,padx=2,pady=7)
        
        ## Father Name
        lbl__fatherName =Label(upper__frame,font=("arial",12,"bold"),text="Father Name:",bg="white")
        lbl__fatherName.grid(row=1,column=4,sticky=W,padx=2,pady=7)
        
        txt__fatherName=ttk.Entry(upper__frame,width=22,font=("arial",11,"bold"))
        txt__fatherName.grid(row=1,column=5,sticky=W,padx=2,pady=7)
        
        #gender
        lbl__gender =Label(upper__frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl__gender.grid(row=2,column=4,sticky=W,padx=2,pady=7)
        
        #wanted
        lbl__wanted =Label(upper__frame,font=("arial",12,"bold"),text="Most Wanted:",bg="white")
        lbl__wanted.grid(row=3,column=4,sticky=W,padx=2,pady=7)
        
        #Radio Button genter
        radio__frame__gender=Frame(upper__frame,bd=2,relief=RIDGE,bg="red")
        radio__frame__gender.place(x=735,y=80,width=185,height=60)
        
        male=Radiobutton(radio__frame__gender,text='Male',value='male',font=("arial",12,"bold"),bg='pink')
        male.grid(row=0,column=0,pady=2,padx=4,sticky=W)
      
        
        female=Radiobutton(radio__frame__gender,text='female',value='female',font=("arial",12,"bold"),bg='blue')
        female.grid(row=0,column=1,pady=2,padx=4,sticky=W)
    
        #Radio Button wanted
        radio__frame__wanted=Frame(upper__frame,bd=2,relief=RIDGE,bg="yellow")
        radio__frame__wanted.place(x=735,y=120,width=185,height=40)
    
        yes=Radiobutton(radio__frame__wanted,text='Yes',value='yes',font=("arial",12,"bold"),bg='green')
        yes.grid(row=0,column=0,pady=2,padx=4,sticky=W)
        
        no=Radiobutton(radio__frame__wanted,text='No',value='no',font=("arial",12,"bold"),bg='red')
        no.grid(row=0,column=1,pady=2,padx=4,sticky=W)
        
        #Butons
        button__frame=Frame(upper__frame,bd=2,relief=RIDGE,bg="red")
        button__frame.place(x=8,y=190,width=610,height=40)
    
        #add button
        btn__add=Button(button__frame,text='Record Saved',font=("arial",12,"bold"),width=14,bg='blue',fg='white')
        btn__add.grid(row=0,column=0,padx=3,pady=5)
        
        
        
        #update button
        btn__update=Button(button__frame,text='Update',font=("arial",12,"bold"),width=14,bg='blue',fg='white')
        btn__update.grid(row=0,column=1,padx=3,pady=5)
        
        
        #Delete button
        btn__delete=Button(button__frame,text='Delete',font=("arial",12,"bold"),width=14,bg='blue',fg='white')
        btn__delete.grid(row=0,column=2,padx=3,pady=5)
        
        
        
        #clear button
        btn__clear=Button(button__frame,text='Clear',font=("arial",12,"bold"),width=14,bg='blue',fg='white')
        btn__clear.grid(row=0,column=3,padx=3,pady=5)
        
        
        #background right side images
        
        img__crime=Image.open('images/AR.png')
        img__crime=img__crime.resize((300,200),Image.ANTIALIAS)
        self.photocrime=ImageTk.PhotoImage(img__crime)
        
        self.img__crime=Label(upper__frame,image=self.photocrime)
        self.img__crime.place(x=999,y=0,width=300,height=210)
        
        
        
        
        

        #Down frame
        down__frame=LabelFrame(Main__frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION TABEL',font=('times new roman',15,'bold'),fg='red',bg='white')
        down__frame.place(x=10,y=260,width=1340,height=190)
        
        search__frame=LabelFrame(Main__frame,bd=10,relief=RIDGE,text='Search Criminal Records',font=('times new roman',15,'bold'),fg='blue',bg='white')
        search__frame.place(x=20,y=290,width=1330,height=70)
       
        search__by=Label(search__frame,font=("arial",12,"bold"),text="Search By:",bg="red")
        search__by.grid(row=0,column=0,sticky=W,padx=2,pady=5)
                           
        combo__search__box=ttk.Combobox(search__frame,font=("arial",12,"bold"),width=18,state='readonly')                   
        combo__search__box['value']=('search option','case__id','criminal__no')    
        combo__search__box.current(0)
        combo__search__box.grid(row=0,column=1,sticky=W,padx=2,pady=5)                 
                           
        search__txt=ttk.Entry(search__frame,width=18,font=("arial",11,"bold"))
        search__txt.grid(row=0,column=2,sticky=W,padx=2,pady=5)
        
        
        
        #Search button
        btn__delete=Button(search__frame,text='Search',font=("arial",12,"bold"),width=14,bg='blue',fg='white')
        btn__delete.grid(row=0,column=3,padx=3,pady=5)
        
        
        
        #all button
        btn__clear=Button(search__frame,text='Show All',font=("arial",12,"bold"),width=14,bg='blue',fg='white')
        btn__clear.grid(row=0,column=5,sticky=W,padx=3,pady=5) 
                             
        
        
        #table frame
        table__frame=Frame(down__frame,bd=2,relief=RIDGE)
        table__frame.place(x=10,y=80,width=1330,height=90)
        
        crimeagency=Label(search__frame,font=("arial",20,"bold"),text="NATIONAL CRIME AGENCY",bg="white",fg='blue')
        crimeagency.grid(row=0,column=4,sticky=W,padx=50,pady=0)
              
                          
        #Scroll bar                   
        scroll__x=ttk.Scrollbar(table__frame,orient=HORIZONTAL)                  
        scroll__y=ttk.Scrollbar(table__frame,orient=VERTICAL)
        
        
        self.criminal__table=ttk.Treeview(table__frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll__x.set,yscrollcommand=scroll__y.set)
        
        scroll__x.pack(side=BOTTOM,fill=X)
        scroll__y.pack(side=RIGHT,fill=Y)
        
 
        scroll__x.config(command=self.criminal__table.xview)                 
        scroll__y.config(command=self.criminal__table.yview)
        
        
        self.criminal__table.heading('1',text='CaseId')
        self.criminal__table.heading('2',text="CrimeNo")
        self.criminal__table.heading('3',text='Criminal Name')
        self.criminal__table.heading('4',text='NickName')
        self.criminal__table.heading('5',text='ArrestDate')
        self.criminal__table.heading('6',text='CrimeOfDate')
        self.criminal__table.heading('7',text='Address')
        self.criminal__table.heading('8',text='Age')
        self.criminal__table.heading('9',text='Occupation')
        self.criminal__table.heading('10',text='Birth Mark')
        self.criminal__table.heading('11',text='Crime Type')
        self.criminal__table.heading('12',text='FathersName')
        self.criminal__table.heading('13',text='Gender')
        self.criminal__table.heading('14',text='Wanted')
        
        self.criminal__table['show'] = 'headings'
        self.criminal__table.column('1', width=90)
        self.criminal__table.column('2', width=90)
        self.criminal__table.column('3', width=90)
        self.criminal__table.column('4', width=90)
        self.criminal__table.column('5', width=90)
        self.criminal__table.column('6', width=90)
        self.criminal__table.column('7', width=90)
        self.criminal__table.column('8', width=90)
        self.criminal__table.column('9', width=90)
        self.criminal__table.column('10', width=90)
        self.criminal__table.column('11', width=90)
        self.criminal__table.column('12', width=90)
        self.criminal__table.column('13', width=90)
        self.criminal__table.column('14', width=90)
        self.criminal__table.pack(fill=BOTH, expand=1)
          
        
if __name__== "__main__":
    root = Tk()
    obj = criminal(root)
    root.mainloop()