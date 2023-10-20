label after_load:
python:
    renpy.music.stop("ctc")
    renpy.music.stop("altcry")
    renpy.music.stop("XYgame")
    renpy.music.stop("crowd")
    renpy.music.stop("crowd2")
    renpy.music.stop("crowd3")
    renpy.music.stop("points")
    renpy.music.stop("misc")
    changemade = False
    for keyname in defaultpersondex.keys():
        if (keyname in persondex.keys()):
            if "Sex" not in persondex[keyname].keys():
                changemade = True
                persondex[keyname]["Sex"] = defaultpersondex[keyname]["Sex"]
            if "Relationship" not in persondex[keyname].keys():
                changemade = True
                persondex[keyname]["Relationship"] = defaultpersondex[keyname]["Relationship"]
            if "RelationshipRank" not in persondex[keyname].keys():
                changemade = True
                persondex[keyname]["RelationshipRank"] = 0
            if "Events" not in persondex[keyname].keys():
                changemade = True
                persondex[keyname]["Events"] = []

            if ("Instructor" in keyname or "Instructrice" in keyname or "Sensei" in keyname or "Lieutenant" in keyname):
                if (IsBefore(12, 4, 2004) and persondex[keyname]["ClassesKnown"] == [] and classstats[classtaught[keyname]] > 0):
                    changemade = True
                    persondex[keyname]["ClassesKnown"].append(1)
        else:
            changemade = True
            persondex[keyname] = copy.deepcopy(defaultpersondex[keyname])

    if ("Kris" in persondex.keys()):
        changemade = True
        del persondex["Kris"]

    if (persondex["Professor Cherry"]["Value"] > 0 and IsBefore(8, 4, 2004)):
        changemade = True
        persondex["Professor Cherry"]["Value"] = 0

    if (len(playerparty) == 1 and playerparty[0].GetLevel() == 5):
        changemade = True
        playerparty[0].Moves = GetStartingMoves(playerparty[0])

    if (len(persondex["Tia"]["ClassesKnown"]) > 2):
        changemade = True
        persondex["Tia"]["ClassesKnown"] = ["Dragon", "Psychic"]

    if ('starter_species_name' not in globals()):
        changemade = True
        starter_species_name = pokedexlookup(starter_id, DexMacros.Name)

    if ('starterobj' not in globals() or starterobj == None):
        for mon in playerparty + box:
            if (mon.GetNickname() == starter_name and mon.GetId() == starter_id):
                changemade = True
                starterobj = mon

    if (starterobj != None):
        if (starter_id != starterobj.GetId()):
            changemade = True
            starter_id = starterobj.GetId()

        if (starter_name != starterobj.GetNickname()):
            changemade = True
            starter_name = starterobj.GetNickname()

        if (starter_species_name != pokedexlookup(starterobj.GetId(), DexMacros.Name)):
            changemade = True
            starter_species_name = pokedexlookup(starterobj.GetId(), DexMacros.Name)

    for mon in playerparty + box:
        for problemmove in mon.GetMoves():
            if (isinstance(problemmove.Power, str)):
                changemade = True
                problemmove.Power = GetMove(problemmove.Name).Power

    if (taughtmove != None):
        taughtmove = None
        changemade = True

    if (activeitem != None):
        activeitem = None
        changemade = True

    if (randseedtime == None):
        randseedtime = time.localtime()
        changemade = None

    luckyeggcount = 0
    for mon in playerparty + box:
        if (mon.Item == "Lucky Egg"):
            luckyeggcount += 1
    luckyeggcount += GetItemCount("Lucky Egg")
    if (luckyeggcount > 1):
        changemade = True
        for mon in playerparty + box:
            if (mon.Item == "Lucky Egg"):
                mon.Item = None
        inventory["Lucky Egg"] = 1

    experiencesharecount = 0
    for mon in playerparty + box:
        if (mon.Item == "Experience Share"):
            experiencesharecount += 1
    experiencesharecount += GetItemCount("Experience Share")
    if (experiencesharecount > 1):
        changemade = True
        for mon in playerparty + box:
            if (mon.Item == "Experience Share"):
                mon.Item = None
        inventory["Experience Share"] = 1

    if (changemade):
        renpy.block_rollback()

    pkmnlocked = -1
    randcount = randcount % 1000000

return


define defaultpersondex = {
        "Professor Oak" : {"Named" : True, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Blue" : {"Named" : True, "Value" : 0, "Contact": True, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": []},
        "Silver" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": []},
        "Brawly" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": []},
        "Roxanne" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": []},
        "Falkner" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": []},
        "Leaf" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Ethan" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Calem" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Hilbert" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": []},
        "Brendan" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "May" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Flannery" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Whitney" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Sabrina" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": []},
        "Serena" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Cheren" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": []},
        "Misty" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": []},
        "Bianca" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Dawn" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": []},
        "Nate" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Rosa" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Bea" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Training Partner", "RelationshipRank": 0, "Events": []},
        "Nessa" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Date", "RelationshipRank": 0, "Events": []},
        "Hilda" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Gardenia" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Skyla" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Brock" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": []},
        "Erika" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": []},
        "Janine" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Tool", "RelationshipRank": 0, "Events": []},
        "Tia" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Protector", "RelationshipRank": 0, "Events": []},
        "Sonia" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": []},
        "Jasmine" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": []},
        "Grusha" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": []},
        "Victini" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Unexpected Interloper", "RelationshipRank": 0, "Events": []},
        "Professor Cherry" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Lenora" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Blaine" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Wallace" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Ramos" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Lieutenant Surge" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Melony" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Sensei Marshal" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Grasshopper", "RelationshipRank": 0, "Events": []},
        "Instructor Koga" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Bertha" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Will" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Burgh" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Olivia" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructrice Fantina" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Karen" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Clair" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Byron" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Valerie" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Instructor Winona" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Bruno" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Alder" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Lance" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": []},
        "Iris" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": []},
        "Dean Drayden" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": []}
    }

