from tkinter import *
from tkinter.tix import *
from math import tan, pi

global cAns
global wAns
cAns = 0
wAns = 0

root= Tk()

def madlibs_generator():
    
    root= Tk()
    root.configure(bg='DarkSlategray2')
    root.title('Nistha Singh-Mad Libs Generator')
    myLabel=Label(root,text='MAD LIBS GENERATOR',font='Helvetica 20 bold',bg='turquoise3',fg='black')
    myLabel.pack()
    myLabel1=Label(root,text='Choose any one',font='Helvetica 20 bold',bg='lavender',fg='black')
    myLabel1.pack()
    def madlib1():
        place=Entry(root,width=50)
        place.pack()
        place.insert(0,"Enter the name of a place:")
        food=Entry(root,width=50)
        food.pack()
        food.insert(0,"enter a food name:")
        name=Entry(root,width=50)
        name.pack()
        name.insert(0,"enter a person's name:")
        animal=Entry(root,width=50)
        animal.pack()
        animal.insert(0,"enter an animal's name:")
        thing=Entry(root,width=50)
        thing.pack()
        thing.insert(0,"enter a thing's name:")
        verb=Entry(root,width=50)
        verb.pack()
        verb.insert(0,"enter a verb ending with 'ing':")
        colour=Entry(root,width=50)
        colour.pack()
        colour.insert(0,"enter a colour:")
        body=Entry(root,width=50)
        body.pack()
        body.insert(0,"enter the name of a body part:")
        def tyy():
            Label(root,text=("Me and "+name.get()+" were sitting in "+place.get()+" eating \n "+food.get()+" when we saw a "+colour.get()+" "+animal.get()+" \n"+verb.get()+" a "+thing.get()+" with it's \n"+body.get())).pack()
        bt1=Button(root,text="see story",command=tyy)
        bt1.pack()
    def madlib2():
        adjective=Entry(root,width=50)
        adjective.pack()
        adjective.insert(0,"Enter an adjective:")
        colour=Entry(root,width=50)
        colour.pack()
        colour.insert(0,"enter a colour:")
        name=Entry(root,width=50)
        name.pack()
        name.insert(0,"enter a person's name:")
        number=Entry(root,width=50)
        number.pack()
        number.insert(0,"enter a number>1:")
        thing=Entry(root,width=50)
        thing.pack()
        thing.insert(0,"enter a thing's name:")
        verb=Entry(root,width=50)
        verb.pack()
        verb.insert(0,"enter a verb ending with 'ing':")
        vehicle=Entry(root,width=50)
        vehicle.pack()
        vehicle.insert(0,"enter a vehicle name:")
        def ty():
            Label(root,text=(name.get()+" had "+number.get()+" "+thing.get()+"s.\n "+"They were "+colour.get()+" in colour and were very "+adjective.get()+"\n "+name.get()+" drove them around in a "+vehicle.get()+" while occasionally "+verb.get()+" them.")).pack()
        bt2=Button(root,text="see story",command=ty)
        bt2.pack()
    Button(root, text= 'Game 1', font ='arial 15', command= madlib1, bg = 'dark violet',fg='ghost white').pack()
    Button(root, text= 'Game 2', font ='arial 15', command = madlib2 , bg = 'dark violet',fg='ghost white').pack()
    root.mainloop()



def hangman():
        import random
        import sys
        root=Tk()
        root.title('Nistha Singh-HANGMAN')
        root.configure(bg='thistle')
        Label(root, text= 'HANGMAN GAME \n GUESS THE WORD!!!' , font = 'castellar 20 bold',bg='RosyBrown1').pack()
        guess=Entry(root,width=50)
        guess.pack()
        words=["apple","orange","mango","banana","coyote","crow","deer","dog","donkey","duck","eagle",
            "ferret","fox","frog","goat","goose","hawk","lion","lizard","llama","mole","monkey",
            "moose","mouse","mule","tiger","otter","owl","panda","parrot","pigeon","python","rabbit"
            ]   
        chosen_word=random.choice(words)
        print(chosen_word)
        a=len(chosen_word)
        li=list(chosen_word)
        blanks=[]
        for i in range(a):
            blanks.append("_")
            i=i+1
        Label(root,text=blanks).pack()
        
        c=0
        def check():
            nonlocal c
            nonlocal a
            nonlocal li
            if c<7 and blanks!=li:
                w=0
                for i in range(a):
                    if(guess.get()==li[i]):
                        blanks[i]=li[i]
                        w=w+1
                Label(root,text=blanks).pack() 
                guess.delete(0,END)
                if(w==0):
                    c=c+1
                    Label(root,text=(str((7-c))+" chances left"),bg='lavender').pack()
                    
                
            elif c==7 or blanks==li:
                Label(root,text=("The word is "+chosen_word)).pack()
                c=c+1
            elif c>7:
                sys.exit()
        bt=Button(root,text="enter",command=check,bg='MistyRose2')
        bt.pack()
        root.mainloop()


