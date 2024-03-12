from os import system

levels = {
    "abandonedBuildingEntrance": {
        "location": "Abandoned Building | Entrance",
        "firstTime": [
            True,
            "When the undead first attacked, we weren't ready.\n"\
            "The whole outbreak started over two weeks ago\n"\
            "and it's been getting worse since. This time we\n"\
            "barely made it out. Chuck was bitten, we both\n"\
            "knew what that meant. We decided to stay the night\n"\
            "in this abandoned buidling, we needed rest and sleep.\n"\
            "A huge horde of the living dead are coming this way,\n"\
            "they'll reach us by sunset. I have to lock this place\n"\
            "up before then, and maybe, just maybe, i'll be able to\n"\
            "live another day.\n\n"\
            "You can use help for a list of commands! Stay alive!"
        ],
        "states": {
            "open": "A sturdy, open wide door looks down over you.",
            "closed": "A sturdy, closed door looks down over you.",
            "locked": "A sturdy, locked door looks down over you.",
            "current": "open"
        },
        "movement": {
            "abandonedBuildingWindow": {
                "action": "west",
                "time": 0
            },
            "abandonedBuildingOutside": {
                "action": "east",
                "time": 0,
                "condition": "open",
                "unsuccesful": "The door is shut. That's not going to work buster."
            }
        },
        "interactions": [
            "door"
        ]
    },
    "abandonedBuildingWindow": {
        "location": "Abandoned Building | Window"
    }
}

class level:
    def __init__(self):
        self.scene = "abandonedBuildingEntrance"
        self.time = 480
    
    def convertTime(self):
        hours = str(self.time // 60)
        minutes = str(self.time % 60)

        if len(minutes) < 2:
            minutes = "0" + minutes

        return hours + ":" + minutes
    
    def hud(self):
        current = levels[self.scene]
        inputCheck = True

        print("Location: " + current["location"])
        print("Time Left: " + self.convertTime())
        print("_____________________________________________________________________\n")

        if current["firstTime"][0]:
            print(current["firstTime"][1] + "\n")
            current["firstTime"][0] = False
        
        print(current["states"][current["states"]["current"]] + "\n")

        action = input("Action: ").lower().split()

        system("cls")

        if action != "":
            if action[0] == "use"[:len(action[0])]:
                print(action[1])
                inputCheck = False
            elif action[0] == "interact"[:len(action[0])]:
                if action[1] == "door"[:len(action[1])]:
                    if current["states"]["current"] != "locked":
                        if current["states"]["current"] == "open":
                            current["states"]["current"] = "closed"
                        else:
                            current["states"]["current"] = "open"
                
                    inputCheck = False
                else:
                    for i in current["interactions"]:
                        if action[1] == i[:len(action[1])]:
                            pass
            else:
                for i, v in current["movement"].items():
                    if action[0] == v["action"][:len(action[0])]:
                        #self.scene = i
                        print(i)
                        inputCheck = False
        
        if inputCheck:
            print("Invalid Input! Try Again!")

        
game = level()

while True:
    game.hud()