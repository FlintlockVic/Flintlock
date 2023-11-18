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
                persondex[keyname]["Sex"] = copy.copy(defaultpersondex[keyname]["Sex"])
            if "Relationship" not in persondex[keyname].keys():
                changemade = True
                persondex[keyname]["Relationship"] = copy.copy(defaultpersondex[keyname]["Relationship"])
            if "Mood" not in persondex[keyname].keys():
                changemade = True
                persondex[keyname]["Mood"] = copy.copy(defaultpersondex[keyname]["Mood"])
            if "Nature" not in persondex[keyname].keys():
                changemade = True
                persondex[keyname]["Nature"] = copy.copy(defaultpersondex[keyname]["Nature"])
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

    if ("Instructeur Fantina" in persondex.keys()):
        changemade = True
        del persondex["Instructeur Fantina"]

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

    if (not WonBattle("BrendanMay2")):
        changemade = True
        mayhaslarvesta = True

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
        changemade = True

    if (SecureShareAndEggAmount()):
        changemade = True

    if (changemade):
        renpy.block_rollback()

    pkmnlocked = -1
    randcount = randcount % 1000000

    highestlevel = 0
    saltgiven = False
    for mon in playerparty + box:
        if (mon.GetLevel() > highestlevel):
            highestlevel = min(100, mon.GetLevel())
        if (mon.GetId() in [932, 933, 934]):
            saltgiven = True

    if (not saltgiven and not soldmysterygift and not giftedmysterygift):#FIX THIS: Remove for next release.
        saltparty = copy.copy(playerparty)
        playerparty = []
        levelincrease = 100 / (100 - highestlevel)
        renpy.notify("You gained a Mystery Gift! Check out your PC next chance you get!")
        box.append(Pokemon(932, nickname = "Gabirel", level=max(10, GetHighestLevelAll()), ability="Purifying Salt", item="Mystery Gift"))
        playerparty = saltparty

return