def areacalculator():
    
    


    def area_3():
        side = float(entry.get())
        area = (3**0.5) / 4 * side*side
        op_lbl3.configure(text = ' Area of Triangle= {:.2f} ' .format(area))

    def area_4():
            side = float(entry.get())
            area4=side*side
            op_lbl4.configure(text = ' Area of Square= {:.2f} ' .format(area4))

    def area_5():
            side = float(entry.get())
            area5= 5 * (side** 2) / (4 * tan(pi / 5))
            op_lbl5.configure(text = ' Area of Regular Pentagon= {:.2f} ' .format(area5))

    def area_6():
            side = float(entry.get())
            area6= 6 * (side** 2) / (4 * tan(pi / 6))
            op_lbl6.configure(text = ' Area of Regular Hexagon= {:.2f} ' .format(area6))
            
    def area_7():
            side = float(entry.get())
            area7= 7 * (side** 2) / (4 * tan(pi / 7))
            op_lbl7.configure(text = ' Area of Regular Septagon= {:.2f} ' .format(area7))
            
    def area_8():
            side = float(entry.get())
            area8= 8 * (side** 2) / (4 * tan(pi / 8))
            op_lbl8.configure(text = ' Area of Regular Octagon= {:.2f} ' .format(area8))

    def area_9():
            side = float(entry.get())
            area9= 9 * (side** 2) / (4 * tan(pi / 9))
            op_lbl9.configure(text = ' Area of Regular Nonagon= {:.2f} ' .format(area9))

    def area_10():
            side = float(entry.get())
            area10= 10 * (side** 2) / (4 * tan(pi / 10))
            op_lbl10.configure(text = ' Area of Regular Decagon= {:.2f} ' .format(area10))

        
        
    root = Tk()
    root.title('Area Of Regular Shapes')

    lbl = Label(text= 'Enter side: ')
    lbl.grid(row=1, column=0)

    entry= Entry(width=6)
    entry.grid(row=1, column=1)
    op_lbl3 = Label(text='Area of Triangle is:')
    op_lbl3.grid(row=3, column=0, columnspan=3)
    calc_button_3= Button(text= ' Calculate Area Of Equilateral Triangle=',command=area_3)
    calc_button_3.grid(row=1, column=2, rowspan=2)

    op_lbl4 = Label(text='Area of Square is:')
    op_lbl4.grid(row=6, column=0, columnspan=3)
    calc_button_4= Button(text= ' Calculate Area Of Square=',command=area_4)
    calc_button_4.grid(row=4, column=2, rowspan=2)

    op_lbl5 = Label(text='Area of Regular Pentagon is:')
    op_lbl5.grid(row=9, column=0, columnspan=3)
    calc_button_5= Button(text= ' Calculate Area Of Regular Pentagon=',command=area_5)
    calc_button_5.grid(row=7, column=2, rowspan=2)

    op_lbl6 = Label(text='Area of Regular Hexagon is:')
    op_lbl6.grid(row=12, column=0, columnspan=3)
    calc_button_6= Button(text= ' Calculate Area Of Regular Hexagon=',command=area_6)
    calc_button_6.grid(row=10, column=2, rowspan=2)

    op_lbl7 = Label(text='Area of Regular Septagon is:')
    op_lbl7.grid(row=15, column=0, columnspan=3)
    calc_button_7= Button(text= ' Calculate Area Of Regular Septagon=',command=area_7)
    calc_button_7.grid(row=13, column=2, rowspan=2)

    op_lbl8 = Label(text='Area of Regular Octagon is:')
    op_lbl8.grid(row=18, column=0, columnspan=3)
    calc_button_8= Button(text= ' Calculate Area Of Regular Octagon=',command=area_8)
    calc_button_8.grid(row=16, column=2, rowspan=2)

    op_lbl9 = Label(text='Area of Regular Nonagon is:')
    op_lbl9.grid(row=21, column=0, columnspan=3)
    calc_button_9= Button(text= ' Calculate Area Of Regular Nonagon=',command=area_9)
    calc_button_9.grid(row=19, column=2, rowspan=2)

    op_lbl10 = Label(text='Area of Regular Decagon is:')
    op_lbl10.grid(row=24, column=0, columnspan=3)
    calc_button_10= Button(text= ' Calculate Area Of Regular Decagon=',command=area_10)
    calc_button_10.grid(row=22, column=2, rowspan=2)
    root.mainloop()