init python:
    def SetRandSeed(staySame = False, extraseed = ""):
        global randcount
        if (not IsBefore(6, 4, 2004)):
            random.seed(str(randseedtime) + str(calDate.day) + str(calDate.month) + str(calDate.year) + ("" if staySame else str(randcount)) + extraseed)
            if (not staySame):
                randcount += 1

    def RandomUniform(min, max):
        SetRandSeed()
        return random.uniform(min, max)

    def Random(staySame = False, extraseed = ""):
        SetRandSeed(staySame, extraseed)
        return random.random()

    def RandomChoice(options, staySame = False):
        SetRandSeed(staySame)
        return random.choice(options)
    
    def RandomChoices(options, k):
        SetRandSeed()
        return random.choices(options, k=k)

    def RandInt(min, max):
        SetRandSeed()
        return random.randint(min, max)

    def KnowClasses(name, classList):
        if name in persondex:
            for classname in classList:
                if (classname not in persondex[name]["ClassesKnown"]):
                    persondex[name]["ClassesKnown"].append(classname)
        else:
            persondex[name] = {"Named" : False, "Value" : 0, "Contact" : False, "ClassesKnown" : classList }

    def BecomeNamed(name):
        if name in persondex:
            persondex[name]["Named"] = True
        else:
            persondex[name] = {"Named" : True, "Value" : 0, "Contact" : False, "ClassesKnown" : [] }

    renpy.add_layer("arrowlayer", above="master")

    def AnimateArrow(value, position):
        imagename = "pointsplus" + str(value)
        if (value < 0):
            imagename = "pointsminus" + str(-value)
            
        tagname = "name" + str(value) + ''.join(RandomChoices(string.ascii_lowercase, 10))
        renpy.show(imagename, [pointsup(position)], tag=tagname, layer="arrowlayer")

        renpy.music.set_volume(0.25, delay=0.0, channel="music")
        if (value > 0):
            renpy.sound.play("Audio/PointsUp.ogg", channel="misc")
        else:
            renpy.sound.play("Audio/PointsDown.ogg", channel="misc")   
        renpy.music.set_volume(1.0, delay=2.0, channel="music")

    def ValueChange(name, value, position, pausing=True):
        if name in persondex:
            persondex[name]["Value"] += value
        else:
            persondex[name] = {"Named" : True, "Value" : value, "Contact" : False, "ClassesKnown" : [] }

        AnimateArrow(value, position)
        if (pausing):
            renpy.pause(1.5)

    def InvestmentChange(value, ignoremoney = False):
        global money
        global investment
        if (money >= value or ignoremoney):
            money -= value
            investment += value
            PlaySound("PointsUp.ogg")
            renpy.say(narrator, "You invested ${}! Your total investment is now ${}!".format(value, investment))
        else:
            PlaySound("PointsDown.ogg")
            renpy.say(narrator, "You don't have enough money to invest ${}!".format(value))

    def TraitChange(name):
        personalstats[name] += 1
        color = ""
        if (name == "Charm"):
            color = "#b7669e"
        elif (name == "Knowledge"):
            color = "#66b77d"
        elif (name == "Courage"):
            color = "#ff8412"
        elif (name == "Wit"):
            color = "#60c2f8"
        elif (name == "Patience"):
            color = "#e226a6"

        renpy.show("traitspointplus1", [pointsup(0.5), Transform(matrixcolor=TintMatrix(color))])
        renpy.music.set_volume(0.5, delay=0.0, channel="music")
        renpy.music.set_volume(1.0, delay=0.0, channel="points")
        renpy.music.play("Audio/PointsUp.ogg", channel='points', loop=None)
        renpy.say("", "Your {{color={}}}{}{{/color}} increased to {}!".format(color, name, personalstats[name]))
        
        renpy.pause(1.5)
        renpy.hide("traitspointplus1")
        renpy.music.set_volume(1.0, delay=0.25, channel="music")

    def BecomeContacted(name):
        renpy.music.set_volume(0.0, delay=0.0, channel="music")
        renpy.sound.play("Audio/PhoneNumber.mp3")

        if name in persondex:
            persondex[name]["Contact"] = True
        else:
            persondex[name] = {"Named" : False, "Value" : 0, "Contact" : True, "ClassesKnown" : [] }

        renpy.music.set_volume(1.0, delay=1.5, channel="music")
        renpy.say("", "{{color=#e70000}}{{cps=0}}Received {}'s contact info!{{/cps}}{{w=2.0}}{{/color}}".format(name))
        renpy.pause(2.0, hard=True)

    def WonBattle(battle_id):
        if (battle_id in gymbattles.keys()):
            return gymbattles[battle_id]
        else:
            return False

    def HealParty(trainer = None):
        if (trainer == None):
            for pkmn in playerparty:
                pkmn.Heal()
        else:
            for pkmn in trainer.GetTeam():
                pkmn.Heal()

    def GetColor(monid):
        formatcolor = "#000"
        dexcolor = pokedexlookup(monid, DexMacros.Color)
        if (dexcolor == "Red"):
            formatcolor = "#ff0000"
        elif (dexcolor == "Blue"):
            formatcolor = "#0000ff"
        elif (dexcolor == "Yellow"):
            formatcolor = "#c4a300"
        elif (dexcolor == "Green"):
            formatcolor = "#00ff00"
        elif (dexcolor == "Brown"):
            formatcolor = "#ff8000"
        elif (dexcolor == "Purple"):
            formatcolor = "#ff00ff"
        elif (dexcolor == "Gray"):
            formatcolor = "#6b6b6b"
        elif (dexcolor == "Pink"):
            formatcolor = "#ff57b4"
        elif (dexcolor == "White"):
            formatcolor = "#282828"
        return formatcolor

    class CustomCharacter():
        def __init__(self, name, color, image):
            self.image = image
            self.name = name
            self.color = color
            self.do_extend = donothing
            self.empty_window = donothing

        def __call__(self, what, **kwargs):
            if (what == ""):
                _window_hide(None)
                return Character(name="", color=self.color, image=self.image)("{nw}", **kwargs)
            else:
                formatname = self.name
                dynamic = False
                formatcolor = self.color

                if (formatname == "Red"):
                    formatname = (lambda: first_name)
                elif (formatname == "Pikachu"):
                    formatname = (lambda: pika_name)
                elif (formatname == "Blue" and persondex["Blue"]["Named"]):
                    formatname = (lambda: blue_name)
                elif (formatname == "Kris"):
                    formatname = "Professor Cherry"
                elif (formatname == "Your Starter"):
                    formatcolor = GetColor(starter_id)
                    formatname = (lambda: starter_name)
                elif (formatname == "Sidemon"):
                    formatcolor = GetColor(sidemonnum)
                    formatname = (lambda: pokedexlookup(sidemonnum, DexMacros.Name))
                elif (formatname == "Victini" and persondex["Victini"]["Named"]):
                    formatname = (lambda: victini_name)

                dynamic = self.name != formatname

                if (formatname in persondex.keys() and not persondex[formatname]["Named"]):
                    formatname = "???"

                formatcallback=callbackcontinue

                if (formatname == "You"):
                    formatwhat = "{{i}}({}){{/i}}".format(what)
                elif (formatname == ""):
                    formatwhat = ">{{cps=*0.8}}{}".format(what)
                elif (formatname == "Tia"):
                    if (what[-4:] == "{nw}"):#if this sentence ends in a no-wait...
                        formatcallback=None
                        formatwhat = "<{}".format(what)#remove the ending quote
                    else:
                        formatwhat = "<{}>".format(what)
                elif (what[-4:] == "{nw}"):#if this sentence ends in a no-wait...
                    formatcallback=None
                    formatwhat = "\"{}".format(what)#remove the ending quote
                else:
                    formatwhat = "\"{}\"".format(what)

                if (not profanity):
                    profanitylist = ["fuck", "shit", "Crap", " crap", "...crap", "...Crap", "damn", "dick", " ass ", "asshole", "goddamn", "bullshit", "horseshit", "bullcrap", "dickhead", "dickheads", "bitch", "bastard", "kickASS", "ASSBAGS", "jackass", "douchebag", "pussy"]
                    for word in profanitylist:
                        replacement = "*" * len(word)
                        formatwhat = formatwhat.replace(word, replacement).replace(word.capitalize(), replacement).replace(word.upper(), replacement).replace(word + "s", replacement + "s").replace(word + "es", replacement + "es")

                return Character(name=formatname, color=formatcolor, image=self.image, ctc="ctc_blink", ctc_position="fixed", callback=formatcallback, dynamic=dynamic)(formatwhat, **kwargs)           

    renpy.music.register_channel("ctc", mixer="sfx", loop=False)
    renpy.music.register_channel("altcry", mixer="sfx", loop=False)
    renpy.music.register_channel("XYgame", mixer="music", loop=False)
    renpy.music.register_channel("crowd", mixer="sfx", loop=True)
    renpy.music.register_channel("crowd2", mixer="sfx", loop=True)
    renpy.music.register_channel("crowd3", mixer="sfx", loop=False)
    renpy.music.register_channel("points", mixer="sfx", loop=False)
    renpy.music.register_channel("misc", mixer="sfx", loop=False)

    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.music.play("Audio/Button_A.wav", channel="ctc")

    def donothing():
            pass

    def getCharColor(findname):
        for char in charlist:
            if (findname.lower() in char.name.lower() or (char.image == "red" and findname == first_name) or (char.image == "pikachu" and findname == pika_name) or (char.image == "blue" and findname == blue_name)):
                return char.color
        return "#000"
    
    def getTotalElectives():
        return classstats["Normal"] + classstats["Fire"] + classstats["Water"] + classstats["Grass"] + classstats["Electric"] + classstats["Ice"] + classstats["Fighting"] + classstats["Poison"] + classstats["Ground"] + classstats["Flying"] + classstats["Psychic"] + classstats["Bug"] + classstats["Rock"] + classstats["Ghost"] + classstats["Dark"] + classstats["Dragon"] + classstats["Steel"] + classstats["Fairy"]

    def getElective(type):
        return classstats[type]

    def getRankStat(rank):
        return sorted(classstats.items(), key=lambda x:x[1], reverse=True)[rank][0]

    def GetCharacterLevel(character):
        x = persondex[character]["Value"]
        iterations = 0
        iterator = 5
        totalsize = 0

        while (x >= totalsize):
            iterations += 1
            iterator += 5
            totalsize += iterator

        return iterations

    def GetEXPRequiredForLevel(character):
        level = GetCharacterLevel(character)

        iterations = 0
        iterator = 5
        totalsize = 0
        for i in range(0, level):
            iterations += 1
            iterator += 5
            totalsize += iterator

        return totalsize

    def GetHighestLevel():
        highestlevel = 0
        for mon in playerparty:
            if (mon.GetLevel() > highestlevel):
                highestlevel = mon.GetLevel()
        return highestlevel

    def GetAllPokemonIn():
        return [446, 143, 427, 428, 428.1, 359, 870, 506, 4, 258, 387, 179, 363, 532, 41, 328, 396, 280, 540, 246, 607, 551, 371, 304, 669, 206, 554, 194, 548, 170, 361, 447, 747, 529, 198, 677, 290, 566, 200, 559, 696, 597, 742, 531, 631, 746, 781, 556, 479, 615, 214, 336, 618, 357, 561, 213, 774, 778, 302, 780, 227, 303, 263, 155, 399, 191, 835, 133, 919, 406, 29, 32, 333, 307, 401, 111, 710, 659, 967, 777, 764, 431, 607, 767, 412, 81, 351, 559, 568, 104, 629, 677, 917, 744, 353, 88.1, 714, 965, 439, 507, 5, 259, 388, 180, 364, 533, 42, 329, 397, 281, 541, 247, 608, 552, 372, 305, 670, 982, 555, 195, 549, 171, 362, 448, 748, 530, 199, 678, 291, 567, 429, 560, 697, 598, 743, 264, 156, 400, 192, 836, 134, 920, 315, 30, 33, 334, 308, 402, 112, 711, 660,432, 608, 768, 413, 82,560, 569, 105, 630, 678, 918, 745, 354, 89.1, 715, 966, 122, 508, 6, 260, 389, 181, 365, 534, 169, 330, 398, 282, 542, 248, 609, 553, 373, 306, 671,478,430, 678.1, 292,157,135,407, 31, 34,464, 609,414, 462,745.1,745.2, 136, 196, 197, 470, 471, 700, 636, 637, 175, 176, 468, 236, 237, 106, 107, 238, 124, 240, 126, 467, 360, 202, 438, 185, 440, 113, 242, 458, 226, 848, 849, 849.1, 79, 80, 199, 215, 461, 725, 726, 727, 633, 634, 635, 556, 183, 184, 58, 59, 602, 603, 604, 131, 852, 853, 690, 691, 194.1, 980, 580, 581, 976, 595, 596, 688, 689, 592, 593, 318, 319, 885, 886, 887, 393, 394, 395, 183, 184, 190, 424, 223, 224]
    
    def GetImplementedSpecialEvos():
        return [414, 413, 413.1, 413.2, 292, 122, 745, 745.1, 745.2, 678.1, 106, 107, 237, 124, 126, 202, 980, 424, 853, 185, 226, 849, 849.1]

    def GetPartySpecies():
        partyids = []
        for mon in playerparty:
            partyids.append(mon.GetId())
        return partyids

    def getGrade():
        grade = 0
        for key in gymbattles.keys():
            if (key[:3] == "Oak"):
                grade += 1
        return grade

    def IncreaseProficiency(type, amount):
        classstats[type] = round(classstats[type] + amount, 2)
        newtotal = FormatNum(classstats[type])
        levelcap = str(math.floor(classstats[type]))
        renpy.say(narrator, "Your {} proficiency increased to {}! Your {}-type Pokemon can now reach level {}.".format(type, newtotal, type, levelcap))

    def GetAverageProficiency():
        avgprof = 0
        for value in classstats.values():
            avgprof += value
        return round(avgprof / 18, 2)

    def GetNumItems(itemname):
        if (itemname in inventory.keys()):
            return inventory[itemname]
        return 0

    def GetRememberableMoves(partymon):
        moveslist = GetLevelMoves(partymon, partymon.GetLevel())
        justmoves = []
        for move in moveslist:
            if (move[1] not in partymon.GetMoveNames() and move[1] not in justmoves):
                justmoves.append(move[1])
        return justmoves

    def AddPikachu():
        if (pikachuobj not in playerparty):
            pikachuobj.Heal()
            AddMon(pikachuobj)

    def BattleTeamTraining():
        renpy.transition(dissolve)
        renpy.hide_screen("currentdate")
        for mon in playerparty:
            mon.GainExperience(pow(AimLevel(), 3) / 25 * (1 + max(0, (AimLevel() - mon.GetLevel()) / 10)))
        renpy.transition(dissolve)
        renpy.show_screen("currentdate")

    def AddMon(newmon, nickname = False):
        global hidebattleui
        global mustswitch
        playerparty.append(newmon)
        if (nickname):
            newmon.Nickname = renpy.input("Would you like to give it a nickname?", default=newmon.GetNickname(), exclude="{}[[]%<>", length=12)
            if (newmon.Nickname == "" or newmon.Nickname == pokedexlookup(newmon.GetId(), DexMacros.Name).lower()):
                newmon.Nickname = pokedexlookup(newmon.GetId(), DexMacros.Name)
        if (len(playerparty) > 6):
            hidebattleui = True
            mustswitch = True
            renpy.say(None, "Please pick a Pokémon to send to the PC. You can hover over the Pokémon in your party to view their stats.")
            sendtopc = renpy.call_screen("SendToPC")
            playerparty.remove(sendtopc)
            box.append(sendtopc)
            hidebattleui = False
            mustswitch = False

    def PlaySound(soundname, otherchannel="misc"):
        renpy.music.set_volume(0.25, delay=0.0, channel="music")
        renpy.sound.queue("Audio/" + soundname, channel=otherchannel)
        renpy.music.set_volume(1.0, delay=2.0, channel="music")

    def GetItem(itemname, count = 1, text = None, audio = True):
        if (audio):
            PlaySound("item_get.ogg")
        if ("Egg" in itemname and itemname != "Lucky Egg"):
            renpy.show("egg", [itemhover])
            renpy.pause(2.0)
            renpy.show("egg", [itemhide])
            renpy.pause(1.5)
            renpy.hide("egg")

        if (itemname in inventory.keys()):
            inventory[itemname] += count
        else:
            inventory[itemname] = count

        if (text != None):
            renpy.say(None, text)

    def LoseItem(itemname, count = 1):
        inventory[itemname] -= count

        if (inventory[itemname] <= 0):
            del inventory[itemname]

    def RemoveItem(pkmn):
        if (inbattle):
            renpy.invoke_in_new_context(renpy.say, None, "Please wait until the battle is over to unequip items.")
        else:
            GetItem(pkmn.Item, 1, audio = False)
            pkmn.Item = None

    def FormatNum(num):
        return str(round(num, 2)).replace(".00", "").replace(".0", "")

    def GetCharsInPlace(place):
        if (excusesecondelective or excusesecondhomeroom):
            return []
        additive = []
        subtractive = []
        if (place == "Garden" and not IsBefore(13, 4, 2004)):
            additive = ["Tia"]
        if (place == "Research Center" and not IsBefore(20, 4, 2004)):
            additive = ["Sonia"]
        if (place == "Academy" and not IsBefore(26, 4, 2004)):
            if (Random(True, "JasmineHangout" + timeOfDay) > 0.5 or IsDate(26, 4, 2004)):
                additive.append("Jasmine")
            if (Random(True, "GrushaHangout" + timeOfDay) > 0.5 or IsDate(26, 4, 2004)):
                additive.append("Grusha")
        if (place == "Academy" and not IsBefore(15, 4, 2004)):
            subtractive = ["Cheren"]
        if (place in availablechars.keys()):
            total = availablechars[place] + additive
            for char in subtractive:
                if (char in total):
                    total.remove(char)
            return total
        return [] + additive

    def GetCharsInTable(table):
        npcs = []
        if (table == "Angry Table"):
            npcs = ["Blue", "Flannery", "Misty", "Hilbert"]
        elif (table == "Cheerful Table"):
            npcs = (["Whitney", "Gardenia", "Bianca", "Leaf"] if IsBefore(13, 4, 2004) else ["Bianca", "Leaf", "Tia", "Whitney", "Gardenia"])
        elif (table == "Busy Table"):
            npcs = ["Nate", "Skyla", "Nessa", "Rosa"] 
            if (not IsBefore(20, 4, 2004)):
                npcs = ["Nate", "Skyla", "Nessa", "Sonia", "Rosa"] 
            if (IsDate(20, 4, 2004)):
                npcs = ["Nate", "Skyla", "Rosa"] 
        elif (table == "Romantic Table"):
            npcs = ["Serena", "Calem", "Brendan", "May"]
        elif (table == "Calm Table"):
            npcs = ["Sabrina", "Bea", "Hilda", "Cheren"]
            if (not IsBefore(15, 4, 2004)):
                npcs = ["Sabrina", "Bea", "Hilda"]
                if (not IsBefore(26, 4, 2004)):
                    npcs = ["Sabrina", "Bea", "Hilda", "Jasmine", "Grusha"]
                    if (Random(True, "Jasmine") <= 0.5):
                        npcs.remove("Jasmine")
                    if (Random(True, "Grusha") <= 0.5):
                        npcs.remove("Grusha")

                    if (IsDate(26, 4, 2004)):
                        npcs = ["Bea", "Hilda", "Jasmine", "Grusha"]
        elif (table == "Quiet Table"):
            npcs = ["Silver", "Erika", "Dawn", "Professor Cherry"]

        return npcs
    
    def GetCharValue(char):
        if ("Value" not in persondex[char].keys()):
            persondex[char]["Value"] = 0
        return persondex[char]["Value"]

    def getscenes(characters):
        scenes = []
        for character in characters:
            if (character == "Dawn"):
                scenes.append(DawnHasUnseenScene())
            elif (character == "Hilda"):
                scenes.append(HildaHasUnseenScene())
            elif (character == "Leaf"):
                scenes.append(LeafHasUnseenScene())
            elif (character == "Sabrina"):
                scenes.append(SabrinaHasUnseenScene())
            elif (character == "Serena"):
                scenes.append(SerenaHasUnseenScene())
            elif (character == "Rosa"):
                scenes.append(RosaHasUnseenScene())
            elif (character == "May"):
                scenes.append(MayHasUnseenScene())
            elif (character == "Nessa"):
                scenes.append(NessaHasUnseenScene())
            elif (character == "Silver"):
                scenes.append(SilverHasUnseenScene())
            elif (character == "Skyla"):
                scenes.append(SkylaHasUnseenScene())
            elif (character == "Misty"):
                scenes.append(MistyHasUnseenScene())
            elif (character == "Janine"):
                scenes.append(JanineHasUnseenScene())
            elif (character == "Bea"):
                scenes.append(BeaHasUnseenScene())
            elif (character == "Flannery"):
                scenes.append(FlanneryHasUnseenScene())
            elif (character == "Tia"):
                scenes.append(TiaHasUnseenScene())
            elif (character == "Blue"):
                scenes.append(BlueHasUnseenScene())
            elif (character == "Sonia"):
                scenes.append(SoniaHasUnseenScene())
            elif (character == "Whitney"):
                scenes.append(WhitneyHasUnseenScene())
            elif (character == "Professor Cherry"):
                scenes.append(KrisHasUnseenScene())
            elif (character == "Hilbert"):
                scenes.append(HilbertHasUnseenScene())
            elif (character == "Victini"):
                scenes.append(VictiniHasUnseenScene())
            else:
                scenes.append(False)

        for i in range(len(scenes)):
            scenes[i] = (characters[i], scenes[i])
        return scenes

    def GetRelationship(character):
        if "Relationship" in persondex[character].keys():
            return persondex[character]["Relationship"]
        else:
            return "Acquaintance"

    def GetEvents(character):
        if "Events" not in persondex[character].keys():
            persondex[character]["Events"] = []
        return persondex[character]["Events"]

    def AddEvent(character, event):
        if "Events" not in persondex[character].keys():
            persondex[character]["Events"] = []
        persondex[character]["Events"].append(event)

    def GetRelationshipRank(character):
        if "RelationshipRank" in persondex[character].keys():
            return persondex[character]["RelationshipRank"]
        else:
            return 0

    # leave static, altered by GetStudents
    altclassdex = {
        "Normal" : {"Bianca", "Whitney", "Cheren"},
        "Fire" : {"May", "Serena", "Flannery"},
        "Water" : {"Nessa", "Misty", "Skyla"},
        "Grass" : {"Brendan", "Leaf", "Gardenia"},
        "Electric" : {"Nate", "Leaf", "Rosa"},
        "Ice" : {"Hilbert", "Misty", "Dawn"},
        "Fighting" : {"Calem", "May", "Bea"},
        "Poison" : {"Hilda", "Silver", "Nate"},
        "Ground" : {"Brendan", "Serena", "Flannery"},
        "Flying" : {"Calem", "Skyla", "Blue"},
        "Psychic" : {"Bianca", "Sabrina", "Rosa"},
        "Bug" : {"Rosa", "Brendan", "May"},
        "Rock" : {"Nessa", "Bea", "Hilda"},
        "Ghost" : {"Sabrina", "Gardenia", "Hilbert"},
        "Dark" : {"Cheren", "Serena", "Silver"},
        "Dragon" : {"Dawn", "Leaf", "Blue"},
        "Steel" : {"Hilbert", "Hilda", "Nate"},
        "Fairy" : {"Dawn", "Whitney", "Calem"}
    }
    
    def GetStudents(type):
        return (altclassdex[type] 
        | ({"Erika"} if type in ["Grass", "Poison"] and (not IsBefore(11, 4, 2004)) else set()) 
        | ({"Tia"} if type in ["Dragon", "Psychic"] and ((calDate.day > 12 and timeOfDay == "Afternoon") or not IsBefore(14, 4, 2004)) else set())
        | ({"Sonia"} if type in ["Electric", "Fairy"] and ((calDate.day > 19 and timeOfDay == "Afternoon") or not IsBefore(20, 4, 2004)) else set())
        | ({"Jasmine"} if type in ["Steel", "Ground"] and (not IsBefore(27, 4, 2004) and (Random(True, "JasmineElective" + timeOfDay) > 0.5) or IsDate(26, 4, 2004) and timeOfDay == "Afternoon") else set())
        | ({"Grusha"} if type in ["Ice", "Flying"] and (not IsBefore(27, 4, 2004) and (Random(True, "GrushaElective" + timeOfDay) > 0.5) or IsDate(26, 4, 2004) and timeOfDay == "Afternoon") else set())
        - ({"Cheren"} if type in ["Dark", "Normal"] and (not IsBefore(15, 4, 2004)) else set()))

    def PartyHasType(element):
        for mon in playerparty:
            if mon.HasType(element):
                return True
        return False

    def PlayerHighestLevel():
        highestlevel = 0
        for mon in playerparty + box:
            if (mon.GetLevel() > highestlevel):
                highestlevel = mon.GetLevel()
        return highestlevel

    def MonCanLearn(mon, move):
        if (move in mon.GetMoveNames()):
            return False
        specialmoves = {
            "Simple World": ["Normal"],
            "Steady Flame": ["Fire"],
            "Healing Spring": ["Water"],
            "Bark Up": ["Grass"],
            "Energize": ["Electric"],
            "Slow Freeze": ["Ice"],
            "Disabling Poke": ["Fighting"],
            "Bad Breath": ["Poison"],
            "Burial Ground": ["Ground", "Ghost"],
            "Wing It": ["Flying"],
            "Clear Mind": ["Psychic"],
            "Chrysalize": ["Bug"],
            "Splinter Shield": ["Rock"],
            "Deathless": ["Ghost"],
            "Enshroud": ["Dark"],
            "Legacy": ["Dragon"],
            "Metallize": ["Steel"],
            "Ardent Gaze": ["Fairy"]
        }
        if (move in specialmoves.keys()):
            for element in specialmoves[move]:
                if (mon.HasType(element)):
                    return True
        return move in str(GetLearnset(mon.GetId()))

    def PartyCanLearn(move):
        count = 0
        for mon in playerparty:
            if (MonCanLearn(mon, move)):
                count += 1
        return count

    ##TESTING FEATURES##
    def MaxAll():
        for keyname in defaultpersondex.keys():
            persondex[keyname]["Value"] = 350
        for stat in personalstats.keys():
            personalstats[stat] = 100
        for stat in classstats.keys():
            classstats[stat] = 100
        for person in persondex.keys():
            persondex[person]["ClassesKnown"].append(2.1)

    def GetUnimplementedPokemon():
        unimplemented = []
        for mon in GetAllPokemonIn():
            found = False
            for entry in pokedex:
                if (entry[DexMacros.Id] == mon):
                    found = True
                    break
            if (not found):
                unimplemented.append(mon)
        return unimplemented

    def GetUnimplementedLearnsets():
        unimplemented = []
        for mon in GetAllPokemonIn():
            found = False
            for entry in learndex:
                if (entry[0] == mon):
                    found = True
                    break
            if (not found):
                unimplemented.append(mon)
        return unimplemented

    def GetEvolutions():
        for mon in GetAllPokemonIn():
            if (mon not in GetImplementedSpecialEvos()):
                evoconditions = pokedexlookup(mon, DexMacros.Evolve)
                if (evoconditions != None and len(evoconditions) != 6 or pokedexlookup(mon, DexMacros.Prevo) != None and pokedexlookup(mon, DexMacros.Prevo) != pokedexlookup(mon - 1, DexMacros.Name)):
                    print(pokedexlookup(mon, DexMacros.Name) + ": " + (evoconditions if evoconditions != None else "None"))

    def GetImplements(levels):
        finalmoves = set()
        for level in levels:
            for mon in GetAllPokemonIn():
                newmoves = GetLevelMoves(Pokemon(mon), level, True)
                for move in newmoves:
                    if (not MoveIsIn(move[1])):
                        finalmoves.add(move[1])

        finalabilities = set()
        for mon in GetAllPokemonIn():
            for ability in GetAbilities(mon):
                if (not AbilityIsIn(ability)):
                    finalabilities.add(ability)

        finalmovestring = ""
        for move in finalmoves:
            finalmovestring += move + ", "

        finalmovestring += "\n\n\nabilities after this\n\n\n"

        for ability in finalabilities:
            finalmovestring += ability + ", "

        print(finalmovestring)
        with open("Pokemon Academy Life Forever/Moves.txt","w") as egg:
            egg.write(finalmovestring)
        egg.closed

    def RankUpClasses():
        for classkey in classstats.keys():
            classstats[classkey] += 10
        for teacher in classtaught.keys():
            persondex[teacher]["ClassesKnown"].append(1)
    ##END TESTING FEATURES##

    def IsBefore(day, month, year):
        return (calDate.year < year 
            or calDate.month < month and calDate.year == calDate.year
            or calDate.day < day and calDate.month == month and calDate.year == calDate.year)

    def IsDate(day = None, month = None, year = None):
        return (day == None or day == calDate.day) and (month == None or month == calDate.month) and (year == None or year == calDate.year)

    def GetSocialPoints():
        value = 0
        for keyname in persondex.keys():
            value += persondex[keyname]["Value"]
        return value

    def InventoryCategory(item):
        categories = { 
            "Healing": ["Potion", "Super Potion", "Hyper Potion", "Revive", "Max Revive", "Max Potion", "Full Restore", "Antidote", "Paralyze Heal", "Ice Heal", "Awakening", "Full Heal", "Oran Berry", "Sitrus Berry"],
            "Evo Items": ["Washing Mchn", "Fan", "Microwave", "Refrigerator", "Lawnmower"],
            "Poké Balls": ["Poké Ball", "Great Ball", "Ultra Ball", "Premier Ball", "Master Ball"],
            "Battle Items": ["Silk Scarf", "Charcoal", "Mystic Water", "Miracle Seed", "Magnet", "Never-Melt Ice", "Black Belt", "Poison Barb", "Soft Sand", "Sharp Beak", "Twisted Spoon", "Silver Powder", "Hard Stone", "Spell Tag", "Black Glasses", "Dragon Fang", "Metal Coat", "Pink Bow"]
        }
        for key in categories.keys():
            if item in categories[key]:
                return key
        return "Misc."

    def GiveItem(partymon):
        global activemon
        global invoverwrite
        activemon = partymon
        monnickname = partymon.GetNickname()
        olditem = partymon.GetItem()
        if (olditem == None):
            LoseItem(activeitem)
            partymon.GiveItem(activeitem)
            invoverwrite = "{} was given the {}.".format(monnickname, activeitem)
        else:
            invoverwrite = "{} is already holding the {}. Swap it for the {}?".format(monnickname, olditem, activeitem)

    def SwapItems():
        global invoverwrite
        olditem = activemon.GetItem()
        GetItem(olditem)
        LoseItem(activeitem)
        activemon.TakeItem()
        activemon.GiveItem(activeitem)
        invoverwrite = "{} was given the {}, and you put the {} in your bag.".format(activemon.GetNickname(), activeitem, olditem)

    def ItemSuccess(partymon):
        global invoverwrite
        if (activeitem not in ["Microwave", "Fan", "Lawnmower", "Washing Mchn", "Refrigerator"]):
            LoseItem(activeitem)
        invoverwrite = "You used the {} on {}.".format(activeitem, partymon.GetNickname())
        return True

    def ItemFailure(partymon):
        global invoverwrite
        invoverwrite = "The {} would have no effect on {}.".format(activeitem, partymon.GetNickname())
        return False

    def TrainerItemSuccess():
        global invoverwrite
        LoseItem(activeitem)
        invoverwrite = "You used the {}.".format(activeitem)
        if (activeitem == "Escape Rope"):
            renpy.jump("freeroam")
        else:
            return True

    def TrainerItemFailure():
        global invoverwrite
        invoverwrite = "The {} would have no effect.".format(activeitem)
        return False

    def UseItem(partymon, checksuccess = False, inbattle = False, forceuse = False, autotrigger = False):
        global activerepel
        global repelstepsleft
        global Fled
        success = False

        if (inbattle and partymon.HasAbility("Klutz", not checksuccess)):
            return False

        #menu-usable items
        if (activeitem == "Potion"):
            if (partymon.GetHealthPercentage() < 1):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(20)
                success = True
        elif (activeitem == "Super Potion"):
            if (partymon.GetHealthPercentage() < 1):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(60)
                success = True
        elif (activeitem == "Hyper Potion"):
            if (partymon.GetHealthPercentage() < 1):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(120)
                success = True
        elif (activeitem == "Max Potion"):
            if (partymon.GetHealthPercentage() < 1):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(999)
                success = True
        elif (activeitem == "Full Restore"):
            if (partymon.GetHealthPercentage() < 1 or partymon.HasNormalStatus() or partymon.HasStatus("confused")):
                if (checksuccess):
                    return True
                partymon.ClearStatus("all", nonvolatilesandconfusion=True)
                partymon.AdjustHealth(999)
                success = True
        elif (activeitem == "Antidote"):
            if (partymon.HasStatus("poisoned") or partymon.HasStatus("badly poisoned")):
                if (checksuccess):
                    return True
                partymon.ClearStatus("poisoned")
                partymon.ClearStatus("badly poisoned")
                success = True
        elif (activeitem == "Burn Heal"):
            if (partymon.HasStatus("burned")):
                if (checksuccess):
                    return True
                partymon.ClearStatus("burned")
                success = True
        elif (activeitem == "Ice Heal"):
            if (partymon.HasStatus("frozen") or partymon.HasStatus("frostbitten")):
                if (checksuccess):
                    return True
                partymon.ClearStatus("frozen")
                partymon.ClearStatus("frostbitten")
                success = True
        elif (activeitem == "Awakening"):
            if (partymon.HasStatus("asleep")):
                if (checksuccess):
                    return True
                partymon.ClearStatus("asleep")
                success = True
        elif (activeitem == "Paralyze Heal"):
            if (partymon.HasStatus("paralyzed")):
                if (checksuccess):
                    return True
                partymon.ClearStatus("paralyzed")
                success = True
        elif (activeitem == "Full Heal"):
            if (partymon.HasNormalStatus() or partymon.HasStatus("confused")):
                if (checksuccess):
                    return True
                partymon.ClearStatus("all", nonvolatilesandconfusion=True)
                success = True
        elif (activeitem == "Revive"):
            if (partymon.GetHealthPercentage() <= 0.0):
                if (checksuccess):
                    return True
                if (partymon in FaintedMons):
                    FaintedMons.remove(partymon)
                partymon.AdjustHealth(partymon.GetStat(Stats.Health) / 2.0)
                success = True
        elif (activeitem == "Max Revive"):
            if (partymon.GetHealthPercentage() <= 0.0):
                if (checksuccess):
                    return True
                if (partymon in FaintedMons):
                    FaintedMons.remove(partymon)
                partymon.AdjustHealth(partymon.GetStat(Stats.Health))
                success = True
        elif (activeitem in ["Microwave", "Washing Mchn", "Refrigerator", "Fan", "Lawnmower"]):
            if (math.floor(partymon.GetId()) == 479):
                if (checksuccess):
                    return True
                newid = "Rotom (Rotom)"
                if (activeitem == "Microwave"):
                    newid = "Rotom (Heat Rotom)"
                elif (activeitem == "Washing Mchn"):
                    newid = "Rotom (Wash Rotom)"
                elif (activeitem == "Refrigerator"):
                    newid = "Rotom (Frost Rotom)"
                elif (activeitem == "Fan"):
                    newid = "Rotom (Fan Rotom)"
                elif (activeitem == "Lawnmower"):
                    newid = "Rotom (Mow Rotom)"
                if (newid == pokedexlookup(partymon.GetId(), DexMacros.Forme)):
                    newid = "Rotom (Rotom)"
                renpy.invoke_in_new_context(partymon.ChangeForme, newid)
                success = True

        #items without targets
        elif (activeitem in ["Repel", "Super Repel", "Max Repel"]):
            if (activerepel == None):
                if (checksuccess):
                    return True
                activerepel = activeitem
                repelstepsleft = 20
                success = True
        elif (activeitem == "Escape Rope"):
            if (freeroaming):
                if (checksuccess):
                    return True
                success = True
        elif (activeitem == "Poké Doll"):
            if (inbattle and WildBattle and not Unrunnable):
                if (checksuccess):
                    return True
                Fled = True

        #items with battle triggers
        elif (activeitem == "Oran Berry"):
            if (partymon.GetHealthPercentage() < 1.0 and (not autotrigger or partymon.GetHealthPercentage() <= 0.5) and not AbilityOnOpponentField(partymon, "Unnerve") or forceuse):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(10)
                success = True
        elif (activeitem == "Sitrus Berry"):
            if (partymon.GetHealthPercentage() < 1.0 and (not autotrigger or partymon.GetHealthPercentage() <= 0.5) and not AbilityOnOpponentField(partymon, "Unnerve") or forceuse):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(partymon.GetStat(Stats.Health) / 4.0)
                success = True
        elif (activeitem == "Pecha Berry"):
            if (partymon.HasStatus("poisoned") or partymon.HasStatus("badly poisoned") and not AbilityOnOpponentField(partymon, "Unnerve") or forceuse):
                if (checksuccess):
                    return True
                partymon.ClearStatus("poisoned")
                success = True

        #battle items
        elif (activeitem == "Sticky Barb"):
            if (checksuccess):
                return True
            if (inbattle and not autotrigger):
                partymon.AdjustHealth(partymon.GetStat(Stats.Health) / -4.0)
                success = True

        if (checksuccess):
            return False
        if (not inbattle):
            if (not TrainerItem(activeitem)):
                if (success):
                    ItemSuccess(partymon)
                else:
                    ItemFailure(partymon)
            else:
                if (success):
                    TrainerItemSuccess()
                else:
                    TrainerItemFailure()
        elif (success):
            if (autotrigger):
                partymon.MarkItemUsed()
            return True

        return False

    def TrainerItem(item):
        return item in ["Repel", "Super Repel", "Max Repel", "Escape Rope", "Poké Doll"]

    def AimLevel():
        index = (calDate - datetime.datetime(2004, 4, 5)).days
        levels = [5, 5, 5, 5, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 50, 50, 50, 50, 50, 51, 51, 51, 51, 51, 52, 52, 52, 52, 52, 53, 53, 53, 53, 53, 54, 54, 54, 54, 54, 55, 55, 55, 55, 55, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 58, 58, 58, 58, 58, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 70, 70, 70, 70, 70, 71, 71, 71, 71, 71, 72, 72, 72, 72, 72, 73, 73, 73, 73, 73, 74, 74, 74, 74, 74, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 78, 78, 78, 78, 78, 79, 79, 79, 79, 79, 80, 80, 80, 80, 80, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 83, 83, 83, 83, 83, 84, 84, 84, 84, 84, 85, 85, 85, 85, 85]
        return levels[index]

    def GetItemCount(item):
        for otheritem, amount in inventory.items():
            if (item == otheritem):
                return amount
        return 0
        