init python:
    def SecureShareAndEggAmount():
        changemade = False
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
        
        return changemade

    def SetRandSeed(staySame = False, extraseed = ""):
        global randcount
        if (IsAfter(5, 4, 2004)):
            random.seed(timeOfDay + str(randseedtime) + str(calDate.day) + str(calDate.month) + str(calDate.year) + ("" if staySame else str(randcount)) + extraseed)
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

    def AnimateArrow(value, position, changemood=True):
        imagename = "pointsplus" + str(value)
        if (value < 0):
            imagename = "pointsminus" + str(-value)
            
        tagname = "name" + str(value) + ''.join(RandomChoices(string.ascii_lowercase, 10))
        renpy.show(imagename, [pointsup(position)], tag=tagname, layer="arrowlayer")
        if (usingmoods and changemood):
            renpy.show(("pointsminus3" if value < 0 else "pointsplus3"), [pointsup(position + 0.01), Transform(zoom=0.5, matrixcolor=InvertMatrix(1.0))], tag=tagname + "mood", layer="arrowlayer")

        renpy.music.set_volume(0.25, delay=0.0, channel="music")
        if (value > 0):
            renpy.sound.play("Audio/PointsUp.ogg", channel="misc")
        else:
            renpy.sound.play("Audio/PointsDown.ogg", channel="misc")   
        renpy.music.set_volume(1.0, delay=2.0, channel="music")

    def ValueChange(name, value, position, pausing=True, changemood=True):
        if name not in persondex:
            persondex[name] = copy.deepcopy(defaultpersondex[name])
    
        persondex[name]["Value"] += value

        if (changemood and usingmoods):
            if (GetNature(name) != TrainerNature.Special):
                if (value > 0):
                    persondex[name]["Mood"] = GetMood(name) + 3
                else:
                    persondex[name]["Mood"] = GetMood(name) - 3

        AnimateArrow(value, position, changemood)
        if (pausing):
            renpy.pause(1.5)

    def InvestmentChange(value, ignoremoney = False):
        global money
        global investment
        if (money >= value or ignoremoney):
            if (not ignoremoney):
                money -= value
            investment += value
            PlaySound("PointsUp.ogg")
            renpy.say(narrator, "You invested ${}! Your total investment is now ${}!".format(value, investment))
        else:
            PlaySound("PointsDown.ogg")
            renpy.say(narrator, "You don't have enough money to invest ${}!".format(value))

    def TraitChange(name, increase=1):
        personalstats[name] += increase
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

        renpy.show("traitspointplus" + str(increase), [pointsup(0.5), Transform(matrixcolor=TintMatrix(color))])
        renpy.music.set_volume(0.5, delay=0.0, channel="music")
        renpy.music.set_volume(1.0, delay=0.0, channel="points")
        renpy.music.play("Audio/PointsUp.ogg", channel='points', loop=None)
        renpy.say("", "Your {{color={}}}{}{{/color}} increased to {}!".format(color, name, personalstats[name]))
        
        renpy.pause(1.5)
        renpy.hide("traitspointplus" + str(increase))
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

    renpy.music.register_channel("ctc", mixer="sfx", loop=False)
    renpy.music.register_channel("altcry", mixer="sfx", loop=False)
    renpy.music.register_channel("XYgame", mixer="music", loop=False)
    renpy.music.register_channel("crowd", mixer="sfx", loop=True)
    renpy.music.register_channel("crowd2", mixer="sfx", loop=True)
    renpy.music.register_channel("crowd3", mixer="sfx", loop=False)
    renpy.music.register_channel("points", mixer="sfx", loop=False)
    renpy.music.register_channel("misc", mixer="sfx", loop=False)
    renpy.music.register_channel("evolution", mixer="music", loop=True)

    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.music.play("Audio/Button_A.wav", channel="ctc")

    def donothing():
        pass

    def getCharColor(findname):
        for char in charlist:
            if (findname.lower() in char.name.lower() or (char.image == "red" and findname == first_name) or (char.image == "pikachu" and findname == pika_name) or (char.image == "blue" and findname == blue_name)):
                return char.color
        if (findname == "Gramps"):
            return "#5e5e5e"
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

    def GetHighestLevelAll():
        highestlevel = 0
        for mon in playerparty + box:
            if (mon.GetLevel() > highestlevel):
                highestlevel = mon.GetLevel()
        return highestlevel

    def GetAllPokemonIn():
        return [932, 933, 934, 531.1, 122.1, 866, 131.1, 88, 89, 359.1, 263.1, 264.1, 862, 554.1, 555.2, 555.3, 38, 38.1, 446, 143, 427, 428, 428.1, 359, 870, 506, 4, 258, 387, 179, 363, 532, 41, 328, 396, 280, 540, 246, 607, 551, 371, 304, 669, 206, 554, 194, 548, 170, 361, 447, 747, 529, 198, 677, 290, 566, 200, 559, 696, 597, 742, 531, 631, 746, 781, 556, 479, 615, 214, 336, 618, 357, 561, 213, 774, 778, 302, 780, 227, 303, 263, 155, 399, 191, 835, 133, 919, 406, 29, 32, 333, 307, 401, 111, 710, 659, 967, 777, 764, 431, 607, 767, 412, 81, 351, 559, 568, 104, 629, 677, 917, 744, 353, 88.1, 714, 965, 439, 507, 5, 259, 388, 180, 364, 533, 42, 329, 397, 281, 541, 247, 608, 552, 372, 305, 670, 982, 555, 195, 549, 171, 362, 448, 748, 530, 199, 678, 291, 567, 429, 560, 697, 598, 743, 264, 156, 400, 192, 836, 134, 920, 315, 30, 33, 334, 308, 402, 112, 711, 660,432, 608, 768, 413, 82,560, 569, 105, 630, 678, 918, 745, 354, 89.1, 715, 966, 122, 508, 6, 260, 389, 181, 365, 534, 169, 330, 398, 282, 542, 248, 609, 553, 373, 306, 671,478,430, 678.1, 292,157,135,407, 31, 34,464, 609,414, 462,745.1,745.2, 136, 196, 197, 470, 471, 700, 636, 637, 175, 176, 468, 236, 237, 106, 107, 238, 124, 240, 126, 467, 360, 202, 438, 185, 440, 113, 242, 458, 226, 848, 849, 849.1, 79, 80, 199, 215, 461, 725, 726, 727, 633, 634, 635, 556, 183, 184, 58, 59, 602, 603, 604, 131, 852, 853, 690, 691, 194.1, 980, 580, 581, 976, 595, 596, 688, 689, 592, 593, 318, 319, 885, 886, 887, 393, 394, 395, 183, 184, 190, 424, 223, 224]
    
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
        renpy.say(narrator, "Your {} proficiency increased to {}! Your {}-type Pokémon can now reach level {}.".format(type, newtotal, type, levelcap))

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
            if (SecureShareAndEggAmount()):
                renpy.notify("An error occurred, and your number of Exp Shares/Lucky Eggs has been set back to 1. Please report this bug, as well as when this showed up, in the discord. TRIGGERED ON REMOVEITEM")

    def RemoveForeverals(pkmn):
        if (inbattle):
            renpy.invoke_in_new_context(renpy.say, None, "Please wait until the battle is over to unequip Foreverals.")
        else:
            foreveralinv.append(pkmn.GetForeverals()[0])
            pkmn.Foreverals = []
            pkmn.RecalculateStats()

    def FormatNum(num):
        return f'{num:g}'

    def GetCharsInPlace(place):
        if (excusesecondelective or excusesecondhomeroom):
            return []
        additive = []
        subtractive = []
        if (place == "Garden" and IsAfter(12, 4, 2004) and IsBefore(1, 5, 2004)):
            additive.append("Tia")
        if (place == "Research Center" and IsAfter(19, 4, 2004)):
            additive.append("Sonia")
        if (place == "Academy" and IsAfter(25, 4, 2004)):
            if (Random(True, "JasmineHangout" + timeOfDay) > 0.5 or IsDate(25, 4, 2004)):
                additive.append("Jasmine")
            if (Random(True, "GrushaHangout" + timeOfDay) > 0.5 or IsDate(25, 4, 2004)):
                additive.append("Grusha")
        if (place == "Academy" and IsAfter(14, 4, 2004)):
            subtractive.append("Cheren")
        if (place == "Academy" and IsAfter(1, 5, 2004)):
            subtractive.append("Sabrina")
        if (place == "Garden" and IsAfter(1, 5, 2004)):
            subtractive.append("Erika")
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
            if (IsAfter(19, 4, 2004)):
                npcs = ["Nate", "Skyla", "Nessa", "Sonia", "Rosa"] 
            if (IsDate(19, 4, 2004)):
                npcs = ["Nate", "Skyla", "Rosa"] 
        elif (table == "Romantic Table"):
            npcs = ["Serena", "Calem", "Brendan", "May"]
        elif (table == "Calm Table"):
            npcs = ["Sabrina", "Bea", "Hilda", "Cheren"]
            if (IsAfter(14, 4, 2004)):
                npcs = ["Sabrina", "Bea", "Hilda"]
                if (IsAfter(25, 4, 2004)):
                    npcs = ["Sabrina", "Bea", "Hilda", "Jasmine", "Grusha"]
                    if (Random(True, "Jasmine") <= 0.5):
                        npcs.remove("Jasmine")
                    if (Random(True, "Grusha") <= 0.5):
                        npcs.remove("Grusha")

                elif (IsDate(26, 4, 2004)):
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

    def GetNature(character):
        if "Nature" not in persondex[character].keys():
            persondex[character]["Nature"] = copy.copy(defaultpersondex[character]["Nature"])
        return persondex[character]["Nature"]

    def GetMood(character):
        if "Mood" not in persondex[character].keys():
            persondex[character]["Mood"] = copy.copy(defaultpersondex[character]["Mood"])
        return persondex[character]["Mood"]

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
        return ((altclassdex[type] 
        | ({"Erika"} if type in ["Grass", "Poison"] and (IsAfter(10, 4, 2004)) else set()) 
        | ({"Tia"} if type in ["Dragon", "Psychic"] and ((IsDate(13, 4, 2004) and timeOfDay == "Afternoon") or IsAfter(13, 4, 2004)) and IsBefore(1, 5, 2004) else set())
        | ({"Sonia"} if type in ["Electric", "Fairy"] and ((IsDate(20, 4, 2004) and timeOfDay == "Afternoon") or IsAfter(19, 4, 2004)) else set())
        | ({"Jasmine"} if type in ["Steel", "Ground"] and (IsAfter(26, 4, 2004) and (Random(True, "JasmineElective") > 0.5) or IsDate(26, 4, 2004) and timeOfDay == "Afternoon") else set())
        | ({"Grusha"} if type in ["Ice", "Flying"] and (IsAfter(26, 4, 2004) and (Random(True, "GrushaElective") > 0.5) or IsDate(26, 4, 2004) and timeOfDay == "Afternoon") else set()))
        - ({"Sabrina"} if type in ["Psychic", "Ghost"] and (IsAfter(1, 5, 2004)) else set()))

    def WillStudy(type):
        return (GetStudents(type)
        - ({"Erika"} if type in ["Grass", "Poison"] and (IsAfter(1, 5, 2004)) else set())
        - ({"Cheren"} if type in ["Dark", "Normal"] and (IsAfter(14, 4, 2004)) else set()))

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

        for fvl in foreveraldex:
            for move in fvl[FVLMacros.FVLMoves]:
                if (not MoveIsIn(move)):
                    finalmoves.add(move)

        finalabilities = set()
        for mon in GetAllPokemonIn():
            for ability in GetAbilities(mon):
                if (not AbilityIsIn(ability)):
                    finalabilities.add(ability)

        for fvl in foreveraldex:
            if (fvl[FVLMacros.FVLType] == ForeveralTypes.AddAbility):
                for ability in fvl[FVLMacros.FVLTypeData]:
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

    def IsAfter(day, month, year):
        return not IsBefore(day, month, year) and not IsDate(day, month, year)

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
            "Healing": ["Potion", "Super Potion", "Hyper Potion", "Revive", "Max Revive", "Max Potion", "Full Restore", "Max Elixir", "Antidote", "Paralyze Heal", "Ice Heal", "Awakening", "Burn Heal", "Full Heal", "Oran Berry", "Sitrus Berry"],
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
            if (partymon.GetHealthPercentage() < 1 and partymon.GetHealthPercentage() != 0):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(20)
                success = True
        elif (activeitem == "Super Potion"):
            if (partymon.GetHealthPercentage() < 1 and partymon.GetHealthPercentage() != 0):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(60)
                success = True
        elif (activeitem == "Hyper Potion"):
            if (partymon.GetHealthPercentage() < 1 and partymon.GetHealthPercentage() != 0):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(120)
                success = True
        elif (activeitem == "Max Potion"):
            if (partymon.GetHealthPercentage() < 1 and partymon.GetHealthPercentage() != 0):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(999)
                success = True
        elif (activeitem == "Full Restore"):
            if ((partymon.GetHealthPercentage() < 1 or partymon.HasNormalStatus() or partymon.HasStatus("confused")) and partymon.GetHealthPercentage() != 0):
                if (checksuccess):
                    return True
                partymon.ClearStatus("all", nonvolatilesandconfusion=True)
                partymon.AdjustHealth(999)
                success = True
        elif (activeitem == "Max Elixir"):
            movemissingpp = False
            for move in partymon.GetMoves():
                if (move.PP != move.MaxPP):
                    movemissingpp = True
            if (movemissingpp and partymon.GetHealthPercentage() != 0):
                if (checksuccess):
                    return True
                for move in partymon.GetMoves():
                    move.PP = move.MaxPP
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
            if ((partymon.GetHealthPercentage() < 1.0 and (not autotrigger or partymon.GetHealthPercentage() <= 0.5) and not AbilityOnOpponentField(partymon, "Unnerve") or forceuse) and partymon.GetHealthPercentage() != 0):
                if (checksuccess):
                    return True
                partymon.AdjustHealth(10)
                success = True
        elif (activeitem == "Sitrus Berry"):
            if ((partymon.GetHealthPercentage() < 1.0 and (not autotrigger or partymon.GetHealthPercentage() <= 0.5) and not AbilityOnOpponentField(partymon, "Unnerve") or forceuse) and partymon.GetHealthPercentage() != 0):
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

    def GetGiftValue(character, item):
        global giftedmysterygift
        if (item == "Premier Ball"):
            return 7
        if (item == "Mystery Gift"):
            if (giftedmysterygift):
                return 0
            else:
                giftedmysterygift = True
                return 10
        
        if (character in classdex.keys()):
            for shopitem in shopitems.values():
                if (item == shopitem[1]):
                    if (shopitem[0] < 500):
                        return 2
                    elif (shopitem[0] < 800):
                        return 3
                    elif (shopitem[0] < 1001):
                        return 4
                    elif (shopitem[0] < 5001):
                        return 5
                    else:
                        return 10
            
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
                return 20
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
        global soldmysterygift
        returnvalue = 100
        for shopitem in shopitems.values():
            if (item == shopitem[1]):
                returnvalue = shopitem[0] / 2.0
                break
        if (item in elementitems.keys()):
            returnvalue = 500
        if (item == "Mystery Gift"):
            if (not soldmysterygift):
                soldmysterygift = True
                returnvalue = 2000
            else:
                return 0
        return math.floor(returnvalue)

    def GetLiberaColor(firstcolor = True):
        if (pikachuobj.GetTypes() == ["Electric"]):
            return "#fff"
        if (libtypes == []):
            if (firstcolor):
                return GetTypeColor(pikachuobj.GetTypes()[0])
            else:
                if (len(pikachuobj.GetTypes()) > 1):
                    return GetTypeColor(pikachuobj.GetTypes()[1])
                else:
                    return GetTypeColor(pikachuobj.GetTypes()[0]) 
        elif (firstcolor):
            return GetTypeColor(libtypes[0])
        else:
            if (len(libtypes) > 1):
                return GetTypeColor(libtypes[1])
            else:
                return GetTypeColor(libtypes[0]) 

    def UpdateForeverals():
        added = []
        for fvl in foreveraldex:
            requiredrank = 0
            level = fvl[FVLMacros.FVLLevel]
            trainer = fvl[FVLMacros.FVLTrainer]
            name = fvl[FVLMacros.FVLName]
            if (level == 3):
                requiredrank = 1
            elif (level == 5):
                requiredrank = 2
            elif (level == 7):
                requiredrank = 3
            elif (level == 9):
                requiredrank = 4
            elif (level == 10):
                requiredrank = 5
            if (GetCharacterLevel(trainer) >= level
            and GetRelationshipRank(trainer) >= requiredrank
            and name not in claimedforeverals):
                foreveralinv.append(name)
                claimedforeverals.append(name)
                added.append(name)
        return added

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

