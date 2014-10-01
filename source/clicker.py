"""This is the Teleporter clicker source"""
#This gets the stuff needed for gui
import tkinter as tk
#NOTICE:
#If any things in here seem unbalanced please tell me
class Building:
    """The base object for a building"""
    def __init__(self, cost, bpsadd):
        self.cost = cost
        #How much it adds to the global bps
        self.bpsadd = bpsadd
        #Amount
        self.amt = 0

class Achievement:
    """For achievements dummy"""
    def __init__(self, text, task, prize=lambda: None):
        self.text = text
        self.task = task
        #What happens when completed
        self.prize = prize
        self.gotten = False

class Upgrade:
    """For upgrades"""
    def __init__(self, name, text, cond, cost, effect, location):
        self.name = name
        self.text = text
        self.cond = cond
        self.cost = cost
        self.effect = effect
        self.loc = location
        self.bought = False
        self.shown = False

#BUILDINGS:
#Going by base 10 values until I think of better ones
#Level 1,2, and 3 teleporters
TELE = Building(10, 0.1)
#ENGINEERS
ENGI = Building(100, 1)
#LASTS
SERB = Building(1000, 10)
GAME = Building(10000, 100)
#2op4u
RBRED = Building(100000, 1000)
#ALL of the stuff above is here
BUILDLIST = [TELE, ENGI, SERB, GAME, RBRED]

#ACHIEVEMENTS:
ACH1 = Achievement("'It begins!'", lambda: APP.totalbread == 1)
ACH2 = Achievement("'Actually playing!'", lambda: APP.totalbread == 10)
ACH3 = Achievement("'Dont stop now!'", lambda: APP.totalbread == 100)
ACH4 = Achievement("'Love!'", lambda: APP.bps == 1)
ACH5 = Achievement("'And!'", lambda: APP.bps == 10)
ACH6 = Achievement("'War!'", lambda: APP.bps == 100)
ACH7 = Achievement("'Update!'", lambda: APP.bps == 1000)
ACH8 = Achievement("'Confirmed!'", lambda: APP.bps == 10000)
ACH9 = Achievement("'Released!'", lambda: APP.bps == 100000)
ACH10 = Achievement("'Keep going!'", lambda: APP.clicks == 10)
ACH11 = Achievement("'Your doing great!'", lambda: APP.clicks == 100)
ACH12 = Achievement("'Its time to stop clicking!'", lambda: APP.clicks == 1000)
ACH13 = Achievement("'Autoclicker!'", lambda: APP.clicks == 10000)

ACHLIST = [ACH1, ACH2, ACH3, ACH4, ACH5, ACH6, ACH7, ACH8, ACH9, ACH10, ACH11,
           ACH12, ACH13]
#UPGRADES:
UP1 = Upgrade("tele1", "Level 2 teleporters", lambda: APP.buildings[0].amt == 1,
              100, lambda: exec("APP.buildings[0].bpsadd *= 2"), 0)
UP2 = Upgrade("tele2", "Level 3 teleporters", lambda: APP.buildings[0].amt == 50,
              10000, lambda: exec("APP.buildings[0].bpsadd *= 4"), 1)
UP3 = Upgrade("tele", "Level 4 teleporters", lambda: APP.buildings[0].amt == 100,
              100000, lambda: exec("APP.buildings[0].bpsadd *= 6"), 2)