default first_name = "You"
default last_name = "Satoshi"
default pika_name = "Your Pikachu"
default blue_name = "Blue"

define oak = CustomCharacter("Professor Oak", "#000000", "oak")
define pikachu = CustomCharacter("Pikachu", "#fca600", "pikachu")
define starter = CustomCharacter("Your Starter", "#fca600", "starterportrait")
define red = CustomCharacter("Red", "#cf0000", "red")
define redmind = CustomCharacter("You", "#cf0000", "red")
define mom = CustomCharacter("Mom", "#b7669e", "mom")

#students
define blue = CustomCharacter("Blue", "#3110dd", "blue")
define silver = CustomCharacter("Silver", "#686080", "silver")
define face = CustomCharacter("Ace Student F", "#C89BE3", "face")
define mace = CustomCharacter("Ace Student M", "#665787", "mace")
define leaf = CustomCharacter("Leaf", "#00b23f", "leaf")
define ethan = CustomCharacter("Ethan", "#c1861e", "ethan")
define ethanmind = CustomCharacter("You", "#c1861e", "ethan")
define calem = CustomCharacter("Calem", "#4d7ac4", "calem")
define hilbert = CustomCharacter("Hilbert", "#353535", "hilbert")
define brendan = CustomCharacter("Brendan", "#db4039", "brendan")
define may = CustomCharacter("May", "#493bff", "may")
define flannery = CustomCharacter("Flannery", "#d62e0d", "flannery")
define whitney = CustomCharacter("Whitney", "#e47282", "whitney")
define sabrina = CustomCharacter("Sabrina", "#600080", "sabrina")
define serena = CustomCharacter("Serena", "#cb6e8b", "serena")
define cheren = CustomCharacter("Cheren", "#1f67df", "cheren")
define misty = CustomCharacter("Misty", "#eb6400", "misty")
define bianca = CustomCharacter("Bianca", "#55b13c", "bianca")
define dawn = CustomCharacter("Dawn", "#cc8fdb", "dawn")
define nate = CustomCharacter("Nate", "#36A8CB", "nate")
define rosa = CustomCharacter("Rosa", "#ff5a73", "rosa")
define bea = CustomCharacter("Bea", "#F87816", "bea")
define nessa = CustomCharacter("Nessa", "#5B81D9", "nessa")
define hilda = CustomCharacter("Hilda", "#ea5091", "hilda")
define gardenia = CustomCharacter("Gardenia", "#00712b", "gardenia")
define skyla = CustomCharacter("Skyla", "#5c87b9", "skyla")
define erika = CustomCharacter("Erika", "#34a59a", "erika")
define tia = CustomCharacter("Tia", "#C96A70", "tia")
define sonia = CustomCharacter("Sonia", "#F19272", "sonia")
define jasmine = CustomCharacter("Jasmine", "#939393", "jasmine")
define grusha = CustomCharacter("Grusha", "#00b8d0", "grusha")
define victini = CustomCharacter("Victini", "#f57c51", "victini")

