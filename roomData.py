roomData = {
    "abandonedBuildingEntrance": {
        "name": "abandonedBuildingEntrance",
        "title": "abandoned building",
        "subtitle": "Entrance",
        "firstTimeText": "When the undead first attacked, we weren't ready.\n"\
            "The whole outbreak started over two weeks ago\n"\
            "and it's been getting worse since. This time we\n"\
            "barely made it out. Chuck was bitten, we both\n"\
            "knew what that meant. We decided to stay the night\n"\
            "in this abandoned buidling, we needed rest and sleep.\n"\
            "A huge horde of the living dead are coming this way,\n"\
            "they'll reach us by sunset. I have to lock this place\n"\
            "up before then, and maybe, just maybe, i'll be able to\n"\
            "live another day.\n\n",
        "roomText": "The entrance to the old, crumbling building is marked by\n"\
            "a large, worn wooden door. The door shows signs of age,\n"\
            "with peeling paint and patches of moss. It creaks as it moves,\n"\
            "revealing the bright outdoors contrasting sharply with the dim\n"\
            "interior of the abandoned building.",
        "interactions": [
            "door (open)"
        ],
        "movement": {
            "west": "abandonedBuildingWindow",
            "east": "abandonedBuildingOutside"
        }
    },
    "abandonedBuildingWindow": {
        "name": "abandonedBuildingWindow",
        "title": "abandoned building",
        "subtitle": "Window",
        "firstTimeText": "\"Ugh... This... this isn't good. It hurts like hell...\n"\
            "But I'm still... still hanging on. Hey, you... you gotta help me, please.\n"\
            "I don't wanna end up like those... those things out there. Get me outta here\n"\
            "before it's too late.\" Frank winces in pain, blood dripping from his wound.\n"\
            "\"I know I'm asking a lot, but I can't... I can't stay here like this.\n"\
            "I trust you... please.\"",
        "roomText": "The room is dimly lit by daylight filtering through a dirty\n"\
            "window, illuminating an abandoned building's dusty interior. In one corner\n"\
            "lies a large container filled with sand, untouched for years. Frank, slumped\n"\
            "against the wall, bleeds profusely from a wound, his desperate eyes seeking\n"\
            "help amidst the desolation.",
        "interactions": [],
        "movement": {
            "west": "abandonedBuildingHatch",
            "east": "abandonedBuildingEntrance"
        }
    }
}