define mooddict = {
    -10: { TrainerNature.Distant: (-5,0), TrainerNature.Moody: (-5,1), TrainerNature.Neutral: (-5,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -9: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -8: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -7: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -6: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-5,0), TrainerNature.Devoted: (0,2)},
    -5: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-3,1), TrainerNature.Friendly: (-3,1), TrainerNature.Devoted: (0,2)},
    -4: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-2,1), TrainerNature.Friendly: (-3,1), TrainerNature.Devoted: (0,2)},
    -3: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-2,1), TrainerNature.Friendly: (-3,1), TrainerNature.Devoted: (0,2)},
    -2: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-1,1), TrainerNature.Friendly: (-1,1), TrainerNature.Devoted: (0,2)},
    -1: { TrainerNature.Distant: (-3,1), TrainerNature.Moody: (-3,1), TrainerNature.Neutral: (-1,1), TrainerNature.Friendly: (-1,1), TrainerNature.Devoted: (0,1)},
    0: { TrainerNature.Distant: (-1,0), TrainerNature.Moody: (0,0), TrainerNature.Neutral: (0,0), TrainerNature.Friendly: (1,0), TrainerNature.Devoted: (2,0)},
    1: { TrainerNature.Distant: (1,-1), TrainerNature.Moody: (2,-1), TrainerNature.Neutral: (1,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    2: { TrainerNature.Distant: (1,-1), TrainerNature.Moody: (2,-1), TrainerNature.Neutral: (1,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    3: { TrainerNature.Distant: (1,-1), TrainerNature.Moody: (2,-1), TrainerNature.Neutral: (2,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    4: { TrainerNature.Distant: (1,-1), TrainerNature.Moody: (2,-1), TrainerNature.Neutral: (2,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    5: { TrainerNature.Distant: (1,-2), TrainerNature.Moody: (3,-1), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    6: { TrainerNature.Distant: (1,-2), TrainerNature.Moody: (3,-1), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    7: { TrainerNature.Distant: (3,-2), TrainerNature.Moody: (3,-1), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    8: { TrainerNature.Distant: (3,-3), TrainerNature.Moody: (3,-1), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    9: { TrainerNature.Distant: (3,-3), TrainerNature.Moody: (5,-2), TrainerNature.Neutral: (3,-1), TrainerNature.Friendly: (3,-1), TrainerNature.Devoted: (3,-1)},
    10: { TrainerNature.Distant: (5,-3), TrainerNature.Moody: (5,-2), TrainerNature.Neutral: (5,-1), TrainerNature.Friendly: (5,-1), TrainerNature.Devoted: (5,-1)}
}

define liberizefirstsentence = {
    "Normal": "Everyone",
    "Fire": "The torch of revolution",
    "Water": "The primordial sea",
    "Grass": "The circle of life",
    "Electric": "A bolt from the blue",
    "Ice": "The frigid sky",
    "Fighting": "A just fist",
    "Poison": "Every option",
    "Ground": "An ancient nation",
    "Flying": "Freedom's wing",
    "Psychic": "A brilliant mind",
    "Bug": "A union of millions",
    "Rock": "The earth itself",
    "Ghost": "An ancient soul",
    "Dark": "A necessary evil",
    "Dragon": "A legendary power",
    "Steel": "Justice's blade",
    "Fairy": "The people's hope"
}

define liberizesecondsentence = {
    "Normal": "moves toward liberty!",
    "Fire": "ignites the flames of liberty!",
    "Water": "crashes down for liberty!",
    "Grass": "restores liberty!",
    "Electric": "surges towards liberty!",
    "Ice": "preserves liberty!",
    "Fighting": "fights for liberty!",
    "Poison": "removes obstacles to liberty!",
    "Ground": "unearths liberty!",
    "Flying": "soars toward liberty!",
    "Psychic": "concludes with liberty!",
    "Bug": "joins for liberty!",
    "Rock": "carves liberty into stone!",
    "Ghost": "empowers undying liberty!",
    "Dark": "fights dirty for liberty!",
    "Dragon": "roars for liberty!",
    "Steel": "gilds the banner of liberty!",
    "Fairy": "wishes for liberty!"
}

define nonvolatiles = ["burned", "frozen", "paralyzed", "poisoned", "badly poisoned", "asleep", "busted disguise", "frenzied", "mega evolved", "minigigamaxed"]
define normalstatuses = ["burned", "frozen", "paralyzed", "poisoned", "badly poisoned", "asleep"]
define bluecolor = "{color=#0048ff}"
define sabrinacolor = "{color=#600080}"
define movesin = ['Salt Cure', 'Heavy Slam', 'Heat Crash', 'Defense Curl', 'Tackle', 'Echoed Voice', 'Trick', 'Play Nice', 'Thunder Shock', 'Tail Whip', 'Play Rough', 'Copycat', 'Mega Drain', 'Bullet Seed', 'Constrict', 'Rage', 'Confusion', 'Poison Sting', 'Sharpen', 'Sandstorm', 'Absorb', 'Fake Tears', 'Wing Attack', 'Last Resort', 'Pound', 'Spite', 'Double Team', 'Minimize', 'Pursuit', 'Sticky Web', 'Wrap', 'String Shot', 'Mud Sport', 'Sand Attack', 'Razor Leaf', 'Vine Whip', 'Iron Head', 'Growth', 'Splash', 'Leaf Storm', 'Bubble', 'Supersonic', 'Peck', 'Swagger', 'Misty Terrain', 'Flail', 'Charge', 'Covet', 'Mud-Slap', 'Rock Throw', 'Sheer Cold', 'Bind', 'Taunt', 'Quick Attack', 'Harden', 'Discharge', 'Growl', 'Helping Hand', 'Hyper Voice', 'Scratch', 'Rollout', 'Icy Wind', 'Wood Hammer', 'Fairy Wind', 'Encore', 'Feint Attack', 'Astonish', 'Switcheroo', 'Fissure', 'Ember', 'Gust', 'Smog', 'Water Gun', 'Bide', 'Foresight', 'Rapid Spin', 'Bite', 'Focus Energy', 'Confuse Ray', 'Baby-Doll Eyes', 'Leer', 'Ice Shard', 'Twister', 'Miracle Eye', 'Arm Thrust', 'Incinerate', 'Psywave', 'Headbutt', 'Horn Attack', 'Powder Snow', 'Night Slash', 'Hone Claws', 'Odor Sleuth', 'Withdraw', 'Endure', 'Thunder Wave', 'Hypnosis', 'Lick', 'Poison Powder', 'Vise Grip', 'Dragon Rage', 'Draco Meteor', 'Poison Gas', 'Whirlwind', 'Roar', 'Disable', 'Vacuum Wave', 'Stun Spore', 'Counter', 'Sweet Scent', 'Night Shade', 'Seismic Toss', 'Feint', 'Fire Spin', 'Leech Seed', 'Uproar', 'Bulldoze', 'Bug Bite', 'Refresh', 'Mud Shot', 'Electro Ball', 'Mist', 'Haze', 'Poison Tail', 'Teleport', 'Protect', 'Curse', 'Metal Claw', 'Smokescreen', 'Spore', 'Sleep Powder', 'Aerial Ace', 'Stomp', 'Screech', 'Torment', 'Lucky Chant', 'Struggle Bug', 'Acid', 'Rock Smash', 'Disarming Voice', 'Leafage', 'Yawn', 'Wide Guard', 'Rest', 'Facade', 'Detect', 'Agility', 'Shadow Sneak', 'Heal Pulse', 'Light Screen', 'Reflect', 'Toxic Spikes', 'Trick-or-Treat', 'Pluck', 'Swift', 'Nuzzle', 'Flame Burst', 'Camouflage', 'Chip Away', 'Gyro Ball', 'Pin Missile', 'Magical Leaf', 'Metal Sound', 'Take Down', 'Wake-Up Slap', 'Natural Gift', 'Worry Seed', 'Ancient Power', 'Tailwind', 'Synthesis', 'Sweet Kiss', 'Fire Fang', 'Poison Fang', 'Ice Fang', 'Thunder Fang', 'Safeguard', 'Stealth Rock', 'Sand Tomb', 'Endeavor', 'Scary Face', 'Iron Defense', 'Acid Armor', 'Sing', 'Force Palm', 'Hidden Power', 'Double Slap', 'Aqua Ring', 'Assurance', 'Flame Wheel', 'Dig', 'Work Up', 'Venoshock', 'Low Kick', 'Psybeam', 'Cotton Spore', 'Slam', 'Brine', 'Glare', 'Wish', 'Grass Whistle', 'Meditate', 'Mimic', 'Slash', 'Drill Run', 'Fury Swipes', 'Fake Out', 'Attract', 'Ice Ball', 'Payback', 'Round', 'Mud Bomb', 'Draining Kiss', 'Body Slam', 'Hyper Fang', 'Smack Down', 'Water Sport', 'Ingrain', 'Silver Wind', 'Bubble Beam', 'Mean Look', 'Block', 'Fury Attack', 'Water Shuriken', 'Air Cutter', 'Charm', 'Rock Tomb', 'Spark', 'Aurora Beam', 'Will-O-Wisp', 'Breaking Swipe', 'Flower Shield', 'Double Kick', 'Toxic', 'Dragon Breath', 'Rock Slide', 'Milk Drink', 'Recover', 'Mach Punch', 'Chrysalize', 'Enshroud', 'Legacy', 'Energize', 'Ardent Gaze', 'Disabling Poke', 'Rain Dance', 'Steady Flame', 'Wing It', 'Deathless', 'Bark Up', 'Burial Ground', 'Slow Freeze', 'Simple World', 'Bad Breath', 'Clear Mind', 'Splinter Shield', 'Metallize', 'Lightning Rod', 'Magnitude', 'Acid Spray', 'Acupressure', 'Howl', 'Spikes', 'Bone Rush', 'Bonemerang', 'First Impression', 'Hex', 'Bone Club', 'Tearful Look', 'Brave Bird', 'Boomburst', 'Shock Wave', 'Ice Punch', 'Double-Edge', 'Freeze-Dry', 'Dragon Pulse', 'Air Slash', 'Grass Knot', 'Dragon Claw', 'Explosion', 'Power-Up Punch', 'Pain Split', 'Power Whip', 'Power Trip', 'Electrify', 'Dragon Tail', 'Tickle', 'Zap Cannon', 'Heat Wave', 'Poison Jab', 'Fury Cutter', 'Petal Blizzard', 'Quick Guard', 'Fly', 'Power Swap', 'Flatter', 'Embargo', 'Megahorn', 'Rock Climb', 'Magnet Bomb', 'Stored Power', 'Superpower', 'Rototiller', 'Magnetic Flux', 'Barrier', 'Weather Ball', 'Head Smash', 'Brick Break', 'Recycle', 'Healing Wish', 'Flare Blitz', 'Nasty Plot', 'Laser Focus', 'Mirror Move', 'Calm Mind', 'False Swipe', 'Teeter Dance', 'Accelerock', 'Future Sight', 'Eerie Impulse', 'Aura Sphere', 'Hail', 'Sunny Day', 'Silk Trap', 'Destiny Bond', 'Baneful Bunker', 'Sky Attack', 'Dragon Dance', 'Tri Attack', 'Sonic Boom', 'Crunch', 'Quiver Dance', 'Thunder Punch', 'Earthquake', 'Magnet Rise', 'Morning Sun', 'Moonlight', 'Moonblast', 'Roost', 'Perish Song', 'Swords Dance', 'Sucker Punch', 'Petal Dance', 'Fire Punch', 'Water Spout', 'Eruption', 'Electric Terrain', 'Sludge', 'Bulk Up', 'Grassy Terrain', 'Shift Gear', 'Pollen Puff', 'Phantom Force', 'Hammer Arm', 'Mirror Shot', 'Swallow', 'Ion Deluge', 'Spit Up', 'Aromatherapy', 'Water Pulse', 'Close Combat', 'Cross Poison', 'Venom Drench', 'Knock Off', 'Mirror Coat', 'Power Gem', 'Giga Drain', 'Amnesia', 'Mystical Fire', 'Guard Swap', 'Self-Destruct', 'Aqua Jet', 'Lunge', 'Shadow Claw', 'Ominous Wind', 'Zen Headbutt', 'Horn Drill', 'Guillotine', 'Stockpile', 'Rock Wrecker', 'Hyper Beam', 'Giga Impact', 'Blast Burn', 'Hydro Cannon', 'Frenzy Plant', 'Roar of Time', 'Bounce', 'Frustration', 'Return', 'Magic Coat', 'Dizzy Punch', 'Sludge Bomb', 'Me First', 'Rage Powder', 'Synchronoise', 'Triple Kick', 'Power Trick', 'Memento', 'Substitute', 'Leaf Tornado', 'Mind Reader', 'Bullet Punch', 'Dark Pulse', 'Retaliate', 'Shell Smash', 'Dive', 'Steel Wing', 'U-turn', 'Razor Shell', 'Noble Roar', 'Clear Smog', 'Extreme Speed', 'Reversal', 'Ice Beam', 'Belly Drum', 'Psychic', 'Follow Me', 'Whirlpool', 'Bestow', 'High Jump Kick', 'Soft-Boiled', 'Secret Power', 'Psych Up', 'Razor Wind', 'Spike Cannon', 'Captivate', 'Charge Beam', 'Coil', 'Entrainment', 'Solar Beam', 'Shadow Ball', 'Metronome', 'Comet Punch', 'Iron Tail', 'Skill Swap', 'Psyshock', 'Psystrike', 'Mega Kick', 'Hyper Drill', 'Gastro Acid', 'Autotomize', 'Defog', 'Imprison', 'Fell Stinger', 'Zing Zap', 'Focus Punch', 'Fiery Dance', 'Dynamic Punch', 'Beat Up', 'Acrobatics', 'Heart Stamp', 'Thrash', 'Dazzling Gleam', 'Anchor Shot', 'After You', 'Flame Charge', 'Super Fang', 'Bug Buzz', 'Lava Plume', 'Earth Power', 'Rolling Kick', 'Baton Pass', 'Shed Tail', 'Snatch', 'Jump Kick', 'Belch', 'Flash Cannon', 'Assist', 'Lovely Kiss', 'Revenge', 'Cotton Guard', 'Signal Beam', 'Leech Life', 'Rock Blast', 'Punishment', 'Fling', 'X-Scissor', 'Snore', 'Avalanche', 'Thief', 'Throat Chop', 'Hurricane', 'Darkest Lariat', 'Discard', 'U-turn', 'Lock-On', 'Electroweb', 'Crush Claw', 'Octazooka', 'Outrage', 'Skull Bash', 'Aqua Cutter', 'Feather Dance', 'Needle Arm', 'Spiky Shield', 'Stone Edge', 'Spider Web', 'Aqua Tail', 'Clamp', 'Rock Polish', 'Gunk Shot', 'Dual Chop', 'Sludge Wave', 'Double Hit', 'Wring Out', 'Infestation', 'Twineedle', 'Branch Poke', 'No Retreat', 'Scale Shot', 'Headlong Rush', 'Spirit Break', 'Flip Turn', 'Liberage', 'Stomping Tantrum', 'Psycho Cut', 'Drill Peck', 'Sleep Talk', 'Foul Play', 'Cross Chop', 'Gravity', 'Grudge', 'Shadow Punch', 'Obstruct', 'Hydro Pump', 'Aurora Veil', 'Icicle Crash', 'Parting Shot', 'Slack Off', 'Extrasensory', 'Leaf Blade', 'Fillet Away', 'Flamethrower', 'Cosmic Power', 'Energy Ball', 'Submission', 'Muddy Water', 'Dream Eater', 'Floral Healing', 'Inferno', 'Low Sweep', 'Ally Switch', 'Shore Up', 'Snarl', 'Circle Throw', 'Karate Chop', 'Role Play', 'Fire Blast', 'Blizzard', 'Mega Punch', 'Frost Breath', 'Psychic Fangs']
define abilitiesin = ['Purifying Salt', 'Stall', 'Trace', 'Shell Armor', 'Chlorophyll', 'Steelworker', 'Hustle', 'Keen Eye', 'Plus', 'Healer', 'Merciless', 'Sweet Veil', 'Rock Head', 'Iron Fist', 'Overgrow', 'Tinted Lens', 'Shield Dust', 'Volt Absorb', 'Disguise', 'Magic Guard', 'Weak Armor', 'White Smoke', 'Synchronize', 'Overcoat', 'Own Tempo', 'Prankster', 'Sheer Force', 'Contrary', 'Iron Barbs', 'Telepathy', 'Blaze', 'Serene Grace', 'Run Away', 'Pickup', 'Steadfast', 'Levitate', 'Mold Breaker', 'Shed Skin', 'Shields Down', 'Strong Jaw', 'Reckless', 'Illuminate', 'Intimidate', 'Regenerator', 'Sap Sipper', 'Hyper Cutter', 'Guts', 'Solar Power', 'Flash Fire', 'Swarm', 'Damp', 'Cloud Nine', 'Leaf Guard', 'Limber', 'Rattled', 'Wonder Skin', 'Anger Point', 'Harvest', 'Ice Body', 'Compound Eyes', 'Insomnia', 'Arena Trap', 'Defeatist', 'Gluttony', 'Klutz', 'Vital Spirit', 'Flame Body', 'Super Luck', 'Water Absorb', 'Sand Force', 'Honey Gather', 'Moody', 'Unaware', 'Infiltrator', 'Heavy Metal', 'Sturdy', 'Thick Fat', 'Oblivious', 'Berserk', 'Flower Veil', 'Torrent', 'Inner Focus', 'Symbiosis', 'Sand Rush', 'Sand Veil', 'Moxie', 'Static', 'Schooling', 'Sniper', 'Aftermath', 'Clear Body', 'Speed Boost', 'Technician', 'Frisk', 'Simple', 'Rivalry', 'Early Bird', 'Anticipation', 'Lightning Rod', 'Natural Cure', 'Poison Point', 'Pure Power', 'Cheek Pouch', 'Adaptability', 'Triage', 'Huge Power', 'Quick Feet', 'Ball Fetch', 'Scrappy', 'Gale Wings', 'Toxic Debris', 'Defiant', 'Magic Bounce', 'Tough Claws', 'Cute Charm', 'Soundproof', 'Slow Start', 'Big Pecks', 'Pixilate', 'No Guard', 'Wimp Out', 'Power of Alchemy', 'Sand Stream', 'Emergency Exit', 'Forecast', 'Sticky Hold', 'Cursed Body', 'Vital spirit', 'Stakeout', 'Unnerve', 'Filter', 'Stench', 'Pressure', 'Justified', 'Hydration', 'Poison Touch', 'Magnet Pull', 'Wonder Guard', 'Competitive', 'Scrappy', 'Battle Armor', 'Solid Rock', 'Zen Mode', 'Snow Cloak', 'Analytic', 'Drizzle', 'Drought', 'Snow Warning', 'Minus', 'Shadow Tag', 'Swift Swim', 'Dry Skin', 'Punk Rock', 'Unburden', 'Water Veil', 'Forewarn', 'Friend Guard', 'Suction Cups', 'Pickpocket', 'Skill Link', 'Storm Drain', 'Rough Skin', 'Sharpness', 'Prism Armor', 'Parental Bond', 'Fluffy', 'Tangled Feet', 'Immunity', 'Gorilla Tactics', 'Screen Cleaner']
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
#the list that all Pokemon in the PC are kept in
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
#blue's nickname, after you start calling him Blue
default oldblue_name = "Blueberry"
#activated once Ethan teaches you about moods
default usingmoods = False
#keeps track of the button text for the tera button
default terabuttontext = "Terastalize"
#used to keep track of which moves have been avoided in the first Dawn fight
default movesdodged = []
#keeps track of which dialog has already been shown in a battle with cutscenes
default dialogshown = []
#allows the usage of fractions for dramatic effect in dawn fight
default allowfractions = False
#keeps track of the button text for the liberize button 
default libbuttontext = "Liberize"
#keeps track of which types you're Liberized into
default libtypes = []
#true if it's the first dawn battle
default dawnbattle = False
#keeps track of the max number of types you can liberize into (2 in first Dawn battle)
default libtypesnum = 1
#keeps track of when you're allowed to use Foreverals
default usingforeverals = False
#the foreveral inventory
default foreveralinv = []
default claimedforeverals = []
#keeps track of how we're sorting the foreveral inventory page
default foreveralsort = None
default foreveralsortinverse = False
default foreveralpage = 0
default examinedf = None
#keeps track of if I'm currently explaining how a foreveral works
default explainingf = False
#mystery gift variables to prevent exploitation
default soldmysterygift = False
default giftedmysterygift = False
#saw wallyellow scene
default sawwallyellow = False