#Not technically students
define brawly = CustomCharacter("Brawly", "#467595", "brawly")
define roxanne = CustomCharacter("Roxanne", "#a2254b", "roxanne")
define falkner = CustomCharacter("Falkner", "#1d8fc5", "falkner")
define brock = CustomCharacter("Brock", "#6D211D", "brock")
define janine = CustomCharacter("Janine", "#6f4097", "janine")
define iris = CustomCharacter("Iris", "#82007e", "iris")

#type instructors
define lenora = CustomCharacter("Instructor Lenora", "#aa4a1b", "lenora")
define blaine = CustomCharacter("Instructor Blaine", "#cd5733", "blaine")
define wallace = CustomCharacter("Instructor Wallace", "#46897c", "wallace")
define ramos = CustomCharacter("Instructor Ramos", "#657f61", "ramos")
define surge = CustomCharacter("Lieutenant Surge", "#545241", "surge")
define melony  = CustomCharacter("Instructor Melony", "#288cff", "melony")
define marshal = CustomCharacter("Sensei Marshal", "#6e492d", "marshal")
define koga = CustomCharacter("Instructor Koga", "#5f3869", "koga")
define bertha = CustomCharacter("Instructor Bertha", "#906438", "bertha")
define winona = CustomCharacter("Instructor Winona", "#52adbe", "winona")
define will = CustomCharacter("Instructor Will", "#664f79", "will")
define burgh = CustomCharacter("Instructor Burgh", "#71a230", "burgh")
define olivia = CustomCharacter("Instructor Olivia", "#595554", "olivia")
define fantina = CustomCharacter("Instructrice Fantina", "#784972", "fantina")
define karen = CustomCharacter("Instructor Karen", "#314876", "karen")
define clair = CustomCharacter("Instructor Clair", "#5a94c6", "clair")
define byron = CustomCharacter("Instructor Byron", "#4a4a5b", "byron")
define valerie = CustomCharacter("Instructor Valerie", "#de5b99", "valerie")

