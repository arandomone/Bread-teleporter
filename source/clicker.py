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
#Engineers
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
#ALL of the stuff above is here
BUILDLIST = [TELE1, TELE2, TELE3, ENGI, MECHENGI, UBERENGI, SERB24, SERB24,
             SERB32, GAMEL, GAMEM, GAMEH]
class Application(tk.Frame):
    def __init__(self, master=None):
        """To get this all set up"""
        tk.Frame.__init__(self, master)
        self.grid()
        self.buildings = BUILDLIST
        self.bread = 0
        self.bps = 0
        self.bislist = []
        self.createWidgets()

    def increaseval(self, name, val):
        """Increasing values (Expect this to be replaced)"""
        #DO NOT use this for buying buildings
        exec("self." + name + " += " + str(val))

    def buybuilding(self, location):
        """The correct way of buying a building"""
        building = self.buildings[location]
        if self.bread >= building.cost:
            self.bread -= building.cost
            building.amt += 1
            building.cost *= 1.5 
            self.buildings[location] = building
        
    def recalcbps(self):
        """Recalculates the bps"""
        tempbps = 0
        for building in self.buildings:
            tempbps += building.amt * building.bpsadd
        self.bps = tempbps

    def addtoapp(self, name, text, tktype="Label", command=None, disabled=False,
                 grid = ""):
        """The easy(?) way to add something to the app"""
        exec("self." + name + " = tk." + tktype + "(self)")
        exec("self." + name + "['text'] = text")
        if not command == None:
            exec("self." + name + "['command'] = " + command)
        if not disabled == False:
            exec("self." + name + "['state'] = tk.DISABLED")
        exec("self." + name + ".grid(" + grid + ")")
        self.bislist.append([name, text])

    def createWidgets(self):
        """Create the buttons and labels"""
        #GET BREAD BUTTON
        self.addtoapp("add_bread", "Teleport bread", "Button",
                      "lambda: app.increaseval('bread', 1)")
        #BREAD COUNT
        self.addtoapp("breadcount", "str(self.bread)")
        #BPS COUNT
        self.addtoapp("bpscount", "str(self.bps)")
        ##TELEPORTERS##
        self.teleframe = tk.Frame()
        self.teleframe.grid(row=1)
        #BUY TELE1 BUTTON
        self.addtoapp("teleframe.buy_tele1",
                      "Buy a level 1 Teleporter (cost: " + str(self.buildings[0].cost) + " )",
                      "Button", "lambda: app.buybuilding(0)")
        #BUY TELE2 BUTTON
        self.addtoapp("teleframe.buy_tele2",
                      "Buy a level 2 Teleporter (cost: " + str(self.buildings[1].cost) + " )",
                      "Button", "lambda: app.buybuilding(1)" #True
                      )
        #BUY TELE3 BUTTON
        self.addtoapp("teleframe.buy_tele3",
                      "Buy a level 3 Teleporter (cost: " + str(self.buildings[2].cost) + " )",
                      "Button", "lambda: app.buybuilding(2)" #True
                      )
        
    def updateWidgets(self):
        """It looks easy but I want to try and put a for loop in here"""
        self.breadcount["text"] = str(int(self.bread))
        self.teleframe.buy_tele1["text"] = "Buy a level 1 Teleporter (cost: " + str(round(self.buildings[0].cost)) + " )"
        self.teleframe.buy_tele2["text"] = "Buy a level 2 Teleporter (cost: " + str(round(self.buildings[1].cost)) + " )"
        self.teleframe.buy_tele3["text"] = "Buy a level 3 Teleporter (cost: " + str(round(self.buildings[2].cost)) + " )"
        self.bpscount["text"] = str(self.bps)


root = tk.Tk()
app = Application(master=root)

def pigloop1():
    """This loop piggybacks on to tkinter's main loop"""
    app.bread += app.bps
    app.after(1000, pigloop1)

def pigloop2():
    app.recalcbps()
    app.updateWidgets()
    app.after(100, pigloop2)

app.after(0, pigloop1)
app.after(0, pigloop2)
app.mainloop()