def dice():
    import random

    root=Tk()
    root.configure(bg='light blue')
    root.title('Dice rolling stimulator')
    myLabel=Label(root,text='DICE ROLLING STIMULATOR',font='Helvetica 20 bold',bg='pink',fg='black')
    myLabel.grid(row=1,column=2)
    def roll():
        x=random.randint(1,6)
        if(x==1):
            one()
        if(x==2):
            two()
        if(x==3):
            three()
        if(x==4):
            four()
        if(x==5):
            five()
        if(x==6):
            six()
        
    def one():
        c = Canvas(master=root,bg = "pink",height = 200,width = 200)  
        arc = c.create_oval((75,75,125,125),fill= "white")  
        c.grid(row=4,column=2)
    def two():
        c = Canvas(master=root,bg = "pink",height = 200,width = 200)  
        arc1 = c.create_oval((10,10,60,60),fill= "white")  
        arc2 = c.create_oval((140,140,190,190),fill= "white")
        c.grid(row=4,column=2)
    def three():
        c = Canvas(master=root,bg = "pink",height = 200,width = 200)  
        arc1 = c.create_oval((10,10,60,60),fill= "white")  
        arc2 = c.create_oval((140,140,190,190),fill= "white")
        arc3 = c.create_oval((75,75,125,125),fill="white")
        c.grid(row=4,column=2)
    def four():
        c = Canvas(master=root,bg = "pink",height = 200,width = 200)  
        arc1 = c.create_oval((10,10,60,60),fill= "white")  
        arc2 = c.create_oval((140,140,190,190),fill= "white")
        arc3 = c.create_oval((10,140,60,190),fill="white")
        arc4 = c.create_oval((140,10,190,60),fill="white")
        c.grid(row=4,column=2)
    def five():
        c = Canvas(master=root,bg = "pink",height = 200,width = 200)  
        arc1 = c.create_oval((10,10,60,60),fill= "white")  
        arc2 = c.create_oval((140,140,190,190),fill= "white")
        arc3 = c.create_oval((10,140,60,190),fill="white")
        arc4 = c.create_oval((140,10,190,60),fill="white")
        arc5 = c.create_oval((75,75,125,125),fill="white")
        c.grid(row=4,column=2)
    def six():
        c = Canvas(master=root,bg = "pink",height = 200,width = 200)  
        arc1 = c.create_oval((10,10,60,60),fill= "white")  
        arc2 = c.create_oval((140,140,190,190),fill= "white")
        arc3 = c.create_oval((10,140,60,190),fill="white")
        arc4 = c.create_oval((140,10,190,60),fill="white")
        arc5 = c.create_oval((75,10,125,60),fill="white")
        arc6 = c.create_oval((75,140,125,190),fill="white")
        c.grid(row=4,column=2)

    bt1=Button(root,text='roll',command=roll)
    bt1.grid(row=2,column=2)
    root.mainloop()