#other staff
define bruno = CustomCharacter("Bruno", "#585355", "bruno")
define alder = CustomCharacter("Alder", "#af4c2e", "alder")
define lance = CustomCharacter("Lance", "#16367a", "lance")
define kris = CustomCharacter("Professor Cherry", "#1dcc88", "kris")
define drayden = CustomCharacter("Dean Drayden", "#583C68", "drayden")

#others...?
define narrator = CustomCharacter("", "#000", "")
define security = CustomCharacter("Security", "#ff4400", "")
define roughneck = CustomCharacter("Roughneck", "#ff4400", "roughneck")
define roughneck2 = CustomCharacter("Toughneck", "#ff4400", "roughneck2")
define roughneck3 = CustomCharacter("Buffneck", "#ff4400", "roughneck3")
define sidemon = CustomCharacter("Sidemon", "#000", "sidemonportrait")

define charlist = [oak, pikachu, starter, red, mom, blue, silver, brawly, roxanne, 
    face, mace, falkner, leaf, ethan, calem, hilbert, brendan, may, flannery,
    whitney, sabrina, serena, cheren, misty, bianca, dawn, nate, rosa, bea,
    nessa, hilda, gardenia, skyla, brock, erika, janine, tia, sonia, iris,
    jasmine, grusha,

    lenora, blaine, wallace, ramos, surge, melony, marshal, koga, bertha, 
    winona, will, burgh, olivia, fantina, karen, clair, byron, valerie,

    bruno, alder, lance, kris, drayden,
    victini,
    narrator, security, roughneck, roughneck2, roughneck3, sidemon]

