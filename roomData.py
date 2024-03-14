roomData = {
    "abandonedBuildingEntrance": {
        "name": "abandonedBuildingEntrance",
        "title": "abandoned building",
        "subtitle": "Entrance",
        "firstTimeText": "When the undead first attacked, we weren't ready.\n"\
            "The whole outbreak started over two weeks ago\n"\
            "and it's been getting worse since. This time we\n"\
            "barely made it out. Frank was bitten, we both\n"\
            "knew what that meant. We decided to stay the night\n"\
            "in this abandoned buidling, we needed rest and sleep.\n"\
            "A huge horde of the living dead are coming this way,\n"\
            "they'll reach us by sunset. I have to lock this place\n"\
            "up before then, and maybe, just maybe, i'll be able to\n"\
            "live another day.\n\n",
        "roomText": [
            "The entrance to the old, crumbling building is marked by\n"\
            "a large, worn wooden door. The door shows signs of age,\n"\
            "with peeling paint and patches of moss. It creaks as it moves,\n"\
            "revealing the bright outdoors contrasting sharply with the dim\n"\
            "interior of the abandoned building."
        ],
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
        "roomText": [
            "The room is dimly lit by daylight filtering through a dirty\n"\
            "window, illuminating an abandoned building's dusty interior. In one corner\n"\
            "lies a large container filled with sand, untouched for years. Frank, slumped\n"\
            "against the wall, bleeds profusely from a wound, his desperate eyes seeking\n"\
            "help amidst the desolation."
        ],
        "interactions": [],
        "movement": {
            "west": "abandonedBuildingHatch",
            "east": "abandonedBuildingEntrance"
        }
    },
    "abandonedBuildingHatch": {
        "name": "abandonedBuildingHatch",
        "title": "abandoned building",
        "subtitle": "Hatch",
        "firstTimeText": None,
        "roomText": [
            "A weathered shovel rests against the cracked wall, its wooden handle worn\n"\
            "smooth from years of use. Adjacent to it, a heavy hatch leading down to the basement\n"\
            "is secured with a rusted lock.",
            "A heavy hatch leading down to the basement is secured with a rusted lock.",
            "In the abandoned building, the spot where the shovel once leaned against the wall now\n"\
            "sits empty, while the hatch to the basement stands ajar, revealing the darkness within."
        ],
        "interactions": [
            "shovel",
            "hatch (locked)"
        ],
        "movement": {
            "south": "abandonedBuildingBasement",
            "east": "abandonedBuildingWindow"
        }
    },
    "abandonedBuildingOutside": {
        "name": "abandonedBuildingOutside",
        "title": "abandoned building",
        "subtitle": "Outside",
        "firstTimeText": "Out in the open, you watch the sun sinking low, its light casting long\n"\
            "shadows. With a sinking feeling, you realize you only have until 8 PM before the\n"\
            "zombie horde descends upon you, prompting you to act swiftly to fortify your defenses.",
        "roomText": [
            "A weathered dumpster sits beside a massive generator, both bearing the scars of time\n"\
            "and neglect. The surrounding broken fence barely stands against the encroaching wilderness,\n"\
            "while the entire scene is set upon barren dirt, devoid of life."
        ]
    }
}