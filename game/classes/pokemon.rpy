init python:
    class Pokemon:
        def __init__(self, id, level=5, moves=None, nickname=None, ivs=None, evs=None, nature=None, gender=None, item=None, ability=None, intelligence=0, teratype=None, foreverals = None, vic_touched=0):
            self.Nickname = nickname#string
            if (isinstance(id, str)):
                id = pokedexlookupname(id, DexMacros.Id)
            self.Id = id#int
            self.Level = level#int
            self.IVs = ivs#[int]
            if (self.IVs == None):
                self.IVs = []
                for i in range(0, 6):
                    self.IVs.append(RandInt(0, 31))
            self.EVs = evs#[int]
            if (self.EVs == None):
                self.EVs = [0, 0, 0, 0, 0, 0]
            self.Moves = moves#[Move]
            if (self.Moves == None):
                if (self.Level == 5):
                    self.Moves = GetStartingMoves(self)
                else:
                    self.Moves = GetMovesForLevel(self)

            movenames = []
            removemoves = []
            for newmove in self.Moves:
                if (newmove.Name in movenames):
                    removemoves.append(newmove)
                else:
                    movenames.append(newmove.Name)
            for oldmove in removemoves:
                self.Moves.remove(oldmove)
            self.Nature = nature#Natures macro
            if (self.Nature == None):
                self.Nature = RandInt(0, 24)
            self.Item = item#string or None
            self.Gender = gender#Genders Macro
            if (self.Gender == None and not IsGenderless(self)):
                self.Gender = RandomChoice([Genders.Male, Genders.Female])
            if (self.GetId() in [669, 670, 671, 548, 549, 29, 30, 31, 413, 413.1, 413.2, 629, 630, 440, 113, 242, 238, 124, 440, 113, 242, 592.1, 593.1]):
                self.Gender = Genders.Female
            if (self.GetId() in [32, 33, 34, 414, 627, 628, 236, 237, 106, 107, 592, 593]):
                self.Gender = Genders.Male

            self.Stats = [0, 0, 0, 0, 0, 0]
            self.RecalculateStats()
            
            self.Health = self.Stats[Stats.Health]
            self.StatChanges = {}
            self.Status = {}#statuses that begin with "." don't get printed
            self.Ability = ability
            if (self.Ability == None):
                self.Ability = RandomChoice(GetAbilities(id))
            self.Personality = Random()
            self.Image = None
            self.Experience = self.CalculateAllExperienceNeededForLevel(self.Level)
            self.Owner = None#Trainer object, defined during battle
            self.TrainerType = None#TrainerType Macro, defined during battle
            self.WasCaught = 0#int, defined during battle
            self.DamagedThisTurn = False#bool, defined during battle
            self.TurnSwitchedIn = 0#int, defined during battle
            self.Intelligence = intelligence
            self.FaintedOnTurn = -10
            self.ItemHistory = []#list of item changes in battle--set at the start of every battle. List of tuples formatted like ("Started", None, 0), ("Gained", "Oran Berry", 1), ("Lost", "Oran Berry", 2), ("Gained", "Oran Berry", 3), ("Used", "Oran Berry", 4)
            if (teratype == None):
                self.TeraType = pokedexlookup(self.GetId(), DexMacros.Type1)#The 'mon's inherent tera type
            else:
                self.TeraType = teratype
            self.Terastalized = -1#-1 if not terastalized. Otherwise, it's the turn you terastalized
            self.FormeOverride = None#keeps track of the current form you're taking
            self.AbilityOverride = None#keeps track of the current ability you have
            self.Foreverals = foreverals
            if (self.Foreverals == None):
                self.Foreverals = []#keeps track of what foreverals are active for you
            self.AbilityChanged = False#keeps track of if your ability changes, through mega evolution, diveralization, or minigigamax
            self.vic_touched = vic_touched

        def GetForeverals(self):
            if (not hasattr(self, 'Foreverals')):
                self.Foreverals = []
            return self.Foreverals

        def HasForeveral(self, foreveralname):
            return foreveralname in self.GetForeverals()

        def GetFaintedTurn(self):
            if (not hasattr(self, 'FaintedOnTurn')):
                self.FaintedOnTurn = -10
            return self.FaintedOnTurn

        def GetIntelligence(self):
            if (not hasattr(self, 'Intelligence')):
                self.Intelligence = 0
            return self.Intelligence

        def GetTurnSwitchedIn(self):
            if (not hasattr(self, 'TurnSwitchedIn')):
                self.TurnSwitchedIn = 0
            return self.TurnSwitchedIn

        def SetTurnSwitchedIn(self, turnnum):
            self.TurnSwitchedIn = max(0, turnnum)

        def GetDamagedThisTurn(self):
            if (not hasattr(self, 'DamagedThisTurn')):
                self.DamagedThisTurn = False
            return self.DamagedThisTurn

        def SetDamagedThisTurn(self, bool):
            self.DamagedThisTurn = bool

        def GetPersonality(self):
            return self.Personality

        def MakeCaught(self, hp):
            self.WasCaught = hp
            if (len(playerparty) != 6):
                playerparty.append(self)
            else:
                AddMon(self)

        def ResetCaught(self):
            self.WasCaught = 0

        def GetCaught(self):
            if (not hasattr(self, 'WasCaught')):
                self.ResetCaught()
            return self.WasCaught

        def RecalculateStats(self, updateHealth = True):
            for i in range(6):
                basestat = pokedexlookup(self.GetId(), i + DexMacros.Health)
                for fvl in self.GetForeverals():
                    if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Scaling):
                        scalingmon, scalinglevel = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
                        scalingstat = pokedexlookupname(scalingmon, i + DexMacros.Health)
                        newstat = basestat * max((scalinglevel - self.GetLevel()) / scalinglevel, 0) + scalingstat * min(self.GetLevel() / scalinglevel, 1)
                        if (newstat > basestat):
                            basestat = newstat

                self.Stats[i] = round((math.floor(0.01 * (2 * basestat + self.IVs[i] + math.floor(0.25 * self.EVs[i])) * self.Level) + 5) * NatureToBonus(self.Nature, i))

            if (self.GetId() == 292):#Shedinja
                self.Stats[Stats.Health] = 1
            else:
                maxhealth = round(math.floor(0.01 * (2 * pokedexlookup(self.GetId(), DexMacros.Health) + self.IVs[Stats.Health] + math.floor(0.25 * self.EVs[Stats.Health])) * self.Level) + self.Level + 10)
                self.Stats[Stats.Health] = maxhealth
                self.Health = min(self.GetHealth(), maxhealth)

        def CalculateExperienceNeededForLevel(self, level):
            if (level < 2):
                return 0
            return pow(level, 3) / 25

        def CalculateAllExperienceNeededForLevel(self, level):
            totalval = 0
            for i in range(1, level + 1):
                totalval += self.CalculateExperienceNeededForLevel(i)
            return totalval

        def CalculateGivingExperience(self, othermon):
            ownlevel = min(AimLevel(), self.GetLevel())
            return math.floor(10 + self.CalculateExperienceNeededForLevel(ownlevel) * ownlevel / (othermon.GetLevel() + max(0, (othermon.GetLevel() - self.GetLevel())) * 10) * pokedexlookup(self.GetId(), DexMacros.Total) / 300 * 0.1)

        def GetLevelCap(self):
            highest = 1
            if (self.Ability == "Freelectric" and 1 in freelectricphases):
                highest = classstats[getRankStat(0)] + 1

            elements = self.GetTypes(True)
            for fvl in self.GetForeverals():
                if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddProficiency):
                    for proficientelement in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                        elements.append(proficientelement)
            for element in elements:
                if (classstats[element] > highest):
                    highest = classstats[element]
            return math.floor(highest)

        def GetMaxLevel(self):
            for i in range(100):
                if (self.GetExperience() < self.CalculateAllExperienceNeededForLevel(i)):
                    return i - 1
            return 100

        def LearnNewMove(self, newmoves):
            if (len(newmoves) > 0):
                for movetuple in newmoves:
                    newmove = movetuple[1]
                    moveconfirmed = False
                    
                    if (newmove not in self.GetMoveNames()):
                        newmoveobj = GetMove(newmove)
                        self.Moves.append(newmoveobj)
                    
                        while (not moveconfirmed):
                            if (len(self.GetMoves()) > 4):
                                renpy.say("", self.GetNickname() + " wants to learn " + newmove + ", but " + self.GetNickname() + " already knows four moves. Which move should " + self.GetNickname() + " forget?")
                                removal = renpy.call_screen("modalnonbattlemoves", self, True, True)
                                moveconfirmed = renpy.display_menu([("Forget " + removal.Name, True), ("Keep " + removal.Name, False)], interact=True, screen="choice")
                                if (moveconfirmed):
                                    self.Moves.remove(removal)
                                    if (removal.Name != newmove):
                                        renpy.say("", self.GetNickname() + " forgot " + removal.Name + " and learned " + newmove + "!")
                                        if (newmove != "Liberage"):
                                            newmoveobj.PP = min(removal.PP, newmoveobj.MaxPP)
                                    else:
                                        renpy.say("", self.GetNickname() + " did not learn " + newmove + "!")
                            else:
                                moveconfirmed = True
                                renpy.say("", self.GetNickname() + " learned " + newmove + "!")

        def GainExperience(self, newexp, fainting=False):
            global starter_id
            global starter_name
            global starter_species_name

            if (not hasattr(self, 'Experience')):
                self.Experience = self.CalculateAllExperienceNeededForLevel(self.Level)

            if (not hasattr(self, 'vic_touched')):
                self.vic_touched = 0

            if (inbattle and self.HasItem("Lucky Egg", activating=False) and self.vic_touched == 0):
                newexp *= 2
            
            posttext = ""
            if (self.Level >= self.GetLevelCap()):
                posttext = " The experience has been stored for later!"
            renpy.say("", self.GetNickname() + " gained " + str(math.floor(newexp)) + " experience!" + posttext)
            self.Experience += newexp

            self.LevelUp(fainting)

            expleft = math.floor(self.GetExperience() - self.CalculateAllExperienceNeededForLevel(self.Level))
            if (posttext == "" and self.Level >= self.GetLevelCap() and expleft != 0):
                renpy.say("", str(expleft) + " experience has been stored for later!")

        def LevelUp(self, fainting=False):
            priorlevel = self.GetLevel()
            while (self.GetExperience() > self.CalculateAllExperienceNeededForLevel(self.Level + 1) and self.Level < self.GetLevelCap()):
                self.Level += 1
                OldHp = self.Stats[Stats.Health]
                self.RecalculateStats()
                if (not fainting):
                    NewHp = self.Stats[Stats.Health]
                    self.AdjustHealth(NewHp - OldHp, directdamage=True)
                renpy.say("", self.GetNickname() + " leveled up to level " + str(self.GetLevel()) + "!")
                newmoves = GetLevelMoves(self, self.GetLevel(), True)
                self.LearnNewMove(newmoves)   

            if (self.GetLevel() != priorlevel and self.Id != 25.2):
                evoconditions = []

                for mon in pokedex:
                    if (mon[DexMacros.Prevo] == pokedexlookup(self.GetId(), DexMacros.Forme)):
                        evocondition = mon[DexMacros.Evolve]
                        if (evocondition != None and len(evocondition) <= 6 and "Lv." in evocondition):
                            evoconditions.append(mon[DexMacros.Evolve])

                if (evoconditions != []):
                    evocondition = evoconditions[0]
                else:
                    evocondition = ""

                oldname = self.GetNickname()
                damagebefore = self.GetStat(Stats.Health, absolute=True) - self.Health

                passesevocondition = (self.GetId() in [412, 412.1, 412.2] and self.GetLevel() >= 20# burmy
                    or self.GetId() == 439 and "Mimic" in self.GetMoveNames()#Mime Jr.
                    or self.GetId() == 438 and "Mimic" in self.GetMoveNames()#Bonsly
                    or self.GetId() == 852 and "Taunt" in self.GetMoveNames()#Clobbopus
                    or self.GetId() == 190 and "Double Hit" in self.GetMoveNames()#Aipom
                    or self.GetId() == 744 and timeOfDay in ["Noon", "Afternoon", "Night"] and self.GetLevel() >= 25#Rockruff
                    or self.GetId() == 236 and self.GetLevel() >= 20#Tyrogue
                    or self.GetId() == 458 and 223 in GetPartySpecies()#Mantyke
                    or self.GetId() == 848 and self.GetLevel() >= 30#Toxel
                    or evocondition != "" and int(evocondition.split("Lv. ")[1]) <= self.GetLevel())

                evolveinto = self.GetId() + 1
                if (self.GetId() in [412, 412.1, 412.2] and self.GetGender() == Genders.Male):#male burmy -> mothim
                    evolveinto = 414
                elif (self.GetId() == 439):#Mime Jr -> Mr. Mime
                    evolveinto = 122
                elif (self.GetId() == 194.1):#Paldean Wooper
                    evolveinto = 980
                elif (self.GetId() == 744):
                    if (timeOfDay in ["Evening"]):#dusk lycanroc
                        evolveinto = 745.2
                    elif (timeOfDay == "Night"):#midnight lycanroc
                        evolveinto = 745.1
                elif (self.GetId() == 677):
                    if (self.GetGender() == Genders.Female):#female meowstic
                        evolveinto = 678.1
                elif (self.GetId() == 236):
                    if (self.GetStat(Stats.Attack, absolute=True) > self.GetStat(Stats.Defense, absolute=True)):#hitmonlee 
                        evolveinto = 106
                    elif (self.GetStat(Stats.Attack, absolute=True) < self.GetStat(Stats.Defense, absolute=True)):#hitmonchan
                        evolveinto = 107
                elif (self.GetId() == 240):
                    evolveinto = 126#magmar
                elif (self.GetId() == 238):
                    evolveinto = 124#jynx
                elif (self.GetId() == 360):
                    evolveinto = 202#wobbufett
                elif (self.GetId() == 194.1):
                    evolveinto = 980#clodsire
                elif (self.GetId() == 190):
                    evolveinto = 424#ambipom
                elif (self.GetId() == 438):
                    evolveinto = 185#sudowoodo
                elif (self.GetId() == 458):
                    evolveinto = 226#Mantine
                elif (self.GetId() == 848 and self.GetNature() in [Natures.Lonely, Natures.Bold, Natures.Relaxed, Natures.Timid, Natures.Serious, Natures.Modest, Natures.Mild, Natures.Quiet, Natures.Bashful, Natures.Calm, Natures.Gentle, Natures.Careful]):
                    evolveinto = 849.1

                if (passesevocondition):
                    oldabilityslot = GetAbilities(self.GetId()).index(self.Ability)
                    renpy.say(None, "What?")
                    renpy.pause(1.0)

                    renpy.music.set_volume(0.0, 0.5)
                    renpy.music.set_volume(0.0, 0.5, channel="crowd")
                    renpy.music.set_volume(0.0, 0.5, channel="crowd2")
                    renpy.music.set_volume(0.0, 0.5, channel="misc")
                    renpy.music.queue("audio/music/evolution_cut.mp3", channel="evolution")

                    evolved = renpy.call_screen("evolution", self.GetId(), evolveinto)
                    if (evolved):
                        renpy.music.set_volume(1.0, 0.5)
                        renpy.music.set_volume(1.0, 0.5, channel="crowd")
                        renpy.music.set_volume(1.0, 0.5, channel="crowd2")
                        renpy.music.set_volume(1.0, 0.5, channel="misc")
                        renpy.music.stop(channel="evolution")
                        PlaySound("Get.ogg")

                        newspeciesname = pokedexlookup(evolveinto, DexMacros.Name)
                        oldspeciesname = pokedexlookup(self.GetId(), DexMacros.Name)
                        self.Id = evolveinto
                        self.RecalculateStats()
                        self.Ability = GetAbilities(self.GetId())[min(oldabilityslot, len(GetAbilities(self.GetId())) - 1)]
                        self.AdjustHealth(self.GetStat(Stats.Health, absolute=True) - damagebefore, True)
                        renpy.say(None, "{} evolved into a {}!".format(oldname, newspeciesname))
                        
                        if (self.GetNickname() == oldspeciesname):
                            self.Nickname = newspeciesname
                        if (len(self.GetForeverals()) > 0):
                            renpy.say(None, "But its Foreveral is no longer in tune with {}'s wishes!".format(self.GetNickname()))
                            for fvl in self.GetForeverals():
                                foreveralinv.append(fvl)
                            self.Foreverals = []
                        self.ChangeForme(None, revert=True)
                        newmoves = GetLevelMoves(self, self.GetLevel(), True)
                        self.LearnNewMove(GetEvoMoves(self) + newmoves)

                        if (self.GetId() == 291 and len(playerparty) < 6):#Ninjask
                            playerparty.append(Pokemon(292, level=self.GetLevel(), ivs=copy.copy(self.IVs), evs=copy.copy(self.EVs), nature=self.GetNature(), gender=Genders.Unknown))

                        if (self == starterobj):
                            starter_id = self.GetId()
                            starter_name = self.GetNickname()
                            starter_species_name = newspeciesname
                        
                    else:
                        renpy.music.set_volume(1.0, 0.5)
                        renpy.music.set_volume(1.0, 0.5, channel="crowd")
                        renpy.music.set_volume(1.0, 0.5, channel="crowd2")
                        renpy.music.set_volume(1.0, 0.5, channel="misc")
                        renpy.music.stop(channel="evolution")

                        renpy.music.queue("audio/music/evolution_cut.mp3")

                        renpy.say(None, "{} didn't evolve...".format(self.GetNickname()))               

        def GetItem(self):
            return self.Item

        def GetItemHistory(self):
            if (not hasattr(self, 'ItemHistory')):
                self.ItemHistory = []
            return self.ItemHistory

        def AdjustItemHistory(self, action, item):
            if (not hasattr(self, 'ItemHistory')):
                self.ItemHistory = []
            self.ItemHistory.append((action, item, Turn))

        def GetStartingItem(self):
            try:
                return mon.GetItemHistory()[0][1]
            except:
                return None

        def TakeItem(self):
            if (self.GetItem() != None and not self.HasStatus("substitute")):
                olditem = self.GetItem()
                self.Item = None
                self.AdjustItemHistory("Lost", olditem)
                return "{} lost its {}!".format(self.GetNickname(), olditem)
            elif (self.HasStatus("substitute")):
                return "The substitute isn't holding anything!"
            else:
                return "But {} isn't holding anything!".format(self.GetNickname())

        def GiveItem(self, item, overwrite=False):
            global activeitem
            activeitem = item
            if (item != None and self.GetItem() != None and not overwrite):
                return "But {} is already holding the {}!".format(self.GetNickname(), self.GetItem())
            elif (item != None):
                self.Item = item
                self.AdjustItemHistory("Gained", item)
                activeitem = item
                if (Turn != 0 and UseItem(self, checksuccess=True, inbattle=True, autotrigger=True)):#should trigger stolen berries immediately
                    self.HasItem(item)
                return "{} gained the {}!".format(self.GetNickname(), item)
            elif (self.GetItem() != None):
                self.TakeItem()

            if (SecureShareAndEggAmount()):
                renpy.notify("An error occurred, and your number of Exp Shares/Lucky Eggs has been set back to 1. Please report this bug, as well as when this showed up, in the discord. TRIGGERED ON GIVEITEM")

            return ""

        def GetFormeOverride(self):
            if (not hasattr(self, 'FormeOverride')):
                self.FormeOverride = None
            return self.FormeOverride

        def GetId(self):
            return (self.Id if self.GetFormeOverride() == None else self.GetFormeOverride())

        def GetStatusKeys(self):
            return self.Status.keys()

        def GetStatusCount(self, status):
            if (self.HasStatus(status)):
                return self.Status[status]
            return 0

        def HasStatus(self, status):
            try:
                return status.lower() in self.GetStatusKeys()
            except:
                return False

        def HasNormalStatus(self):
            for status in normalstatuses:
                if (self.HasStatus(status)):
                    return True
            return False

        def GetNature(self):
            return self.Nature

        def GetWeight(self):
            return max(0.2, pokedexlookup(target.GetId(), DexMacros.Weight) - self.GetStatusCount("nimble") * 220)

        def GetAbilityChanged(self):
            if (not hasattr(self, 'AbilityChanged')):
                self.AbilityChanged = False
            return self.AbilityChanged

        def ApplyStatus(self, status, count=1, applier=None, overwrite=False):
            returnable = ""
            if (applier == None):
                applier = self

            if (status == ".tracing"):#don't need to set abilitychanged, because it's automatic
                ReactivateAbility(self, True)

            if (applier != self and self.HasStatus("substitute") and not IsSoundMove(ActiveMove) and not applier.HasAbility("Infiltrator")):
                return "The substitute absorbed the status!"
            elif (BattlefieldExists("Misty Terrain") and (status in normalstatuses or status == "confused")):
                return "Misty Terrain prevented the affliction!"
            elif (BattlefieldExists("Electric Terrain") and status in ["asleep", "drowsy"]):
                return "Electric Terrain prevented the affliction!"
            elif (WeatherIs("sunny") and (status in normalstatuses) and self.HasAbility("Leaf Guard")):
                return "The leaf guard prevented the affliction!"
            elif (applier != self and EffectOnOwnField(self, "safeguard") and status in normalstatuses):
                return "The safeguard prevented the affliction!"
            elif (status == "asleep" and self.HasAbility("Sweet Veil")):
                return "Sweet Veil prevented sleep!"
            elif (status == "asleep" and (self.HasAbility("Insomnia") or self.HasAbility("Vital Spirit") or StatusInBattlers("uproaring"))):
                return "{} can't fall asleep!".format(self.GetNickname())
            elif (status == "confused" and self.HasAbility("Own Tempo")):
                return "Own Tempo prevented confusion!"
            elif (status == "flinching" and self.HasAbility("Steadfast")):
                self.ChangeStats(Stats.Speed, 1, self)
            elif (status == "flinching" and self.HasAbility("Inner Focus")):
                return "{} didn't flinch!".format(self.GetNickname())
            elif (status == "paralyzed" and self.HasAbility("Limber")):
                return "{} is too limber to be paralyzed!".format(self.GetNickname())
            elif (status == "paralyzed" and self.HasType("Electric")):
                return "{} cannot be paralyzed!".format(self.GetNickname())
            elif (status == "taunted" and self.HasAbility("Oblivious")):
                return "{} is oblivious to the taunt!".format(self.GetNickname())
            elif (status == "infatuated" and self.HasAbility("Oblivious")):
                return "{} is oblivious to the foe's charms!".format(self.GetNickname())
            elif (status == "burned" and self.HasType("Fire")):
                return "{} cannot be burned!".format(self.GetNickname())
            elif ((status == "poisoned" or status == "badly poisoned") and (self.HasType("Poison") or self.HasType("Steel") or self.HasAbility("Immunity"))):
                return "{} cannot be poisoned!".format(self.GetNickname())
            elif (self.Image == None and (status in normalstatuses or status == "drowsy") and self.HasAbility("Shields Down")):
                return "But {}'s shield is up!".format(self.GetNickname())
            elif ((status in normalstatuses or status == "drowsy") and self.HasAbility("Purifying Salt")):
                return "But {}'s salt is pure!".format(self.GetNickname())
            elif (status == "burned" and self.HasAbility("Water Veil")):
                return "Water Veil prevents burns!"
            elif (status in ["poisoned", "badly poisoned"] and self.HasAbility("Immunity")):
                return "{} is immune to poison!".format(self.GetNickname())

            if (not overwrite):
                for affliction in normalstatuses:
                    if (status[0] != "."):
                        if ((status in normalstatuses or status == "drowsy") and affliction in self.Status.keys()):
                            return "But {} is already {}!".format(self.GetNickname(), affliction)
                        elif (self.HasStatus(status)):
                            return "But {} is already {}!".format(self.GetNickname(), status)
            
            if (applier != self and status in ["burned", "paralyzed", "poisoned", "badly poisoned"] and self.HasAbility("Synchronize")):
                applier.ApplyStatus(status, count)
                returnable = "Synchronize copied the status!"

            if (status == "asleep" and self.HasAbility("Early Bird")):
                count = math.floor(count / 2.0)

            self.Status[status] = count

            statusberries = ["Pecha Berry"]
            for berry in statusberries:
                self.HasItem(berry)

            if (status == "raging"):
                return "{} started raging!".format(self.GetNickname())
            elif (status == "stockpiled"):
                return "{} stockpiled {}!".format(self.GetNickname(), self.GetStatusCount("stockpiled"))
            elif (status == "substitute"):
                return "{} hid behind a substitute!".format(self.GetNickname())
            elif (status == "flinching" or status[0] == "."):
                return ""
            elif (status == "aqua ring"):
                return "{} set up an Aqua Ring!".format(self.GetNickname())
            elif (status == "gorging" and self.HasStatus("frenzied")):
                return "The frenzied Cramorant is trying to swallow [pika_name]!"
            return "{} became {}! {}".format(self.GetNickname(), status, returnable)

        def DecrementStatus(self, status):
            returnable = ""
            if (self.HasStatus(status)):
                self.Status[status] = self.GetStatusCount(status) - 1
                if (status == "wrapped" and self.Status["wrapped"] == 0):
                    returnable += "{} was freed from Wrap!".format(self.GetNickname())
                if (status == "bound" and self.Status["bound"] == 0):
                    returnable += "{} was freed from Bind!".format(self.GetNickname())
                if (status == "firespun" and self.Status["firespun"] == 0):
                    returnable += "{} was freed from Fire Spin!".format(self.GetNickname())
                if (status == "whirlpooled" and self.Status["whirlpooled"] == 0):
                    returnable += "{} was freed from Whirlpool!".format(self.GetNickname())
                if (status == "entombed" and self.Status["entombed"] == 0):
                    returnable += "{} was freed from Sand Tomb!".format(self.GetNickname())
                if (status == "clamped" and self.Status["clamped"] == 0):
                    returnable += "{} was freed from Clamp!".format(self.GetNickname())
                if (status == "infested" and self.Status["infested"] == 0):
                    returnable += "{} was freed from Infestation!".format(self.GetNickname())
                if (status == "perishing"):
                    returnable += "{}'s perish count fell to {}!".format(self.GetNickname(), self.GetStatusCount(status))
            return returnable

        def HasItem(self, item, activating = True, autotriggerset=True):
            global ItemText
            global activeitem
            if (not activating):
                return self.GetItem() == item
            else:
                if (self.GetItem() == item and not self.HasStatus("embargoed")):
                    activeitem = item
                    if (UseItem(self, checksuccess=False, inbattle=True, forceuse=False, autotrigger=autotriggerset)):
                        ItemText += "{}'s {} was used!".format(self.GetNickname(), activeitem)                
                    return True
                else:
                    return False

        def MarkItemUsed(self):
            self.AdjustItemHistory("Used", self.GetItem())
            for ally in GetBattlers(self):
                if (ally.GetItem() == None and ally.HasAbility("Symbiosis")):
                    ally.GiveItem(self.GetItem())
                    break
            if (IsBerry(self.GetItem()) and self.HasAbility("Cheek Pouch")):
                self.AdjustHealth(self.GetStat(Stats.Health) / 3.0)
            self.Item = None

        def ClearStatus(self, status, all=False, volatiles=False, nonvolatilesandconfusion=False):
            returntext = ""
            if (volatiles):
                copystatus = self.Status.copy()
                for existingstatus in copystatus.keys():
                    if (existingstatus not in nonvolatiles):
                        del self.Status[existingstatus]
            elif (nonvolatilesandconfusion):
                copystatus = self.Status.copy()
                for existingstatus in copystatus.keys():
                    if (existingstatus in normalstatuses + ["confused"]):
                        del self.Status[existingstatus]
            elif (all):
                if (self.HasStatus("busted disguise") and self.GetHealthPercentage() < 1):
                    self.Status = {"busted disguise": 1}
                else:
                    self.Status = {}
            elif (status in self.Status):
                if (status == "thrashing" and self.GetStatusCount("thrashing") == 0):
                    returntext += self.ApplyStatus("confused", RandInt(4, 5), self)
                del self.Status[status]
                return self.GetNickname() + " is no longer " + status + "!" + returntext

        def AdjustHealth(self, adjustment, absolute=False, directdamage=False):
            global activeitem
            diddamage = False
            if (absolute):
                self.Health = (math.floor(adjustment) if not allowfractions else adjustment)
                diddamage = True
            elif (directdamage or adjustment > 0 or not self.HasAbility("Magic Guard")):
                if (adjustment < 0):
                    self.SetDamagedThisTurn(True)
                self.Health += math.floor(adjustment)
                if (self.Health <= 0):
                    self.Health = 0
                elif (self.Health > self.Stats[Stats.Health]):
                    self.Health = self.Stats[Stats.Health]    
                diddamage = True 

            if (adjustment < 0 and self.GetHealth() > 0):
                itemchecks = ["Oran Berry", "Sitrus Berry"]
                for item in itemchecks:
                    if (self.GetItem() == item):
                        activeitem = item
                        if (UseItem(self, checksuccess=True, inbattle=True, forceuse=False, autotrigger=True)):
                            self.HasItem(item)
                            break               

                if (self.GetId() == 774 and self.GetHealthPercentage() > 0.5):#Minior
                    self.ChangeForme("Minior (Meteor Form)")

            if (self.GetId() in [334, 334.1] and dawnbattle and self.GetHealth() < 1):
                self.Health = 1#I'm genuinely sorry I had to do this. If it's any consolation, you're very smart.

            return diddamage

        def GetHealth(self):
            if (not hasattr(self, 'Health')):
                self.Health = 1
            return self.Health

        def GetHealthPercentage(self):
            return self.GetHealth() / self.Stats[Stats.Health]

        def GetStat(self, stat, ignorepositive=False, ignorenegative=False, triggerAbilities = True, absolute=False):
            if (absolute):
                return self.Stats[stat]

            rawstat = self.Stats[stat]
            if (self.HasStatus("power tricked")):
                if (stat == Stats.Attack):
                    rawstat = self.Stats[Stats.Defense]
                elif (stat == Stats.Defense):
                    rawstat = self.Stats[Stats.Attack]

            modifier = self.GetStatChanges(stat)
            if (modifier > 0):
                modifier = (modifier + 2) / 2.0
            elif (modifier < 0):
                modifier = 2.0 / (-modifier + 2)
            
            if (modifier == 0 or (modifier > 0 and ignorepositive) or (modifier < 0 and ignorenegative)):
                modifier = 1
            
            if (stat == Stats.Speed):
                if (self.HasStatus("paralyzed")):
                    if (self.HasAbility("Quick Feet")):
                        modifier *= 1.5
                    else:
                        modifier /= 2.0
                if (WeatherIs("sunny") and self.HasAbility("Chlorophyll", triggerAbilities)):
                    modifier *= 2.0
                elif (WeatherIs("sandstorm") and self.HasAbility("Sand Rush", triggerAbilities)):
                    modifier *= 2.0
                elif (WeatherIs("rainy") and self.HasAbility("Swift Swim", triggerAbilities)):
                    modifier *= 2.0
                elif (self.HasAbility("Slow Start") and self.GetTurnSwitchedIn() + 5 > Turn):
                    modifier *= 0.5
                if (EffectOnOwnField(self, "tailwind")):
                    modifier *= 2.0
            elif (stat == Stats.Attack):
                if (self.HasAbility("Hustle")):
                    modifier *= 1.5
                elif (self.HasNormalStatus() and self.HasAbility("Guts", triggerAbilities)):
                    modifier *= 1.5
                elif (self.GetHealthPercentage() <= 0.5 and self.HasAbility("Defeatist", triggerAbilities)):
                    modifier *= 0.5
                elif (self.HasAbility("Pure Power") or self.HasAbility("Huge Power")):
                    modifier *= 2.0
                elif (self.HasAbility("Slow Start") and self.GetTurnSwitchedIn() + 5 > Turn):
                    modifier *= 0.5
                elif (self.HasAbility("Gorilla Tactics")):
                    modifier *= 1.5
            elif (stat == Stats.SpecialAttack):
                if (WeatherIs("sunny") and self.HasAbility("Solar Power", triggerAbilities)):
                    modifier *= 1.5
                elif (self.GetHealthPercentage() <= 0.5 and self.HasAbility("Defeatist", triggerAbilities)):
                    modifier *= 0.5
                elif ((self.HasAbility("Plus") and AbilityOnOwnField(self, "Minus")) or (self.HasAbility("Minus") and AbilityOnOwnField(self, "Plus"))):
                    modifier *= 1.5

            return rawstat * modifier

        def GetEV(self, stat):
            return self.EVs[stat]

        def GetIV(self, stat):
            return self.IVs[stat]

        def GetMoves(self):
            if (self.HasStatus("mimicking")):
                moveslist = []
                for move in self.Moves:
                    if (move.Name != "Mimic"):
                        moveslist.append(move)
                moveslist.append(self.GetStatusCount("mimicking"))
                return moveslist
            return self.Moves

        def GetMoveNames(self):
            movenames = []
            for move in self.Moves:
                movenames.append(move.Name)
            return movenames

        def GetMove(self, moveid):
            return self.GetMoves()[moveid]

        def GetMoveByName(self, movename):
            for move in self.Moves:
                if (move.Name == movename):
                    return move
            return None

        def HasPPLeft(self):
            for mymove in self.Moves:
                if (mymove.PP > 0):
                    return True
            return False

        def GetNickname(self):
            return self.Nickname if self.Nickname != None else pokedexlookup(self.GetId(), DexMacros.Name)

        def GetLevel(self):
            return self.Level

        def GetGender(self):
            return self.Gender

        def GetAllStatChanges(self):
            return self.StatChanges

        def GetStatChanges(self, keyname):
            if (keyname in self.StatChanges):
                return self.StatChanges[keyname]
            else:
                return 0

        def GetTotalStatChanges(self):
            totalchanges = 0
            for keyname in self.GetAllStatChanges().keys():
                totalchanges += self.GetStatChanges(keyname)
            return totalchanges

        def GetMovePP(self, movename):
            for move in self.GetMoves():
                if (move.Name == movename):
                    return move.PP
            return 0

        def GetWeight(self):
            return pokedexlookup(self.GetId(), DexMacros.Weight) * (2.0 if self.HasAbility("Heavy Metal") else 1.0)

        def ResetStatChanges(self):
            self.StatChanges = {}

        def ChangeStats(self, keyname, change, inflicter=None):
            selfinflicted = inflicter == None
            if (selfinflicted):
                inflicter = self

            if (inflicter != self and self.HasStatus("substitute") and not IsSoundMove(ActiveMove) and not inflicter.HasAbility("Infiltrator")):
                return "The substitute absorbed the stat changes!"

            if (self.HasAbility("Contrary")):
                change = -change
            elif (self.HasAbility("Simple")):
                change = math.floor(change * 2)

            if (change < 0 and not selfinflicted):
                if (self.HasType("Grass") and AbilityOnOwnField(self, "Flower Veil")):
                    return "The Flower Veil prevented the stat decreases!"
                elif (EffectOnOwnField(self, "mist") and not inflicter.HasAbility("Infiltrator")):
                    return "The Mist prevented the stat decreases!"
                elif (self.HasAbility("White Smoke")):
                    return "The White Smoke prevented the stat decreases!"
                elif (self.HasAbility("Clear Body")):
                    return "{}'s Clear Body can't be blemished!".format(self.GetNickname())
                elif (keyname == Stats.Attack and self.HasAbility("Hyper Cutter")):
                    return "{} is a Hyper Cutter!".format(self.GetNickname())
                elif (keyname == Stats.Defense and self.HasAbility("Big Pecks")):
                    return "{} has Big Pecks!".format(self.GetNickname())
                elif (keyname == Stats.Accuracy and self.HasAbility("Keen Eye")):
                    return "{} has Keen Eyes!".format(self.GetNickname())
            if (keyname in self.StatChanges):
                if (change > 0 and self.StatChanges[keyname] == 6):
                    return "{}'s {} cannot go any higher!".format(self.GetNickname(), StatToString(keyname))
                elif (change < 0 and self.StatChanges[keyname] == -6):
                    return "{}'s {} cannot go any lower!".format(self.GetNickname(), StatToString(keyname))
                else:
                    returnable = "{}'s {} {}!".format(self.GetNickname(), StatToString(keyname), ("rose" if change > 0 else "fell"))
                    self.StatChanges[keyname] += change
                    if (self.StatChanges[keyname] == 0):
                        del self.StatChanges[keyname]
                    renpy.sound.play(("audio/Stat_Increase.wav" if change > 0 else "audio/Stat_Decrease.wav"))
                    if (change < 0 and not selfinflicted):
                        if (self.HasAbility("Defiant")):
                            returnable += " " + self.ChangeStats(Stats.Attack, 2)
                        elif (self.HasAbility("Competitive")):
                            returnable += " " + self.ChangeStats(Stats.SpecialAttack, 2)
                    
                    deletechanges = []
                    for stat in self.StatChanges.keys():
                        self.StatChanges[stat] = max(min(self.StatChanges[stat], 6), -6)
                        if (self.StatChanges[stat] == 0):
                            deletechanges.append(stat)

                    for stat in deletechanges:
                        del self.StatChanges[stat]
                    
                    return returnable 
            else:
                renpy.sound.play(("audio/Stat_Increase.wav" if change > 0 else "audio/Stat_Decrease.wav"))
                self.StatChanges[keyname] = change
                returnable = "{}'s {} {}!".format(self.GetNickname(), StatToString(keyname), ("rose" if change > 0 else "fell"))
                if (change < 0 and not selfinflicted):
                    if (self.HasAbility("Defiant")):
                        returnable += " " + self.ChangeStats(Stats.Attack, 2)
                    elif (self.HasAbility("Competitive")):
                        returnable += " " + self.ChangeStats(Stats.SpecialAttack, 2)
                
                deletechanges = []
                for stat in self.StatChanges.keys():
                    self.StatChanges[stat] = max(min(self.StatChanges[stat], 6), -6)
                    if (self.StatChanges[stat] == 0):
                        deletechanges.append(stat)

                for stat in deletechanges:
                    del self.StatChanges[stat]
                
                return returnable

        def GetTeraType(self):
            if (not hasattr(self, 'TeraType')):
                self.TeraType = pokedexlookup(self.GetId(), DexMacros.Type1)
            return self.TeraType

        def GetTerastalized(self):
            if (not hasattr(self, 'Terastalized')):
                self.Terastalized = -1
            return self.Terastalized

        def IsTerad(self):
            return self.GetTerastalized() != -1

        def GetTypes(self, raw=False, ignoreTera=False):
            types = []
            if (not self.IsTerad() or ignoreTera or raw):
                if (self.GetId() == 25.2):
                    if (libtypes == []):
                        for fvl in self.GetForeverals():
                            types.append(pokedexlookupname(GetForeveralMonname(fvl), DexMacros.Type1))
                        if (types == []):
                            types = ["Electric"]
                    else:
                        for element in libtypes:
                            types.append(element)
                else:
                    types.append(pokedexlookup(self.GetId(), DexMacros.Type1))
                    type2 = pokedexlookup(self.GetId(), DexMacros.Type2)
                    if (type2 != None):
                        types.append(type2)
                if (raw):
                    return types
                for fvl in self.GetForeverals():
                    if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddType):
                        types = types + lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
            else:
                types.append(self.GetTeraType())
            if (BattlefieldExists("Simple World") and IsGroundedSimpleWorld(self, "Flying" in types)):
                types = ["Normal"]
            if (self.HasStatus("trick-or-treating")):
                types.append("Ghost")
            if (self.HasStatus("metallic")):
                types.append("Steel")
            if (self.HasStatus("roosted") and "Flying" in types):
                types.remove("Flying")
            if (self.HasStatus("camouflaged")):
                return [self.GetStatusCount("camouflaged")]
            return types

        def HasType(self, element):
            return element in self.GetTypes()

        def HasAbility(self, abilityname, triggersplash=True):
            fvlability = False
            for fvl in self.GetForeverals():
                if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility and abilityname in lookupforeveraldata(fvl, FVLMacros.FVLTypeData)):
                    fvlability = True
            if (self.GetAbility() == abilityname or fvlability):
                foeignoringabilities = UsingMove and MoveUser != None and MoveUser != self and MoveUser.HasAbility("Mold Breaker")

                if (foeignoringabilities and self.GetAbility() not in ["Prism Armor"]):
                    return False

                if (triggersplash):
                    if (self in FriendlyPokemon()):
                        renpy.hide_screen("abilitysplashleft")
                        renpy.show_screen("abilitysplashleft", (self.GetNickname(), abilityname))
                    else:
                        renpy.hide_screen("abilitysplashright")
                        renpy.show_screen("abilitysplashright", (self.GetNickname(), abilityname))
                return True
            return False 

        def UpdateLevel(self, level, updateMoves=True):
            self.Level = level
            self.Experience = self.CalculateAllExperienceNeededForLevel(level)
            if (updateMoves):
                self.Moves = GetMovesForLevel(self)
            self.RecalculateStats()

        def UpdateMoves(self, moves):
            self.Moves = []
            for move in moves:
                self.Moves.append(GetMove(move))

        def Heal(self):
            self.AdjustHealth(self.GetStat(Stats.Health), absolute = True)
            self.ClearStatus("All", all=True)
            for move in self.GetMoves():
                move.PP = move.MaxPP

        def GetAbility(self):
            ownability = self.Ability
            if (self.GetAbilityOverride() != None):
                ownability = self.GetAbilityOverride()
            tracedability = self.GetStatusCount(".tracing")
            alchemizedability = self.GetStatusCount("alchemized")
            if (alchemizedability != 0):
                ownability = alchemizedability
            if (tracedability != 0):
                ownability = tracedability
            if (self.HasStatus("worried")):
                ownability = "Insomnia"
            return ownability

        def GetAbilityOverride(self):
            if (not hasattr(self, 'AbilityOverride')):
                self.AbilityOverride = None
            return self.AbilityOverride

        def ChangeForme(self, formename, revert=False):
            if (formename == self.Id):
                revert = True
            if (revert):
                self.AbilityChanged = False
                self.FormeOverride = None
                self.AbilityOverride = None
            elif (isinstance(formename, float) or isinstance(formename, int)):
                self.FormeOverride = formename
                oldabilityslot = GetAbilities(self.Id).index(self.Ability)
                self.AbilityOverride = GetAbilities(self.GetId())[min(oldabilityslot, len(GetAbilities(self.GetId())) - 1)]
                self.AbilityChanged = True
            elif (formename == "Minior (Red Core)"):
                self.Image = "Pokemon/774-red.webp"
            elif (formename == "Minior (Orange Core)"):
                self.Image = "Pokemon/774-orange.webp"
            elif (formename == "Minior (Yellow Core)"):
                self.Image = "Pokemon/774-yellow.webp"
            elif (formename == "Minior (Green Core)"):
                self.Image = "Pokemon/774-green.webp"
            elif (formename == "Minior (Blue Core)"):
                self.Image = "Pokemon/774-blue.webp"
            elif (formename == "Minior (Indigo Core)"):
                self.Image = "Pokemon/774-indigo.webp"
            elif (formename == "Minior (Violet Core)"):
                self.Image = "Pokemon/774-violet.webp"
            elif (formename == "Wishiwashi (School Form)"):
                self.Image = "Pokemon/746-schooling.webp"
            elif (formename == "Castform (Rainy Form)"):
                self.FormeOverride = 351.2
            elif (formename == "Castform (Sunny Form)"):
                self.FormeOverride = 351.1
            elif (formename == "Castform (Snowy Form)"):
                self.FormeOverride = 351.3
            elif (formename == "Castform (Normal)"):
                self.FormeOverride = 351
            elif (formename == "Darmanitan (Standard Mode)"):
                self.FormeOverride = 555
            elif (formename == "Darmanitan (Zen Mode)"):
                self.FormeOverride = 555.1
            elif (formename == "Burmy (Plant Cloak)"):
                self.FormeOverride = 412
            elif (formename == "Burmy (Sandy Cloak)"):
                self.FormeOverride = 412.1
            elif (formename == "Burmy (Trash Cloak)"):
                self.FormeOverride = 412.2
            elif (formename == "Rotom (Rotom)"):
                self.FormeOverride = 479
            elif (formename == "Rotom (Heat Rotom)"):
                self.FormeOverride = 479.1
            elif (formename == "Rotom (Wash Rotom)"):
                self.FormeOverride = 479.2
            elif (formename == "Rotom (Frost Rotom)"):
                self.FormeOverride = 479.3
            elif (formename == "Rotom (Fan Rotom)"):
                self.FormeOverride = 479.4
            elif (formename == "Rotom (Mow Rotom)"):
                self.FormeOverride = 479.5
            else:
                self.Image = None

            self.RecalculateStats(False)

            if (math.floor(self.GetId()) == 479):# rotom move changes
                removemove = None
                oldpp = -1
                for move in self.GetMoves():
                    if (move.Name in ["Air Slash", "Leaf Storm", "Overheat", "Hydro Pump", "Blizzard"]):
                        removemove = move
                        oldpp = removemove.PP
                        self.Moves.remove(removemove)
                        break
                if (self.Moves == []):
                    self.LearnNewMove([(0, "Thunder Shock")])
                if (self.GetId() == 479.1):
                    self.LearnNewMove([(0, "Overheat")])
                elif (self.GetId() == 479.2):
                    self.LearnNewMove([(0, "Hydro Pump")])
                elif (self.GetId() == 479.3):
                    self.LearnNewMove([(0, "Blizzard")])
                elif (self.GetId() == 479.4):
                    self.LearnNewMove([(0, "Air Slash")])
                elif (self.GetId() == 479.5):
                    self.LearnNewMove([(0, "Leaf Storm")])
                if (oldpp != -1):
                    self.GetMoves()[len(self.GetMoves()) - 1].PP = oldpp

            return "{} changed forme!".format(self.GetNickname())

        def GetImage(self):
            seminvuls = ["diving", "airborne", "ethereal", "dug in"]
            for status in seminvuls:
                if (self.HasStatus(status)):
                    return "GFX/empty.png"
            if (self.HasStatus("substitute")):
                return "Pokemon/substitute.webp"
            if (self.Image == None):
                if (self.GetId() == 845):#cramorant's two forms
                    if (self.HasStatus("gulping")):
                        return "Pokemon/845.1.webp"
                    elif (self.HasStatus("gorging")):
                        return "Pokemon/845.2.webp"
                elif (self.Id == 25.2):
                    return "Pokemon/25.2.webp" 
                return "Pokemon/" + str(self.GetId()) + ".webp"
            else: 
                return self.Image

        def GetMiniorForme(self):
            if (self.Personality < 1.0/7.0):
                return "Minior (Red Core)"
            elif (self.Personality < 2.0/7.0):
                return "Minior (Orange Core)"
            elif (self.Personality < 3.0/7.0):
                return "Minior (Yellow Core)"
            elif (self.Personality < 4.0/7.0):
                return "Minior (Green Core)"
            elif (self.Personality < 5.0/7.0):
                return "Minior (Blue Core)"
            elif (self.Personality < 6.0/7.0):
                return "Minior (Indigo Core)"
            else:
                return "Minior (Violet Core)"

        def GetExperience(self):
            if (not hasattr(self, 'Experience')):
                self.Experience = self.CalculateAllExperienceNeededForLevel(self.Level)
            return (self.Experience if self.Experience != None else CalculateAllExperienceNeededForLevel(self.GetLevel()))

        def GetTrainer(self):
            return self.Owner

        def GetTrainerType(self):
            return self.TrainerType

        def PlayCry(self):
            if renpy.exists("Pokemon/Cries/{}.wav".format(self.GetId())):
                PlaySound("Pokemon/Cries/{}.wav".format(self.GetId()), otherchannel="altcry")
            else:
                PlaySound("Pokemon/Cries/{}.wav".format(math.floor(self.GetId())), otherchannel="altcry")

        def GetVicTouched(self):
            return self.vic_touched

        def SetVicTouched(self, level_add=0):
            self.vic_touched = level_add
            self.Level = self.Level + level_add
            self.RecalculateStats()

        def ResetVicTouched(self):
            self.Level = self.Level - self.vic_touched
            self.vic_touched = 0
            self.RecalculateStats()
            self.LevelUp(self)