# change with new characters
define classdex = {
    "Bianca" : { "Normal", "Psychic"},
    "Cheren" : { "Normal", "Dark"},
    "May" : { "Fire", "Fighting", "Bug"},
    "Whitney" : { "Normal", "Fairy"},
    "Hilbert" : { "Ice", "Steel", "Ghost"},
    "Hilda" : { "Poison", "Steel", "Rock"},
    "Calem" : { "Fighting", "Flying", "Fairy"},
    "Sabrina" : { "Psychic", "Ghost"},
    "Nessa" : { "Water", "Rock"},
    "Dawn" : { "Ice", "Dragon", "Fairy"},
    "Nate" : { "Electric", "Steel", "Poison"},
    "Rosa" : { "Electric", "Psychic", "Bug"},
    "Silver" : { "Poison", "Dark"},
    "Brendan" : { "Grass", "Ground", "Bug"},
    "Flannery" : { "Fire", "Ground"},
    "Serena" : { "Dark", "Fire", "Ground"},
    "Skyla" : { "Water", "Flying",},
    "Leaf" : { "Grass", "Electric", "Dragon"},
    "Misty" : { "Water", "Ice"},
    "Bea" : { "Fighting", "Rock"},
    "Blue" : { "Flying", "Dragon"},
    "Gardenia" : { "Grass", "Ghost"},
    "Erika" : { "Grass", "Poison" },
    "Tia" : { "Dragon", "Psychic" },
    "Sonia" : { "Electric", "Fairy" },
    "Jasmine" : { "Steel", "Ground" },
    "Grusha" : { "Ice", "Flying" }
}

define classtaught = {
    "Instructor Lenora" : "Normal",
    "Instructor Blaine" : "Fire",
    "Instructor Wallace" : "Water",
    "Instructor Ramos" : "Grass",
    "Lieutenant Surge" : "Electric",
    "Instructor Melony" : "Ice",
    "Sensei Marshal" : "Fighting",
    "Instructor Koga" : "Poison",
    "Instructor Bertha" : "Ground",
    "Instructor Will" : "Psychic",
    "Instructor Burgh" : "Bug",
    "Instructor Olivia" : "Rock",
    "Instructrice Fantina" : "Ghost",
    "Instructor Karen" : "Dark",
    "Instructor Clair" : "Dragon",
    "Instructor Byron" : "Steel",
    "Instructor Valerie" : "Fairy",
    "Instructor Winona" : "Flying"
}

define starters = {
    "Normal":[506,206,531],
    "Fire":[4,554,631],
    "Water":[258,194,746],
    "Grass":[387,548,556],
    "Electric":[179,170,479],
    "Ice":[363,361,615],
    "Fighting":[532,447,214],
    "Poison":[41,747,336],
    "Ground":[328,529,618],
    "Flying":[396,198,357],
    "Psychic":[280,79,561],
    "Bug":[540,290,213],
    "Rock":[246,566,774],
    "Ghost":[607,200,778],
    "Dragon":[371,696,780],
    "Steel":[304,597,227],
    "Fairy":[669,742,303],
    "Dark":[551,215,302]
}

define availablechars = {
    "Battle Hall" : ["Blue", "Janine"],
    "Academy" : ["Sabrina", "Cheren", "Dawn"],
    "Recreation Center" : ["Misty", "Nessa", "Bea"],
    "Aura Hall" : ["Leaf", "May", "Hilda", "Serena"],
    "Research Center" : ["Nate", "Bianca"],
    "Garden" : ["Erika", "Professor Cherry"],
    "Relic Hall" : ["Ethan", "Brendan", "Calem", "Hilbert"],
    "Student Center" : ["Rosa", "Skyla"],
    "Baseball Field" : ["Flannery", "Whitney", "Gardenia"],
    "Pledge Hall" : ["Silver"]
}

define sceneconditions = {
    "Leaf": {"Friend" : "Lv. 2"},
    "Dawn": {"Classmate" : "Lv. 2"},
    "Serena": {"Friend" : "Lv. 2"},   
    "Sabrina": {"Classmate" : "Lv. 2"},
    "Hilda" : {"Friend" : "Lv. 2"},
    "Rosa" : {"Friend" : "Lv. 2, Knowledge: 4"},
    "May" : {"Friend" : "Lv. 2"},
    "Silver" : {"Classmate" : "Lv. 2, Courage: 5"},
    "Nessa" : {"Date" : "Lv. 2, Wit: 2"},
    "Skyla" : {"Friend" : "Lv. 2, Patience: 4"},
    "Misty" : {"Classmate" : "Lv. 2, Courage: 7"},
    "Janine" : {"Tool" : "Lv. 2, Patience: 7"},
    "Bea" : {"Training Partner" : "Lv. 2"},
    "Flannery" : {"Friend" : "Lv. 2, Charm: 6, Evening"},
    "Tia" : {"Protector" : "Lv. 2"},
    "Blue" : {"Rival" : "Lv. 2, Charm: 6"},
    "Sonia" : {"Classmate" : "Lv. 2, Rank 2 w/Nessa"},
    "Whitney" : {"Friend" : "Lv. 2, Charm: 7"},
    "Professor Cherry" : {"Student" : "Lv. 2"},
    "Hilbert" : {"Dormmate" : "Lv. 2, Knowledge: 4"}
}

init python:
    def GetGiftValue(character, item):
        if (item == "Premier Ball"):
            return 7
        
        if (character in classdex.keys()):
            for shopitem in shopitems.values():
                if (item == shopitem[1]):
                    if (shopitem[0] < 500):
                        return 2
                    elif (shopitem[0] < 800):
                        return 3
                    elif (shopitem[0] < 1001):
                        return 4
                    else:
                        return 5
            
            if item in elementitems.keys():
                for element in elementitems[item]:
                    if element in classdex[character]:
                        return 5

                return 3
        elif (character == "Janine"):
            if (item in ["Poison Barb", "Black Belt", "Ultra Ball", "Full Restore", "Max Repel", "Max Revive"]):
                return 5
        elif (character == "Professor Cherry"):
            if (item in ["Washing Mchn", "Lawnmower", "Fan", "Microwave", "Refrigerator"]):
                return 10
            elif (item in elementitems.keys()):
                return 5
        elif (character == "Ethan"):
            return 5

        return 1

    def GetShopItems():
        items = []
        for investmentcost, item in shopitems.items():
            if (gains >= investmentcost):
                itemname = item[1]
                if (not (itemname in ["Fan", "Microwave", "Lawnmower", "Refrigerator", "Washing Mchn"] and GetNumItems(itemname) > 0)):
                    #("Poké Ball", 200, "Used for catching Pokémon. Decent, at best.")
                    items.append((itemname, item[0], item[2]))
        return items

    def GetItemSellValue(item):
        returnvalue = 100
        for shopitem in shopitems.values():
            if (item == shopitem[1]):
                returnvalue = shopitem[0] / 2.0
                break
        if (item in elementitems.keys()):
            returnvalue = 500
        return math.floor(returnvalue)

