levels = {
    "start": {
        "location": "Home Base | Entrance",
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
            "live another day."
        ]
    }
}

class level:
    def __init__(self):
        self.scene = "start"
        self.time = 480
    
    def convertTime(self):
        hours = str(self.time // 60)
        minutes = str(self.time % 60)

        if len(minutes) < 2:
            minutes = "0" + minutes

        return hours + ":" + minutes
    
    def hud(self):
        current = levels[self.scene]
        print(current["location"])
        print(self.convertTime())
        print("_____________________________________________________________________")

        if current["firstTime"][0]:
            print(current["firstTime"][1])
        
test = level()
test.hud()