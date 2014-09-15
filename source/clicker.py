"""This is the Teleporter clicker source"""
#This gets the stuff needed for gui
import tkinter as tk
#NOTICE:
#If any things in here seem unbalanced please tell me
class Building:
    """The base object for a building"""
    def __init__(self, cost, bpsadd, amt=0):
        self.cost = cost
        #How much it adds to the global bps
        self.bpsadd = bpsadd
        #Amount
        self.amt = amt

#BUILDINGS:
#All buildings have 3 types, the latter 2 are only unlocked through upgrades
#Going by base 10 values until I think of better ones
#Level 1,2, and 3 teleporters
TELE1 = Building(10, 0.1)
TELE2 = Building(100, 10)
TELE3 = Building(1000, 1000)
#ENGINEERS
ENGI = Building(100, 1)
MECHENGI = Building(1000, 100)
UBERENGI = Building(10000, 10000)
#SERVER
SERB12 = Building(1000, 10)
SERB24 = Building(10000, 1000)
SERB32 = Building(100000, 100000)
#GAME
GAMEL = Building(10000, 100)
GAMEM = Building(100000, 10000)
GAMEH = Building(1000000, 1000000)
#RED BRED
#2op4u
RBRED = Building(100000000, 100000000)
#ALL of the stuff above is here
BUILDLIST = [TELE1, TELE2, TELE3, ENGI, MECHENGI, UBERENGI, SERB24, SERB24,
             SERB32, GAMEL, GAMEM, GAMEH, RBRED]
class Application(tk.Frame):
    """The application used in bread teleportation"""
    def __init__(self, master=None):
        """To get this all set up"""
        tk.Frame.__init__(self, master)
        self.grid()
        self.buildings = BUILDLIST
        self.bread = 0
        self.bps = 0
        self.bislist = []
        self.createwidgets()

    def buybuilding(self, location):
        """The correct way of buying a building"""
        building = self.buildings[location]
        if self.bread >= building.cost:
            self.bread -= building.cost
            building.amt += 1
            building.cost = int(building.cost * 1.5)
            self.buildings[location] = building

    def recalcbps(self):
        """Recalculates the bps"""
        tempbps = 0
        for building in self.buildings:
            tempbps += building.amt * building.bpsadd
        self.bps = tempbps

    def addtoapp(self, name, text, tktype="Label", command=None, disabled=False,
                 grid=""):
        """The easy(?) way to add something to the APP"""
        exec("self.%s = tk.%s(self)" % (name, tktype))
        exec("self.%s['text'] = text" % (name))
        if not command == None:
            exec("self.%s['command'] = %s" % (name, command))
        if not disabled == False:
            exec("self.%s['state'] = tk.Disabled" % (name))
        exec("self.%s.grid(%s)" % (name, grid))
        if not text == "Teleport bread":
            self.bislist.append([name, text])

    def createwidgets(self):
        """Create the buttons and labels"""
        #GET BREAD BUTTON
        self.addtoapp("add_bread", "Teleport bread", "Button",
                      "lambda: increaseval('bread', 1)")
        #BREAD COUNT
        self.addtoapp("breadcount", "str(int(self.bread))")
        #BPS COUNT
        self.addtoapp("bpscount", "str(self.bps)")
        ##TELEPORTERS##
        self.teleframe = tk.Frame()
        self.teleframe.grid()
        #BUY TELE1 BUTTON
        self.addtoapp("teleframe.buy_tele1",
                      "'Buy a level 1 Teleporter (cost: %s)' % (str(self.buildings[0].cost))",
                      "Button", "lambda: APP.buybuilding(0)")
        #BUY TELE2 BUTTON
        self.addtoapp("teleframe.buy_tele2",
                      "'Buy a level 2 Teleporter (cost: %s)' % (str(self.buildings[1].cost))",
                      "Button", "lambda: APP.buybuilding(1)" #True
                      )
        #BUY TELE3 BUTTON
        self.addtoapp("teleframe.buy_tele3",
                      "'Buy a level 3 Teleporter (cost: %s)' % (str(self.buildings[2].cost))",
                      "Button", "lambda: APP.buybuilding(2)" #True
                      )
        ##ENGIS##
        self.engiframe = tk.Frame()
        self.teleframe.grid()
        #BUY ENGI BUTTON
        self.addtoapp("engiframe.buy_engi",
                      "'Buy an engineer (cost: %s)' % (str(self.buildings[3].cost))",
                      "Button", "lambda: APP.buybuilding(3)")
        #BUY MECHA ENGI BUTTON
        self.addtoapp("engiframe.buy_tobengi",
                      "'Buy a robotic engineer (cost: %s)' % (str(self.buildings[4].cost))",
                      "Button", "lambda: APP.buybuilding(4)" #True
                      )
        self.addtoapp("engiframe.buy_ubengi",
                      "'Buy an ubercharged engineer (cost: %s)' % (str(self.buildings[5].cost))",
                      "Button", "lambda: APP.buybuilding(5)" #True
                      )

    def updatewidgets(self):
        """It looks easy but I want to try and put a for loop in here"""
        for bis in self.bislist:
            exec("self.%s['text'] = %s" % (bis[0], bis[1]))


def increaseval(name, val):
    """Increasing values from tkinter (Expect this to be replaced)"""
    #DO NOT use this for buying buildings
    exec("APP.%s += val" % (name))

ROOT = tk.Tk()
APP = Application(master=ROOT)

def pigloop1():
    """This loop piggybacks on to tkinter's main loop"""
    APP.bread += APP.bps
    APP.after(1000, pigloop1)

def pigloop2():
    """This also piggybacks but is used for updating numbers"""
    APP.recalcbps()
    APP.updatewidgets()
    APP.after(100, pigloop2)

APP.after(0, pigloop1)
APP.after(0, pigloop2)
APP.mainloop()