define shopitems = {
    0: (200, "Poké Ball", "Used for catching Pokémon. Decent, at best."),
    200: (200, "Potion", "Restores 20 HP to a Pokémon. Scientifically proven to be less useful than water."),
    400: (200, "Antidote", "Purges poison from a Pokémon. May cause violent expulsion of toxins."),
    600: (200, "Burn Heal", "Liquidized aloe. Soothes burns and smells like cucumbers."),
    800: (200, "Ice Heal", "Cures frostbitten and frozen Pokémon. It's literally just warm water."),
    1000: (200, "Awakening", "Wakes up Pokémon. It's an air horn."),
    1200: (200, "Paralyze Heal", "Cures full-body paralysis in most Pokémon. Contains tiny rubber molecules that ground the charge."),
    1500: (300, "Poké Doll", "Guarantees escape from wild Pokémon. A grown man carrying it around will get weird looks."),
    1900: (400, "Full Heal", "A panacea of incredible proportions. Makes all prior medicines purposeless."),
    2000: (5000, "Lawnmower", "Used to mow lawns. This one's motor is broken, so it's on sale."),
    2400: (500, "Repel", "Repels weaker Pokémon, so only the Pokémon in the top half of the level range of an area appear. Guarantees escape."),
    3000: (600, "Great Ball", "Designed for capturing Pokémon. Decent enough, though suffers from middle-child syndrome."),
    3700: (700, "Super Potion", "Restores 60 HP to a Pokémon. Slightly less effective than a glass of lemonade."),
    4000: (5000, "Fan", "Keeps rooms cool. This one's motor is broken, so it's on sale."),
    4450: (750, "Super Repel", "Repels most Pokémon, so only the maximum-level Pokémon in an area will appear. Guarantees escape."),
    5250: (800, "Ultra Ball", "An excellent Poké Ball, at a premium price. The Poké Ball of Champions."),
    6000: (5000, "Refrigerator", "Keeps food cold. This one's motor is broken, so it's on sale."),
    6750: (1500, "Hyper Potion", "Restores 120 HP to a Pokémon. Knits wounds, heals bruises, and also acts as a powerful degreaser."),
    8000: (5000, "Microwave", "Heats up food. This one's motor is broken, so it's on sale."),
    8250: (1500, "Max Repel", "Repels all but the strongest Pokémon. The only Pokémon that appear in the wild will be around your level. Guarantees escape."),
    10000: (5000, "Washing Mchn", "Keeps clothes clean. This one's motor is broken, so it's on sale."),
    10250: (2000, "Revive", "Restores a fainted Pokémon to half health. Useless in Nuzlockes."),
    12750: (2500, "Max Potion", "Restores a Pokémon to full health. The chemicals here are banned in five regions."),
    15750: (3000, "Full Restore", "Restores a Pokémon to full health and purifies most status conditions. Every Champion carries five."),
    20750: (5000, "Max Revive", "Restores a fainted Pokémon to full health. Absolutely useless in Nuzlockes."),
    25750: (5000, "Escape Rope", "Brings you from any wild area back to campus immediately.")
}

define elementitems = {
    "Silk Scarf": "Normal",
    "Charcoal": "Fire",
    "Mystic Water": "Water",
    "Miracle Seed": "Grass",
    "Magnet": "Electric",
    "Never-Melt Ice": "Ice",
    "Black Belt": "Fighting",
    "Poison Barb": "Poison",
    "Soft Sand": "Ground",
    "Sharp Beak": "Flying",
    "Twisted Spoon": "Psychic",
    "Silver Powder": "Bug",
    "Hard Stone": "Rock",
    "Spell Tag": "Psychic",
    "Black Glasses": "Dark",
    "Dragon Fang": "Dragon",
    "Metal Coat": "Steel",
    "Pink Bow": "Fairy"
}