UPLIST = [UP1, UP2, UP3]
class Application(tk.Frame):
    """The application used in bread teleportation"""
    def __init__(self, master=None):
        """To get this all set up"""
        tk.Frame.__init__(self, master)
        self.grid()
        self.buildings = BUILDLIST
        self.bread = 0
        self.totalbread = 0
        self.bps = 0
        self.clicks = 0
        self.achievements = ACHLIST
        self.upgrades = UPLIST
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
    
    def buyupgrade(self, location):
        """testing/buying upgrades"""
        upgrade = self.upgrades[location]
        if self.bread >= upgrade.cost:
            self.bread -= upgrade.cost
            upgrade.bought = True
            upgrade.effect()
            print("You have bought the %s upgrade!" % (upgrade.text))
            exec("self.upframe.%s.destroy()" % (upgrade.name))
            


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
        #The little band-aid
        if not text == "Teleport bread":
            self.bislist.append([name, text])

    def createwidgets(self):
        """Create the buttons and labels"""
        #GET BREAD BUTTON
        self.addtoapp("add_bread", "Teleport bread", "Button",
                      "lambda: increasebread(1, True)", grid="row=0, column=0")
        #BREAD COUNT
        self.addtoapp("breadcount", "'You have %i breads' % (APP.bread)", grid="row=1, column=0")
        #BPS COUNT
        self.addtoapp("bpscount", "'You are making %s bread per second' % (str(APP.bps))", grid="row=2, column=0")
        #BUY TELE BUTTON
        self.addtoapp("buy_tele",
                      "'Buy a Teleporter (cost: %i)' % (APP.buildings[0].cost)",
                      "Button", "lambda: APP.buybuilding(0)")
        #BUY ENGI BUTTON
        self.addtoapp("buy_engi",
                      "'Buy an engineer (cost: %i)' % (APP.buildings[1].cost)",
                      "Button", "lambda: APP.buybuilding(1)")
        #BUY SERVER
        self.addtoapp("buy_serb",
                      "'Buy your own server (cost: %i)' % (APP.buildings[2].cost)",
                      "Button", "lambda: APP.buybuilding(2)")
        #BUY GAME
        self.addtoapp("buy_game",
                      "'Buy a game making company (cost: %i)' % (APP.buildings[3].cost)",
                      "Button", "lambda: APP.buybuilding(3)")
        #BUY RED BRED
        self.addtoapp("buy_rbred",
                      "'Buy Red Bread (cost: %i)' % (APP.buildings[4].cost)",
                      "Button", "lambda: APP.buybuilding(4)")
        self.upframe = tk.Frame()
        self.upframe.grid()
        
    def addupgrade(self, up):
        exec("self.upframe.%s = tk.Button(self)" % (up.name))
        exec("self.upframe.%s['text'] = up.text + ' (cost: %i)'" % (up.name, up.cost))
        exec("self.upframe.%s['command'] = lambda: APP.buyupgrade(%s)" % (up.name, up.loc))
        exec("self.upframe.%s.grid()" % (up.name))
        self.upgrades[up.loc].shown = True


def increasebread(val=1, click=False):
    """Increasing values from tkinter (Expect this to be replaced( or not))"""
    #DO NOT use this for buying buildings
    APP.bread += val
    APP.totalbread += val
    if click:
        APP.clicks += 1

ROOT = tk.Tk()
APP = Application(master=ROOT)

def pigloop1():
    """This loop piggybacks on to tkinter's main loop"""
    increasebread(APP.bps)
    APP.after(1000, pigloop1)

def pigloop2():
    """This also piggybacks but is used for updating numbers"""
    #BPS RECALCULATION
    tempbps = 0
    for building in APP.buildings:
        tempbps += building.amt * building.bpsadd
    APP.bps = tempbps
    #BUILDING UPDATE
    for bis in APP.bislist:
        exec("APP.%s['text'] = %s" % (bis[0], bis[1]))
    #ACHIEVEMENT UPDATE
    for goal in APP.achievements:
        if goal.task() and not goal.gotten:
            goal.prize()
            print("You have achieved the %s achievement!" % (goal.text))
            goal.gotten = True
    #UPGRADE UPDATE
    for up in APP.upgrades:
        if up.cond() and not up.bought and not up.shown:
            APP.addupgrade(up)
    APP.after(100, pigloop2)

APP.after(0, pigloop1)
APP.after(0, pigloop2)
APP.mainloop()
