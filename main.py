'''
Created on Mar 31, 2017

@author: Krystal
'''

from tkinter import *
import os
import random

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
myfile_path = os.path.join(ROOT_PATH)

def MAIN():
    global counter2
    global numToPick
    
    dollars = [.01,1,5,10,25,50,75,
               100,200,300,400,500,
               750,1000,5000,10000,
               25000,50000,75000,100000,
               200000,300000,400000,
               500000,750000,1000000]
    dollarsDict = [.01,1,5,10,25,50,75,
               100,200,300,400,500,
               750,1000,5000,10000,
               25000,50000,75000,100000,
               200000,300000,400000,
               500000,750000,1000000]
    random.shuffle(dollars)
    cases = list(range(1,len(dollars)+1))
    
    app = Tk()
    app.title("Deal or No Deal")
    fname = Canvas(bg = "black", height = 600, width=1300)
    fname.pack(side=TOP)
    image1 = PhotoImage(file = "imagy.png")   
    image = fname.create_image(1000,50,anchor = NE, image = image1)

    casesB = {}
    buttonBases = {}
    
    z = 0
    w = 0
    counter = 0
    counter2 = 0
    
    for x in range(1,27):
        counter += 1
        if x == 7:
            z = 100
            w = 720
        if x == 13:
            z = 200
            w = 1380
        if x == 18:
            z = 300
            w = 1980
        if x == 23:
            z = 400
            w = 2520
    
        casesB["case%d" % x] = PhotoImage(file = "case%d.png" % x)   
        buttonBases["button%d" % x] = Button(app, image = casesB["case%d" % x], text=counter)
        buttonBases["button%d" % x].config(command = lambda counter=counter :GetCase(counter))
        buttonBases["button%d" % x].place(x=(177+(x*120))-w,y=450-z)
        
    scoreboard = PhotoImage(file = "dond_board - Copy.png") 
    scoreboardImage = fname.create_image(250,50,anchor = NE, image = scoreboard)
    
    ScoreBoardDict = {}
    ScoreBoardDictForStructure = {}
    z = 0
    w = 0
     
    for x in range(1,27):
        if x == 14:
            z = 120
            w = 342
        ScoreBoardDict["dollar%d$" % x] = PhotoImage(file = "dollar%d.png" % x)
        ScoreBoardDictForStructure["dollar%d$" % x] = fname.create_image(125+z,31+(x*26.25)-w,anchor = NE, image = ScoreBoardDict["dollar%d$" % x])

    numToPick = int(len(cases)//4)
    def GetCase(CaseNumber):
        """
        
        Called when a case is picked. Used to determine if the case is valid, check off the used $ on the left, remove the case, and the game's basic logic.
        """
        global numToPick
        global counter2
        global counter2
        offer = "_"
        
        def EndGame(money):
            """
            
            End game function. Tells you what you won.
            """
            
            if BankerApp.state() == 'normal':
                BankerApp.destroy()
            global Ender
            Ender = Toplevel()
            Ender.title("Deal or No Deal - You win")
            f2name = Canvas(Ender, bg = "light grey", height = 100, width=400)
            f2name.pack(side=TOP)
            
            text = "You won $" + str(money) + "!"
            EndLabel = Label(Ender, text=text).pack()
            
            def center(toplevel):
                '''
                
                Pulls tkinter box to the middle of the screen
                '''
                toplevel.update_idletasks()
                w = toplevel.winfo_screenwidth()
                h = toplevel.winfo_screenheight()
                size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
                x = w/2 - size[0]/2
                y = h/2 - size[1]/2
                toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
            
            win = Ender
            center(win)
            Ender.mainloop()

        
        def BankerOffer(offer):
            """
            
            Summons the banker.
            """
            global BankerApp
            BankerApp = Toplevel()
            BankerApp.title("Deal or No Deal - Banker Offer")
            numToPick = int(len(cases)//4)
            if numToPick <= 0:
                numToPick = 1
            f1name = Canvas(BankerApp, bg = "black", height = 263, width=400)
            f1name.pack(side=TOP)
            
            def NoCommand():
                """
                
                Command for the No button.
                """
                BankerApp.destroy()
                
            def YesCommand():
                """
                
                Command for the Yes button.
                """
                
                EndGame(offer)
                
                
            image11 = PhotoImage(file = "dealornodeal.png")   
            
            image = f1name.create_image(400,0,anchor = NE, image = image11)
            OfferText = "The Banker has made an offer for $" + str(offer) + "."
            OfferLabel = Label(BankerApp, text = OfferText).pack()
            
            YesButton = Button(BankerApp, text = "Yes", command = YesCommand)
            NoButton = Button(BankerApp, text = "No", command = NoCommand) 
            YesButton.pack(side=LEFT, anchor=SE)
            YesButton.config(width = 25)
            NoButton.pack(side=RIGHT, anchor=SW)
            NoButton.config(width = 25)
            
            
            def center(toplevel):
                '''
                
                Pulls tkinter box to the middle of the screen
                '''
                toplevel.update_idletasks()
                w = toplevel.winfo_screenwidth()
                h = toplevel.winfo_screenheight()
                size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
                x = w/2 - size[0]/2
                y = h/2 - size[1]/2
                toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
            
        
            win = BankerApp
            center(win)
            BankerApp.mainloop()
            
        choice = int(CaseNumber)
        if choice in cases:
            percentage = .2
            

            if counter2 != numToPick:

                choice = CaseNumber
                loc = cases.index(choice)
                tester = dollars[loc]
                fname.delete(ScoreBoardDictForStructure["dollar%d$" % int(int(dollarsDict.index(dollars[loc]))+1)])
                buttonBases["button%d" % CaseNumber].destroy()
                cases.pop(loc)
                dollars.pop(loc)

            counter2 += 1
            
            if counter2 == numToPick and len(cases) >= 2:
                counter2 = 0
                percentage += .07
                offer = int(sum(dollars)/len(cases)*percentage)
                numToPick = int(len(cases)//4)
                if numToPick <= 0:
                    numToPick = 1
                BankerOffer(offer)
        if len(cases) <= 1:
            EndGame(dollars[0])      
            
    
    def center(toplevel):
        '''
        
        Pulls tkinter box to the middle of the screen
        '''
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))
    

    win = app
    center(win)
    
    fname.pack()
    app.mainloop()
    
    app.quit()

MAIN()