define nonvolatiles = ["burned", "frozen", "paralyzed", "poisoned", "badly poisoned", "asleep", "busted disguise", "frenzied"]
define normalstatuses = ["burned", "frozen", "paralyzed", "poisoned", "badly poisoned", "asleep"]
define bluecolor = "{color=#0048ff}"
define sabrinacolor = "{color=#600080}"
define movesin = ['Defense Curl', 'Tackle', 'Echoed Voice', 'Trick', 'Play Nice', 'Thunder Shock', 'Tail Whip', 'Play Rough', 'Copycat', 'Mega Drain', 'Bullet Seed', 'Constrict', 'Rage', 'Confusion', 'Poison Sting', 'Sharpen', 'Sandstorm', 'Absorb', 'Fake Tears', 'Wing Attack', 'Last Resort', 'Pound', 'Spite', 'Double Team', 'Minimize', 'Pursuit', 'Sticky Web', 'Wrap', 'String Shot', 'Mud Sport', 'Sand Attack', 'Razor Leaf', 'Vine Whip', 'Iron Head', 'Growth', 'Splash', 'Leaf Storm', 'Bubble', 'Supersonic', 'Peck', 'Swagger', 'Misty Terrain', 'Flail', 'Charge', 'Covet', 'Mud-Slap', 'Rock Throw', 'Sheer Cold', 'Bind', 'Taunt', 'Quick Attack', 'Harden', 'Discharge', 'Growl', 'Helping Hand', 'Hyper Voice', 'Scratch', 'Rollout', 'Icy Wind', 'Wood Hammer', 'Fairy Wind', 'Encore', 'Feint Attack', 'Astonish', 'Switcheroo', 'Fissure', 'Ember', 'Gust', 'Smog', 'Water Gun', 'Bide', 'Foresight', 'Rapid Spin', 'Bite', 'Focus Energy', 'Confuse Ray', 'Baby-Doll Eyes', 'Leer', 'Ice Shard', 'Twister', 'Miracle Eye', 'Arm Thrust', 'Incinerate', 'Psywave', 'Headbutt', 'Horn Attack', 'Powder Snow', 'Night Slash', 'Hone Claws', 'Odor Sleuth', 'Withdraw', 'Endure', 'Thunder Wave', 'Hypnosis', 'Lick', 'Poison Powder', 'Vise Grip', 'Dragon Rage', 'Draco Meteor', 'Poison Gas', 'Whirlwind', 'Roar', 'Disable', 'Vacuum Wave', 'Stun Spore', 'Counter', 'Sweet Scent', 'Night Shade', 'Seismic Toss', 'Feint', 'Fire Spin', 'Leech Seed', 'Uproar', 'Bulldoze', 'Bug Bite', 'Refresh', 'Mud Shot', 'Electro Ball', 'Mist', 'Haze', 'Poison Tail', 'Teleport', 'Protect', 'Curse', 'Metal Claw', 'Smokescreen', 'Spore', 'Sleep Powder', 'Aerial Ace', 'Stomp', 'Screech', 'Torment', 'Lucky Chant', 'Struggle Bug', 'Acid', 'Rock Smash', 'Disarming Voice', 'Leafage', 'Yawn', 'Wide Guard', 'Rest', 'Facade', 'Detect', 'Agility', 'Shadow Sneak', 'Heal Pulse', 'Light Screen', 'Reflect', 'Toxic Spikes', 'Trick-or-Treat', 'Pluck', 'Swift', 'Nuzzle', 'Flame Burst', 'Camouflage', 'Chip Away', 'Gyro Ball', 'Pin Missile', 'Magical Leaf', 'Metal Sound', 'Take Down', 'Wake-Up Slap', 'Natural Gift', 'Worry Seed', 'Ancient Power', 'Tailwind', 'Synthesis', 'Sweet Kiss', 'Fire Fang', 'Poison Fang', 'Ice Fang', 'Thunder Fang', 'Safeguard', 'Stealth Rock', 'Sand Tomb', 'Endeavor', 'Scary Face', 'Iron Defense', 'Acid Armor', 'Sing', 'Force Palm', 'Hidden Power', 'Double Slap', 'Aqua Ring', 'Assurance', 'Flame Wheel', 'Dig', 'Work Up', 'Venoshock', 'Low Kick', 'Psybeam', 'Cotton Spore', 'Slam', 'Brine', 'Glare', 'Wish', 'Grass Whistle', 'Meditate', 'Mimic', 'Slash', 'Drill Run', 'Fury Swipes', 'Fake Out', 'Attract', 'Ice Ball', 'Payback', 'Round', 'Mud Bomb', 'Draining Kiss', 'Body Slam', 'Hyper Fang', 'Smack Down', 'Water Sport', 'Ingrain', 'Silver Wind', 'Bubble Beam', 'Mean Look', 'Block', 'Fury Attack', 'Water Shuriken', 'Air Cutter', 'Charm', 'Rock Tomb', 'Spark', 'Aurora Beam', 'Will-O-Wisp', 'Breaking Swipe', 'Flower Shield', 'Double Kick', 'Toxic', 'Dragon Breath', 'Rock Slide', 'Milk Drink', 'Recover', 'Mach Punch', 'Chrysalize', 'Enshroud', 'Legacy', 'Energize', 'Ardent Gaze', 'Disabling Poke', 'Rain Dance', 'Steady Flame', 'Wing It', 'Deathless', 'Bark Up', 'Burial Ground', 'Slow Freeze', 'Simple World', 'Bad Breath', 'Clear Mind', 'Splinter Shield', 'Metallize', 'Lightning Rod', 'Magnitude', 'Acid Spray', 'Acupressure', 'Howl', 'Spikes', 'Bone Rush', 'Bonemerang', 'First Impression', 'Hex', 'Bone Club', 'Tearful Look', 'Brave Bird', 'Boomburst', 'Shock Wave', 'Ice Punch', 'Double-Edge', 'Freeze-Dry', 'Dragon Pulse', 'Air Slash', 'Grass Knot', 'Dragon Claw', 'Explosion', 'Power-Up Punch', 'Pain Split', 'Power Whip', 'Power Trip', 'Electrify', 'Dragon Tail', 'Tickle', 'Zap Cannon', 'Heat Wave', 'Poison Jab', 'Fury Cutter', 'Petal Blizzard', 'Quick Guard', 'Fly', 'Power Swap', 'Flatter', 'Embargo', 'Megahorn', 'Rock Climb', 'Magnet Bomb', 'Stored Power', 'Superpower', 'Rototiller', 'Magnetic Flux', 'Barrier', 'Weather Ball', 'Head Smash', 'Brick Break', 'Recycle', 'Healing Wish', 'Flare Blitz', 'Nasty Plot', 'Laser Focus', 'Mirror Move', 'Calm Mind', 'False Swipe', 'Teeter Dance', 'Accelerock', 'Future Sight', 'Eerie Impulse', 'Aura Sphere', 'Hail', 'Sunny Day', 'Silk Trap', 'Destiny Bond', 'Baneful Bunker', 'Sky Attack', 'Dragon Dance', 'Tri Attack', 'Sonic Boom', 'Crunch', 'Quiver Dance', 'Thunder Punch', 'Earthquake', 'Magnet Rise', 'Morning Sun', 'Moonlight', 'Moonblast', 'Roost', 'Perish Song', 'Swords Dance', 'Sucker Punch', 'Petal Dance', 'Fire Punch', 'Water Spout', 'Eruption', 'Electric Terrain', 'Sludge', 'Bulk Up', 'Grassy Terrain', 'Shift Gear', 'Pollen Puff', 'Phantom Force', 'Hammer Arm', 'Mirror Shot', 'Swallow', 'Ion Deluge', 'Spit Up', 'Aromatherapy', 'Water Pulse', 'Close Combat', 'Cross Poison', 'Venom Drench', 'Knock Off', 'Mirror Coat', 'Power Gem', 'Giga Drain', 'Amnesia', 'Mystical Fire', 'Guard Swap', 'Self-Destruct', 'Aqua Jet', 'Lunge', 'Shadow Claw', 'Ominous Wind', 'Zen Headbutt', 'Horn Drill', 'Guillotine', 'Stockpile', 'Rock Wrecker', 'Hyper Beam', 'Giga Impact', 'Blast Burn', 'Hydro Cannon', 'Frenzy Plant', 'Roar of Time', 'Bounce', 'Frustration', 'Return', 'Magic Coat', 'Dizzy Punch', 'Sludge Bomb', 'Me First', 'Rage Powder', 'Synchronoise', 'Triple Kick', 'Power Trick', 'Memento', 'Substitute', 'Leaf Tornado', 'Mind Reader', 'Bullet Punch', 'Dark Pulse', 'Retaliate', 'Shell Smash', 'Dive', 'Steel Wing', 'U-turn', 'Razor Shell', 'Noble Roar', 'Clear Smog', 'Extreme Speed', 'Reversal', 'Ice Beam', 'Belly Drum', 'Psychic', 'Follow Me', 'Whirlpool', 'Bestow', 'High Jump Kick', 'Soft-Boiled', 'Secret Power', 'Psych Up', 'Razor Wind', 'Spike Cannon', 'Captivate', 'Charge Beam', 'Coil', 'Entrainment', 'Solar Beam', 'Shadow Ball', 'Metronome', 'Comet Punch', 'Iron Tail', 'Skill Swap', 'Psyshock', 'Psystrike', 'Mega Kick', 'Hyper Drill', 'Gastro Acid', 'Autotomize', 'Defog', 'Imprison', 'Fell Stinger', 'Zing Zap', 'Focus Punch', 'Fiery Dance', 'Dynamic Punch', 'Beat Up', 'Acrobatics', 'Heart Stamp', 'Thrash', 'Dazzling Gleam', 'Anchor Shot', 'After You', 'Flame Charge', 'Super Fang', 'Bug Buzz', 'Lava Plume', 'Earth Power', 'Rolling Kick', 'Baton Pass', 'Shed Tail', 'Snatch', 'Jump Kick', 'Belch', 'Flash Cannon', 'Assist', 'Lovely Kiss', 'Revenge', 'Cotton Guard', 'Signal Beam', 'Leech Life', 'Rock Blast', 'Punishment', 'Fling', 'X-Scissor', 'Snore', 'Avalanche', 'Thief', 'Throat Chop', 'Hurricane', 'Darkest Lariat', 'Discard', 'U-turn', 'Lock-On', 'Electroweb', 'Crush Claw', 'Octazooka', 'Outrage', 'Skull Bash', 'Aqua Cutter', 'Feather Dance', 'Needle Arm', 'Spiky Shield', 'Stone Edge', 'Spider Web', 'Aqua Tail', 'Clamp', 'Rock Polish', 'Gunk Shot', 'Dual Chop', 'Sludge Wave', 'Double Hit', 'Wring Out', 'Infestation']
define abilitiesin = ['Stall', 'Trace', 'Shell Armor', 'Chlorophyll', 'Steelworker', 'Hustle', 'Keen Eye', 'Plus', 'Healer', 'Merciless', 'Sweet Veil', 'Rock Head', 'Iron Fist', 'Overgrow', 'Tinted Lens', 'Shield Dust', 'Volt Absorb', 'Disguise', 'Magic Guard', 'Weak Armor', 'White Smoke', 'Synchronize', 'Overcoat', 'Own Tempo', 'Prankster', 'Sheer Force', 'Contrary', 'Iron Barbs', 'Telepathy', 'Blaze', 'Serene Grace', 'Run Away', 'Pickup', 'Steadfast', 'Levitate', 'Mold Breaker', 'Shed Skin', 'Shields Down', 'Strong Jaw', 'Reckless', 'Illuminate', 'Intimidate', 'Regenerator', 'Sap Sipper', 'Hyper Cutter', 'Guts', 'Solar Power', 'Flash Fire', 'Swarm', 'Damp', 'Cloud Nine', 'Leaf Guard', 'Limber', 'Rattled', 'Wonder Skin', 'Anger Point', 'Harvest', 'Ice Body', 'Compound Eyes', 'Insomnia', 'Arena Trap', 'Defeatist', 'Gluttony', 'Klutz', 'Vital Spirit', 'Flame Body', 'Super Luck', 'Water Absorb', 'Sand Force', 'Honey Gather', 'Moody', 'Unaware', 'Infiltrator', 'Heavy Metal', 'Sturdy', 'Thick Fat', 'Oblivious', 'Berserk', 'Flower Veil', 'Torrent', 'Inner Focus', 'Symbiosis', 'Sand Rush', 'Sand Veil', 'Moxie', 'Static', 'Schooling', 'Sniper', 'Aftermath', 'Clear Body', 'Speed Boost', 'Technician', 'Frisk', 'Simple', 'Rivalry', 'Early Bird', 'Anticipation', 'Lightning Rod', 'Natural Cure', 'Poison Point', 'Pure Power', 'Cheek Pouch', 'Adaptability', 'Triage', 'Huge Power', 'Quick Feet', 'Ball Fetch', 'Scrappy', 'Gale Wings', 'Toxic Debris', 'Defiant', 'Magic Bounce', 'Tough Claws', 'Cute Charm', 'Soundproof', 'Slow Start', 'Big Pecks', 'Pixilate', 'No Guard', 'Wimp Out', 'Power of Alchemy', 'Sand Stream', 'Emergency Exit', 'Forecast', 'Sticky Hold', 'Cursed Body', 'Vital spirit', 'Stakeout', 'Unnerve', 'Filter', 'Stench', 'Pressure', 'Justified', 'Hydration', 'Poison Touch', 'Magnet Pull', 'Wonder Guard', 'Competitive', 'Scrappy', 'Battle Armor', 'Solid Rock', 'Zen Mode', 'Snow Cloak', 'Analytic', 'Drizzle', 'Drought', 'Snow Warning', 'Minus', 'Shadow Tag', 'Swift Swim', 'Dry Skin', 'Punk Rock', 'Unburden', 'Water Veil', 'Forewarn', 'Friend Guard', 'Suction Cups', 'Pickpocket', 'Skill Link', 'Storm Drain', 'Rough Skin', 'Sharpness']
default persondex = copy.deepcopy(defaultpersondex)

default classstats = {
    "Normal" : 0,
    "Fire" : 0,
    "Water" : 0,
    "Grass" : 0,
    "Electric" : 0,
    "Ice" : 0,
    "Fighting" : 0,
    "Poison" : 0,
    "Ground" : 0,
    "Flying" : 0,
    "Psychic" : 0,
    "Bug" : 0,
    "Rock" : 0,
    "Ghost" : 0,
    "Dark" : 0,
    "Dragon" : 0,
    "Steel" : 0,
    "Fairy" : 0
}

default personalstats = {
    "Charm" : 0,
    "Knowledge" : 0,
    "Courage" : 0,
    "Wit" : 0,
    "Patience" : 0
}

default gymbattles = { }

default council_campaigning = False
default leafwindowjump = False
default lastclass = ""
default chosenindex = -247
default starter_id = 0
default starter_name = ""
default playerparty = []
default pkmnlocked = -1
default profanity = False
default money = 0
default sidemonnum = 0
default inventory = {}
default location = ""
default mustswitch = False
default hidebattleui = False
default randcount = 0
default box = []
default freelectricphases = []
default boughtitems = 1
default pikachudenial = 0
default testbattle = False
default persistent.testwarning = False
default excusesecondelective = False
default excusesecondhomeroom = False
default lastfight = datetime.datetime(2004, 4, 16)
default punkwins = 0
default hideside = False
default janinedomming = True
# keeps track of the amount of money you've invested
default investment = 0
# keeps track of the amount of money your investment has returned
default gains = 0
default patiencefix = False
default starterobj = None
default invpage = "Healing"
default invoverwrite = None
default activeitem = None
default activemon = None
default activerepel = None
default repelstepsleft = 0
default freeroaming = False
default usinginventory = False
#variables for sorting pc boxes
default currentbox = 0
default currentsort = None
default reversesort = True
#variables for sorting social screen
default socialsort = None
#turned on at start of battle, turned off at end
default inbattle = False
#turns true when you defeat/catch Cramorant
default seaportunlocked = False
#turns true the first time you challenge Cramorant
default seencramorant = False
#counts the number of conscutive battles you've had in the wild area
default wildcount = 0
default highestwildcount = 0
# triggers if you've just passed a battle exam in an elective
default passedclass = False
# used to display item messages
default ItemText = ""
#used to keep track of who you've given gifts to. Resets weekly on Monday
default GiftsGiven = []
#keeps track of if you've ever performed a critical capture
default CritCaptures = 0
#keeps track of the move you're teaching for overriding the "switch" menu
default taughtmove = None
#keeps track of who you're playing as for gimmick days. None = "Red"
default playercharacter = None
#keeps track of the eggs you took and hatched. Also counts the Happiny.
default eggshatched = []
#keeps track of when the random seed was created
default randseedtime = None