def password_generator():
    
    from tkinter import ttk
    
    import random
    import pyperclip
    from itertools import permutations

    #declaration of numbers,lowercase,uppercase,and special charecters
    numbers_list=['1','2','3','4','5','6','7','8','9']
    low_case_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    special_Char_list=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',':',';','"','<','>','?','/','\',']

    #total is the combined list of all the characters
    total=numbers_list+low_case_list+upper_case_list+special_Char_list

    #totals is the combined list excluding numbers
    totals=low_case_list+upper_case_list+special_Char_list

    #point is the grading system for the password
    global point
    point=0

    #declaration of the root window
    root= Tk()

    #declaration of different styles for the ttk buttons and labels
    style1 = ttk.Style()
    style1.configure('B1.TButton', font=('Segoe UI', 10))

    style2 = ttk.Style()
    style2.configure('B2.TButton', font=('Segoe UI', 7),height=1,width=1)

    style3 = ttk.Style()
    style3.configure('B3.TButton', font=('Segoe UI', 8))

    style4 = ttk.Style()
    style4.configure('B4.TButton', font=('Segoe UI', 7),height=1,width=3)

    style4 = ttk.Style()
    style4.configure('L4.TLabel', font=('Segoe UI', 9))

    #delcaration of the frame 
    #this frame is used to generate continuous navigation effect
    frame = Frame(root,width=1700,height=1400)

    #placement of frame onto full screen
    frame.place(x=0, y=0, relwidth=1.0, relheight=1.0)
            
    #title for the root  window        
    root.title('Pannag kumaar password strength checker and generator')

    #suggest is for suggesting the changes that should be done in the password
    #function for password checker

    def suggest():
        
        #suggestions- for printing out the line
        def suggestions():
            
            label=Label(frame,text=('some suggestions to improve your passwords strength\n--------------------------------------'))
            label.grid(column=0,row=5)
            nonlocal num_val
            num_val=6
        #suggest to use numbers,lowercase,uppercase,special charaters if not used

        if((num)==0):
            suggestions()
            label=Label(frame,text=('>>use atleast enter one number'))
            label.grid(column=0,row=num_val)
            num_val+=1
            new_inp=inp+random.choice(numbers_list)
            
            if((small_case)==0):
                label=Label(frame,text=('>>use atleast enter one lowercase character'))
                label.grid(column=0,row=num_val)
                num_val+=1
                new_inp+=random.choice(low_case_list)
                
            if((upper)==0):
                label=Label(frame,text=('>>use atleast enter one uppercase'))
                label.grid(column=0,row=num_val)
                num_val+=1
                new_inp+=random.choice(upper_case_list)
                
            
            
                    
            if((special_char)==0):
                label=Label(frame,text=('>>use atleast one special character'))
                label.grid(column=0,row=num_val)
                new_inp+=random.choice(special_Char_list)
                num_val+=1
                
                
                        
            
                        
        elif((small_case)==0):
            suggestions()
            label=Label(frame,text=('>>use atleast enter one lowercase character'))
            label.grid(column=0,row=num_val)
            num_val+=1
            new_inp=inp+random.choice(low_case_list)

            
            if((upper)==0):
                label=Label(frame,text=('>>use atleast enter one uppercase'))
                label.grid(column=0,row=num_val)
                num_val+=1
                new_inp+=random.choice(upper_case_list)
                
            
            if((special_char)==0):
                label=Label(frame,text=('>>use atleast one special character'))
                label.grid(column=0,row=num_val)
                new_inp+=random.choice(special_char_list)
                num_val+=1            
            
        elif((upper)==0):
            suggestions()
            label=Label(frame,text=('>>use atleast enter one uppercase'))
            label.grid(column=0,row=num_val)
            num_val+=1
            new_inp=inp+random.choice(upper_case_list)
            
            if((special_char)==0):
                label=Label(frame,text=('>>use atleast one special character'))
                label.grid(column=0,row=num_val)
                new_inp+=random.choice(special_Char_list)
                num_val+=1
        
                
        elif((special_char)==0):
            suggestions()
            label=Label(frame,text=('>>use atleast one special character'))
            label.grid(column=0,row=num_val)
            new_inp=inp+random.choice(special_Char_list)
            num_val+=1

            #if wordlist is used to check whether something personal related to the person is in the password
            if words_in_password==[]:
                pass
            else:
                label=Label(frame,text=('try not to use personal things in your password'))
                label.grid(column=0,row=num_val)
                
        
            
        
        else:
            return None
        #suggestions to improve on the password
        label=Label(frame,text=('you can use something like'+' '+new_inp))
        label.grid(column=0,row=num_val)    

    #for the i button on the home screen
    def infobutton():
        new_frame()
        Label(frame,text='Basic rules everyone should follow.\nIn order to combat this problem, we need to establish some rules of engagement for passwords and ensure their strength is sufficient. First here are some basic rules everyone should follow:\n >>Never re-use the same password between work and home\n >>Never re-use the same password for financial institutions and social media\n >>Never re-use the same password for an administrator account at work as your standard logon\n >>Never tell anyone your password. If you need to share it, change it when the other person is done with using it.\n >>Change your passwords frequently.\n >>Length of the password  preferably over 12 characters\n >>Complexity of the password  must contain letters (upper and lower case), numbers, and symbols and have a minimum number of each\n >>Contain no repetitive characters\n >>Contain no human readable words, names, dates, or recognize context with the password\n >>Should not be reused from a previous time and date\n >>Should not contain sequences from a keyboard like qwerty or zxcvb\n ').grid(column=0, row=0)
        Button(frame, text= 'back', command= back).grid(column=0, row=1)

    #for the i button on the password generator screen
    def infobutton2():
        new_frame()
        Label(frame,text='Hello there!!\nOur password generator is very easy to use\nClick on the entry box to clear contents\nEnter the number of digits you want your password to have\nClick on generate to generate your password\nUse the copy button to copy the generated password onto the clipboard\n---------------------------------------------------------------------\nHow is it proper password??\nIt has one number, one lowercase letter, one uppercase, one special character\nto enure maximum strength\nDigits are very randomly choosen ').grid(column=0, row=1)
        Button(frame, text= 'back', command= pass_gen_part1).grid(column=0, row=0,sticky=tkinter.NW)

    #click 0-7 are the functions for deleting the contents of the entry box when clicked
    def click(event):
        password.configure(state=NORMAL)
        password.delete(0, END)
        password.unbind('<Button-1>', clicked)
        return None

    def click1(event):
        digits.configure(state=NORMAL)
        digits.delete(0, END)
        digits.unbind('<Button-1>', clicked1)  

    def click2(event):
        name.configure(state=NORMAL)
        name.delete(0, END)
        name.unbind('<Button-1>', clicked2)  

    def click3(event):
        petsname.configure(state=NORMAL)
        petsname.delete(0, END)
        petsname.unbind('<Button-1>', clicked3)  

    def click4(event):
        dateofbirth.configure(state=NORMAL)
        dateofbirth.delete(0, END)
        dateofbirth.unbind('<Button-1>', clicked4)  

    def click5(event):
        father.configure(state=NORMAL)
        father.delete(0, END)
        father.unbind('<Button-1>', clicked5)  

    def click6(event):
        mother.configure(state=NORMAL)
        mother.delete(0, END)
        mother.unbind('<Button-1>', clicked6)  

    def click7(event):
        key.configure(state=NORMAL)
        key.delete(0, END)
        key.unbind('<Button-1>', clicked7)  


    #the function for the copy button to copy generated password onto clipboard
    def copy1():
        random_password = temp_tot 
        pyperclip.copy(random_password)

    #function to clear frame whenever used
    def clearFrame():
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()
        
        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        frame.pack_forget()

    #uses clear frame and generartes new one instead of the prior
    def new_frame():
        clearFrame()
        frame.pack(fill="both",expand=1)

    #used to generate password
    #to run after part 1
    def pass_gen_part2():

        #get input from the entry box    
        inpu=digits.get()

        for i in inpu:

            #check whether the input is digits or not
            if i in totals:
                #enabling and disabling the passwordbox entry to avoid confusion
                passwordbox.configure(state='normal')    
                passwordbox.delete(0,END)
                passwordbox.insert(0,'enter a valid number')
                passwordbox.configure(state='readonly')    
                break

        else:
            inp=int(inpu)

            #checking whether the given input is in the range of 8-20
            if inp<=8 or inp>=20 :
                passwordbox.configure(state='normal')    
                passwordbox.delete(0,END)
                passwordbox.insert(0,'enter a number between 8 and 20')
                passwordbox.configure(state='readonly')    
                pass_gen_part2()
                    
            else:    
                #execution of the generator  
                #num is the randomly choosen number
                num_=random.choice(numbers_list)

                #low_case is the randomly choosen lower case
                low_case_=random.choice(low_case_list)

                #upper_case is the randomly choosen upper case 
                upper_case_=random.choice(upper_case_list)
                
                #special is the randomly choosen special character
                special=random.choice(special_Char_list)

                #temp tot is a 4 letter string having num,uppercase,lower case,splchar
                global temp_tot
                temp_tot=num_+low_case_+upper_case_+special

                #in order to create the rest of the password the number of digits is
                z=inp-4

                while z!=0:
                    #choosing one character randomly from total
                    temp_tot+=random.choice(total)
                    z-=1
                passwordbox.configure(state='normal')
                passwordbox.delete(0,END)

                #displaying the password
                passwordbox.insert(0,temp_tot)
                passwordbox.configure(state='readonly')

    #putting all the widgets for password generator  in place
    global pass_gen_part1
    def pass_gen_part1():
        
        new_frame()

        #for the back button on top of the screem
        back_key=ttk.Button(frame, text= '<-', command= back,style='B4.TButton')
        back_key.grid(sticky=tkinter.NW)
        
        #for the balloon message for the back button 
        tip=Balloon(frame)
        tip.bind_widget(back_key,balloonmsg="click to go back")
        for sub in tip.subwidgets_all():
            sub.config(bg='white')
        
        label1=Label(frame,text=('Length'))
        label1.grid(column=0,row=1)

        label2=Label(frame,text=('Password'))
        label2.grid(column=0,row=3)
        
        #digits is the entry box  where the length of the password is taken from the user
        global digits
        digits=Entry(frame,width=30)
        digits.grid(column=1, row=1)    
        digits.insert(0,"Enter the number of  digits:")

        #clicked is the key to clear the entry when clicked on
        global clicked1
        clicked1 = digits.bind('<Button-1>', click1)
        bt1=ttk.Button(frame,text='Generate' ,command=pass_gen_part2,style='B3.TButton')
        bt1.grid(column=2, row=1,padx=7)

        #passwordbox is where the password or the given output is displayed        
        global passwordbox
        passwordbox=Entry(frame,width=30)
        passwordbox.grid(column=1, row=3,pady=1)
        passwordbox.configure(state='readonly')
        
        #copy button is for copying the generated password using the pypeclip
        copy_button = ttk.Button(frame, text="Copy", command=copy1,style='B3.TButton')
        copy_button.grid(column=2,row=3,padx=7,pady=1)
        
        #info button to help user understand the usage of the generator
        info=ttk.Button(frame, text= 'i', command= infobutton2,style='B2.TButton')
        info.grid(row=0,column=3,sticky=tkinter.NE,ipadx=0.000000001,ipady=0.000000001)
        
        #creation of balloon message when the cursor is over the info widget
        tip.bind_widget(info,balloonmsg="info")
        
        for sub in tip.subwidgets_all():
            sub.config(bg='white')

    #function for asking the user for using our generator if the password they have entered is weak    
    def newgen():
        
        #function if they say no for using the generator
        def no():
            new_frame()
            Label(frame,text=('Have a wonderful day!!')).grid(column=0,row=15)
            
            #ends the execution of the root window after 4 sec
            root.after(4000,lambda:root.destroy())
        Label(frame,text=('--------------------------------------------------------------------\nDo you want to use our password generator \nfor generating your password??')).grid(column=0, row=12,columnspan=2)
        Button(frame, text= 'Yes', command= pass_gen_part1).grid(column=0,row=13)
        Button(frame, text= 'No', command = no).grid(column=1, row=13,sticky=tkinter.W)

    #the password strength checker
    #used to check the strength of a password 
    #scale used to check points
    #points is the grading system for this checker
    def pass_strength_checker():
        new_frame()
        
        #BACK KEY
        back_key2=ttk.Button(frame, text= '<-', command= back,style='B4.TButton')
        back_key2.grid(sticky=tkinter.NW)
        
        #balloon message for the back key
        tip=Balloon(frame)
        tip.bind_widget(back_key2,balloonmsg="click to go back")
        for sub in tip.subwidgets_all():
            sub.config(bg='white')

        #the box for the entry of password    
        global password
        password=Entry(frame,width=50)
        password.insert(0,'Enter the password you want to get checked')    
        password.grid(column=1, row=1,padx=5,pady=2)   

        #clear entry box when clicked
        global clicked
        clicked = password.bind('<Button-1>', click)  

        #function for the check button
        # it is the function where the strength is checked
        
        def checker():

            #inp is the variable where the password is stored
            global inp
            inp=str(password.get())
    
            #convert the given input into list
            y=list(inp)
            r=[]
    
            # to convert the given password list into their respective ascii values
            #it is converted to ascii in order to check the nature of the digits
            for i in y: 
                z=(ord(i))
                r.append(z)
            
            #declaring the variable point
            global point
            point=0

            #take length of password=a
            a=len(y)

            #declaration of number num,lower and upper cases,spl char
            global num
            num=0

            global small_case
            small_case=0

            global upper
            upper=0

            global special_char
            special_char=0
            
            fake_num=1
            
            print(a)
            #checking whether the length of the password is appropriate
            if (a<7 or a>30):
                label=Label(frame,text=('YOUR PASSWORD IS TOO SHORT ENTER SOME THING THAT IS 8-20 DIGITS LONG'))
                label.grid(column=0,row=3)
                
            #point allotment
            else:
                
                #1 point if the length is less than 10
                if a<=10:
                    point+=1
                
                #2 points if the point is greater than 10
                else:
                    point+=2

                for i in r:
                    
                    #1 point if the digit is number
                    if(i>47 and i<58):
                        point+=1
                        num+=1
                
                #2 point if there are uppper and lower cases
                    elif(i>64 and i<91):
                        point+=2
                        upper+=1
                    elif(i>96 and i<123):
                        point+=2
                        small_case+=1

                    #3 points for a special character
                    else:
                        point+=3
                        special_char+=1
                
                #point decrement if there are no number,lower and upper cases, special characters
                if num==0:
                    point-=5
                if small_case==0:
                    point-=7
                if upper==0:
                    point-=7
                if special_char==0:
                    point-=9
            
            if fake_num==0:
                pass
            
                
            else:
                
                #decrement if there are too many numbers
                if((num>4 or num>=(a/2) )):
                    point-=1

                
                if((special_char>5 or special_char>=(a/2))):
                    point-=2

                
                #function for giving the output regarding the strength of the password based on the points recieved
                #prints out a progress bar with the strength of the given password
                #gives suggestions if password is weak on improving th password
                def done():
                    new_frame()

                    #declaration of a progress bar to show strength of a password
                    progress = ttk.Progressbar(frame, orient = HORIZONTAL,length = 300, mode = 'determinate')

                    if(point<=5):
                        progress['value'] = 5
                        root.update_idletasks()
                        progress.grid(column=0, row=1)
                        Label(frame,text=('extremly weak password')).grid(column=0, row=2)
                        newgen()       

                    elif(point<=10):
                        progress['value'] = 20
                        root.update_idletasks()
                        progress.grid(column=0, row=1)
                        Label(frame,text=('very weak password')).grid(column=0, row=2)
                        newgen()       

                    elif(point<=13):
                        progress['value'] = 30
                        root.update_idletasks()
                        progress.grid(column=0, row=1)
                        Label(frame,text=(' weak password')).grid(column=0, row=2)
                        newgen()

                    elif(point<=16):
                        progress['value'] = 40
                        root.update_idletasks()
                        progress.grid(column=0, row=1)                       
                        Label(frame,text=('medium password')).grid(column=0, row=2)
                        newgen()

                    elif(point<=18):
                        progress['value'] = 55
                        root.update_idletasks()
                        progress.grid(column=0, row=1)
                        Label(frame,text=('good password')).grid(column=0, row=2)
            

                    elif(point<=20):
                        progress['value'] = 70
                        root.update_idletasks()
                        progress.grid(column=0, row=1)
                        Label(frame,text=('very good password')).grid(column=0, row=2)
                        
                    elif(point<=22):
                        progress['value'] = 80
                        root.update_idletasks()
                        progress.grid(column=0, row=1)
                        Label(frame,text=('strong password')).grid(column=0, row=2)


                        
                    elif(point<=25):
                        progress['value'] = 90
                        root.update_idletasks()
                        progress.grid(column=0, row=1)
                        Label(frame,text=('very strong password')).grid(column=0, row=2)

                    elif(point>25):
                        progress['value'] = 100
                        root.update_idletasks()
                        progress.grid(column=0, row=1)
                        Label(frame,text=('extremely strong password')).grid(column=0, row=2)
                    
                    #calling suggestt to check whether the passwrod could be better in any way
                    suggest()        
                    Label(frame,text=('the given password was'+' '+inp)).grid(column=0, row=3)
                    Button(frame, text= 'home', command= start).grid(column=0, row=4)
                
                #wordlist is created to assess if the password is vulnerable
                global ask
                def ask():
                    print(point)
                    new_frame()
                    Label(frame,text=('DO YOU WANT TO GENERATE A WORDLIST')).grid(column=1, row=1)

                    bt1=ttk.Button(frame,text="yes",command=wordlist_box,style='B3.TButton')
                    bt1.grid(column=1, row=2)

                    bt2=ttk.Button(frame,text="no",command=done,style='B3.TButton')
                    bt2.grid(column=2,row=2)

                    bt3=ttk.Button(frame,text="<-",command=pass_strength_checker,style='B4.TButton')
                    bt3.grid(row=0,column=0,sticky=tkinter.NW)
                    tip=Balloon(frame)
                    tip.bind_widget(bt3,balloonmsg="click to go back")
                    for sub in tip.subwidgets_all():
                        sub.config(bg='white')
        


                # for creating a wordlist for better asessment

                global wordlist_box
                def wordlist_box():
                    global back3
                    def back3():
                        ask()
            
                    new_frame()

                    #personal aspects of the user is asked for checking the password
                    global name
                    name=Entry(frame,width=50)
                    name.grid(column=0, row=3)
                    global clicked2
                    clicked2 = name.bind('<Button-1>', click2)
                    name.insert(0,"Enter your Name")

                    global petsname
                    petsname=Entry(frame,width=50)
                    petsname.grid(column=0, row=4)
                    global clicked3
                    clicked3 = petsname.bind('<Button-1>', click3)
                    petsname.insert(0,"Enter your Pet's name:")

                    global dateofbirth
                    dateofbirth=Entry(frame,width=50)
                    dateofbirth.grid(column=0, row=5)
                    global clicked4
                    clicked4 = dateofbirth.bind('<Button-1>', click4)
                    dateofbirth.insert(0,"Enter your date of birth in this format dd/mm/yyyy")

                    global father
                    father=Entry(frame,width=50)
                    father.grid(column=0, row=6)
                    global clicked5
                    clicked5 = father.bind('<Button-1>', click5)
                    father.insert(0,"Enter your  Father's name:")

                    global mother
                    mother=Entry(frame,width=50)
                    mother.grid(column=0, row=7)
                    global clicked6
                    clicked6 = mother.bind('<Button-1>', click6)
                    mother.insert(0,"Enter your Mother's name:")

                    global key
                    key=Entry(frame,width=50)
                    key.grid(column=0, row=8)
                    global clicked7
                    clicked7 = key.bind('<Button-1>', click7)
                    key.insert(0,"Enter some keywords related to you separated by ','")

                    Button(frame, text= 'back', command= back3).grid(column=0, row=9)

                    def wordlist_get_input():
                        # taking input from the entry windows
                        name1=name.get()

                        pet=petsname.get()

                        dob1=dateofbirth.get()

                        #splitting date of birth into individual components
                        dd,mm,yyyy=dob1.split('/')

                        father1=father.get()

                        mother1=mother.get()

                        keywords=key.get()

                        #splitting the keywords 
                        key_split=keywords.split(',')

                        #making a list for assessment
                        list_to_be_combined=[name1,pet,dd,mm,yyyy,father1,mother1]
                        list_to_be_combined.extend(key_split)

                        #permuting the inputs given by the users to generate combinations
                        perm=permutations(list_to_be_combined)
                        
                        #for creating separate sting from the combination
                        lis=list(perm)
                        lis.extend(list_to_be_combined,2)
                        lis1=[]
                        for i in lis:
                            lis1.append(''.join(i))
                        lis1.extend(list_to_be_combined)
                        global words_in_password
                        words_in_password=[]
                    
                        x1=inp.lower()
                        for i in lis1:
                                if i in x1:
                                    words_in_password.append(i)
                                    point-=4
                        

                        #the function done is used here
                        progress = Progressbar(root, orient = HORIZONTAL,length = 300, mode = 'determinate')
                    
                        if(point<=5):
                            progress['value'] = 5
                            root.update_idletasks()
                            progress.grid(column=0, row=1)
                            Label(frame,text=('extremly weak password')).grid(column=0, row=2)
                            newgen()       

                        elif(point<=10):
                            progress['value'] = 20
                            root.update_idletasks()
                            progress.grid(column=0, row=1)
                            Label(frame,text=('very weak password')).grid(column=0, row=2)
                            newgen()       

                        elif(point<=13):
                            progress['value'] = 30
                            root.update_idletasks()
                            progress.grid(column=0, row=1)
                            Label(frame,text=(' weak password')).grid(column=0, row=2)
                            newgen()

                        elif(point<=16):
                            progress['value'] = 40
                            root.update_idletasks()
                            progress.grid(column=0, row=1)                       
                            Label(frame,text=('medium password')).grid(column=0, row=2)
                            newgen()

                        elif(point<=18):
                            progress['value'] = 55
                            root.update_idletasks()
                            progress.grid(column=0, row=1)
                            Label(frame,text=('good password')).grid(column=0, row=2)
                

                        elif(point<=20):
                            progress['value'] = 70
                            root.update_idletasks()
                            progress.grid(column=0, row=1)
                            Label(frame,text=('very good password')).grid(column=0, row=2)
                            
                        elif(point<=22):
                            progress['value'] = 80
                            root.update_idletasks()
                            progress.grid(column=0, row=1)
                            Label(frame,text=('strong password')).grid(column=0, row=2)
                            
                        elif(point<=25):
                            progress['value'] = 90
                            root.update_idletasks()
                            progress.grid(column=0, row=1)
                            Label(frame,text=('very strong password')).grid(column=0, row=2)

                        elif(point<=25):
                            progress['value'] = 100
                            root.update_idletasks()
                            progress.grid(column=0, row=1)
                            Label(frame,text=('extremely strong password')).grid(column=0, row=2)

                        suggest()
                    Label(frame,text=('the given password was'+' '+inp)).grid(column=0, row=11)
                    bt3=Button(frame,text="Next",command=wordlist_get_input)
                    bt3.grid(column=0, row=10)
                    Button(frame, text= 'home', command= start).grid(column=0, row=12)

                    
                    
                ask()
    
            


        bt2=ttk.Button(frame,text="Check",command=checker,style='B3.TButton')

        bt2.grid(row=2,column=1)
        
    def start():
        new_frame()
        tip= Balloon(frame)

        
        myLabel1=ttk.Label(frame,text='Hello!!,Cick one of the following based on your requirement ',style='L4.TLabel')
        myLabel1.grid(column=0, row=1,columnspan=2)
        ttk.Button(frame, text= 'Generate password', command= pass_gen_part1,style='B1.TButton').grid(column=0, row=3 )
        ttk.Button(frame, text= 'Check strength of password', command = pass_strength_checker ,style='B1.TButton').grid(column=1, row=3)
        
        info=ttk.Button(frame, text= 'i', command= infobutton,style='B2.TButton')
        info.grid(row=0,column=2,sticky=tkinter.NE)
        
        tip.bind_widget(info,balloonmsg="click to get info")
        
        for sub in tip.subwidgets_all():
            sub.config(bg='white')
            
    global back
    def back():
        new_frame()
        start()   
    start()
    root.mainloop()


bt1=Button(root,text="dice rooling simulator",command=dice)
bt1.grid(column=1,row=0)
bt2=Button(root,text="area calculator",command=areacalculator)
bt2.grid(column=1,row=1)
bt3=Button(root,text="madlibs generator",command=madlibs_generator)
bt3.grid(column=1,row=2)
bt4=Button(root,text="hangman",command=hangman)
bt4.grid(column=1,row=3)
bt5=Button(root,text="password generator",command=password_generator)
bt5.grid(column=1,row=4)
root.mainloop()