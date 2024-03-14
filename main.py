from os import system
from roomData import roomData

system("cls")

class room:
    def __init__(self, name, title, subtitle, firstTimeText, roomText, interactions, movement):
        self.changeRoom = name
        self.title = title
        self.subtitle = subtitle
        self.roomText = roomText
        self.interactions = interactions
        self.movement = movement
        self.startScreen = True
        self.state = 0
        self.inventory = []

        if firstTimeText != None:
            self.firstTime = [True, firstTimeText]
        else:
            self.firstTime = [False]

    def calculateTime(self):
        hours = str(time // 60)
        minutes = str(time % 60)

        if len(minutes) < 2:
            minutes = "0" + minutes
        
        if hours == "0":
            hours = "12"
            minutes += " AM"
        else:
            minutes += " PM"
        
        return hours + ":" + minutes

    def colourText(self, colour, string):
        colours = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "purple": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
        }

        return "\033[1m" + colours[colour] + string + "\033[0m"

    def printASCII(self, string):
        art = {
            "default": [
                "┏┓┏┓┳┓┓┏┳┳┏┓┏┓┏┓┏┓┳┓┏┓┏┓┓┏┓ ┏┓┏┓┳┓┳┓",
                "┃┃┣ ┣┫┗┫┃┃┃┃┃┃┣┫┗┓┃┃┣ ┃┓┣┫┃ ┏┛┃ ┣┫┃┃",
                "┗┻┗┛┛┗┗┛┗┛┗┛┣┛┛┗┗┛┻┛┻ ┗┛┛┗┗┛┗┛┗┛┻┛┛┗"
            ],
            "w": [
                "┓ ┏",
                "┃┃┃",
                "┗┻┛"
            ],
            "t": [
                "┏┳┓",
                " ┃ ",
                " ┻ "
            ],
            "m": [
                "┳┳┓",
                "┃┃┃",
                "┛ ┗"
            ],
            "i": [
                "┳",
                "┃",
                "┻"
            ]
        }

        letters = [
            "q", "e", "r", "y",
            "u", "o", "p", "a",
            "s", "d", "f", "g",
            "h", "l", "z", "c",
            "b", "n"
        ]

        for i in range(3):
            toPrint = ""

            for v in string:
                if v == "i" or v == "w" or v == "t" or v == "m":
                    toPrint += art[v][i] + " "
                elif v == " ":
                    toPrint += "   "
                else:
                    toPrint += art["default"][i][letters.index(v) * 2:(letters.index(v) * 2) + 2] + " "
            
            print(self.colourText("red", toPrint))
    
    def inputManager(self):
        action = input(self.colourText("purple", "\033[1mAction: ")).lower().split()

        try:
            if action[0] != "":
                if len(action) == 1:
                    return action
                elif len(action) == 2:
                    if action[1] != "":
                        return action
                    else:
                        print("Error, Try Again!")
                        return " "
                else:
                    print("Error, Try Again!")
                    return " "
        except:
            print("Error, Try Again!")
            return " "
    
    def getCommand(self, string, command):
        if string == command[:len(string)]:
            return True
        else:
            return False
    
    def getStringInList(self, string, list):
        for i in list:
            if i == string:
                return True
        
        return False

    def errorMessage():
        print("Error, Try Again!")

    def interact(self, argument):
        if argument == "/":
            print("List of possible interactions:")

            for i in self.interactions:
                print(i.title())
        elif self.getCommand(argument, "door") and self.changeRoom == "abandonedBuildingEntrance":
            if self.state == 0:
                print("You grip the door handle tightly, thrusting it closed with a forceful slam.")

                self.state = 1
                self.interactions.append("door (closed)")
                self.interactions.remove("door (open)")
            elif self.state == 1:
                print("You grab the door handle and pull it open.")

                self.state = 0
                self.interactions.append("door (open)")
                self.interactions.remove("door (closed)")
            elif self.state == 2:
                print("You attempt to turn the doorknob, but it refuses to budge, signaling that the door is securely locked and inaccessible.")
        elif self.getCommand(argument, "shovel") and self.changeRoom == "abandonedBuildingHatch" and self.getStringInList("shovel", self.interactions):
            print("You pick up the weathered shovel.")

            self.state = 1
            self.inventory.append("shovel")
            self.interactions.remove("shovel")
        else:
            self.errorMessage()

    def use(self, argument):
        if argument == "/":
            print("Inventory:")

            if len(self.inventory) == 0:
                print("Nothing")
            else:
                for i in self.inventory:
                    print(i.title())

    def help(self):
        print("[" + self.colourText("yellow", "North, East, South, West") + "] Movement Commands")
        print("[" + self.colourText("yellow", "Map") + "] Displays the Map")
        print("[" + self.colourText("yellow", "Use") + "] Item Usage (Type / For a List of Items)")
        print("[" + self.colourText("yellow", "Interact") + "] Room Interaction (Type / For a List of Interactions)")
        print("[" + self.colourText("yellow", "Clear") + "] Clears the Console")
        print("[" + self.colourText("yellow", "Help") + "] Get the Command List\n")

    def run(self):
        if self.startScreen:
            system("cls")

            self.printASCII(self.title)

            if self.firstTime[0]:
                print(self.firstTime[1] + "\n")
                self.firstTime[0] = False
                system("pause")
                system("cls")
                self.printASCII(self.title)
            
            print(self.colourText("red", self.subtitle + " | " + self.calculateTime()) + "\n")
            self.help()
            
            if self.changeRoom == "abandonedBuildingEntrance":
                print(self.roomText[0] + "\n")
            else:
                print(self.roomText[self.state] + "\n")

            self.startScreen = False

        action = self.inputManager()
        
        if self.getCommand(action[0], "interact"):
            self.interact(action[1])
        elif self.getCommand(action[0], "clear"):
            self.startScreen = True
        elif self.getCommand(action[0], "help"):
            self.help()
        elif self.getCommand(action[0], "use"):
            self.use(action[1])
        
        for i, v in self.movement.items():
            if self.getCommand(action[0], i):
                self.changeRoom = v
                self.startScreen = True

        print("")

currentRoom = "abandonedBuildingEntrance"
time = 0
rooms = {}

for i, v in roomData.items():
    rooms[i] = room(v["name"], v["title"], v["subtitle"], v["firstTimeText"], v["roomText"], v["interactions"], v["movement"])

while True:
    rooms[currentRoom].run()

    if rooms[currentRoom].changeRoom != currentRoom:
        currentRoom = rooms[currentRoom].changeRoom