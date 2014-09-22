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

class Goal:
    """For achievements"""
    def __init__(self, text, task, prize=lambda: None):
        self.text = text
        self.task = task
        #What happens when completed
        self.prize = prize
        self.gotten = False

#BUILDINGS:
#Going by base 10 values until I think of better ones
#Level 1,2, and 3 teleporters
TELE1 = Building(10, 0.1)
TELE2 = Building(100, 10)
TELE3 = Building(1000, 1000)
#ENGINEERS
ENGI = Building(100, 1)
MECHENGI = Building(1000, 100)
UBERENGI = Building(10000, 10000)
#LASTS
SERB = Building(100000, 1000)
GAME = Building(1000000, 100000)
#2op4u
RBRED = Building(100000000, 100000000)
#ALL of the stuff above is here
BUILDLIST = [TELE1, TELE2, TELE3, ENGI, MECHENGI, UBERENGI, SERB, GAME, RBRED]

#ACHIEVEMENTS:
ACH1 = Goal("'It begins!'", lambda: APP.totalbread == 1)
ACH2 = Goal("'Actually playing!'", lambda: APP.totalbread == 10)
ACH3 = Goal("'Dont stop now!'", lambda: APP.totalbread == 100)
ACH4 = Goal("'Love!'", lambda: APP.bps == 1)
ACH5 = Goal("'And!'", lambda: APP.bps == 10)
ACH6 = Goal("'War!'", lambda: APP.bps == 100)
ACH7 = Goal("'Update!'", lambda: APP.bps == 1000)
ACH8 = Goal("'Confirmed!'", lambda: APP.bps == 10000)
ACH9 = Goal("'Released!'", lambda: APP.bps == 100000)
ACH10 = Goal("'Keep going!'", lambda: APP.clicks == 10)
ACH11 = Goal("'Your doing great!'", lambda: APP.clicks == 100)
ACH12 = Goal("'Its time to stop clicking!'", lambda: APP.clicks == 1000)
ACH13 = Goal("'Autoclicker!'", lambda: APP.clicks == 10000)

ACHLIST = [ACH1, ACH2, ACH3, ACH4, ACH5, ACH6, ACH7, ACH8, ACH9, ACH10, ACH11,
           ACH12, ACH13]
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
        ##TELEPORTERS##
        self.teleframe = tk.Frame()
        self.teleframe.grid(row=3, column=0)
        #BUY TELE1 BUTTON
        self.addtoapp("teleframe.buy_tele1",
                      "'Buy a level 1 Teleporter (cost: %i)' % (APP.buildings[0].cost)",
                      "Button", "lambda: APP.buybuilding(0)")
        #BUY TELE2 BUTTON
        self.addtoapp("teleframe.buy_tele2",
                      "'Buy a level 2 Teleporter (cost: %i)' % (APP.buildings[1].cost)",
                      "Button", "lambda: APP.buybuilding(1)")
        #BUY TELE3 BUTTON
        self.addtoapp("teleframe.buy_tele3",
                      "'Buy a level 3 Teleporter (cost: %i)' % (APP.buildings[2].cost)",
                      "Button", "lambda: APP.buybuilding(2)")
        ##ENGIS##
        self.engiframe = tk.Frame()
        self.teleframe.grid(row=3, column=1)
        #BUY ENGI BUTTON
        self.addtoapp("engiframe.buy_engi",
                      "'Buy an engineer (cost: %i)' % (APP.buildings[3].cost)",
                      "Button", "lambda: APP.buybuilding(3)")
        #BUY MECHA ENGI BUTTON
        self.addtoapp("engiframe.buy_tobengi",
                      "'Buy a robotic engineer (cost: %i)' % (APP.buildings[4].cost)",
                      "Button", "lambda: APP.buybuilding(4)")
        #BUY UBER ENGI BUTTON
        self.addtoapp("engiframe.buy_ubengi",
                      "'Buy an ubercharged engineer (cost: %i)' % (APP.buildings[5].cost)",
                      "Button", "lambda: APP.buybuilding(5)")
        ##LASTS###
        self.lastframe = tk.Frame()
        self.lastframe.grid(row=3, column=2)
        #BUY SERVER
        self.addtoapp("lastframe.buy_serb",
                      "'Buy your own server (cost: %i)' % (APP.buildings[6].cost)",
                      "Button", "lambda: APP.buybuilding(6)")
        #BUY GAME
        self.addtoapp("lastframe.buy_game",
                      "'Buy a game making company (cost: %i)' % (APP.buildings[7].cost)",
                      "Button", "lambda: APP.buybuilding(7)")
        #BUY RED BRED
        self.addtoapp("lastframe.buy_rbred",
                      "'Buy Red Bread (cost: %i)' % (APP.buildings[8].cost)",
                      "Button", "lambda: APP.buybuilding(8)")


def increasebread(val=1, click=False):
    """Increasing values from tkinter (Expect this to be replaced)"""
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
    APP.after(100, pigloop2)

APP.after(0, pigloop1)
APP.after(0, pigloop2)
APP.mainloop()
