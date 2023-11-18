label Battle(trainers, currentWeather=None, customexpressions=[], reanchor=[], uniforms=[], clearstats=True, gainexp=True, healParty=True, specialmusic=None, unrunnable=False, levelscale=None, stopmusic=True, lockbag=False, dialogfunc=None, custombrain=None, catchable=True, victiniwatch=False):
$ renpy.transition(dissolve)
call clearscreens from _call_clearscreens
python:
    if (renpy.in_rollback()):
        renpy.rollback(True)
    inbattle = True
    renpy.suspend_rollback(True)
    _rollback = False
    hidebattleui = False
    Trainers = trainers#[Trainer Class]
    ActionLog = []#[Action]
    CurrentActions = []#[Action] - after these are executed, put them in ActionLog
    CurrentWeather = currentWeather#None or (string, int)
    FriendlyEffects = {}#[Effect] - Includes hazards, reflect, whirlpool, etc.
    EnemyEffects = {}#[Effect]
    BattlefieldEffects = {}#[Effect] - Includes stuff like trick room, terrains, and the increasing power of echoed voice
    Turn = 0
    StopMusic = stopmusic
    
    UsingMove = False
    MoveUser = None
    ActiveMove = None
    BeginningEffects = False
    GainExp = gainexp
    BattlerIndex = 0
    FaintedMons = []
    Fled = False
    Unrunnable = unrunnable
    terabuttontext = "Terastalize"

    if (levelscale != None):
        Trainers = copy.deepcopy(trainers)
        for trainer in Trainers:
            for mon in trainer.GetTeam():
                mon.Level = levelscale
                mon.RecalculateStats()

    playerteamnames = []
    enemyteamnames = []
    pkmnnames = []
    WildBattle = True
    GimmickCost = 1 

    AssignOwners()# sets a bunch of battle variables of the 'mons
    for trainer in Trainers:
        for mon in trainer.GetTeam():
            if (clearstats):
                mon.ResetStatChanges()
            if (healParty):
                mon.Health = mon.GetStat(Stats.Health)
                mon.ClearStatus(None, all = True)
            if (mon.GetHealthPercentage() <= 0):
                FaintedMons.append(mon)
        trainer.ReorderTeam()
        if (trainer.GetType() != TrainerType.Enemy):
            playerteamnames.append(trainer.GetName())
        else:
            if (not trainer.GetIsPokemon()):
                WildBattle = False
            enemyteamnames.append(trainer.GetName())
        if (trainer.GetIsPokemon()):
            pkmnnames.append(trainer.GetName())        
    
    if (specialmusic != "Nothing"):
        renpy.music.stop()
        renpy.music.stop(channel="crowd")
        renpy.music.stop(channel="crowd2")
        if (specialmusic == None):
            renpy.music.queue("Audio/Music/KantoTrainerStart_Rock.ogg", channel='music', loop=None, fadein=1.0, tight=None)
            renpy.music.queue("Audio/Music/KantoTrainerLoop_Rock.ogg", channel='music', loop=True)
        elif (WildBattle):
            renpy.music.queue("Audio/Music/RBY_Pokemon_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
            renpy.music.queue("Audio/Music/RBY_Pokemon_Loop.ogg", channel='music', loop=True)
        elif (len(specialmusic) == 2):
            renpy.music.queue(specialmusic[0], channel='music', loop=None, fadein=1.0, tight=None)
            renpy.music.queue(specialmusic[1], channel='music', loop=True)
        else:
            renpy.music.queue(specialmusic, channel='music', loop=None, fadein=1.0, tight=None) 

call CreateSplash(playerteamnames, enemyteamnames, customexpressions, reanchor, uniforms, pkmnnames) from _call_CreateSplash

if victiniwatch is True:
    show victini neutral:
        xpos 0.1 ypos 0.6 zoom 0.85
        parallel:
            ease 0.18 ypos .6
            ease 0.18 ypos .59
            ease 0.18 ypos .6
            ease 0.18 ypos .61
            repeat
    $ renpy.music.set_volume(0.5, delay=0.0, channel="music")
    $ PlaySound("Pokemon/Cries/494.wav", otherchannel="altcry")
    #$ renpy.sound.queue("audio/Pokemon/Cries/494.wav", channel='sound', loop=False, tight=None)
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

label Start:
while (Turn == 0 or not BattleOver()):
    python:
        random.seed()
        MultihitCount = None
        MultihitMax = None
        UsedEchoedVoice = False
        CurrentActions = []
        ItemText = ""
        SwappingInMon = []
    if (not renpy.get_screen("Battle")):
        show screen battle

    python:
        if (not BeginningEffects):
            for mon in Battlers(True):
                mon.SetDamagedThisTurn(False)
                SwitchInEffects(mon, False, True)
                FormeChanges(mon)
            BeginningEffects = True
        if (dialogfunc != None):
            dialogfunc("BeforeBattle")
        if (Turn == 0):
            Turn = 1

    label ChooseStart:
    $ BattlerIndex = len(CurrentActions)
    while BattlerIndex < len(FriendlyBattlers()):
        hide screen battle
        python:
            mon = FriendlyBattlers()[BattlerIndex]

            skipchoices = False
            statuses = {
                "ice ball": ["Ice Ball"],
                "rollout": ["Rollout"],
                "thrashing": ["Thrash"],
                "outraged": ["Outrage"],
                "dug in": ["Dig"],
                "diving": ["Dive"],
                "airborne": ["Fly", "Bounce"],
                "ethereal": ["Phantom Force"],
                "cloaked in light": ["Sky Attack"],
                "charging light": ["Solar Beam"],
                "hardheaded": ["Skull Bash"],
                "whipping up winds": ["Razor Wind"],
                "petal dancing": ["Petal Dance"]
            }

            for status, move_names in statuses.items():
                if mon.HasStatus(status):
                    skipchoices = True
                    lastmove = GetLastMove(ActionLog, mon, lookformoves=move_names, returnaction=True)
                    lasttarget = lastmove.GetTargets()[0]
                    if lasttarget not in Battlers():
                        lasttarget = GetTargets(mon, GetMoveRange(lastmove.Move), True)[min(len(GetTargets(mon, GetMoveRange(lastmove.Move), True)) - 1, lastmove.GetTargetSlots()[0])]
                    CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, GetMove(lastmove.Move.Name), [lasttarget.GetTrainer()], [lasttarget], Turn))

        if (not mon.HasStatus("recharging") and not skipchoices):
            show screen battle

            python:
                createmegaitem = None
                
                if (mon.GetItem() == None):
                    for fvl in mon.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                            createmegaitem = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[0]

                    if (createmegaitem != None):
                        mon.GiveItem(createmegaitem)
                        if (mon.GetItem() == createmegaitem):
                            renpy.say(None, "{}'s wishes coalesced into a {}!".format(mon.GetNickname(), createmegaitem))

                battleCommand = renpy.call_screen("battle", currentMon=mon)

            if (battleCommand == 'tera'):
                if (mon.IsTerad()):
                    $ mon.Terastalized = -1
                else:
                    $ mon.Terastalized = Turn
                jump ChooseStart
            elif (battleCommand == 'lib'):
                if (mon.GetId() == 25):
                    call dawnpikachudialog6 from _call_dawnpikachudialog6
                else:
                    label newbanner:
                    narrator "What color will your banner be?"

                    $ renpy.call_screen("liberize")

                    if (len(libtypes) == 0):
                        narrator "You must pick a banner to fly! Liberation has no room for bystanders!"

                        jump newbanner

                    $ types = libtypes[0]
                    if (len(libtypes) == 2):
                        $ types = libtypes[0] + "/" + libtypes[1]

                    narrator "Do you want to raise up the banner of the [types]-type?"

                    menu:
                        "Let me fight for another cause.":
                            jump newbanner

                        "Raise it high!":
                            pass

                jump ChooseStart
            elif (battleCommand == 'div'):
                python:
                    forms = []
                    for fvl in mon.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
                            forms = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)
                    numdiv = 0
                    for othermon in PlayerBattlers():
                        if ((othermon.HasStatus("mega evolved") or othermon.HasStatus("diveralized") or othermon.HasStatus("minigigamaxed")) and othermon != mon):
                            numdiv += 1
                    if ((GimmickCost - numdiv) <= 0):
                        renpy.say(None, "The power of the Foreverals has been expended for this battle...")
                    elif (mon.GetId() == forms[0]):
                        mon.ChangeForme(forms[1])
                        mon.ApplyStatus("diveralized")
                    elif (mon.GetId() == forms[1]):
                        mon.ClearStatus("diveralized")
                        mon.ChangeForme(None, revert=True)
                    else:
                        mon.ChangeForme(forms[0])
                        mon.ApplyStatus("diveralized")
                jump ChooseStart
            elif (battleCommand == 'mega'):
                python:
                    megaid = None
                    for fvl in mon.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                            megaid = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[1]
                    numdiv = 0
                    for othermon in PlayerBattlers():
                        if ((othermon.HasStatus("mega evolved") or othermon.HasStatus("diveralized") or othermon.HasStatus("minigigamaxed")) and othermon != mon):
                            numdiv += 1
                    if ((GimmickCost - numdiv) <= 0):
                        renpy.say(None, "The power of the Foreverals has been expended for this battle...")
                    elif (mon.GetId() != megaid):
                        mon.ChangeForme(megaid)
                        mon.ApplyStatus("mega evolved")
                    else:
                        mon.ClearStatus("mega evolved")
                        mon.ChangeForme(None, revert=True)
                jump ChooseStart
            elif (battleCommand == 'giga'):
                python:
                    megaid = None
                    for fvl in mon.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Mega):
                            megaid = lookupforeveraldata(fvl, FVLMacros.FVLTypeData)[1]
                    numdiv = 0
                    for othermon in PlayerBattlers():
                        if ((othermon.HasStatus("mega evolved") or othermon.HasStatus("diveralized") or othermon.HasStatus("minigigamaxed")) and othermon != mon):
                            numdiv += 1
                    if ((GimmickCost - numdiv) <= 0):
                        renpy.say(None, "The power of the Foreverals has been expended for this battle...")
                    elif (mon.GetId() != megaid):
                        mon.ChangeForme(megaid)
                        mon.ApplyStatus("minigigamaxed")
                    else:
                        mon.ClearStatus("minigigamaxed")
                        mon.ChangeForme(None, revert=True)
                jump ChooseStart
            elif (battleCommand == 'fight'):
                $ moveCommand = renpy.call_screen("moves", mon)
                if (moveCommand == 'back'):
                    jump ChooseStart
                elif (moveCommand == 'Struggle'):
                    $ foe = GetRandomAdjacentFoe(mon)
                    $ CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, struggle, [foe.GetTrainer()], [foe], Turn))
                else:
                    $ moveselected = mon.GetMove(moveCommand)
                    if (not MoveValid(mon, moveselected)):
                        $ renpy.say(None, "Can't use that!")
                        jump ChooseStart
                    $ targetFoes = GetTargets(mon, GetMoveRange(moveselected))
                    if (len(GetTargets(mon, GetMoveRange(moveselected))) > 1 and (GetMoveRange(moveselected) == Range.AnyOrSelf or len(Battlers()) > 2)):
                        $ targetFoes = renpy.call_screen("choosetarget", moveselected, mon)
                        if (targetFoes == 'back'):
                            jump ChooseStart
                    $ CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, moveselected, GetTrainers(targetFoes), targetFoes, Turn))    
            elif (battleCommand == 'bag'):
                python:
                    if (not lockbag):
                        if (mon.GetTrainerType() == TrainerType.Player):
                            if (len(inventory.keys()) > 0):
                                if (not renpy.get_screen("inventory")):
                                    itemuse = renpy.call_screen("inventory")
                                    activeitem = itemuse
                                    targetFoes = []
                                    if (itemuse == "Back"):
                                        renpy.jump("ChooseStart")
                                    elif (InventoryCategory(itemuse) == "Poké Balls"):
                                        targetFoes = [EnemyBattlers()[0]]
                                        if (len(EnemyBattlers()) != 1):
                                            targetFoes = renpy.call_screen("choosetarget", Range.Any, mon)
                                        if (len(playerparty) == 6 and IsBefore(17, 4, 2004)):
                                            renpy.say(None, "Your party is full, and you don't have anywhere to send your extra Pokémon yet!")
                                            renpy.jump("ChooseStart")
                                        if (not targetFoes[0].GetTrainer().GetIsPokemon()):
                                            renpy.say(None, "You can't catch an opponent's Pokémon! You don't even have a Snag Machine!")
                                            renpy.jump("ChooseStart")
                                    else:
                                        if (not TrainerItem(itemuse)):
                                            targetFoes = renpy.call_screen("switch", mon.GetTrainer())
                                            targetFoes = mon.GetTrainer().GetTeam()[targetFoes]
                                            if (targetFoes == "back"):
                                                renpy.jump("ChooseStart")
                                        if (not UseItem(targetFoes, True, True) or (not TrainerItem(itemuse) and targetFoes.HasStatus("embargoed"))):
                                            if (TrainerItem(itemuse)):
                                                renpy.say(None, "You can't use that item right now!")
                                            else:
                                                renpy.say(None, "You can't use that item on that Pokémon!")
                                            renpy.jump("ChooseStart") 
                                        targetFoes = [targetFoes]

                                    CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Bag, mon.GetTrainer(), mon, itemuse, GetTrainers(targetFoes), targetFoes, Turn))

                            else:
                                renpy.say(None, "You have no items in your bag!")
                                renpy.jump("ChooseStart")
                        else:
                            renpy.say(None, "Only you can reach into your bag!")
                            renpy.jump("ChooseStart")
                    else:
                        renpy.say(None, "You can't use your bag right now!")
                        renpy.jump("ChooseStart")
            elif (battleCommand == 'pokemon'):
                $ ShowBattleUI()
                label Switching:
                    python:
                        if (CanSwitch(mon, False)):
                            hideback = False
                            mustswitch = False
                            switchCommand = renpy.call_screen('switch', mon.GetTrainer())
                            if (switchCommand == 'back'):
                                renpy.jump("ChooseStart")
                            newPokemon = mon.GetTrainer().GetTeam()[switchCommand]
                            if (newPokemon.GetHealth() == 0):
                                renpy.say(None, "{} has fainted, and cannot fight!".format(newPokemon.GetNickname()))
                                renpy.jump("Switching")
                            elif (newPokemon in Battlers()):
                                renpy.show_screen("battleui")
                                renpy.say(None, "{} is already in battle!".format(newPokemon.GetNickname()))
                                renpy.jump("Switching")
                            elif (newPokemon in SwappingInMon):
                                renpy.show_screen("battleui")
                                renpy.say(None, "{} is already switching in!".format(newPokemon.GetNickname()))
                                renpy.jump("Switching")
                            SwappingInMon.append(newPokemon)
                            CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Pokemon, mon.GetTrainer(), mon, None, [mon.GetTrainer()], [newPokemon], Turn))
                        else:
                            renpy.say(None, "{} cannot switch out!".format(mon.GetNickname()))
                            renpy.jump("ChooseStart")
            elif (battleCommand == 'run'):
                $ ShowBattleUI()
                if (Unrunnable):
                    "You can't run from this battle!"
                elif (WildBattle):
                    $ CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Run, mon.GetTrainer(), mon, None, [mon.GetTrainer()], [mon], Turn))
                else:
                    "No! There's no running from a trainer battle!"
                hide screen battleui
                jump ChooseStart        
            elif (battleCommand == 'back'):
                $ removeditem = CurrentActions.pop()
                if (removeditem.GetActionType() == ActionTypes.Pokemon):
                    $ SwappingInMon.remove(removeditem.GetTargets()[0])
                jump ChooseStart

        
        $ BattlerIndex += 1

    python:
        for mon in PlayerBattlers():
            if (mon.HasStatus("diveralized") or mon.HasStatus("mega evolved") or mon.HasStatus("minigigamaxed")):
                GimmickCost -= 1

        #FIX THIS: this is the opponent's logic. Beef this up.
        for mon in EnemyBattlers():
            validmoves = GetValidMoves(mon)

            if (custombrain == None):
                besttarget = -1
                if ((mon.GetTrainer().GetIsPokemon() or mon.GetIntelligence() == 0) and not testbattle):
                    movechosen = random.choice(validmoves)
                else:
                    bestactions = RankTargets(mon)
                    besttarget = bestactions[0][0]
                    movechosen = bestactions[0][1]
                
                moverange = GetMoveRange(movechosen)
                targets = GetTargets(mon, moverange, True)
                
                if (not (moverange == Range.AllAdjacentFoes
                    or moverange == Range.AllAdjacent
                    or moverange == Range.AllAllies 
                    or moverange == Range.AllFoes
                    or moverange == Range.All
                    or moverange == Range.AllAlliesAndSelf
                    or len(targets) == 0)):
                        if (besttarget != -1):
                            targets = [besttarget]
                        else:
                            targets = [random.choice(targets)]

                CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, movechosen, GetTrainers(targets), targets, Turn))

            else:
                brainresults = custombrain(mon)# generates a tuple with the move's string, and a list of the targets' objects
                movechosen = mon.GetMoveByName(brainresults[0])
                targets = brainresults[1]

                if (movechosen == None):#this is an item
                    CurrentActions.append(Action(6, mon.GetStat(Stats.Speed), ActionTypes.Bag, mon.GetTrainer(), mon, brainresults[0], GetTrainers(targets), targets, Turn))
                elif (movechosen.PP == 0):
                    movechosen = random.choice(GetValidMoves(mon))
                    moverange = GetMoveRange(movechosen)
                    targets = GetTargets(mon, moverange, True)

                    if (not (moverange == Range.AllAdjacentFoes
                        or moverange == Range.AllAdjacent
                        or moverange == Range.AllAllies 
                        or moverange == Range.AllFoes
                        or moverange == Range.All
                        or moverange == Range.AllAlliesAndSelf
                        or len(targets) == 0)):
                            targets = [random.choice(targets)]
                else:

                    CurrentActions.append(Action(0, mon.GetStat(Stats.Speed), ActionTypes.Move, mon.GetTrainer(), mon, movechosen, GetTrainers(targets), targets, Turn))

            #newmon = mon.GetTeam()[random.randint(0, len(mon.GetTeam()) - 1)]
            #CurrentActions.append(Action(1, mon.GetStat(Stats.Speed), ActionTypes.Pokemon, mon.GetTrainer(), mon, None, newmon.GetTrainer(), [newmon], Turn))
        roundsadjusted = False
        for action in CurrentActions:
            if (action.GetActionType() == ActionTypes.Move):
                moveselected = action.GetMove()
                user = action.GetUser()
                if (user.HasAbility("Stall")):
                    action.ChangePriority(-0.5)
                if (moveselected.Category == "Status" and user.HasAbility("Prankster")):
                    action.ChangePriority(1)
                    user.ApplyStatus("pranking")
                if (IsHealingMove(moveselected) and user.HasAbility("Triage")):
                    action.ChangePriority(3)
                if (moveselected.Type == "Flying" and user.GetHealthPercentage() >= 1.0 and user.HasAbility("Gale Wings")):
                    action.ChangePriority(1)
                if (moveselected.Name in ["Whirlwind", "Roar", "Teleport", "Dragon Tail", "Circle Throw"]):
                    action.ChangePriority(-6)
                elif (moveselected.Name in ["Counter", "Mirror Coat"]):
                    action.ChangePriority(-5)
                    if (moveselected.Name == "Counter"):
                        user.ApplyStatus(".countering", None)
                    else:
                        user.ApplyStatus(".mirrorcoat", None)
                elif (moveselected.Name in ["Revenge", "Avalanche"]):
                    action.ChangePriority(-4)
                elif (moveselected.Name in "Focus Punch"):
                    action.ChangePriority(-3)
                elif (moveselected.Name in ["Slow Freeze"]):
                    action.ChangePriority(-1)
                elif (moveselected.Name in ["Bullet Punch", "Quick Attack", "Bide", "Baby-Doll Eyes", "Ice Shard", "Vacuum Wave", "Shadow Sneak", "Water Shuriken", "Legacy", "Mach Punch", "Disabling Poke", "Accelerock", "Sucker Punch", "Aqua Jet", "Ion Deluge"]):
                    action.ChangePriority(1)
                elif (moveselected.Name in ["Feint", "First Impression", "Extreme Speed", "Ally Switch"]):
                    action.ChangePriority(2)
                elif (moveselected.Name in ["Fake Out", "Wide Guard", "Quick Guard"]):
                    action.ChangePriority(3)
                elif (moveselected.Name in ["Snatch", "Endure", "Protect", "Obstruct", "Detect", "Enshroud", "Splinter Shield", "Deathless", "Silk Trap", "Baneful Bunker", "Magic Coat"]):
                    action.ChangePriority(4)
                elif (moveselected.Name in ["Helping Hand"]):
                    action.ChangePriority(5)
                elif (moveselected.Name == "Pursuit"):
                    targetswitching = False
                    for foeaction in CurrentActions:
                        if (foeaction.GetActionType() == ActionTypes.Pokemon and foeaction.GetUser() in action.GetTargets()):
                            action.SetPriority(7)
                            user.ApplyStatus("pursuing")
                elif (moveselected.Name == "Round" and not roundsadjusted):
                    roundsadjusted = True
                    firstround = -1
                    for action in CurrentActions:
                        if (action.GetActionType() == ActionTypes.Move and action.GetMove().Name == "Round"):
                            if (firstround == -1):
                                action.ChangePriority(0.1)
                                firstround = CurrentActions.index(action)
                            else:
                                action.SetSpeed(CurrentActions[firstround].GetSpeed() + action.GetSpeed() / 1000.0)
                elif (moveselected.Name == "Liberage"):
                    action.ChangePriority(1776)#AMMMMMMMEEEEERICCCCAAAA!

        CurrentActions.sort(key=(lambda entry : (-entry.GetPriority(), -entry.GetSpeed())))
       
        if (dialogfunc != None):
            dialogfunc("PreStep")
        for action in CurrentActions:
            if (action.GetUser().GetAbilityChanged()):
                text = ReactivateAbility(action.GetUser())
                if (text != ""):
                    renpy.show_screen("battleui")
                    renpy.say(None, text)
        for action in CurrentActions:
            PerformAction(action)
            BattleCheck()
            ActionLog.append(action)
        CurrentActions = []
        DoEffects()
        BattleCheck()
        DoBattlefieldEffects()
        BattleCheck()
        Turn += 1
        if (dialogfunc != None):
            dialogfunc("PostTurn")
        
label endbattle:
if (StopMusic):
    stop music fadeout 2.0
if (Fled):
    $ IsWinner = False
    $ wildcount = 0
    "You ran away!"
else:
    $ IsWinner = PlayerWon()
    if (IsWinner):
        if (WildBattle):
            $ wildcount += 1
        "You win!"
    else:
        "You lose!"
        $ wildcount = 0

        if (WildBattle):
            $ moneylost = math.floor(money / 10.0)
            $ money -= moneylost
            
            "You lost $[moneylost] in your panicked escape!"
        
        else:
            if (GainExp):
                "Because of the difficult battle, your team gained extra experience!"

                python:
                    bonusexperience = 0

                    highestlevel = 0
                    highestmon = None
                    for mon in PlayerPokemon():
                        if (mon.GetLevel() > highestlevel):
                            highestmon = mon
                            highestlevel = mon.GetLevel()

                    lowestlevel = 101
                    lowestmon = None
                    for mon in EnemyPokemon():
                        if (mon.GetLevel() < lowestlevel):
                            lowestmon = mon
                            lowestlevel = mon.GetLevel()
                    
                    bonusexperience = math.ceil(lowestmon.CalculateGivingExperience(highestmon) * 3.0)

                    for trainer in Trainers:
                        if (trainer.GetType() == TrainerType.Player):
                            for mon in trainer.GetTeam():
                                mon.GainExperience(bonusexperience, True)

hide screen battleui
hide screen battle
hide blank2
with Dissolve(0.5)

if (not renpy.get_screen("currentdate")):
    $ renpy.transition(dissolve)
    show screen currentdate

python:
    for mon in playerparty:
        if (mon.GetCaught() > 0):
            mon.AdjustHealth(mon.GetCaught(), absolute=True)
            mon.ResetCaught()
        if (mon.GetStartingItem() != None and "Berry" not in mon.GetStartingItem()):
            mon.Item = mon.GetStartingItem()
        if (mon.HasStatus("mega evolved") or mon.HasStatus("minigigamaxed")):
            mon.ClearStatus("mega evolved")
            mon.ClearStatus("minigigamaxed")
            mon.ChangeForme(None, revert=True)
        mon.ClearStatus("volatiles", volatiles=True)
        if (mon.GetItem() != None and (mon.GetItem()[-3:] == "ite" or "Minigiga" in mon.GetItem())):
            mon.Item = None
    activeitem = None
    renpy.suspend_rollback(False)
    renpy.block_rollback()
    _rollback = True
    inbattle = False
return IsWinner 

label losebattle:
return False

### Helper Functions ###
init python:
    def ApplyEffect(mon, effect, effectvalue, onfoe):
        effectdict = None
        words = "The opponent's"
        if (not onfoe):
            words = "The allied"

        if (mon.GetTrainerType() == TrainerType.Enemy):
            if (onfoe):
                effectdict = FriendlyEffects
            else:
                effectdict = EnemyEffects
        else:
            if (onfoe):
                effectdict = EnemyEffects
            else:
                effectdict = FriendlyEffects
        if (effect in effectdict):
            return "But it failed!"
        else:
            effectdict[effect] = effectvalue
            return "{} team came under the effect of {}!".format(words, effect)

    def ShowBattleUI():
        if (not renpy.get_screen("battlui")):
            renpy.show_screen("battleui")

    def BattleCheck():
        if (BattleOver()):
            renpy.jump("Start")

    def SwitchInEffects(mon, returntext=False, firstturn=False):
        mon.PlayCry()
        returnmessage = ""
        mon.SetTurnSwitchedIn(Turn)
        if (not firstturn):
            mon.ResetStatChanges()

        foreveralstab = False
        for fvl in mon.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.TurnStartStatus):
                returnmessage += mon.GetNickname() + "'s wishes coalesced! The " + fvl + " activated! "
                for effect in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                    returnmessage += mon.ApplyStatus(effect)

        returnmessage += ReactivateAbility(mon)

        if (mon.HasNormalStatus() and mon.HasAbility("Natural Cure")):
            mon.ClearStatus(None, all=True)            

        if (EffectOnOwnField(mon, "healing wish") 
            and GetBattlers(mon).index(mon) == GetFieldEffects(mon)["healing wish"]
            and (mon.GetHealthPercentage < 1 or mon.HasNormalStatus())):
            del GetFieldEffects(mon)["healing wish"]
            mon.AdjustHealth(mon.GetStat(Stats.Health))
            mon.ClearStatus(None, all=True)

        if (mon.HasStatus("badly poisoned")):
            mon.Status["badly poisoned"] = 1

        if (EffectOnOwnField(mon, "sticky web") and IsGrounded(mon)):
            returnmessage += "{} became tangled in the sticky webs! {}".format(mon.GetNickname(), mon.ChangeStats(Stats.Speed, -1))
        if (EffectOnOwnField(mon, "toxic spikes") and IsGrounded(mon)):
            if (mon.HasType("Poison")):
                del GetFieldEffects(mon)["toxic spikes"]
                returnmessage += "{} absorbed the toxic spikes!".format(mon.GetNickname())
            elif (GetFieldEffects(mon)["toxic spikes"] == 1):
                returnmessage += "{} landed on the toxic spikes! {}" .format(mon.GetNickname(), mon.ApplyStatus("poisoned", 1, mon))
            elif (GetFieldEffects(mon)["toxic spikes"] == 2):
                returnmessage += "{} landed on the toxic spikes! {}" .format(mon.GetNickname(), mon.ApplyStatus("badly poisoned", 1, mon))
        if (EffectOnOwnField(mon, "spikes") and IsGrounded(mon)):
            if (GetFieldEffects(mon)["spikes"] == 1):
                mon.AdjustHealth(-mon.GetStat(Stats.Health) * 1/8.0)
            elif (GetFieldEffects(mon)["spikes"] == 2):
                mon.AdjustHealth(-mon.GetStat(Stats.Health) * 1/6.0)
            elif (GetFieldEffects(mon)["spikes"] == 3):
                mon.AdjustHealth(-mon.GetStat(Stats.Health) * 1/4.0)
            returnmessage += "{} landed on the spikes!".format(mon.GetNickname())
        if (EffectOnOwnField(mon, "stealthy rocks")):
            typebonus = 1.0
            for type in mon.GetTypes():                
                typebonus *= GetEffectiveness("Rock", type)
            mon.AdjustHealth(-mon.GetStat(Stats.Health) * 0.125 * typebonus)
            returnmessage += "{} landed on the sharp rocks!".format(mon.GetNickname())

        for othermon in Battlers():
            if (othermon.HasStatus("wrapped") and othermon.GetStatusCount(".wrappedby") not in Battlers()):
                othermon.ClearStatus("wrapped")
            if (othermon.HasStatus("firespun") and othermon.GetStatusCount(".firespunby") not in Battlers()):
                othermon.ClearStatus("firespun")
            if (othermon.HasStatus("whirlpooled") and othermon.GetStatusCount(".whirlpooledby") not in Battlers()):
                othermon.ClearStatus("whirlpooled")
            if (othermon.HasStatus("bound") and othermon.GetStatusCount(".boundby") not in Battlers()):
                othermon.ClearStatus("bound")
            if (othermon.HasStatus("clamped") and othermon.GetStatusCount(".clampedby") not in Battlers()):
                othermon.ClearStatus("clamped")
            if (othermon.HasStatus("infested") and othermon.GetStatusCount(".infestedby") not in Battlers()):
                othermon.ClearStatus("infested")
            if (othermon.HasStatus("entombed") and othermon.GetStatusCount(".entombedby") not in Battlers()):
                othermon.ClearStatus("entombed")
            if (othermon.HasStatus("anchored") and othermon.GetStatusCount("anchored") not in Battlers()):
                othermon.ClearStatus("anchored")

        if (returntext):
            return returnmessage
        elif (returnmessage != ""):
            renpy.say(None, returnmessage)

    def AdjustPokemon(mon):
        trainer = mon.GetTrainer()
        if (trainer.GetType() != TrainerType.Enemy):
            if victiniwatch is True:
                renpy.show("victini sad")
            newstarters = trainer.GetTeam()[:trainer.GetNumber()]
            replacements = [newmon for newmon in trainer.GetUnfaintedTeam() if newmon not in FriendlyBattlers()]
            switched = False
            while (not switched and len(replacements) > 0):
                switchindex = renpy.call_screen("switch", trainer)
                if (switchindex == "back"):
                    renpy.say(None, "You must select a Pokémon!")
                elif (trainer.GetTeam()[switchindex].GetHealthPercentage() <= 0.0):
                    renpy.say(None, "That Pokémon cannot fight!")
                elif (trainer.GetTeam()[switchindex] in Battlers()):
                    renpy.say(None, "That Pokémon is already in battle!")
                else:
                    switched = True
                    newmon = trainer.GetTeam()[switchindex]
                    trainer.ShiftTeam(trainer.GetTeam().index(mon), switchindex, True)
                    renpy.say(None, "{} switched out, and {} switched in!".format(mon.GetNickname(), newmon.GetNickname()))
                    SwitchInEffects(newmon)
                replacements = [newmon for newmon in trainer.GetUnfaintedTeam() if newmon not in FriendlyBattlers()]
        else:
            if victiniwatch is True:
                if Turn % 2 is 0:
                    renpy.show("victini happy")
                else:
                    renpy.show("victini exclaim")
            newstarters = trainer.GetTeam()[:trainer.GetNumber()]
            for i, mon in enumerate(newstarters):
                replacements = [newmon for newmon in trainer.GetUnfaintedTeam() if newmon not in EnemyBattlers()]
                if (mon.GetHealth() <= 0 and len(replacements) > 0):
                    newmon = random.choice(replacements)
                    trainer.ShiftTeam(i, trainer.GetTeam().index(newmon), True)
                    if (len(trainer.GetUnfaintedTeam()) >= trainer.GetNumber()):
                        renpy.say(None, "{} switched out, and {} switched in!".format(mon.GetNickname(), newmon.GetNickname()))
                        SwitchInEffects(newmon)

    def PerformAction(action):
        global Fled
        actionType = action.GetActionType()
        if (action.GetPerformed() or action.GetUser() != None and (action.GetUser().GetHealth() <= 0 or action.GetUser() not in Battlers())):
            action.ChangeSuccess(False)
            return
        if (actionType == ActionTypes.Move):
            DoMove(action, action.GetUser(), action.GetMove(), action.GetTargets())

            if (dialogfunc != None):
                dialogfunc(["AfterMove", ("Ally" if action.GetUser().GetTrainerType() != TrainerType.Enemy else "Enemy")])

        elif (actionType == ActionTypes.Pokemon):
            swappingmon = action.GetUser()
            swappingmonslot = action.GetUserTrainer().GetTeam().index(swappingmon)
            partymon = action.GetTargets()[0]
            partymonslot = action.GetUserTrainer().GetTeam().index(partymon)
            if (CanSwitch(swappingmon, False)):
                action.GetUserTrainer().ShiftTeam(swappingmonslot, partymonslot)
                renpy.say(None, "{} switched in! ".format(partymon.GetNickname()) + SwitchInEffects(partymon, True))
            else:
                renpy.say(None, "{} cannot switch out!".format(swappingmon.GetNickname()))

        elif (actionType == ActionTypes.Bag):
            UseBattleItem(action)

            if (dialogfunc != None):
                dialogfunc(["UseItem", ("Ally" if action.GetUser().GetTrainerType() != TrainerType.Enemy else "Enemy"), action.GetMove()])

        elif (actionType == ActionTypes.Run):
            opponentspeed = 0
            for mon in EnemyBattlers():
                opponentspeed += mon.GetStat(Stats.Speed)

            selfspeed = 0
            for mon in FriendlyBattlers():
                selfspeed += mon.GetStat(Stats.Speed)
            
            odds = selfspeed / opponentspeed * 0.5

            if (action.GetUser().HasAbility("Run Away") or activerepel != None):
                odds = 1

            if (random.random() < odds):
                Fled = True
            else:
                renpy.say(None, "You failed to get away!")
        
        action.SetPerformed()

    def UseBattleItem(action):
        global activeitem
        global CritCaptures
        item = action.GetMove()
        if (not renpy.get_screen("battleui")):
            renpy.show_screen("battleui")
        if (InventoryCategory(item) == "Poké Balls"):
            target = action.GetTargets()[0]
            currenthp = target.Health

            if (random.random() > GetAverageProficiency() / 100.0 or GetRelationshipRank("Professor Cherry") == 0):
                maxhp = target.GetStat(Stats.Health, ignorepositive=True, ignorenegative=True, triggerAbilities=False)
                statbonus = 1.5 if target.HasStatus("poisoned") or target.HasStatus("burned") or target.HasStatus("paralyzed") or target.HasStatus("badly poisoned") else 1
                statbonus = 2.5 if target.HasStatus("asleep") or target.HasStatus("frozen") else statbonus
                ballbonus = 1
                if (item == "Great Ball"):
                    ballbonus = 1.5
                elif (item == "Ultra Ball"):
                    ballbonus = 2.0
                catchratio = ((maxhp * 3 - currenthp * 2) * 4096 * ((700 - pokedexlookup(target.Id, DexMacros.Total)) / 700) / (3 * maxhp) / 4096) * statbonus * ballbonus

                randnum = random.random()
                caught = catchratio / randnum

                if (item == "Master Ball"):
                    caught = 1

                target.Health = 0

                if (caught > 0.25):
                    renpy.say(None, "The {} {{w=0.5}}shakes...".format(item))

                if (caught > 0.5):
                    renpy.say(None, "The {} {{w=0.5}}shakes.".format(item))
                
                if (caught > 0.75):
                    renpy.say(None, "The {} {{w=0.5}}shakes!".format(item))

                if (caught < 1):
                    renpy.say(None, "The {} {{w=0.5}}{{nw}}".format(item))
                    target.Health = currenthp
                    renpy.say(None, "The {} {{fast}}breaks...".format(item))

                    for mon in FriendlyBattlers():
                        if (mon.GetItem() == None and mon.HasAbility("Ball Fetch")):
                            renpy.say(None, "{} fetched the {}!".format(mon.GetNickname(), item))
                            mon.GiveItem(item)
                            break
                else:
                    renpy.say(None, "The {} {{w=0.5}}clicks!".format(item))
                    target.MakeCaught(currenthp)
            else:#Kris' Kritical Kapture Korner
                target.Health = 0
                CritCaptures += 1
                renpy.say(None, "The {} {{w=0.5}}shakes...".format(item))

                renpy.say(None, "The {} {{w=0.5}}clicks!".format(item))

                renpy.say(None, "{b}A CRITICAL CAPTURE!{/b} You imagine Professor Cherry's proud grin.")

                if (CritCaptures == 1):
                    ValueChange("Professor Cherry", 3, 0.5)

                target.MakeCaught(currenthp)
            
            LoseItem(item)

        else:
            if (action.GetUser().GetTrainerType() == TrainerType.Player):
                if (item in inventory.keys()):
                    activeitem = item
                    if (UseItem(action.GetTargets()[0], False, True)):
                        if (TrainerItem(item)):
                            renpy.say(None, "You used the {}!".format(item))
                        else:
                            renpy.say(None, "You used the {} on {}!".format(item, action.GetTargets()[0].GetNickname()))
                        
                        inventory[item] -= 1

                    else:
                        renpy.say(None, "The {} would have no effect!".format(item))

                    if (inventory[item] <= 0):
                        del inventory[item]

                else:
                    preposition = "a"
                    if (item[0].lower() in ["a", "e", "i", "o", "u"]):
                        preposition += "n"
                    renpy.say(None, "You don't have {} {} to use!".format(preposition, item))
            
            else:
                activeitem = item
                preposition = "a"
                if (item[0].lower() in ["a", "e", "i", "o", "u"]):
                    preposition += "n"
                if (UseItem(action.GetTargets()[0], False, True)):
                    if (TrainerItem(item)):
                        renpy.say(None, "The foe used {} {}!".format(preposition, item))
                    else:
                        renpy.say(None, "The foe used {} {} on {}!".format(preposition, item, action.GetTargets()[0].GetNickname()))

    def DoDamage(user, move, target, overwritetype = None, iscrit=False, overwritepower=0, typebonus=1, fixeddamage=-1, sheerforcebonus=False, recklessbonus=False, atebonus=False, analyticbonus=False, parentalbond=False):
        global ItemText

        damage = 0
        if (fixeddamage == -1):
            power = (move.Power if overwritepower == 0 else overwritepower)
            type = move.Type if overwritetype == None else overwritetype
            isSpecial = move.Category == "Special"
            
            atkStat = Stats.SpecialAttack if isSpecial else Stats.Attack
            atkStatVal = user.GetStat(atkStat, ignorenegative=iscrit)
            if (move.Name != "Foul Play"):
                if (user.GetStatChanges(atkStat) != 0 and target.HasAbility("Unaware")):
                    atkStatVal = user.GetStat(atkStat, ignorenegative=True, ignorepositive=True)
            else:
                atkStatVal = target.GetStat(atkStat, ignorenegative=iscrit)

            defStat = Stats.SpecialDefense if isSpecial else Stats.Defense
            if (move.Name in ["Psyshock", "Psystrike"]):
                defStat = Stats.Defense
            defStatVal = target.GetStat(defStat, ignorepositive=iscrit)
            if (target.GetStatChanges(defStat) != 0 and (user.HasAbility("Unaware") or move.Name in ["Chip Away", "Darkest Lariat"])):
                defStatVal = user.GetStat(defStat, ignorenegative=True, ignorepositive=True)

            foreveralstab = False
            for fvl in user.GetForeverals():
                if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddSTAB):
                    if (type in lookupforeveraldata(fvl, FVLMacros.FVLTypeData)):
                        foreveralstab = True

            stabbonus = 1.5 if foreveralstab or user.HasType(type) or (user.GetTerastalized() != -1 and type == user.GetTeraType()) else 1.0
            stabbonus = 2.0 if (not user.IsTerad() and stabbonus == 1.5 and user.HasAbility("Adaptability")) or (user.IsTerad() and type == user.GetTeraType() and user.HasAbility("Adaptability")) else stabbonus
            stabbonus = 2.25 if (user.IsTerad() and user.HasAbility("Adaptability") and type == user.GetTeraType() and type in user.GetTypes(ignoreTera=True)) else stabbonus
            burnpenalty = 0.5 if (user.HasStatus("burned") and not isSpecial and not user.HasAbility("Guts")) else 1.0
            pursuitbonus = 2.0 if user.HasStatus("pursuing") else 1.0
            mudsportpenalty = 0.33 if type == "Electric" and BattlefieldExists("Mud Sport") else 1.0
            watersportpenalty = 0.33 if type == "Fire" and BattlefieldExists("Water Sport") else 1.0
            critbonus = 1.5 if iscrit else 1.0
            critbonus = 2.25 if iscrit and user.HasAbility("Sniper") else critbonus
            mistyterrainpenalty = 0.5 if type == "Dragon" and BattlefieldExists("Misty Terrain") and IsGrounded(target) else 1.0
            electricterrainbonus = 1.3 if type == "Electric" and BattlefieldExists("Electric Terrain") and IsGrounded(user) else 1.0
            grassyterrainbonus = 1.3 if type == "Grass" and BattlefieldExists("Grassy Terrain") and IsGrounded(user) else 1.0
            grassyterrainpenalty = 0.5 if move.Name in ["Magnitude", "Earthquake", "Bulldoze"] and BattlefieldExists("Grassy Terrain") and IsGrounded(target) else 1.0
            chargedbonus = 2.0 if type == "Electric" and user.HasStatus("charged") else 1.0
            steelworkerbonus = 1.5 if type == "Steel" and user.HasAbility("Steelworker") else 1.0
            ironfistbonus = 1.2 if IsPunchMove(move.Name) and user.HasAbility("Iron Fist") else 1.0
            sharpnessbonus = 1.5 if IsSliceMove(move.Name) and user.HasAbility("Sharpness") else 1.0
            blazebonus = 1.5 if type == "Fire" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Blaze") else 1.0
            torrentbonus = 1.5 if type == "Water" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Torrent") else 1.0
            overgrowbonus = 1.5 if type == "Grass" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Overgrow") else 1.0
            swarmbonus = 1.5 if type == "Bug" and user.GetHealthPercentage() <= 1.0/3.0 and user.HasAbility("Swarm") else 1.0
            tintedlensbonus = 2.0 if typebonus < 1 and user.HasAbility("Tinted Lens") else 1.0
            sheerforcebonus = 1.3 if sheerforcebonus and user.HasAbility("Sheer Force") else 1.0
            strongjawbonus = 1.5 if IsBiteMove(move.Name) and user.HasAbility("Strong Jaw") else 1.0
            recklessbonus = 1.2 if recklessbonus else 1.0
            flashfirebonus = 1.5 if type == "Fire" and user.HasStatus("aflame") and user.HasAbility("Flash Fire") else 1.0
            sandforcebonus = 1.3 if type in ["Rock", "Ground", "Steel"] and WeatherIs("sandstorm") and user.HasAbility("Sand Force") else 1.0
            thickfatpenalty = 0.5 if type in ["Ice", "Fire"] and target.HasAbility("Thick Fat") else 1.0
            defensecurlcombo = 2.0 if move.Name in ["Rollout", "Ice Ball"] and user.HasStatus(".curling") else 1.0
            technicianbonus = 1.5 if move.Power <= 60 and user.HasAbility("Technician") else 1.0
            stompbonus = 2.0 if move.Name in ["Stomp", "Body Slam", "Dragon Rush", "Steamroller", "Heat Crash", "Heavy Slam", "Flying Press", "Malicious Moonsault"] and target.HasStatus(".minimized") else 1.0
            helpinghandbonus = pow(1.5, user.GetStatusCount("helped"))
            dryskinbonus = 1.25 if type == "Fire" and target.HasAbility("Dry Skin") else 1.0
            lightscreenpenalty = 0.5 if isSpecial and EffectOnOwnField(target, "light screen") else 1.0
            reflectpenalty = 0.5 if not isSpecial and EffectOnOwnField(target, "reflect") else 1.0
            auroraveilpenalty = 0.5 if lightscreenpenalty + reflectpenalty == 2 and EffectOnOwnField(target, "aurora veil") else 1.0
            rivalrybonus = 1.25 if user.GetGender() == target.GetGender() and user.GetGender() != Genders.Unknown and user.HasAbility("Rivalry") else 1.0
            rivalrypenalty = 0.75 if user.GetGender() != target.GetGender() and user.GetGender() != Genders.Unknown and target.GetGender() != Genders.Unknown  and user.HasAbility("Rivalry") else 1.0
            sunbonus = 1.5 if WeatherIs("sunny") and type == "Fire" else 1.0
            sunpenalty = 0.5 if WeatherIs("sunny") and type == "Water" else 1.0
            rainbonus = 1.5 if WeatherIs("rainy") and type == "Water" else 1.0
            rainpenalty = 0.5 if WeatherIs("rainy") and type == "Fire" else 1.0
            toughclawsbonus = 1.3 if MakesContact(move) and user.HasAbility("Tough Claws") else 1.0
            atebonus = 1.2 if atebonus and user.HasAbility("Pixilate") else 1.0
            analyticbonus = 1.3 if analyticbonus and user.HasAbility("Analytic") else 1.0
            stakeoutbonus = 2.0 if target.GetTurnSwitchedIn() == Turn and user.HasAbility("Stakeout") else 1.0
            filterpenalty = 0.75 if typebonus > 1 and (target.HasAbility("Filter") or target.HasAbility("Solid Rock") or target.HasAbility("Prism Armor")) else 1.0
            punkrockbonus = 1.3 if IsSoundMove(move.Name) and user.HasAbility("Punk Rock") else 1.0
            punkrockpenalty = 0.5 if IsSoundMove(move.Name) and target.HasAbility("Punk Rock") else 1.0
            friendguardpenalty = 0.75 * GetFriendGuardCount(target)
            parentalbondpenalty = 0.25 if parentalbond else 1.0
            fluffypenalty = 0.5 if MakesContact(move) and target.HasAbility("Fluffy") else 1.0
            fluffybonus = 2.0 if type == "Fire" and target.HasAbility("Fluffy") else 1.0
            purifyingsaltpenalty = 0.5 if type == "Ghost" and target.HasAbility("Purifying Salt") else 1.0
            randomvariation = random.uniform(0.85, 1.0)

            elementbonus = 1
            for elementitem, element in elementitems.items():
                if (user.HasItem(elementitem, False) and type == element):
                    ItemText += "The power was boosted by the {}!".format(elementitem)
                    elementbonus = 1.1
                    break
            
            damage = max(1, math.floor(((2.0 * user.GetLevel() / 5.0 + 2) * power * atkStatVal / defStatVal / 50.0 + 2) 
                * stabbonus * burnpenalty * pursuitbonus * mudsportpenalty * critbonus * mistyterrainpenalty 
                * chargedbonus * typebonus * steelworkerbonus * ironfistbonus * blazebonus * torrentbonus 
                * overgrowbonus * tintedlensbonus * sheerforcebonus * strongjawbonus * recklessbonus * flashfirebonus
                * swarmbonus * sandforcebonus * thickfatpenalty * defensecurlcombo * technicianbonus * stompbonus 
                * helpinghandbonus * dryskinbonus * lightscreenpenalty * reflectpenalty * watersportpenalty 
                * rivalrybonus * rivalrypenalty * sunbonus * sunpenalty * rainbonus * rainpenalty 
                * electricterrainbonus * grassyterrainbonus * toughclawsbonus * atebonus * analyticbonus 
                * stakeoutbonus * filterpenalty * punkrockbonus * punkrockpenalty * sharpnessbonus * elementbonus
                * parentalbondpenalty * fluffypenalty * fluffybonus * auroraveilpenalty * randomvariation))
        else:
            damage = fixeddamage

        if (target.HasStatus("substitute") and not IsSoundMove(move.Name) and not user.HasAbility("Infiltrator")):
            if (target.GetStatusCount("substitute") > damage):
                target.ApplyStatus("substitute", target.GetStatusCount("substitute") - damage, target, True)
            else:
                target.ClearStatus("substitute")
        else:
            target.AdjustHealth(-damage, directdamage=True)

        #renpy.say(None, "//TESTING:{} used {} on {}, dealing {} damage!".format(user.GetNickname(), move.Name, target.GetNickname(), damage))
        return damage

    def BattleOver():
        if (Fled):
            return True

        maxnumber = 0
        for trainer in Trainers:
            if (trainer.GetNumber() > maxnumber):
                maxnumber = trainer.GetNumber()

        battletype = max(maxnumber, len(FriendlyTrainers()), len(EnemyTrainers()))
        partyleads = []
        for trainer in Trainers:
            partyleads += trainer.GetTeam()[:battletype]

        for mon in partyleads:
            if (mon.GetHealth() == 0 and not mon in FaintedMons):
                if (mon.GetCaught() > 0):
                    renpy.say(None, "{} was caught!".format(mon.GetNickname()))
                    if (mon != brendansandshrewobj):
                        renpy.transition(dissolve)
                        renpy.show_screen("mondata", mon)
                        mon.Nickname = renpy.input("Would you like to give it a nickname?", default=mon.GetNickname(), length=12)
                        renpy.transition(dissolve)
                        renpy.hide_screen("mondata")
                else:
                    mon.PlayCry()
                    renpy.say(None, "{} fainted!".format(mon.GetNickname()))
                    mon.FaintedOnTurn = Turn
                    for allymon in GetBattlers(mon):
                        if (allymon.HasAbility("Power of Alchemy")):
                            allymon.ApplyStatus("alchemized", mon.GetAbility())
                FaintedMons.append(mon)
                if (GainExp):
                    if (mon.GetTrainerType() == TrainerType.Enemy):#if opponent faints...
                        splitmons = []
                        for othermon in PlayerPokemon():
                            if (othermon.HasItem("Experience Share", activating=False) and othermon not in PlayerBattlers() and othermon.GetHealthPercentage() > 0):
                                splitmons.append(othermon)
                        for playermon in PlayerBattlers() + splitmons:#give experience to all playerbattlers
                            playermon.GainExperience(mon.CalculateGivingExperience(playermon) / (len(splitmons) + 1) * (playermon.GetTrainer().GetNumber() if playermon.HasItem("Experience Share", activating=False) else 1.0))
                
                AdjustPokemon(mon)

        hasOne = False
        for mon in FriendlyPokemon():
            if (mon.GetHealth() > 0):
                hasOne = True
                break

        if (not hasOne):
            return True

        hasOne = False
        for mon in EnemyPokemon():
            if (mon.GetHealth() > 0):
                hasOne = True
                break

        if (not hasOne):
            return True
        
        return False

    def PlayerWon():
        for mon in FriendlyBattlers():
            if (mon.GetHealth() > 0):
                return True
        return False

    def ApplyWeather(weather, countdown):
        global CurrentWeather
        if (CurrentWeather != None and WeatherIs(weather) or AbilityOnField("Cloud Nine")):
            return "But it failed!"
        else:
            CurrentWeather = (weather, countdown)

            for mon in Battlers():
                if (mon.HasAbility("Forecast", triggersplash=False)):
                    FormeChanges(mon)

            if (WeatherIs("sandstorm")):
                return "A sandstorm whipped up!"
            elif (WeatherIs("hail")):
                return "It started to hail!"
            else:
                return "The sky became {}!".format(weather)

    def FormeChanges(user):
        returnable = ""
        if (user.GetId() != 555 and user.GetHealthPercentage() > 0.5 and user.HasAbility("Zen Mode")):
            returnable += user.ChangeForme("Darmanitan (Standard Mode)")
        elif (user.GetId() != 555.1 and user.GetHealthPercentage() <= 0.5 and user.HasAbility("Zen Mode")):
            returnable += user.ChangeForme("Darmanitan (Zen Mode)")
        elif (user.GetId() == 774 and user.GetHealthPercentage() <= 0.5 and user.Image == None and user.HasAbility("Shields Down")):
            returnable += user.ChangeForme(user.GetMiniorForme())
        elif (user.GetId() == 774 and user.GetHealthPercentage() > 0.5 and user.Image != None and user.HasAbility("Shields Down")):
            returnable += user.ChangeForme("Minior (Meteor Form)")
        elif (user.GetId() == 746 and user.Level >= 20 and user.GetHealthPercentage() > 0.25 and user.Image == None and user.HasAbility("Schooling")):
            returnable += user.ChangeForme("Wishiwashi (School Form)")
        elif (user.GetId() == 746 and user.Level >= 20 and user.GetHealthPercentage() <= 0.25 and user.Image != None and user.HasAbility("Schooling")):
            returnable += user.ChangeForme("Wishiwashi (Solo Form)")
        elif (user.GetId() in [351, 351.1, 351.2, 351.3] and user.HasAbility("Forecast", triggersplash=False)):
            if (WeatherIs("rainy") and user.GetId() != 351.2 and user.HasAbility("Forecast")):
                returnable += user.ChangeForme("Castform (Rainy Form)")
            elif (WeatherIs("sunny") and user.GetId() != 351.1 and user.HasAbility("Forecast")):
                returnable += user.ChangeForme("Castform (Sunny Form)")
            elif (WeatherIs("hail") and user.GetId() != 351.3 and user.HasAbility("Forecast")):
                returnable += user.ChangeForme("Castform (Snowy Form)")
            elif (WeatherIs(None) and user.GetId() != 351 and user.HasAbility("Forecast")):
                returnable += user.ChangeForme("Castform (Normal)")
        elif (user.GetId() in [412, 412.1, 412.2]):
            if (GetCamoType() in ["Grass", "Bug"] and user.GetId() != 412):
                returnable += user.ChangeForme("Burmy (Plant Cloak)")
            elif (GetCamoType() in ["Steel", "Poison"] and user.GetId() != 412.2):
                returnable += user.ChangeForme("Burmy (Trash Cloak)")
            elif (GetCamoType() in ["Ground", "Rock"] and user.GetId() != 412.1):
                returnable += user.ChangeForme("Burmy (Sandy Cloak)")

        return returnable

    def DoEffects():# will do effects, and also increment them down, if applicable
        decrementers = ["gasping", "snatching", "thrashing", "outraged", "the standout", "confused", "asleep", "wrapped", "flinching", "pursuing", "bound", 
            "taunted", "encored", "enduring", "deathless", "protected", "mind read", "locked on", ".lockingon", ".mindreading", ".baneful", ".enshrouded", 
            ".splintering", ".spiky", ".silked", "pranking", "disabled", "firespun", "whirlpooled", "uproaring", "drowsy", "entombed", "dug in", "airborne", 
            "ethereal", "electrified", "ionized", "embargoed", "laser focused", "levitating", "roosted", "perishing", "petal dancing", "coated in magic", 
            "clamped", "infested", "diving", "diveralized", "grudging", ".obstructing"]
        
        for user in Battlers():
            for other in Battlers():
                for status in normalstatuses:
                    if (other.GetTrainerType() == user.GetTrainerType() and other.HasStatus(status) and random.random() <= 0.3 and user.HasAbility("Healer")):
                        other.ClearStatus(status)
        
        pickuped = False
        harvested = False
        for user in Battlers(True):
            returnable = ""
            
            if (user.HasStatus("frenzied") and not user.HasStatus("gorging") and user.HasAbility("Gulp Missile")):
                user.ClearStatus("gulping")
                returnable += user.ApplyStatus("gorging")

            if (user.HasAbility("Pickup", False) and user.GetItem() == None and not pickuped and not harvested):
                for othermon in Battlers():
                    if (othermon != user):
                        for action, item, turn in othermon.GetItemHistory():
                            if (turn == Turn and action == "Used" and user.HasAbility("Pickup")):
                                pickuped = True
                                returnable += user.GiveItem(item)

            if (user.HasAbility("Harvest", False) and user.GetItem() == None and not pickuped and not harvested):
                for othermon in Battlers():
                    if (othermon != user):
                        for action, item, turn in othermon.GetItemHistory():
                            if (IsBerry(item) and action == "Used" and user.HasAbility("Harvest") and (random.random() <= 0.5 or WeatherIs("sunny"))):
                                harvested = True
                                returnable += user.GiveItem(item)

            dellist = []
            for status in user.GetStatusKeys():
                if (status in normalstatuses and random.random() <= 1.0/3.0 and user.HasAbility("Shed Skin")):
                    returnable += "{}'s shed skin sloughed off!".format(user.GetNickname())
                    dellist.append(status)
                elif (status in normalstatuses and WeatherIs("rainy") and user.HasAbility("Hydration")):
                    dellist.append(status)

            for status in dellist:
                returnable += user.ClearStatus(status)

            if (user.HasStatus("aqua ring")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * 1.0/16.0)):
                    returnable += "{} is healed by the aqua ring!".format(user.GetNickname())
            if (user.HasStatus("ingrained")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * 1.0/16.0)):
                    returnable += "{} is healed by its roots!".format(user.GetNickname())
            if (user.HasStatus("salt cured")):
                if (user.HasType("Water") or user.HasType("Steel")):
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/4.0)):
                        returnable += "{} is direly hurt by its salt cure!".format(user.GetNickname())
                else:
                    if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                        returnable += "{} is hurt by its salt cure!".format(user.GetNickname())
            if (user.HasStatus("burned")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/16.0)):
                    returnable += "{} is hurt by its burn!".format(user.GetNickname())
            elif (user.HasStatus("poisoned")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is hurt by poison!".format(user.GetNickname())
            elif (user.HasStatus("badly poisoned")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -user.GetStatusCount("badly poisoned")/16.0)):
                    user.ApplyStatus("badly poisoned", user.GetStatusCount("badly poisoned") + 1, user, True)
                    returnable += "{} is hurt by its deadly poison!".format(user.GetNickname())
            if (user.HasStatus("wrapped")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is hurt by Wrap!".format(user.GetNickname())
            if (user.HasStatus("firespun")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is hurt by Fire Spin!".format(user.GetNickname())
            if (user.HasStatus("whirlpooled")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is hurt by Whirlpool!".format(user.GetNickname())
            if (user.HasStatus("entombed")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is hurt by Sand Tomb!".format(user.GetNickname())
            if (user.HasStatus("cursed")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/4.0)):
                    returnable += "{} is hurt by the curse!".format(user.GetNickname())

            if (EffectOnOwnField(user, "future sight") 
                and GetBattlers(user).index(user) == GetFieldEffects(user)["future sight"][1]
                and Turn >= GetFieldEffects(user)["future sight"][0] + 2):
                moveuser = GetFieldEffects(user)["future sight"][2]
                del GetFieldEffects(user)["future sight"]
                newaction = Action(0, moveuser.GetStat(Stats.Speed, triggerAbilities=False), ActionTypes.Move, moveuser.GetTrainer(), moveuser, GetMove("Future Sight"), [user.GetTrainer()], [user], Turn)
                DoMove(newaction, moveuser, GetMove("Future Sight"), [user], alreadypretext="The vision came true!")

            endturnitems = ["Sticky Barb"]
            for item in endturnitems:
                user.HasItem(item, autotriggerset=False)
                returnable += ItemText

            if (user.HasStatus("seeded")):# in this case, target is the seeder, and user is the one who is seeded
                target = user.GetStatusCount("seeded")[1]#seeded's count is a tuple, (slotint, obj)
                oldtarget = target
                if (target not in Battlers()):
                    possibletargets = GetTargets(user, Range.Any, target.GetTrainerType() != user.GetTrainerType())
                    numtargets = len(possibletargets)
                    if (numtargets != 0):
                        target = possibletargets[min(user.GetStatusCount("seeded")[0], numtargets - 1)]
                        user.ApplyStatus("seeded", (user.GetStatusCount("seeded")[0], target), applier=oldtarget, overwrite=True)
                    else:
                        target = None
                if (target != None):
                    damage = user.GetStat(Stats.Health) * -1.0/8.0
                    if (user.AdjustHealth(damage)):
                        returnable += "{} is hurt by Leech Seed!".format(user.GetNickname())
                        if (target.AdjustHealth(-damage)):
                            returnable += "{} recovered health!".format(target.GetNickname())
            if (user.HasStatus("bound")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is hurt by Bind!".format(user.GetNickname())
            if (user.HasStatus("clamped")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is hurt by Clamp!".format(user.GetNickname())
            if (user.HasStatus("infested")):
                if (user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/8.0)):
                    returnable += "{} is hurt by Infestation!".format(user.GetNickname())
            if (user.HasStatus("charged")):
                lastmove = GetLastMove(ActionLog, user, returnnonemoves=["Charge", "Energize"])
                if (lastmove != None and lastmove.Type == "Electric"):
                    user.ClearStatus("charged")
            if (user.HasStatus("rollout") and not user.HasStatus(".usedrollout")):
                user.ClearStatus("rollout")
            if (user.HasStatus("ice ball") and not user.HasStatus(".usediceball")):
                user.ClearStatus("ice ball")
            if (user.HasStatus("biding")):
                user.ApplyStatus("biding", user.GetStatusCount("biding") + 1, overwrite=True)
            else:
                user.ClearStatus(".bidingdamage")

            user.ClearStatus(".usedrollout")
            user.ClearStatus(".usediceball")
            dellist = []
            for status in user.GetStatusKeys():
                if (status in decrementers):
                    returnable += user.DecrementStatus(status)
                    if (user.GetStatusCount(status) <= 0):
                        dellist.append(status)
            for status in dellist:
                if (status not in ["confused", "asleep"]):
                    if (status == "perishing"):
                        user.AdjustHealth(0, absolute=True)
                        returnable += "{} succumbed to the perish song!".format(user.GetNickname())
                    if (status == "petal dancing"):
                        returnable += user.ApplyStatus("confused", random.randint(2, 5))
                    user.ClearStatus(status)

            if (user.HasStatus("helped")):
                user.ClearStatus("helped")

            if ("drowsy" in dellist):
                returnable += user.ApplyStatus("asleep")

            if (user.HasStatus(".disabling") and not user.HasStatus("disabled")):
                user.ClearStatus(".disabling")

            if (user.HasStatus(".wrappedby") and not user.HasStatus("wrapped")):
                user.ClearStatus(".wrappedby")
            if (user.HasStatus(".firespunby") and not user.HasStatus("firespun")):
                user.ClearStatus(".firespunby")
            if (user.HasStatus(".whirlpooledby") and not user.HasStatus("whirlpooled")):
                user.ClearStatus(".whirlpooledby")
            if (user.HasStatus(".boundby") and not user.HasStatus("bound")):
                user.ClearStatus(".boundby")
            if (user.HasStatus(".clampedby") and not user.HasStatus("clamped")):
                user.ClearStatus(".clampedby")
            if (user.HasStatus(".infestedby") and not user.HasStatus("infested")):
                user.ClearStatus(".infestedby")
            if (user.HasStatus(".entombedby") and not user.HasStatus("entombed")):
                user.ClearStatus(".entombedby")

            if (user.GetTurnSwitchedIn() != Turn or JustSwitchedIn(ActionLog, user)):
                if (user.HasAbility("Moody")):
                    returnable += ActivateMoody(user)
                if (user.HasAbility("Speed Boost")):
                    returnable += user.ChangeStats(Stats.Speed, 1, user)

            returnable += FormeChanges(user)

            if (returnable != ""):
                renpy.say(None, FormatText(returnable))

    def ApplyBattlefieldEffects(effect, count, overwrite=False):
        global BattlefieldEffects
        if (not overwrite and BattlefieldExists(effect)):
            return "But it failed!"
        else:
            if ("Terrain" in effect or effect == "Burial Ground"):
                if (BattlefieldExists("Misty Terrain")):
                    del BattlefieldEffects["Misty Terrain"]
                elif (BattlefieldExists("Electric Terrain")):
                    del BattlefieldEffects["Electric Terrain"]
                elif (BattlefieldExists("Grassy Terrain")):
                    del BattlefieldEffects["Grassy Terrain"]
                elif (BattlefieldExists("Burial Ground")):
                    del BattlefieldEffects["Burial Ground"]
            BattlefieldEffects[effect] = count
            return "The battlefield is under the effect of {}!".format(effect)

    def DoBattlefieldEffects():# will do effects, and also increment them down, if applicable
        global UsedEchoedVoice
        global BattlefieldEffects
        global CurrentWeather
        if (UsedEchoedVoice):
            if (BattlefieldExists("Echoed Voice")):
                ApplyBattlefieldEffects("Echoed Voice", min(BattlefieldEffects["Echoed Voice"] + 40, 200))
            else:
                ApplyBattlefieldEffects("Echoed Voice", 80)
        else:
            if (BattlefieldExists("Echoed Voice")):
                del BattlefieldEffects["Echoed Voice"]

        decrementers = ["Mud Sport", "Gravity", "Misty Terrain", "Water Sport", "Burial Ground", "Simple World", "Electric Terrain", "Grassy Terrain"]
        becopy = BattlefieldEffects.copy()

        for effect in becopy.keys():
            if (effect in decrementers):
                BattlefieldEffects[effect] -= 1
                if (BattlefieldEffects[effect] <= 0):
                    del BattlefieldEffects[effect]

        decrementers = ["mist", "lucky", "wide guard", "tailwind", "quick guard"]
        fecopy = FriendlyEffects.copy()
        for effect in fecopy.keys():
            if (effect in decrementers):
                FriendlyEffects[effect] -= 1
                if (FriendlyEffects[effect] <= 0):
                    del FriendlyEffects[effect]

        if ("wishing star" in FriendlyEffects.keys()):
            if (FriendlyEffects["wishing star"][0] == 2):
                FriendlyEffects["wishing star"][0] = 1
            else:
                slot = FriendlyEffects["wishing star"][1]
                healamount = FriendlyEffects["wishing star"][2]
                if (len(FriendlyBattlers()) > slot):
                    FriendlyBattlers()[slot].AdjustHealth(healamount)
                    renpy.say(None, "The wish came true!")
                    del FriendlyEffects["wishing star"]

        eecopy = EnemyEffects.copy()
        for effect in eecopy.keys():
            if (effect in decrementers):
                EnemyEffects[effect] -= 1
                if (EnemyEffects[effect] <= 0):
                    del EnemyEffects[effect]

        if ("wishing star" in EnemyEffects.keys()):
            if (EnemyEffects["wishing star"][0] == 2):
                EnemyEffects["wishing star"][0] = 1
            else:
                slot = EnemyEffects["wishing star"][1]
                healamount = EnemyEffects["wishing star"][2]
                if (len(EnemyBattlers()) > slot):
                    EnemyBattlers()[slot].AdjustHealth(healamount)
                    renpy.say(None, "The wish came true!")
                    del EnemyEffects["wishing star"]

        if ("Burial Ground" in BattlefieldEffects.keys()):
            for mon in Battlers(True):
                if (IsGrounded(mon) and not (mon.HasType("Ground") or mon.HasType("Ghost"))):
                    mon.AdjustHealth(mon.GetStat(Stats.Health) * -1.0/16.0)
                    mon.ChangeStats(Stats.Speed, -1)
                    renpy.say(None, "The Burial Ground draws {} in!".format(mon.GetNickname()))
        elif ("Grassy Terrain" in BattlefieldEffects.keys()):
            for mon in Battlers(True):
                if (IsGrounded(mon)):
                    mon.AdjustHealth(mon.GetStat(Stats.Health) * 1.0/16.0)
            renpy.say(None, "The Grassy Terrain heals all!")

        if (CurrentWeather != None):
            weather = CurrentWeather[0]
            weathercount = CurrentWeather[1]

            if (WeatherIs("sandstorm")):
                if (weathercount != 0):
                    weathercount -= 1
                    renpy.say(None, "The sandstorm rages!")
                    for mon in Battlers(True):
                        if (not ("Steel" in mon.GetTypes() or "Rock" in mon.GetTypes() or "Ground" in mon.GetTypes()) and not mon.HasAbility("Overcoat") and not mon.HasAbility("Sand Force") and not mon.HasAbility("Sand Rush") and not mon.HasAbility("Sand Veil")):
                            if (mon.AdjustHealth(mon.GetStat(Stats.Health) * -1.0/16.0)):
                                renpy.say(None, "{} is buffeted by the sandstorm!".format(mon.GetNickname()))
                            BattleCheck()
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The sandstorm calmed...")
                    CurrentWeather = None
            elif (WeatherIs("sunny")):
                if (weathercount != 0):
                    weathercount -= 1
                    for mon in Battlers(True):
                        if (mon.HasAbility("Solar Power") or mon.HasAbility("Dry Skin")):
                            mon.AdjustHealth(-mon.GetStat(Stats.Health) / 8.0)
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The sunlight faded...")
                    CurrentWeather = None
            elif (WeatherIs("rainy")):
                if (weathercount != 0):
                    weathercount -= 1
                    for mon in Battlers(True):
                        if (mon.HasAbility("Dry Skin")):
                            mon.AdjustHealth(mon.GetStat(Stats.Health) / 8.0)
                        elif (mon.HasAbility("Rain Dish")):
                            mon.AdjustHealth(mon.GetStat(Stats.Health) / 16.0)
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The rainclouds dissipated...")
                    CurrentWeather = None
            elif (WeatherIs("hail")):
                if (weathercount != 0):
                    weathercount -= 1
                    renpy.say(None, "The hail falls!")
                    for mon in Battlers(True):
                        if (not "Ice" in mon.GetTypes() and not mon.HasAbility("Overcoat") and not mon.HasAbility("Ice Body") and not mon.HasAbility("Snow Cloak")):
                            if (mon.AdjustHealth(mon.GetStat(Stats.Health) / -16.0)):
                                renpy.say(None, "{} is buffeted by the hail!".format(mon.GetNickname()))
                            BattleCheck()
                        elif (mon.HasAbility("Ice Body")):
                            mon.AdjustHealth(mon.GetStat(Stats.Health) / 16.0)
                    CurrentWeather = (weather, weathercount)

                else:
                    renpy.say(None, "The hail calmed...")
                    CurrentWeather = None

    def DoMove(action, user, move, targets, alreadypretext="", alreadyposttext="", repeating=False, parentalbond=False):
        global BattlefieldEffects
        global UsingMove
        global MoveUser
        global ActiveMove
        global ActionLog
        global ItemText

        if (user not in Battlers()):
            action.ChangeSuccess(False)
            return

        if (not MoveValid(user, move)):
            action.ChangeSuccess(False)
            renpy.say(None, "{} can't use {}!".format(user.GetNickname(), move.Name))
            return

        moveboosts = []
        for fvl in user.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.MoveBoost):
                for newmove in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                    moveboosts.append(newmove)

        UsingMove = True
        MoveUser = user
        renpy.show_screen("battleui")
        name = move.Name
        ActiveMove = name
        type = move.Type
        pretext = alreadypretext
        posttext = alreadyposttext
        abortmove = False
        username = user.GetNickname()
        repeat = repeating
        critstage = 0
        healthgain = 0
        power = 0
        fixeddamage = -1
        recoil = 0
        iscrit = False
        sheerforcebonus = False
        subtractpp = True
        atebonus = False#from pixilate, aerilate, stuff like that

        if (user.HasStatus("electrified")):
            type = "Electric"
        if (user.HasStatus("ionized") and type == "Normal"):
            type = "Electric"
        
        if (type == "Normal" and user.HasAbility("Pixilate")):
            type = "Fairy"
            atebonus = True

        user.ClearStatus("bound to destiny")

        if (user.HasStatus("flinching")):
            posttext += "{} flinched!".format(username)
            abortmove = True
        elif (user.HasStatus("frozen")):
            if (random.random() > .2):
                pretext += "{} is frozen!".format(username)
                abortmove = True
            else:
                pretext += "{} thawed out!".format(username)
                user.ClearStatus("frozen")
        elif (user.GetStatusCount("asleep") > 0 and name not in ["Snore", "Sleep Talk"]):
            pretext = "{} is fast asleep...".format(username)
            abortmove = True
        elif (user.HasStatus("asleep") and user.GetStatusCount("asleep") <= 0):
            user.ClearStatus("asleep")
            pretext = "{} woke up!".format(username, move.Name)
        elif (user.HasStatus("paralyzed") and random.random() <= .25):
            posttext += "{} is paralyzed, so it can't move!".format(username)
            abortmove = True
        elif (user.HasStatus("infatuated") and random.random() <= .5):
            posttext += "{} is infatuated, and cannot move!".format(username)
            abortmove = True
        elif (user.HasStatus("confused") and user.GetStatusCount("confused") <= 0):
            user.ClearStatus("confused")
            pretext = "{} snapped out of confusion!".format(username, move.Name)
        elif (user.GetStatusCount("confused") > 0):
            pretext = "{} is confused! ".format(username)
            if (random.random() <= .33):
                    posttext += "{} hurt itself in its confusion!".format(username)
                    if (not user.HasStatus("busted disguise") and user.HasAbility("Disguise")):
                        user.AdjustHealth(-user.GetStat(Stats.Health) / 8.0)
                        user.ApplyStatus("busted disguise")
                        posttext += "{}'s disguise was busted!".format(user.GetNickname())
                    else:
                        DoDamage(user, hurtself, user)
                    abortmove = True
        elif (user.HasStatus("taunted") and move.Category == "Status"):
            posttext += "{} is too angry to use {}!".format(username, move.Name)
            abortmove = True
        elif (user.HasStatus("encored") and move != GetLastMove(ActionLog, user)):
            posttext += "{} is swayed by the encore!".format(username)
            abortmove = True
        elif (IsExplosion(name) and AbilityOnField("Damp")):
            posttext += "It's too damp for explosions!"
            abortmove = True
        elif (move.PP == 0):
            posttext += "{} tried to use {}, but there's no PP left for that move!".format(username, move.Name)
            abortmove = True

        if (name not in ["Endure", "Protect", "Wide Guard", "Detect", "Enshroud", "Deathless", "Splinter Shield", "Quick Guard", "Silk Trap", "Baneful Bunker", "Obstruct"]):
            user.ClearStatus(".protections")
        if (name != "Fury Cutter"):
            user.ClearStatus(".furycutter")
        
        if (abortmove):
            action.ChangeSuccess(False)
            renpy.say(None, pretext + " " + posttext)
            UsingMove = False
            MoveUser = None
            ActiveMove = None
            return

        if (move.Name in moveboosts):
            pretext += "{}'s wishes coalesced! ".format(username)

        pretext += "{} used {}!".format(username, move.Name)


        if (StatusOnFoes(user, "snatching") != None and IsSnatchable(name)):
            user = StatusOnFoes(user, "snatching")
            targets = [user]
            pretext += "The move was snatched by {}!".format(user.GetNickname())
            user.ClearStatus("snatching")

        if (len(targets) == 1 and StatusInBattlers("the standout")):
            for mon in Battlers():
                if (mon.HasStatus("the standout") and mon in GetTargets(user, GetMoveRange(move)) and mon not in GetBattlers(user)):
                    targets = [mon]

        if (GetMoveRange(move) in [Range.All, Range.AllAlliesAndSelf]):
            targets = [user]
        elif (GetMoveRange(move) == Range.AllFoes):
            targets = [targets[0]]

        bouncingmon = None
        for mon in targets:
            if (move.Category == "Status" and GetMoveRange(move) not in [Range.All] and (mon.HasAbility("Magic Bounce") or mon.HasStatus("coated in magic"))):
                posttext += "The move was bounced back!"
                bouncingmon = mon
        if (bouncingmon != None):
            user = bouncingmon
            targets = GetTargets(bouncingmon, GetMoveRange(move))

        if (name == "Magnitude"):
            magnitude = random.random()
            if (magnitude < .05):
                posttext += "Magnitude 4!"
                power = 10
            elif (magnitude < .15):
                posttext += "Magnitude 5!"
                power = 30
            elif (magnitude < .35):
                posttext += "Magnitude 6!"
                power = 50
            elif (magnitude < .65):
                posttext += "Magnitude 7!"
                power = 70
            elif (magnitude < .85):
                posttext += "Magnitude 8!"
                power = 90
            elif (magnitude < .95):
                posttext += "Magnitude 9!"
                power = 110
            else:
                posttext += "Magnitude 10!!!"
                power = 150

        sideeffects = []
        posteffects = []

        for i, target in enumerate(targets):
            sideeffects = []
            posteffects = []
            
            doDamage = (False if move.Category == "Status" else True)

            if (user.GetStatusCount("biding") >= 3):
                if (user.GetStatusCount(".bidingdamage") != 0):
                    fixeddamage = user.GetStatusCount(".bidingdamage")[0] * 2.0
                    doDamage = True
                    subtractpp = True
                    target = user.GetStatusCount(".bidingdamage")[1]
                    if (target not in GetBattlers(user, True)):
                        target = random.choice(GetBattlers(user, True))
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)

            checkaccuracy = ((isinstance(move.Accuracy, float) or isinstance(move.Accuracy, int)) 
                and not (user.HasAbility("No Guard") or target.HasAbility("No Guard"))
                and not (move.Name in ["Thunder", "Hurricane"] and WeatherIs("rainy"))
                and not (move.Name == "Blizzard" and (WeatherIs("snowy") or WeatherIs("hail")))
                and not (user.HasStatus(".mindreading") and target.HasStatus("mind read"))
                and not (user.HasStatus(".lockingon") and target.HasStatus("locked on")))

            trueaccuracy = 1.0
            baseaccuracy = move.Accuracy

            if (move.Name in ["Hurricane", "Thunder"] and WeatherIs("sunny")):
                baseaccuracy = 0.5

            if (type in ["Electric", "Water"] and GetMoveRange(move) in [Range.Adjacent, Range.AdjacentFoe, Range.Any, Range.AnyOrSelf, Range.AdjacentAlly, Range.AdjacentAllyOrSelf]):
                for pkmn in Battlers(True):
                    if (pkmn != user):
                        if (type == "Electric" and pkmn.HasAbility("Lightning Rod")
                            or type == "Water" and pkmn.HasAbility("Storm Drain")):
                            target = pkmn
                            checkaccuracy = False
                            break

            if (target not in target.GetTrainer().GetLead()):
                try:
                    newtarget = target.GetTrainer().GetLead()[action.GetTargetSlots()[i]]
                    action.GetTargets()[action.GetTargets().index(target)] = newtarget
                    target = newtarget
                except:
                    target == None

            if (target == None):
                for trainer in Trainers:
                    for othermon in trainer.GetLead():
                        if (othermon in GetTargets(user, GetMoveRange(move), GetMoveRange(move) in [Range.Adjacent, Range.Any, Range.AnyOrSelf])):
                            target = othermon

            if (name in ["Thrash", "Outrage"]):
                target = random.choice(GetTargets(user, Range.AdjacentFoe))

            if (target == None or target != None and target.GetHealthPercentage() <= 0):
                action.ChangeSuccess(False)
                renpy.say(None, "{} tried to use {}, but there is no target!".format(username, name))
                UsingMove = False
                MoveUser = None
                ActiveMove = None
                return
            
            if (targets[:i + 1].count(target) > 1):
                continue

            targetstring = " It targets " + target.GetNickname() + "!"
            if (GetMoveRange(move) in [Range.All, Range.AllAdjacent, Range.AllAdjacentFoes, Range.AllFoes, Range.AllAllies, Range.Self, Range.AllAlliesAndSelf]
                or (GetMoveRange(move) == Range.AdjacentAlly and len(GetTargets(user, Range.AdjacentAlly)) == 0)
                or len(GetTargets(user, GetMoveRange(move))) < 2
                or name in ["Dive", "Fly", "Bounce", "Dig", "Shadow Force", "Phantom Force"] and not (user.HasStatus("dug in") or user.HasStatus("airborne") or user.HasStatus("diving") or user.HasStatus("ethereal"))):
                targetstring = ""

            pretext += targetstring

            breaksemiinvul = (name in ["Gust", "Hurricane", "Smack Down", "Sky Uppercut", "Thousand Arrows", "Thunder", "Twister", "Whirlwind"] and target.HasStatus("airborne")
            or name in ["Earthquake", "Fissure", "Magnitude"] and target.HasStatus("dug in")
            or name == "Whirlpool" and target.HasStatus("diving")
            or name == "Toxic" and user.HasType("Poison")
            or target.HasAbility("No Guard")
            or user.HasAbility("No Guard"))

            ignoresemiinvul = breaksemiinvul

            if (name in ["Stomp", "Body Slam", "Dragon Rush", "Steamroller", "Heat Crash", "Heavy Slam", "Flying Press", "Malicious Moonsault"] and target.HasStatus(".minimized") 
            or name == "Dig" and not user.HasStatus("dug in")
            or name in ["Fly", "Bounce"] and not user.HasStatus("airborne")
            or name == "Dive" and not user.HasStatus("diving")
            or name == "Phantom Force" and not user.HasStatus("ethereal")
            or name == "Toxic" and user.HasType("Poison")
            or breaksemiinvul
            or (repeat and (name != "Triple Kick" or MultihitMax != None and user.HasAbility("Skill Link")))):
                ignoresemiinvul = True
                checkaccuracy = False

            if (move.Name in ["Feint", "Phantom Force"]):
                if (target.HasStatus("protected") or EffectOnOwnField(target, "wide guard") or EffectOnOwnField(target, "quick guard")):
                    target.ClearStatus("protected")
                    if ("wide guard" in GetFieldEffects(target)):
                        del GetFieldEffects(target)["wide guard"]
                    if ("quick guard" in GetFieldEffects(target)):
                        del GetFieldEffects(target)["quick guard"]
                    checkaccuracy = False

            if (checkaccuracy):
                accuracybuffs = user.GetStatChanges(Stats.Accuracy)
                evasionbuffs = target.GetStatChanges(Stats.Evasion)
                if (target.HasStatus("confused") and target.HasAbility("Tangled Feet")):
                    evasionbuffs += 3
                if (evasionbuffs > 0 and (target.HasStatus("miraculously seen") or target.HasStatus("foreseen") or target.HasStatus("sniffed out") or user.HasAbility("Keen Eye") 
                or (evasionbuffs != 0 and (user.HasAbility("Unaware") or move.Name in ["Chip Away", "Darkest Lariat"])))):
                    evasionbuffs = 0
                if (accuracybuffs != 0 and target.HasAbility("Unaware")):
                    accuracybuffs = 0
                accuracymodifier = accuracybuffs - evasionbuffs
                if (accuracymodifier > 0):
                    accuracymodifier = min(6, accuracymodifier)
                    accuracymodifier = (accuracymodifier + 3) / 3.0
                elif (accuracymodifier < 0):
                    accuracymodifier = max(-6, accuracymodifier)
                    accuracymodifier = 3.0 / (-accuracymodifier + 3)
                elif (accuracymodifier == 0):
                    accuracymodifier = 1

                if (move.Category == "Status" and target.HasAbility("Wonder Skin")):
                    baseaccuracy = 0.5
                elif ((WeatherIs("sandstorm") and target.HasAbility("Sand Veil"))
                    or (WeatherIs("hail") and target.HasAbility("Snow Cloak"))):
                    accuracymodifier *= 0.8

                if (move.Category == "Physical" and user.HasAbility("Hustle")):
                    accuracymodifier *= 0.8
                elif (user.HasAbility("Compound Eyes")):
                    accuracymodifier *= 1.3

                if (BattlefieldExists("Gravity")):
                    accuracymodifier *= 5.0/3.0

                trueaccuracy = baseaccuracy * accuracymodifier

                if (WeatherIs("blinding fog")):
                    if (trueaccuracy < 1):
                        trueaccuracy = 0

            if ((target.HasStatus("poisoned") or target.HasStatus("badly poisoned")) and user.HasAbility("Merciless")):
                iscrit = True

            if (((((GetMoveRange(move) in [Range.Adjacent, Range.AdjacentFoe, Range.AllAdjacent, Range.AllAdjacentFoes, Range.AllFoes, Range.Any, Range.AnyOrSelf] or name in ["Thrash", "Outrage"]) and target.HasStatus("protected"))
                and not (target.HasStatus(".silked") and move.Category == "Status")
                and not (target.HasStatus(".obstructing") and move.Category == "Status"))
            or (GetMoveRange(move) in [Range.All, Range.AllAdjacent, Range.AllFoes, Range.AllAdjacentFoes] and EffectOnOwnField(target, "wide guard"))
            or (action.GetPriority() > 0 and EffectOnOwnField(target, "quick guard")))
            and name not in ["Tearful Look", "Hyper Drill", "Bestow"]
            and not (name in ["Fly", "Bounce"] and not user.HasStatus("airborne")
                    or name == "Dig" and not user.HasStatus("dug in")
                    or name == "Dive" and not user.HasStatus("diving")
                    or name in ["Shadow Force", "Phantom Force"] and not user.HasStatus("ethereal"))):  
                repeat = False                  
                doDamage = False
                posttext += "But {} was protected!".format(target.GetNickname())
                if (name in ["Jump Kick", "High Jump Kick"]):
                    user.AdjustHealth(-user.GetStat(Stats.Health) / 2.0)
                    posttext += "{} kept going and crashed!".format(username)
                if (target.HasStatus(".enshrouded") and not MakesContact(move)):
                    posttext += target.ChangeStats(Stats.Evasion, 1, user)
                    target.ClearStatus(".enshrouded")
                elif (target.HasStatus(".splintering") and MakesContact(move)):
                    posttext += ApplyEffect(target, "stealthy rocks", 1, True)
                    target.ClearStatus(".splintering")
                elif (target.HasStatus(".spiky") and MakesContact(move)):
                    user.AdjustHealth(-user.GetStat(Stats.Health) / 8.0)
                elif (target.HasStatus(".silked") and MakesContact(move)):
                    posttext += user.ChangeStats(Stats.Speed, -1, target)
                elif (target.HasStatus(".baneful") and MakesContact(move)):
                    posttext += user.ApplyStatus("poisoned")
                elif (target.HasStatus(".obstructing") and MakesContact(move)):
                    posttext += user.ChangeStats(Stats.Defense, -2, target)
            elif ((checkaccuracy and random.random() > trueaccuracy) or (target.HasStatus("dug in") or target.HasStatus("airborne") or target.HasStatus("ethereal") or target.HasStatus("diving")) and not breaksemiinvul and not ignoresemiinvul):
                doDamage = False
                posttext += "But it missed {}!".format(target.GetNickname())
                repeat = False
                MultihitMax = None
                MultihitCount = None
                if (name in ["Jump Kick", "High Jump Kick"]):
                    user.AdjustHealth(-user.GetStat(Stats.Health) / 2.0)
                    posttext += "{} kept going and crashed!".format(username)
                action.ChangeSuccess(False)
            elif (target.HasType("Dark") and user.HasStatus("pranking") and target != user and move.Category == "Status"):
                doDamage = False
                pretext += "It had no effect on {}...".format(target.GetNickname())
            elif (type == "Electric" and user != target and target.HasAbility("Volt Absorb")):
                doDamage = False
                target.AdjustHealth(target.GetStat(Stats.Health) / 4.0)
            elif (type == "Water" and user != target and (target.HasAbility("Water Absorb") or target.HasAbility("Dry Skin"))):
                doDamage = False
                target.AdjustHealth(target.GetStat(Stats.Health) / 4.0)
            elif (type == "Grass" and user != target and target.HasAbility("Sap Sipper")):
                doDamage = False
                posttext += target.ChangeStats(Stats.Attack, 1, user)
            elif (type == "Electric" and user != target and target.HasAbility("Lightning Rod") 
                or type == "Water" and user != target and target.HasAbility("Storm Drain")):
                doDamage = False
                posttext += target.ChangeStats(Stats.SpecialAttack, 1, user)
            elif ((type == "Fire" or name == "Will-O-Wisp") and user != target and target.HasAbility("Flash Fire")):
                doDamage = False
                posttext += target.ApplyStatus("aflame")
            elif (IsSoundMove(move.Name) and user != target and target.HasAbility("Soundproof")):
                doDamage = False
                posttext += "{} is soundproof!".format(target.GetNickname())
            elif ((("Spore" in move.Name or ("Powder" in move.Name and move.Name != "Powder Snow")) or move.Name == "Leech Seed") and (target.HasType("Grass") or target.HasAbility("Overcoat"))):
                doDamage = False
                posttext += "But it failed to affect {}...".format(target.GetNickname())
            elif (user.GetTrainerType() == target.GetTrainerType() and GetMoveRange(move) not in [Range.Self, Range.AllAlliesAndSelf, Range.AllAllies, Range.AdjacentAlly, Range.AdjacentAllyOrSelf] and target.HasAbility("Telepathy")):                    
                doDamage = False
                posttext += "{} used telepathy to dodge the ally's attack!".format(target.GetNickname())
            #cancellation of move effects above here
            #move effects under here
            elif (name == "Splash"):
                posttext += "But nothing happened...".format(username)
            elif (name in ["Absorb", "Mega Drain", "Giga Drain", "Leech Life", "Dream Eater"]):
                healthgain += 0.5
                if (name == "Dream Eater" and not target.HasStatus("asleep")):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                    doDamage = False
            elif (name == "Draining Kiss"):
                healthgain += 0.75
            elif (name in ["Tail Whip", "Leer"]):
                posttext += target.ChangeStats(Stats.Defense, -1, user)
            elif (name in ["Rock Smash", "Razor Shell", "Crush Claw"]):
                sideeffects.append(SideEffect(user, target, Stats.Defense, -1, 0.5))
            elif (name in ["Iron Tail"]):
                sideeffects.append(SideEffect(user, target, Stats.Defense, -1, 0.3))
            elif (name == "Flame Charge"):
                sideeffects.append(SideEffect(user, user, Stats.Speed, 1))
            elif (name == "Crunch"):
                sideeffects.append(SideEffect(user, target, Stats.Defense, -1, 0.2))
            elif (name == "Rock Tomb"):
                sideeffects.append(SideEffect(user, target, Stats.Speed, -1))
            elif (name in ["Flamethrower", "Ember", "Flame Wheel", "Heat Wave", "Fire Blast"]):
                sideeffects.append(SideEffect(user, target, "burned", chance=0.1))
            elif (name in ["Lava Plume"]):
                sideeffects.append(SideEffect(user, target, "burned", chance=0.3))
            elif (name in ["Bug Buzz", "Psychic", "Acid", "Earth Power", "Flash Cannon", "Energy Ball"]):
                sideeffects.append(SideEffect(user, target, Stats.SpecialDefense, -1, chance=0.1))
            elif (name == "Shadow Ball"):
                sideeffects.append(SideEffect(user, target, Stats.SpecialDefense, -1, chance=0.2))
            elif (name == "Quiver Dance"):
                posttext += user.ChangeStats(Stats.SpecialAttack, 1, user)
                posttext += user.ChangeStats(Stats.SpecialDefense, 1, user)
                posttext += user.ChangeStats(Stats.Speed, 1, user)
            elif (name == "Venom Drench"):
                if (target.HasStatus("poisoned") or target.HasStatus("badly poisoned")):
                    posttext += target.ChangeStats(Stats.Attack, -1, user)
                    posttext += target.ChangeStats(Stats.SpecialAttack, -1, user)
                    posttext += target.ChangeStats(Stats.Speed, -1, user)
            elif (name == "Hurricane"):
                if (target.HasStatus("Airborne")):
                    power *= 2
                sideeffects.append(SideEffect(user, target, "confused", random.randint(2, 5), chance=0.3))
            elif (name == "Inferno"):
                sideeffects.append(SideEffect(user, target, "burned"))
            elif (name in ["Gust", "Twister"]):
                if (target.HasStatus("Airborne")):
                    power *= 2
            elif (name == "Defense Curl"):
                user.ApplyStatus(".curling")
                posttext += user.ChangeStats(Stats.Defense, 1, user)
            elif (name == "Echoed Voice"):
                global UsedEchoedVoice
                UsedEchoedVoice = True
                if (BattlefieldExists("Echoed Voice")):
                    power = BattlefieldEffects["Echoed Voice"]
            elif (name in ["Trick", "Switcheroo"]):
                useritem = user.GetItem()
                targetitem = target.GetItem()
                if ((useritem == None and targetitem == None) or target.HasStatus("substitute") or target.HasAbility("Sticky Hold")):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    posttext += "{}".format(target.GiveItem(useritem, True))
                    posttext += "{}".format(user.GiveItem(targetitem, True))
            elif (name in ["Play Nice", "Growl", "Baby-Doll Eyes"]):
                posttext += target.ChangeStats(Stats.Attack, -1, user)
            elif (name == "Noble Roar"):
                posttext += target.ChangeStats(Stats.Attack, -1, user)
                posttext += target.ChangeStats(Stats.SpecialAttack, -1, user)
            elif (name in ["Lunge", "Breaking Swipe"]):
                sideeffects.append(SideEffect(user, target, Stats.Attack, -1))
            elif (name in ["Mystical Fire", "Snarl"]):
                sideeffects.append(SideEffect(user, target, Stats.SpecialAttack, -1))
            elif (name == "Tickle"):
                posttext += target.ChangeStats(Stats.Attack, -1, user)
                posttext += target.ChangeStats(Stats.Defense, -1, user)
            elif (name == "Thunder Shock"):
                sideeffects.append(SideEffect(user, target, "paralyzed", chance=0.1))
            elif (name in ["Play Rough", "Aurora Beam"]):
                sideeffects.append(SideEffect(user, target, Stats.Attack, -1, chance=0.1))
            elif (name == "Breaking Swipe"):
                sideeffects.append(SideEffect(user, target, Stats.Attack, -1))
            elif (name == "Copycat"):
                move.PP -= 1
                lastmove = GetLastMove(ActionLog, ignorepp=True, ignoremoves=["Copycat"])
                if (lastmove == None):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    newtargets = GetTargets(user, GetMoveRange(lastmove), True)
                    if (GetMoveRange(lastmove) in [Range.Adjacent, Range.AdjacentAlly, Range.AdjacentAllyOrSelf, Range.AdjacentFoe, Range.Any, Range.AnyOrSelf, Range.Self, Range.All]):
                        newtargets = [random.choice(newtargets)]
                    DoMove(action, user, copy.deepcopy(lastmove), newtargets, alreadypretext=pretext + " {} copied {}! ".format(username, lastmove.Name))
                    ActionLog.append(Action(0, user.GetStat(Stats.Speed), ActionTypes.Move, user.GetTrainer(), user, GetMove(lastmove.Name), GetTrainers(newtargets), newtargets, Turn))
                    return
            elif (name in ["Bullet Seed", "Arm Thrust", "Pin Missile", "Double Slap", "Fury Swipes", "Fury Attack", "Water Shuriken", "Bone Rush", "Spike Cannon", "Comet Punch", "Rock Blast", "Scale Shot"]):
                global MultihitCount
                global MultihitMax
                repeat = True
                if (MultihitCount == None):
                    randval = random.random()
                    if (randval <= 0.35):
                        MultihitCount = 1
                    elif (randval <= 0.7):
                        MultihitCount = 2
                    elif (randval <= 0.85):
                        MultihitCount = 3
                    else:
                        MultihitCount = 4
                    if (user.HasAbility("Skill Link")):
                        MultihitCount = 4
                    MultihitMax = MultihitCount
                posttext += "Hit {} time(s)!".format(MultihitMax - MultihitCount + 1)
                if (MultihitCount != 0):
                    MultihitCount -= 1
                else:
                    if (name == "Scale Shot"):
                        posttext += user.ChangeStats(Stats.Defense, -1, self)
                        posttext += user.ChangeStats(Stats.Speed, 1, self)
                    repeat = False
                    MultihitMax = None
                    MultihitCount = None
            elif (name in ["Double Kick", "Bonemerang", "Dual Chop", "Double Hit", "Twineedle"]):
                global MultihitCount
                global MultihitMax
                repeat = True
                if (name == "Twineedle"):
                    sideeffects.append(SideEffect(user, target, "poisoned", chance=0.2))
                if (MultihitCount == None):
                    MultihitCount = 1
                    MultihitMax = MultihitCount
                posttext += "Hit {} time(s)!".format(MultihitMax - MultihitCount + 1)
                if (MultihitCount != 0):
                    MultihitCount -= 1
                else:
                    repeat = False
                    MultihitMax = None
                    MultihitCount = None
            elif (name in ["Constrict", "Bubble Beam"]):
                sideeffects.append(SideEffect(user, target, Stats.Speed, -1, chance=0.1))
            elif (name == "Rage"):
                posttext += user.ApplyStatus("raging")
            elif (name in ["Confusion", "Psybeam", "Signal Beam"]):
                sideeffects.append(SideEffect(user, target, "confused", random.randint(2, 5), chance=0.1))
            elif (name in ["Water Pulse", "Rock Climb", "Dizzy Punch"]):
                sideeffects.append(SideEffect(user, target, "confused", random.randint(2, 5), chance=0.2))
            elif (name == "Dynamic Punch"):
                sideeffects.append(SideEffect(user, target, "confused", random.randint(2, 5)))
            elif (name in ["Sharpen", "Meditate"]):
                posttext += user.ChangeStats(Stats.Attack, 1, user)
            elif (name == "Howl"):
                for mon in GetBattlers(user):
                    if (not mon.HasAbility("Soundproof")):
                        posttext += mon.ChangeStats(Stats.Attack, 1, user)
            elif (name == "Power-Up Punch"):
                sideeffects.append(SideEffect(user, user, Stats.Attack))
            elif (name == "Swords Dance"):
                posttext += user.ChangeStats(Stats.Attack, 2, user)
            elif (name in ["Poison Sting", "Poison Jab", "Sludge", "Gunk Shot"]):
                sideeffects.append(SideEffect(user, target, "poisoned", chance=0.3))
            elif (name == "Sandstorm"):
                posttext += ApplyWeather("sandstorm", 5)
            elif (name in ["Rain Dance", "Healing Spring"]):
                posttext += ApplyWeather("rainy", 5)
                if (name == "Healing Spring"):
                    user.ApplyStatus("aqua ring")
            elif (name == "Hail"):
                posttext += ApplyWeather("hail", 5)
            elif (name == "Sunny Day"):
                posttext += ApplyWeather("sunny", 5)
            elif (name == "Last Resort"):
                if (not LastResortWorks(ActionLog, user)):
                    doDamage = False
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Spite"):
                lastmove = GetLastMove(ActionLog, target)
                reduction = (min(4, lastmove.PP) if lastmove != None else 0)
                if (lastmove == None or reduction == 0 or lastmove.Name == "Struggle" or target.GetMoveByName(lastmove.Name) == None):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    target.GetMoveByName(lastmove.Name).PP -= reduction
                    posttext += "{}'s {}'s PP was reduced by {}!".format(target.GetNickname(), lastmove.Name, reduction) 
            elif (name == "Double Team"):
                posttext += user.ChangeStats(Stats.Evasion, 1, user)
            elif (name == "Struggle"):
                user.AdjustHealth(user.GetStat(Stats.Health) * -1.0/4.0, directdamage=True)
                posttext += "{} took recoil damage!".format(username)
            elif (name == "Minimize"):
                user.ApplyStatus(".minimized")
                posttext += user.ChangeStats(Stats.Evasion, 2, user)
            elif (name == "Sticky Web"):
                posttext += ApplyEffect(user, "sticky web", 1, True)
            elif (name == "Toxic Spikes"):
                if ("toxic spikes" in GetFieldEffects(target).keys()):
                    if (GetFieldEffects(target)["toxic spikes"] == 2):
                        posttext += "But it failed!"
                    elif (GetFieldEffects(target)["toxic spikes"] == 1):
                        del GetFieldEffects(target)["toxic spikes"]
                        posttext += ApplyEffect(user, "toxic spikes", 2, True)
                else:
                    posttext += ApplyEffect(user, "toxic spikes", 1, True)
            elif (name == "Spikes"):
                if ("spikes" in GetFieldEffects(target).keys()):
                    if (GetFieldEffects(target)["spikes"] == 3):
                        posttext += "But it failed!"
                    else:
                        spikescount = GetFieldEffects(target)["spikes"]
                        del GetFieldEffects(target)["spikes"]
                        posttext += ApplyEffect(user, "spikes", spikescount + 1, True)
                else:
                    posttext += ApplyEffect(user, "spikes", 1, True)
            elif (name in ["String Shot", "Cotton Spore"]):
                posttext += target.ChangeStats(Stats.Speed, -2, user)
            elif (name in ["Sand Attack", "Smokescreen"]):
                posttext += target.ChangeStats(Stats.Accuracy, -1, user)
            elif (name == "Growth"):
                posttext += user.ChangeStats(Stats.Attack, 1, user)
                posttext += user.ChangeStats(Stats.SpecialAttack, 1, user)
            elif (name == "Harden" or name == "Withdraw"):
                posttext += user.ChangeStats(Stats.Defense, 1, user)
            elif (name == "Wrap"):
                sideeffects.append(SideEffect(user, target, ".wrappedby", user))
                sideeffects.append(SideEffect(user, target, "wrapped", random.randint(4, 5)))
            elif (name == "Fire Spin"):
                sideeffects.append(SideEffect(user, target, ".firespunby", user))
                sideeffects.append(SideEffect(user, target, "firespun", random.randint(4, 5)))
            elif (name == "Whirlpool"):
                if (target.HasStatus("diving")):
                    power *= 2
                sideeffects.append(SideEffect(user, target, ".whirlpooledby", user))
                sideeffects.append(SideEffect(user, target, "whirlpooled", random.randint(4, 5)))
            elif (name == "Sand Tomb"):
                sideeffects.append(SideEffect(user, target, ".entombedby", user))
                sideeffects.append(SideEffect(user, target, "entombed", random.randint(4, 5)))
            elif (name == "Leech Seed"):
                posttext += target.ApplyStatus("seeded", (Battlers().index(user), user), user)
            elif (name == "Mud Sport"):
                posttext += ApplyBattlefieldEffects("Mud Sport", 5)
            elif (name == "Water Sport"):
                posttext += ApplyBattlefieldEffects("Water Sport", 5)
            elif (name in ["Razor Leaf", "Night Slash", "Slash", "Drill Run", "Air Cutter", "Shadow Claw", "Aqua Cutter", "Stone Edge", "Psycho Cut", "Cross Chop", "Leaf Blade", "Karate Chop"]):
                critstage += 1
            elif (name in ["Heart Stamp", "Iron Head", "Astonish", "Bite", "Headbutt", "Stomp", "Rock Slide", "Air Slash", "Zing Zap", "Rolling Kick", "Needle Arm", "Icicle Crash"]):
                sideeffects.append(SideEffect(user, target, "flinching", chance=0.3))
            elif (name in ["Fake Out", "Legacy", "First Impression"]):
                if (Turn == 1 or (Turn - user.GetTurnSwitchedIn() <= 1)):
                    if (name == "Fake Out"):
                        sideeffects.append(SideEffect(user, target, "flinching"))
                    else:
                        posttext += target.ApplyStatus("paralyzed", 1, user)
                        target.ApplyStatus("flinching", 1, user)
                else:
                    posttext += "But it failed!"
                    doDamage = False
                    action.ChangeSuccess(False)
            elif (name in ["Leaf Storm", "Draco Meteor"]):
                posteffects.append(SideEffect(user, user, Stats.SpecialAttack, -2))
            elif (name == "Hammer Arm"):
                posteffects.append(SideEffect(user, user, Stats.Speed, -1))
            elif (name == "Superpower"):
                posteffects.append(SideEffect(user, user, Stats.Attack, -1))
                posteffects.append(SideEffect(user, user, Stats.Defense, -1))
            elif (name in ["Close Combat", "Headlong Rush"]):
                posteffects.append(SideEffect(user, user, Stats.Defense, -1))
                posteffects.append(SideEffect(user, user, Stats.SpecialDefense, -1))
            elif (name == "Bubble"):
                sideeffects.append(SideEffect(user, target, Stats.Speed, -1, chance=0.1))
            elif (name in ["Supersonic", "Confuse Ray", "Sweet Kiss", "Teeter Dance"]):
                posttext += target.ApplyStatus("confused", random.randint(2, 5), user)
            elif (name == "Swagger"):
                posttext += target.ApplyStatus("confused", random.randint(2, 5), user)
                posttext += target.ChangeStats(Stats.Attack, 2, user)
            elif (name == "Flatter"):
                posttext += target.ApplyStatus("confused", random.randint(2, 5), user)
                posttext += target.ChangeStats(Stats.SpecialAttack, 2, user)
            elif (name in ["Misty Terrain", "Electric Terrain", "Grassy Terrain", "Gravity"]):
                posttext += ApplyBattlefieldEffects(name, 5)
            elif (name in ["Flail", "Reversal"]):
                percent = user.GetHealth() / user.GetStat(Stats.Health)
                if (percent >= .6875):
                    power = 20
                elif (percent <= .6875 and percent > .3542):
                    power = 40
                elif (percent <= .3542 and percent > .2083):
                    power = 80
                elif (percent <= .2083 and percent > .1042):
                    power = 100
                elif (percent <= .1042 and percent > .0417):
                    power = 150
                else:
                    power = 200
            elif (name == "Mud-Slap"):
                sideeffects.append(SideEffect(user, target, Stats.Accuracy, -1))
            elif (name in ["Leaf Tornado", "Octazooka"]):
                sideeffects.append(SideEffect(user, target, Stats.Accuracy, -1, 0.5))
            elif (name in ["Mud Bomb", "Mirror Shot", "Muddy Water"]):
                sideeffects.append(SideEffect(user, target, Stats.Accuracy, -1, 0.3))
            elif (name == "Bind"):
                sideeffects.append(SideEffect(user, target, ".boundby", user))
                sideeffects.append(SideEffect(user, target, "bound", random.randint(4, 5)))
            elif (name == "Clamp"):
                sideeffects.append(SideEffect(user, target, ".clampedby", user))
                sideeffects.append(SideEffect(user, target, "clamped", random.randint(4, 5)))
            elif (name == "Infestation"):
                sideeffects.append(SideEffect(user, target, ".infestedby", user))
                sideeffects.append(SideEffect(user, target, "infested", random.randint(4, 5)))
            elif (name == "ERROR"):
                posttext += "This move should not show up. If it does, let me know."
            elif (name == "Charge"):
                posttext += user.ChangeStats(Stats.SpecialDefense, 1, user)
                posttext += user.ApplyStatus("charged")
            elif (name == "Energize"):
                posttext += user.ChangeStats(Stats.SpecialAttack, 1, user)
                posttext += user.ChangeStats(Stats.Attack, 1, user)
                posttext += user.ApplyStatus("charged")
            elif (name in ["Covet", "Thief"]):
                useritem = user.GetItem()
                targetitem = target.GetItem()
                if (useritem == None and targetitem != None and not target.HasAbility("Sticky Hold")):
                    posttext += target.TakeItem()
                    posttext += user.GiveItem(targetitem)
            elif (name in ["Guillotine", "Fissure", "Horn Drill", "Sheer Cold"]):
                accuracy = user.GetLevel() - target.GetLevel() + 30
                if (user.HasStatus(".lockingon") and target.HasStatus("locked on") 
                    or user.HasStatus(".mindreading") and target.HasStatus("mind read")
                    or user.HasAbility("No Guard") 
                    or target.HasAbility("No Guard")):
                    accuracy = 100
                if (target.HasAbility("Sturdy")
                    or target.HasType("Ice") and name == "Sheer Cold"
                    or accuracy < 30
                    or random.randint(1, 100) > accuracy 
                    or (name == "Fissure" and not IsGrounded(target))
                    or (name in ["Guillotine", "Horn Drill"] and target.HasType("Ghost"))):
                    posttext += "But it failed!"
                    doDamage = False
                    action.ChangeSuccess(False)
                else:
                    posttext += "It's a one-hit KO!"
                    fixeddamage = 999
            elif (name == "Taunt"):
                posttext += target.ApplyStatus("taunted", 4, user)
            elif (name in ["Discharge", "Body Slam", "Spark", "Dragon Breath"]):
                sideeffects.append(SideEffect(user, target, "paralyzed", chance=0.3))
            elif (name == "Rollout"):
                user.ApplyStatus(".usedrollout")
                if (user.HasStatus("rollout")):
                    count = user.GetStatusCount("rollout")
                    power = 30 * pow(2, count)
                    if (count == 4):
                        user.ClearStatus("rollout")
                    else:
                        user.ApplyStatus("rollout", count + 1, overwrite=True)
                else:
                    user.ApplyStatus("rollout")
            elif (name == "Ice Ball"):
                user.ApplyStatus(".usediceball")
                if (user.HasStatus("ice ball")):
                    count = user.GetStatusCount("ice ball")
                    power = 30 * pow(2, count)
                    if (count == 4):
                        user.ClearStatus("ice ball")
                    else:
                        user.ApplyStatus("ice ball", count + 1, overwrite=True)
                else:
                    user.ApplyStatus("ice ball")
            elif (name in ["Icy Wind", "Electroweb", "Mud Shot", "Low Sweep"]):
                sideeffects.append(SideEffect(user, target, Stats.Speed, -1))
            elif (name in ["Wood Hammer", "Brave Bird", "Double-Edge", "Flare Blitz"]):
                recoil += 1.0/3.0
                if (name == "Flare Blitz"):
                    sideeffects.append(SideEffect(user, target, "burned", chance=0.1))
            elif (name in ["Take Down", "Submission"]):
                recoil += 1.0/4.0
            elif (name == "Head Smash"):
                recoil += 1.0/2.0
            elif (name == "Encore"):
                posttext += target.ApplyStatus("encored", 4, user)
            elif (name == "Smog"):
                sideeffects.append(SideEffect(user, target, "poisoned", chance=0.4))
            elif (name in ["Twister", "Zen Headbutt", "Dark Pulse"]):
                sideeffects.append(SideEffect(user, target, "flinching", chance=0.2))
            elif (name in ["Hyper Fang", "Bone Club", "Extrasensory"]):
                sideeffects.append(SideEffect(user, target, "flinching", chance=0.1))
            elif (name == "Bide"):
                subtractpp = False
                doDamage = False
                if (user.GetStatusCount("biding") == 0):
                    posttext += "{} is storing energy!".format(username)
                    user.ApplyStatus("biding")
                elif (user.GetStatusCount("biding") >= 3):
                    if (user.GetStatusCount(".bidingdamage") != 0):
                        fixeddamage = user.GetStatusCount(".bidingdamage")[0] * 2.0
                        doDamage = True
                        posttext += "{} unleashed energy!".format(username)
                        subtractpp = True
                        target = user.GetStatusCount(".bidingdamage")[1]
                        if (target not in GetBattlers(user, True)):
                            target = random.choice(GetBattlers(user, True))
                            if (target == None):
                                posttext += "But it failed!"
                                action.ChangeSuccess(False)
                    user.ClearStatus("biding")
            elif (name == "Foresight"):
                posttext += target.ApplyStatus("foreseen", applier=user)
            elif (name == "Rapid Spin"):
                sideeffects.append(SideEffect(user, user, Stats.Speed))
            elif (name == "Focus Energy"):
                posttext += user.ApplyStatus("focused")
            elif (name == "Miracle Eye"):
                posttext += target.ApplyStatus("miraculously seen", applier=user)
            elif (name == "Incinerate"):
                if (IsBerry(target.GetItem())):
                    posttext += target.GiveItem(None, True)
            elif (name == "Psywave"):
                fixeddamage = max(1, math.floor(user.GetLevel() * (random.randint(0, 100) + 50)/100.0))
            elif (name == "Dragon Rage"):
                fixeddamage = 40
            elif (name == "Sonic Boom"):
                fixeddamage = 20
            elif (name in ["Powder Snow", "Ice Beam"]):
                sideeffects.append(SideEffect(user, target, "frozen", chance=0.1))
            elif (name == "Slow Freeze"):
                posttext += target.ApplyStatus("frozen", 1, user)
            elif (name == "Hone Claws"):
                posttext += user.ChangeStats(Stats.Attack, 1, user)
                posttext += user.ChangeStats(Stats.Accuracy, 1, user)
            elif (name == "Odor Sleuth"):
                posttext += target.ApplyStatus("sniffed out", applier=user)
            elif (name in ["Endure", "Protect", "Wide Guard", "Detect", "Enshroud", "Deathless", "Splinter Shield", "Spiky Shield", "Quick Guard", "Silk Trap", "Baneful Bunker", "Obstruct"]):
                protectioncount = user.GetStatusCount(".protections")
                successrate = 1.0 / max((user.GetStatusCount(".protections") * 3), 1)
                if (successrate >= random.random()):
                    if (name in "Endure"):
                        posttext += user.ApplyStatus("enduring")
                    elif (name == "Deathless"):
                        posttext += user.ApplyStatus("deathless")
                    elif (name in ["Protect", "Detect", "Splinter Shield", "Enshroud", "Silk Trap", "Obstruct"]):
                        if (name == "Enshroud"):
                            user.ApplyStatus(".enshrouded")
                        elif (name == "Splinter Shield"):
                            user.ApplyStatus(".splintering")
                        elif (name == "Silk Trap"):
                            user.ApplyStatus(".silked")
                        elif (name == "Baneful Bunker"):
                            user.ApplyStatus(".baneful")
                        elif (name == "Spiky Shield"):
                            user.ApplyStatus(".spiky")
                        elif (name == "Obstruct"):
                            user.ApplyStatus(".obstructing")
                        posttext += user.ApplyStatus("protected")
                    elif (name == "Wide Guard"):
                        posttext += ApplyEffect(user, "wide guard", 1, False)
                    elif (name == "Wide Guard"):
                        posttext += ApplyEffect(user, "quick guard", 1, False)

                    user.ApplyStatus(".protections", protectioncount + 1, user, True)
                else: 
                    posttext += "But it failed!"
                    user.ClearStatus(".protections")
                    action.ChangeSuccess(False)
            elif (name == "Fury Cutter"):
                cutcount = user.GetStatusCount(".furycutter")
                power = 40 * pow(2, cutcount)
                user.ApplyStatus(".furycutter", cutcount + 1, user, True)
            elif (name in ["Thunder Wave", "Stun Spore", "Glare", "Zap Cannon"]):
                if (target.HasType("Ground") and name == "Thunder Wave"):
                    posttext += "It had no effect..."
                else:
                    posttext += target.ApplyStatus("paralyzed", applier=user)
            elif (name == "Lick"):
                sideeffects.append(SideEffect(user, target, "paralyzed", chance=0.3))
            elif (name in ["Hypnosis", "Sleep Powder", "Spore", "Sing", "Grass Whistle", "Lovely Kiss"]):
                posttext += target.ApplyStatus("asleep", random.randint(2, 4), user)
            elif (name in ["Will-O-Wisp", "Steady Flame"]):
                posttext += target.ApplyStatus("burned", 1, user)
            elif (name in ["Poison Powder", "Poison Gas"]):
                posttext += target.ApplyStatus("poisoned", applier=user)
            elif (name in ["Whirlwind", "Roar"]):
                if (WildBattle):
                    Fled = True
                else:
                    targettrainer = target.GetTrainer()
                    newlist = []
                    for mon in targettrainer.GetTeam():
                        if (mon.Health >= 1 and mon != target):
                            newlist.append(mon)
                    if (len(newlist) == 0 or target.HasStatus("ingrained")):
                        posttext += "But it failed!"
                        action.ChangeSuccess(False)
                    else:
                        randpkmn = random.choice(newlist)
                        trainer = target.GetTrainer()
                        team = trainer.GetTeam()
                        trainer.ShiftTeam(team.index(target), team.index(randpkmn), True)
                        posttext += "{} was forced out!".format(randpkmn.GetNickname())
                        SwitchInEffects(randpkmn)
            elif (name == "Disable"):
                lastmove = GetLastMove(ActionLog, target)
                if (lastmove != None):
                    posttext += target.ApplyStatus("disabled", 4, user)
                    target.ApplyStatus(".disabling", lastmove.Name)
                elif (name == "Disable"):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Disabling Poke"):
                lastmove = GetLastMove(ActionLog, target)
                if (lastmove != None):
                    sideeffects.append(SideEffect(user, target, "disabled", 4))
                    sideeffects.append(SideEffect(user, target, ".disabling", lastmove.Name))
            elif (name == "Counter"):
                countercount = user.GetStatusCount(".countering")
                if (countercount == None or countercount[1] not in Battlers()):
                    doDamage = False
                    user.ClearStatus(".countering")
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    target = countercount[1]
                    fixeddamage = countercount[0]
                user.ClearStatus(".countering")
            elif (name == "Liberage"):
                posttext += "{} fights for liberty!".format(user.GetNickname())
                for mon in Battlers():
                    mon.ClearStatus("paralyzed")
                    mon.ClearStatus("disabled")
                    mon.ClearStatus("confused")
                    mon.ClearStatus("asleep")
                    mon.ClearStatus("frozen")
                    mon.ResetStatChanges()
                user.ApplyStatus(".liberating")
            elif (name == "Mirror Coat"):
                countercount = user.GetStatusCount(".mirrorcoat")
                if (countercount == None or countercount[1] not in Battlers()):
                    doDamage = False
                    user.ClearStatus(".mirrorcoat")
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    target = countercount[1]
                    fixeddamage = countercount[0]
                user.ClearStatus(".mirrorcoat")
            elif (name == "Sweet Scent"):
                posttext += target.ChangeStats(Stats.Evasion, -2, user)
            elif (name in ["Night Shade", "Seismic Toss"]):
                fixeddamage = user.GetLevel()
            elif (name == "Uproar"):
                targets = GetTargets(user, range = Range.AdjacentFoe)
                if (targets == []):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    target = random.choice(targets)
                    if (user.HasStatus("uproaring")):
                        posttext += "{} continues the Uproar!".format(username)
                    else:
                        posttext += "{} started an Uproar!".format(username)
                        user.ApplyStatus("uproaring", 3)
                        for mon in Battlers():
                            clearstatus = mon.ClearStatus("asleep")
                            posttext += ("" if clearstatus == None else clearstatus)
            elif (name == "Bulldoze"):
                sideeffects.append(SideEffect(user, target, Stats.Speed, -1))
            elif (name == "Metal Claw"):
                sideeffects.append(SideEffect(user, user, Stats.Attack, 1, 0.1))
            elif (name == "Charge Beam"):
                sideeffects.append(SideEffect(user, user, Stats.SpecialAttack, 1, 0.7))
            elif (name == "Fiery Dance"):
                sideeffects.append(SideEffect(user, user, Stats.SpecialAttack, 1, 0.5))
            elif (name == "Steel Wing"):
                sideeffects.append(SideEffect(user, user, Stats.Defense, 1, 0.1))
            elif (name == "Refresh"):
                user.ClearStatus("burned")
                user.ClearStatus("badly poisoned")
                user.ClearStatus("poisoned")
                user.ClearStatus("paralyzed")
                posttext += "{} became refreshed!".format(username)
            elif (name == "Clear Mind"):
                target.ClearStatus("burned")
                target.ClearStatus("badly poisoned")
                target.ClearStatus("poisoned")
                target.ClearStatus("paralyzed")
                target.ClearStatus("asleep")
                target.ClearStatus("frozen")
                target.ResetStatChanges()
                posttext += "{}'s mind was cleared!".format(username)
            elif (name == "Electro Ball"):
                percent = target.GetStat(Stats.Speed) / user.GetStat(Stats.Speed)
                if (percent > 1):
                    power = 40
                elif (percent > .5):
                    power = 60
                elif (percent > .3333):
                    power = 80
                elif (percent > .25):
                    power = 120
                else:
                    power = 150
            elif (name == "Mist"):
                posttext += ApplyEffect(user, "mist", 5, False)
            elif (name == "Clear Smog"):
                target.ResetStatChanges()
            elif (name == "Haze"):
                for mon in Battlers():
                    mon.ResetStatChanges()
            elif (name == "Sludge Wave"):
                sideeffects.append(SideEffect(user, target, "poisoned", chance=0.1))
            elif (name in ["Poison Tail", "Cross Poison"]):
                critstage += 1
                sideeffects.append(SideEffect(user, target, "poisoned", chance=0.1))
                if (name == "Poison Tail" and name in moveboosts):
                    power += 15
                    if (target.HasType("Normal")):
                        power *= 2
                    if ("toxic spikes" in GetFieldEffects(target).keys()):
                        if (GetFieldEffects(target)["toxic spikes"] == 1):
                            del GetFieldEffects(target)["toxic spikes"]
                            posttext += ApplyEffect(user, "toxic spikes", 2, True)
                    else:
                        posttext += ApplyEffect(user, "toxic spikes", 1, True)
            elif (name == "Teleport"):
                usertrainer = user.GetTrainer()
                newlist = []
                for mon in usertrainer.GetTeam():
                    if (mon.Health >= 1 and mon not in Battlers()):
                        newlist.append(mon)
                if (len(newlist) == 0):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                elif (user in FriendlyBattlers()):
                    renpy.say(None, "Pick a Pokémon to switch in.")
                    switchCommand = renpy.call_screen('switch', user.GetTrainer(), True)
                    newPokemon = user.GetTrainer().GetTeam()[switchCommand]
                    if (newPokemon.GetHealth() == 0):
                        renpy.say(None, "{} has fainted, and cannot fight!".format(newPokemon.GetNickname()))
                        DoMove(action, user, move, [user])
                        return
                    elif (newPokemon in Battlers()):
                        renpy.show_screen("battleui")
                        renpy.say(None, "{} is already in battle!".format(newPokemon.GetNickname()))
                        DoMove(action, user, move, [user])
                        return
                    team = usertrainer.GetTeam()
                    usertrainer.ShiftTeam(team.index(user), switchCommand, True)
                    posttext += "{} teleported out, and {} switched in!".format(user.GetNickname(), newPokemon.GetNickname())
                    SwitchInEffects(newPokemon)
                else:
                    newPokemon = random.choice(newlist)
                    team = usertrainer.GetTeam()
                    usertrainer.ShiftTeam(team.index(user), team.index(newPokemon), True)
                    posttext += "{} teleported out, and {} switched in!".format(user.GetNickname(), newPokemon.GetNickname())
                    SwitchInEffects(newPokemon)
            elif (name in ["U-turn", "Flip Turn", "Parting Shot"]):
                usertrainer = user.GetTrainer()
                newlist = []
                for mon in usertrainer.GetTeam():
                    if (mon.Health >= 1 and mon not in Battlers()):
                        newlist.append(mon)
                if (len(newlist) != 0):
                    if (name == "Parting Shot"):
                        posttext += target.ChangeStats(Stats.Attack, -1, self)
                        posttext += target.ChangeStats(Stats.SpecialAttack, -1, self)
                    renpy.say(None, "Pick a Pokémon to switch in.")
                    switchCommand = renpy.call_screen('switch', user.GetTrainer(), True)
                    newPokemon = user.GetTrainer().GetTeam()[switchCommand]
                    if (newPokemon.GetHealth() == 0):
                        renpy.say(None, "{} has fainted, and cannot fight!".format(newPokemon.GetNickname()))
                        DoMove(action, user, move, [user])
                        return
                    elif (newPokemon in Battlers()):
                        renpy.show_screen("battleui")
                        renpy.say(None, "{} is already in battle!".format(newPokemon.GetNickname()))
                        DoMove(action, user, move, [user])
                        return
                    team = usertrainer.GetTeam()
                    usertrainer.ShiftTeam(team.index(user), switchCommand, True)
                    posttext += "{} switched out, and {} switched in!".format(user.GetNickname(), newPokemon.GetNickname())
                    SwitchInEffects(newPokemon)
            elif (name == "Curse"):
                if (not user.HasType("Ghost")):
                    posttext += user.ChangeStats(Stats.Attack, 1, user)
                    posttext += user.ChangeStats(Stats.Defense, 1, user)
                    posttext += user.ChangeStats(Stats.Speed, -1, user)
                else:
                    targets = GetTargets(user, Range.Any, True)
                    if (targets == []):
                        posttext += "But it failed!"
                        action.ChangeSuccess(False)
                    else:
                        target = random.choice(targets)
                        user.AdjustHealth(-user.GetStat(Stats.Health) * 0.5)
                        posttext += target.ApplyStatus("cursed")
            elif (name == "Screech"):
                posttext += target.ChangeStats(Stats.Defense, -2, user)
            elif (name == "Eerie Impulse"):
                posttext += target.ChangeStats(Stats.SpecialAttack, -2, user)
            elif (name in ["Charm", "Feather Dance"]):
                posttext += target.ChangeStats(Stats.Attack, -2, user)
            elif (name == "Scary Face"):
                posttext += target.ChangeStats(Stats.Speed, -2, user)
            elif (name in ["Metal Sound", "Fake Tears"]):
                posttext += target.ChangeStats(Stats.SpecialDefense, -2, user)
            elif (name == "Amnesia"):
                posttext += user.ChangeStats(Stats.SpecialDefense, 2, user)
            elif (name == "Acid Spray"):
                sideeffects.append(SideEffect(user, target, Stats.SpecialDefense, -2))
            elif (name in ["Iron Defense", "Acid Armor"]):
                posttext += user.ChangeStats(Stats.Defense, 2)
            elif (name in ["Barrier", "Cotton Guard"]):
                posttext += user.ChangeStats(Stats.Defense, 3)
            elif (name == "Torment"):
                posttext += target.ApplyStatus("tormented")
            elif (name == "Lucky Chant"):
                posttext += ApplyEffect(user, "lucky", 5, False)
            elif (name in ["Struggle Bug", "Spirit Break"]):
                sideeffects.append(SideEffect(user, target, Stats.SpecialAttack, -1))
            elif (name == "Helping Hand"):
                if (len(GetBattlers(user)) == 1):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    helpcount = target.GetStatusCount("helped")                
                    posttext += target.ApplyStatus("helped", helpcount + 1, user, True)
            elif (name == "Yawn"):
                posttext += target.ApplyStatus("drowsy", 2)
            elif (name in ["Rest", "Chrysalize"]):
                user.ApplyStatus("asleep", 3, user, True)
                if (user.HasStatus("asleep") and user.GetHealthPercentage() < 1.0):
                    user.ClearStatus("everything", True)
                    posttext += user.ApplyStatus("asleep", 3, user)
                    user.AdjustHealth(999)
                    if (name == "Chrysalize"):
                        posttext += user.ChangeStats(Stats.Defense, 1, user)
                        posttext += user.ChangeStats(Stats.SpecialDefense, 1, user)
                else:
                    user.ClearStatus("asleep")
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Facade"):
                for affliction in normalstatuses:
                    if (user.HasStatus(affliction)):
                        power = move.Power * 2
            elif (name in ["Agility", "Rock Polish"]):
                posttext += user.ChangeStats(Stats.Speed, 2, user)
            elif (name == "Autotomize"):
                posttext += user.ChangeStats(Stats.Speed, 2, user)
                posttext += user.ApplyStatus("nimble", user.GetStatusCount("nimble") + 1, user, overwrite=True)
            elif (name == "Wing It"):
                posttext += ActivateMoody(user)
            elif (name == "Heal Pulse"):
                if (target.GetHealthPercentage() < 1):
                    target.AdjustHealth(target.GetStat(Stats.Health) / 2.0)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Floral Healing"):
                if (target.GetHealthPercentage() < 1 and not target.HasStatus("substitute")):
                    if (BattlefieldExists("Grassy Terrain")):
                        target.AdjustHealth(target.GetStat(Stats.Health) / 3.0 * 2.0)
                    else:
                        target.AdjustHealth(target.GetStat(Stats.Health) / 2.0)
                    if ("Floral Healing" in moveboosts):
                        if (BattlefieldExists("Grassy Terrain")):
                            user.AdjustHealth(target.GetStat(Stats.Health) / 3.0 * 2.0)
                        else:
                            user.AdjustHealth(target.GetStat(Stats.Health) / 2.0)
                        target.ClearStatus("burned")
                        target.ClearStatus("badly poisoned")
                        target.ClearStatus("poisoned")
                        target.ClearStatus("paralyzed")
                        target.ClearStatus("asleep")
                        target.ClearStatus("frozen")
                        user.ClearStatus("burned")
                        user.ClearStatus("badly poisoned")
                        user.ClearStatus("poisoned")
                        user.ClearStatus("paralyzed")
                        user.ClearStatus("asleep")
                        user.ClearStatus("frozen")
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Light Screen"):
                posttext += ApplyEffect(user, "light screen", 5, False)
            elif (name == "Reflect"):
                posttext += ApplyEffect(user, "reflect", 5, False)
            elif (name == "Aurora Veil"):
                if (WeatherIs("hail") or WeatherIs("snowy")):
                    posttext += ApplyEffect(user, "aurora veil", 5, False)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Trick-or-Treat"):
                if (not target.HasType("Ghost")):
                    posttext += target.ApplyStatus("trick-or-treating")
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Metallize"):
                posttext += target.ApplyStatus("metallic")
            elif (name == "Nuzzle"):
                sideeffects.append(SideEffect(user, target, "paralyzed"))
            elif (name == "Flame Burst"):
                targetpos = GetBattlers(target).index(target)
                for i, mon in enumerate(GetBattlers(target)):
                    if (abs(i - targetpos) == 1):
                        mon.AdjustHealth(-mon.GetStat(Stats.Health) / 16.0)
            elif (name == "Camouflage"):
                user.ApplyStatus("camouflaged", GetCamoType())
            elif (name == "Gyro Ball"):
                power = min(150, 25 * target.GetStat(Stats.Speed, triggerAbilities = False) / max(1, user.GetStat(Stats.Speed, triggerAbilities = False)) + 1)
            elif (name == "Wake-Up Slap"):
                if (target.HasStatus("asleep")):
                    power = move.Power * 2.0
            elif (name == "Hex"):
                if (target.HasStatus("asleep") or target.HasStatus("burned") or target.HasStatus("frozen") or target.HasStatus("poisoned") or target.HasStatus("badly poisoned")):
                    power = move.Power * 2.0
            elif (name == "Worry Seed"):
                posttext += target.ApplyStatus("worried", 1, user)
            elif (name in ["Ancient Power", "Silver Wind", "Ominous Wind"]):
                rand = random.random()
                sideeffects.append(SideEffect(user, user, Stats.Attack, 1, 0.1, rand))
                sideeffects.append(SideEffect(user, user, Stats.Defense, 1, 0.1, rand))
                sideeffects.append(SideEffect(user, user, Stats.SpecialAttack, 1, 0.1, rand))
                sideeffects.append(SideEffect(user, user, Stats.SpecialDefense, 1, 0.1, rand))
                sideeffects.append(SideEffect(user, user, Stats.Speed, 1, 0.1, rand))
            elif (name == "Tailwind"):
                ApplyEffect(user, "tailwind", 4, False)
            elif (name in ["Synthesis", "Moonlight", "Morning Sun"]):
                if (CurrentWeather == None):
                    user.AdjustHealth(user.GetStat(Stats.Health) / 2.0)
                elif (WeatherIs("sunny")):
                    user.AdjustHealth(user.GetStat(Stats.Health) * 2.0 / 3.0)
                else:
                    user.AdjustHealth(user.GetStat(Stats.Health) / 4.0)
            elif (name == "Shore Up"):
                if (WeatherIs("sandstorm")):
                    user.AdjustHealth(user.GetStat(Stats.Health) * 2.0 / 3.0)
                else:
                    user.AdjustHealth(user.GetStat(Stats.Health) / 2.0)
            elif (name == "Fire Fang"):
                sideeffects.append(SideEffect(user, target, "flinching", 1, 0.1))
                sideeffects.append(SideEffect(user, target, "burned", 1, 0.1))
            elif (name == "Thunder Fang"):
                sideeffects.append(SideEffect(user, target, "flinching", 1, 0.1))
                sideeffects.append(SideEffect(user, target, "paralyzed", 1, 0.1))
            elif (name == "Ice Fang"):
                sideeffects.append(SideEffect(user, target, "flinching", 1, 0.1))
                sideeffects.append(SideEffect(user, target, "frozen", 1, 0.1))
            elif (name == "Blizzard"):
                sideeffects.append(SideEffect(user, target, "frozen", 1, 0.1))
            elif (name == "Poison Fang"):
                sideeffects.append(SideEffect(user, target, "badly poisoned", 1, 0.5))
            elif (name == "Fire Punch"):
                sideeffects.append(SideEffect(user, target, "burned", 1, 0.1))
            elif (name == "Ice Punch"):
                sideeffects.append(SideEffect(user, target, "frozen", 1, 0.1))
            elif (name == "Thunder Punch"):
                sideeffects.append(SideEffect(user, target, "paralyzed", 1, 0.1))
            elif (name == "Thunder"):
                sideeffects.append(SideEffect(user, target, "paralyzed", 1, 0.3))
            elif (name == "Toxic"):
                posttext += target.ApplyStatus("badly poisoned", 1, user)
            elif (name == "Bad Breath"):
                haspoisonalready = target.HasStatus("badly poisoned")
                hasparalysisalready = target.HasStatus("paralyzed")
                finaltext = ""
                finaltext = target.ApplyStatus("badly poisoned", 1, user)
                if (not target.HasStatus("badly poisoned") or haspoisonalready or hasparalysisalready):
                    finaltext = target.ApplyStatus("paralyzed", 1, user)
                    if (not target.HasStatus("paralyzed") or hasparalysisalready):
                        finaltext = target.ApplyStatus("confused", random.randint(2, 5), user)
                posttext += finaltext
            elif (name == "Safeguard"):
                ApplyEffect(user, "safeguard", 5, False)
            elif (name == "Stealth Rock"):
                ApplyEffect(user, "stealthy rocks", 1, True)
            elif (name == "Endeavor"):
                if (target.GetHealth() > user.GetHealth()):
                    fixeddamage = target.GetHealth() - user.GetHealth()
            elif (name == "Force Palm"):
                sideeffects.append(SideEffect(user, target, "paralyzed", 1, .3))
            elif (name == "Hidden Power"):
                type = typeints[math.ceil(user.GetPersonality() * 17)]
            elif (name == "Aqua Ring"):
                user.ApplyStatus("aqua ring")
            elif (name == "Assurance"):
                if (target.GetDamagedThisTurn()):
                    power = move.Power * 2.0
            elif (name == "Dig"):
                if (not user.HasStatus("dug in")):
                    doDamage = False
                    user.ApplyStatus("dug in", 2, overwrite=True)
                else:
                    subtractpp = False
                    user.ClearStatus("dug in")
            elif (name in ["Fly", "Bounce"]):
                if (not user.HasStatus("airborne")):
                    doDamage = False
                    user.ApplyStatus("airborne", 2, overwrite=True)
                else:
                    subtractpp = False
                    user.ClearStatus("airborne")
            elif (name == "Dive"):
                if (not (user.HasStatus("gulping") or user.HasStatus("gorging")) and user.HasAbility("Gulp Missile")):
                    if (user.GetHealthPercentage() > 0.5):
                        posttext += user.ApplyStatus("gulping")
                    else:
                        posttext += user.ApplyStatus("gorging")
                if (not user.HasStatus("diving")):
                    doDamage = False
                    user.ApplyStatus("diving", 2, overwrite=True)
                else:
                    subtractpp = False
                    user.ClearStatus("diving")
            elif (name == "Phantom Force"):
                if (not user.HasStatus("ethereal")):
                    doDamage = False
                    user.ApplyStatus("ethereal", 2, overwrite=True)
                else:
                    subtractpp = False
                    user.ClearStatus("ethereal")
            elif (name == "Surf"):
                if (not (user.HasStatus("gulping") or user.HasStatus("gorging")) and user.HasAbility("Gulp Missile")):
                    if (user.GetHealthPercentage() > 0.5):
                        posttext += user.ApplyStatus("gulping")
                    else:
                        posttext += user.ApplyStatus("gorging")
            elif (name == "Work Up"):
                posttext += user.ChangeStats(Stats.Attack, 1)
                posttext += user.ChangeStats(Stats.SpecialAttack, 1)
            elif (name == "Calm Mind"):
                posttext += user.ChangeStats(Stats.SpecialAttack, 1)
                posttext += user.ChangeStats(Stats.SpecialDefense, 1)
            elif (name == "Bulk Up"):
                posttext += user.ChangeStats(Stats.Attack, 1)
                posttext += user.ChangeStats(Stats.Defense, 1)
            elif (name == "Coil"):
                posttext += user.ChangeStats(Stats.Attack, 1)
                posttext += user.ChangeStats(Stats.Defense, 1)
                posttext += user.ChangeStats(Stats.Accuracy, 1)
            elif (name == "Cosmic Power"):
                posttext += user.ChangeStats(Stats.Defense, 1)
                posttext += user.ChangeStats(Stats.SpecialDefense, 1)
            elif (name == "Stockpile"):
                posttext += user.ChangeStats(Stats.Defense, 1)
                posttext += user.ChangeStats(Stats.SpecialDefense, 1)
                user.ApplyStatus("stockpiled", min(user.GetStatusCount("stockpiled") + 1, 3), overwrite=True)
            elif (name == "Spit Up"):
                stockcount = user.GetStatusCount("stockpiled")
                if (stockcount != 0):
                    power = stockcount * 100
                    posttext += user.ChangeStats(Stats.Defense, -stockcount)
                    posttext += user.ChangeStats(Stats.SpecialDefense, -stockcount)
                    user.ClearStatus("stockpiled")
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Swallow"):
                stockcount = user.GetStatusCount("stockpiled")
                if (stockcount != 0):
                    if (stockcount == 1):
                        user.AdjustHealth(target.GetStat(Stats.Health) / 4.0)
                    elif (stockcount == 2):
                        user.AdjustHealth(target.GetStat(Stats.Health) / 2.0)
                    elif (stockcount == 3):
                        user.AdjustHealth(target.GetStat(Stats.Health))
                    posttext += user.ChangeStats(Stats.Defense, -stockcount)
                    posttext += user.ChangeStats(Stats.SpecialDefense, -stockcount)
                    user.ClearStatus("stockpiled")
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Dragon Dance"):
                posttext += user.ChangeStats(Stats.Attack, 1)
                posttext += user.ChangeStats(Stats.Speed, 1)
            elif (name == "Shift Gear"):
                posttext += user.ChangeStats(Stats.Attack, 1)
                posttext += user.ChangeStats(Stats.Speed, 2)
            elif (name == "Nasty Plot"):
                posttext += user.ChangeStats(Stats.SpecialAttack, 2)
            elif (name == "Venoshock"):
                if (target.HasStatus("poisoned") or target.HasStatus("badly poisoned")):
                    power = move.Power * 2.0
            elif (name in ["Low Kick", "Grass Knot"]):
                foeweight = target.GetWeight()
                if (foeweight < 10):
                    power = 20
                elif (foeweight < 25):
                    power = 40
                elif (foeweight < 50):
                    power = 60
                elif (foeweight < 100):
                    power = 80
                elif (foeweight < 200):
                    power = 100
                else:
                    power = 120
            elif (name == "Brine"):
                if (target.GetHealthPercentage() <= 0.5):
                    power = move.Power * 2.0
            elif (name == "Wish"):
                if (not EffectOnOwnField(user, "wishing star")):
                    ApplyEffect(user, "wishing star", [2, GetBattlers(user).index(user), user.GetStat(Stats.Health) / 2.0], False)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Mimic"):
                lastmove = GetLastMove(ActionLog, target)
                if (not user.HasStatus("mimicking") and lastmove != None):
                    user.ApplyStatus("mimicking", GetMove(lastmove.Name))
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Attract"):
                if (user.GetGender() == Genders.Male and target.GetGender() == Genders.Female or user.GetGender() == Genders.Female and target.GetGender() == Genders.Male):
                    posttext += target.ApplyStatus("infatuated", 1, user)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Captivate"):
                if (user.GetGender() == Genders.Male and target.GetGender() == Genders.Female or user.GetGender() == Genders.Female and target.GetGender() == Genders.Male):
                    posttext += target.ChangeStats(Stats.SpecialAttack, -2, user)
            elif (name == "Ardent Gaze"):
                posttext += target.ApplyStatus("infatuated", 1, user)
            elif (name == "Payback"):
                if (PaybackDoubles(user, target)):
                    power = move.Power * 2.0
            elif (name == "Round"):
                if (RoundDoubles(user)):
                    power = move.Power * 2.0
            elif (name == "Smack Down"):
                posttext += target.ApplyStatus("smacked down", 1, user)
            elif (name in ["Ingrain", "Bark Up"]):
                posttext += user.ApplyStatus("ingrained")
                if (name == "Bark Up"):
                    posttext += user.ChangeStats(Stats.Defense, 1)
                    posttext += user.ChangeStats(Stats.SpecialDefense, 1)
            elif (name == "Mean Look"):
                posttext += target.ApplyStatus("menaced", 1, user)
            elif (name == "Block"):
                posttext += target.ApplyStatus("blocked", 1, user)
            elif (name == "Spider Web"):
                posttext += target.ApplyStatus("webbed", 1, user)
            elif (name == "Flower Shield"):
                for mon in Battlers(True):
                    if (mon.HasType("Grass")):
                        posttext += mon.ChangeStats(Stats.Defense, 1, user)
            elif (name == "Rototiller"):
                for mon in Battlers(True):
                    if (mon.HasType("Grass") and IsGrounded(mon)):
                        posttext += mon.ChangeStats(Stats.Attack, 1, user)
                        posttext += mon.ChangeStats(Stats.SpecialAttack, 1, user)
            elif (name == "Magnetic Flux"):
                for mon in Battlers(True):
                    if (mon.HasAbility("Plus", triggersplash = False) or mon.HasAbility("Minus", triggersplash = False)):
                        posttext += mon.ChangeStats(Stats.Defense, 1, user)
                        posttext += mon.ChangeStats(Stats.SpecialDefense, 1, user)
            elif (name in ["Milk Drink", "Recover", "Soft-Boiled", "Slack Off"]):
                user.AdjustHealth(target.GetStat(Stats.Health) / 2.0)
            elif (name == "Roost"):
                user.AdjustHealth(target.GetStat(Stats.Health) / 2.0)
                user.ApplyStatus("roosted")
            elif (name == "Burial Ground"):
                posttext += ApplyBattlefieldEffects("Burial Ground", 5)
            elif (name == "Simple World"):
                posttext += ApplyBattlefieldEffects("Simple World", 5)
            elif (name == "Magnitude"):
                if (target.HasStatus("dug in")):
                    power *= 2
            elif (name == "Acupressure"):
                canraise = []
                for i in range(Stats.Attack, Stats.Evasion + 1):
                    statmod = target.GetStatChanges(i)
                    if (statmod != 6):
                        canraise.append(i)
                raising = None if len(canraise) == 0 else random.choice(canraise)
                if (raising != None):
                    posttext += target.ChangeStats(raising, 2, user)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Tearful Look"):
                posttext += target.ChangeStats(Stats.Attack, -1, user)
                posttext += target.ChangeStats(Stats.SpecialAttack, -1, user)
            elif (name in ["Explosion", "Self-Destruct"]):
                user.AdjustHealth(0, absolute=True)
            elif (name == "Pain Split"):
                newhealth = math.floor((user.GetHealth() + target.GetHealth()) / 2.0)
                user.AdjustHealth(newhealth, absolute=True)
                target.AdjustHealth(newhealth, absolute=True)
            elif (name in ["Power Trip", "Stored Power"]):
                power = 20 + user.GetTotalStatChanges() * 20
            elif (name == "Electrify"):
                posttext += target.ApplyStatus("electrified", 1, user)
            elif (name == "Ion Deluge"):
                for mon in Battlers():
                    mon.ApplyStatus("ionized", 1, user)
            elif (name == "Power Swap"):
                (userattackchange, userspattackchange) = user.GetStatChanges(Stats.Attack), user.GetStatChanges(Stats.SpecialAttack)
                (targetattackchange, targetspattackchange) = target.GetStatChanges(Stats.Attack), target.GetStatChanges(Stats.SpecialAttack)
                user.StatChanges[Stats.Attack], user.StatChanges[Stats.SpecialAttack] = targetattackchange, targetspattackchange
                target.StatChanges[Stats.Attack], target.StatChanges[Stats.SpecialAttack] = userattackchange, userspattackchange
            elif (name == "Guard Swap"):
                (userdefensechange, userspdefensechange) = user.GetStatChanges(Stats.Defense), user.GetStatChanges(Stats.SpecialDefense)
                (targetdefensechange, targetspdefensechange) = target.GetStatChanges(Stats.Defense), target.GetStatChanges(Stats.SpecialDefense)
                user.StatChanges[Stats.Defense], user.StatChanges[Stats.SpecialDefense] = targetdefensechange, targetspdefensechange
                target.StatChanges[Stats.Defense], target.StatChanges[Stats.SpecialDefense] = userdefensechange, userspdefensechange
            elif (name == "Embargo"):
                posttext += target.ApplyStatus("embargoed", 5, user)
            elif (name == "Weather Ball"):
                if (CurrentWeather != None):
                    power *= 2.0
                    if (WeatherIs("sunny")):
                        type = "Fire"
                    elif (WeatherIs("rainy")):
                        type = "Water"
                    elif (WeatherIs("sandstorm")):
                        type = "Rock"
                    elif (WeatherIs("hail")):
                        type = "Ice"
            elif (name in ["Brick Break", "Psychic Fangs"]):
                if (EffectOnOwnField(target, "reflect")):
                    del GetFieldEffects(target)["reflect"]
                if (EffectOnOwnField(target, "light screen")):
                    del GetFieldEffects(target)["light screen"]
                if (EffectOnOwnField(target, "aurora veil")):
                    del GetFieldEffects(target)["aurora veil"]
            elif (name == "Healing Wish"):
                ApplyEffect(user, "healing wish", GetBattlers(user).index(user), False)
                user.AdjustHealth(0, absolute=True)
            elif (name == "Future Sight"):
                if (alreadypretext != "The vision came true!"):
                    doDamage = False
                    ApplyEffect(target, "future sight", (Turn, GetBattlers(target).index(target), user), False)
            elif (name == "Laser Focus"):
                posttext += user.ApplyStatus("laser focused", 2, user)
            elif (name == "Mirror Move"):
                move.PP -= 1
                lastmove = GetLastMove(ActionLog, target=user, ignorepp=True)
                if (lastmove == None):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    newtargets = [target]
                    if (GetMoveRange(lastmove) not in [Range.Adjacent, Range.AdjacentAlly, Range.AdjacentAllyOrSelf, Range.AdjacentFoe, Range.Any, Range.AnyOrSelf, Range.Self, Range.All]):
                        newtargets = GetTargets(user, GetMoveRange(lastmove))
                    DoMove(action, user, copy.deepcopy(lastmove), newtargets, alreadypretext=pretext + " {} mirrored {}! ".format(username, lastmove.Name))
                    return
            elif (name == "Destiny Bond"):
                if (dawnbattle):
                    posttext += "Your destiny diverges from Altaria, and cannot be bound!"
                else:
                    user.ApplyStatus("bound to destiny")
            elif (name == "Sky Attack"):
                if (not user.HasStatus("cloaked in light")):
                    doDamage = False
                    posttext += user.ApplyStatus("cloaked in light")
                else:
                    critstage += 1
                    sideeffects.append(SideEffect(user, target, "flinching", chance=0.3))
                    user.ClearStatus("cloaked in light")
            elif (name == "Solar Beam"):
                if (not (user.HasStatus("charging light") or WeatherIs("sunny"))):
                    doDamage = False
                    posttext += user.ApplyStatus("charging light")
                else:
                    user.ClearStatus("charging light")
            elif (name == "Skull Bash"):
                if (not (user.HasStatus("hardheaded"))):
                    doDamage = False
                    posttext += user.ChangeStats(Stats.Defense, 1, user)
                    posttext += user.ApplyStatus("hardheaded")
                else:
                    user.ClearStatus("hardheaded")
            elif (name == "Razor Wind"):
                if (not user.HasStatus("whipping up winds")):
                    doDamage = False
                    posttext += user.ApplyStatus("whipping up winds")
                else:
                    critstage += 1
                    user.ClearStatus("whipping up winds")
            elif (name == "Tri Attack"):
                ailment = "burned"
                randnum = random.random()
                if (randnum < 1.0/3.0):
                    ailment = "paralyzed"
                elif (randnum < 2.0 /3.0):
                    ailment = "frozen"
                sideeffects.append(SideEffect(user, target, ailment, chance=0.2))
            elif (name == "Earthquake"):
                if (target.HasStatus("dug in")):
                    power *= 2
            elif (name == "Moonblast"):
                sideeffects.append(SideEffect(user, target, Stats.SpecialAttack, -2, chance=0.3))
            elif (name == "Magnet Rise"):
                user.ApplyStatus("levitating", count=5)
            elif (name == "Perish Song"):
                if (dawnbattle):
                    posttext += "The Altaria's angelic cry cancels out the Perish Song!"
                else:
                    for mon in Battlers():
                        mon.ApplyStatus("perishing", count=4, applier=user)
            elif (name == "Sucker Punch"):
                validmove = False
                for oppaction in CurrentActions[CurrentActions.index(action):]:
                    if (oppaction.GetActionType() == ActionTypes.Move and oppaction.GetUser() == target and oppaction.GetMove().Category in ["Physical", "Special"]):
                        validmove = True
                if (not validmove):
                    doDamage = False
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name in ["Water Spout", "Eruption"]):
                power = user.GetHealthPercentage() * 150.0 
            elif (name == "Petal Dance"):
                target = random.choice(GetTargets(user, Range.AdjacentFoe))
                if (not user.HasStatus("petal dancing")):
                    user.ApplyStatus("petal dancing", random.choice([3, 4]))
            elif (name == "Pollen Puff"):
                if (target in GetBattlers(user)):
                    doDamage = False
                    if (target.GetHealthPercentage() < 1):
                        target.AdjustHealth(target.GetStat(Stats.Health) / 2.0)
                    else:
                        posttext += "But it failed!"
                        action.ChangeSuccess(False)
            elif (name == "Aromatherapy"):
                if (mon in FriendlyBattlers()):
                    for trainer in FriendlyTrainers():
                        for target in trainer.GetTeam():
                            target.ClearStatus("burned")
                            target.ClearStatus("badly poisoned")
                            target.ClearStatus("poisoned")
                            target.ClearStatus("paralyzed")
                            target.ClearStatus("asleep")
                            target.ClearStatus("frozen")
                else:
                    for trainer in EnemyTrainers():
                        for target in trainer.GetTeam():
                            target.ClearStatus("burned")
                            target.ClearStatus("badly poisoned")
                            target.ClearStatus("poisoned")
                            target.ClearStatus("paralyzed")
                            target.ClearStatus("asleep")
                            target.ClearStatus("frozen")
            elif (name in ["Rock Wrecker", "Giga Impact", "Hyper Beam", "Frenzy Plant", "Hydro Cannon", "Blast Burn", "Roar of Time"]):
                user.ApplyStatus("recharging", 2)
            elif (name == "Frustration"):
                points = GetSocialPoints()
                power = min(1, (3000 - points) / 3000) * 102
            elif (name == "Return"):
                power = min(1, GetSocialPoints() / 3000) * 102
            elif (name == "Magic Coat"):
                posttext += user.ApplyStatus("coated in magic")
            elif (name == "Triple Kick"):
                global MultihitCount
                global MultihitMax
                repeat = True
                if (MultihitCount == None):
                    power = 10
                    MultihitCount = 2
                    MultihitMax = MultihitCount
                posttext += "Hit {} time(s)!".format(MultihitMax - MultihitCount + 1)
                if (MultihitCount != 0):
                    MultihitCount -= 1
                    power = 30 - MultihitCount * 10
                else:
                    repeat = False
                    MultihitMax = None
                    MultihitCount = None
            elif (name == "Power Trick"):
                posttext += user.ApplyStatus("power tricked")
            elif (name == "Memento"):
                posttext += target.ChangeStats(Stats.Attack, -2, user)
                posttext += target.ChangeStats(Stats.SpecialAttack, -2, user)
                user.AdjustHealth(0, absolute=True)
            elif (name == "Substitute"):
                if (user.GetHealthPercentage() > 0.25 and not user.HasStatus("substitute")):
                    user.AdjustHealth(-user.GetStat(Stats.Health) / 4.0)
                    user.ApplyStatus("substitute", user.GetStat(Stats.Health) / 4.0, user)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Belly Drum"):
                if (user.GetHealthPercentage() > 0.5 and user.GetStatChanges(Stats.Attack) < 6):
                    user.AdjustHealth(-user.GetStat(Stats.Health) / 2.0)
                    posttext += user.ChangeStats(Stats.Attack, 99)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Fillet Away"):
                if (user.GetHealthPercentage() > 0.5 and (user.GetStatChanges(Stats.Attack) < 6 or user.GetStatChanges(Stats.SpecialAttack) < 6 or user.GetStatChanges(Stats.Speed) < 6)):
                    user.AdjustHealth(-user.GetStat(Stats.Health) / 2.0)
                    posttext += user.ChangeStats(Stats.Attack, 2)
                    posttext += user.ChangeStats(Stats.SpecialAttack, 2)
                    posttext += user.ChangeStats(Stats.Speed, 2)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "No Retreat"):
                if (CanSwitch(user, False)):
                    posttext += user.ChangeStats(Stats.Attack, 1)
                    posttext += user.ChangeStats(Stats.Defense, 1)
                    posttext += user.ChangeStats(Stats.SpecialAttack, 1)
                    posttext += user.ChangeStats(Stats.SpecialDefense, 1)
                    posttext += user.ChangeStats(Stats.Speed, 1)
                    user.ApplyStatus("no retreat")
                    posttext += "{} will not retreat!".format(user.GetNickname())
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Mind Reader"):
                posttext += target.ApplyStatus("mind read", 2, user)
                user.ApplyStatus(".mindreading", 2)
            elif (name == "Lock-On"):
                posttext += target.ApplyStatus("locked on", 2, user)
                user.ApplyStatus(".lockingon", 2)
            elif (name == "Retaliate"):
                avenging = False
                for mon in user.GetTrainer().GetTeam():
                    if (mon.GetFaintedTurn() in [Turn, Turn - 1]):
                        avenging  = True
                if (avenging):
                    power *= 2
                    posttext += "{} avenges the fallen!".format(username)
            elif (name == "Shell Smash"):
                posttext += user.ChangeStats(Stats.Attack, 2)
                posttext += user.ChangeStats(Stats.Defense, -1)
                posttext += user.ChangeStats(Stats.SpecialAttack, 2)
                posttext += user.ChangeStats(Stats.SpecialDefense, -1)
                posttext += user.ChangeStats(Stats.Speed, 2)
            elif (name == "Follow Me"):
                posttext += user.ApplyStatus("the standout")
            elif (name == "Secret Power"):
                if (GetCamoType() in ["Normal", "Electric"]):
                    sideeffects.append(SideEffect(user, target, "paralyzed", chance=0.3))
                elif (GetCamoType() in ["Rock", "Steel"]):
                    sideeffects.append(SideEffect(user, target, "flinching", chance=0.3))
                elif (GetCamoType() in ["Ground", "Dark"]):
                    sideeffects.append(SideEffect(user, target, Stats.Accuracy, -1, chance=0.3))
                elif (GetCamoType() in ["Water", "Fighting"]):
                    sideeffects.append(SideEffect(user, target, Stats.Attack, -1, chance=0.3))
                elif (GetCamoType() in ["Ice"]):
                    sideeffects.append(SideEffect(user, target, "freezing", chance=0.3))
                elif (GetCamoType() in ["Fire"]):
                    sideeffects.append(SideEffect(user, target, "burned", chance=0.3))
                elif (GetCamoType() in ["Ghost", "Dragon"]):
                    sideeffects.append(SideEffect(user, target, Stats.Defense, -1, chance=0.3))
                elif (GetCamoType() in ["Grass", "Bug"]):
                    sideeffects.append(SideEffect(user, target, "asleep", chance=0.3))
                elif (GetCamoType() in ["Fairy", "Poison"]):
                    sideeffects.append(SideEffect(user, target, Stats.SpecialAttack, -1, chance=0.3))
                elif (GetCamoType() in ["Psychic", "Flying"]):
                    sideeffects.append(SideEffect(user, target, Stats.Speed, -1, chance=0.3))
            elif (name == "Psych Up"):
                user.StatChanges = copy.copy(target.StatChanges)
                if (target.HasStatus("focused")):
                    posttext += user.ApplyStatus("focused")
            elif (name == "Entrained"):
                if (not (IsSpecialAbility(user.GetAbility()) or IsSpecialAbility(target.GetAbility()))):
                    target.ApplyStatus(".tracing", user.GetAbility(), user)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Skill Swap"):
                myability = user.GetAbility()
                theirability = target.GetAbility()
                if (not (IsSpecialAbility(myability) or IsSpecialAbility(theirability))):
                    user.ApplyStatus(".tracing", theirability, user)
                    target.ApplyStatus(".tracing", myability, user)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Metronome"):
                move.PP -= 1
                lastmove = GetMove(random.choice(movesin))
                newtargets = GetTargets(user, GetMoveRange(lastmove), True)
                if (GetMoveRange(lastmove) in [Range.Adjacent, Range.AdjacentAlly, Range.AdjacentAllyOrSelf, Range.AdjacentFoe, Range.Any, Range.AnyOrSelf, Range.Self, Range.All]):
                    newtargets = [random.choice(newtargets)]
                DoMove(action, user, copy.deepcopy(lastmove), newtargets, alreadypretext=pretext)
                ActionLog.append(Action(0, user.GetStat(Stats.Speed), ActionTypes.Move, user.GetTrainer(), user, GetMove(lastmove.Name), GetTrainers(newtargets), newtargets, Turn))
                return
            elif (name == "Gastro Acid"):
                target.ApplyStatus(".tracing", "Suppressed", user)
            elif (name == "Defog"):
                posttext += target.ChangeStats(Stats.Evasion, -1, user)
                removeeffects = ["sticky web", "toxic spikes", "stealthy rocks", "spikes"]
                effectdel = []
                for cleareffect in FriendlyEffects.keys():
                    if (cleareffect in removeeffects):
                        effectdel.append(cleareffect)
                for clearingeffect in effectdel:
                    del FriendlyEffects[clearingeffect]
                if (len(effectdel) > 0):
                    posttext += "Cleared own field!"
                removeeffects += ["light screen", "reflect", "safeguard", "mist", "aurora veil"]
                effectdel = []
                for cleareffect in EnemyEffects.keys():
                    if (cleareffect in removeeffects):
                        effectdel.append(cleareffect)
                for clearingeffect in effectdel:
                    del EnemyEffects[clearingeffect]
                if (len(effectdel) > 0):
                    posttext += "Cleared foe's field!"
            elif (name == "Imprison"):
                user.ApplyStatus("imprisoning")
            elif (name == "Focus Punch"):
                if (user.GetDamagedThisTurn() == Turn):
                    doDamage = False
                    subtractpp = False
                    posttext += "{} lost its focus!".format(username)
            elif (name == "Beat Up"):
                global MultihitCount
                global MultihitMax
                repeat = True
                if (MultihitCount == None):
                    MultihitCount = len(user.GetTrainer().GetUnfaintedTeam()) - 1
                    MultihitMax = MultihitCount
                beatupper = user.GetTrainer().GetUnfaintedTeam()[MultihitCount]
                posttext += "{} joined the fray!".format(beatupper.GetNickname())
                power = beatupper.GetStat(Stats.Attack) / 10 + 5
                if (MultihitCount != 0):
                    MultihitCount -= 1
                else:
                    repeat = False
                    MultihitMax = None
                    MultihitCount = None
            elif (name == "Acrobatics"):
                if (user.GetItem() == None):
                    power *= 2
            elif (name == "Thrash"):
                if (target == None):
                    doDamage = False
                    action.ChangeSuccess(False)
                    posttext += "But it failed!"
                if (not user.HasStatus("thrashing")):
                    user.ApplyStatus("thrashing", random.randint(2, 3), user)
            elif (name == "Outrage"):
                if (target == None):
                    doDamage = False
                    action.ChangeSuccess(False)
                    posttext += "But it failed!"
                if (not user.HasStatus("outraged")):
                    user.ApplyStatus("outraged", random.randint(2, 3), user)
            elif (name == "Super Fang"):
                fixeddamage = math.floor(target.GetHealth() / 2.0)
            elif (name == "Anchor Shot"):
                posttext += target.ApplyStatus("anchored", user, user)
                if ("Anchor Shot" in moveboosts):
                    power += 10
                    sideeffects.append(SideEffect(user, target, Stats.Attack, -1))
                    sideeffects.append(SideEffect(user, target, Stats.Speed, -1))
            elif (name == "After You"):
                for newaction in CurrentActions:
                    if (newaction.GetUser() == target and newaction.GetActionType() == ActionTypes.Move):
                        newaction.SetPerformed()
                        DoMove(newaction, target, newaction.GetMove(), newaction.GetTargets(), alreadypretext=pretext)
                        return
                posttext += "But it failed!"
                action.ChangeSuccess(False)
            elif (name == "Baton Pass"):
                usertrainer = user.GetTrainer()
                newlist = []
                for mon in usertrainer.GetTeam():
                    if (mon.Health >= 1 and mon not in Battlers()):
                        newlist.append(mon)
                if (len(newlist) == 0):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    statchanges = copy.copy(user.GetAllStatChanges())
                    statuslist = ["confused", "focused", ".mindreading", ".lockingon", ".tracing", "blocked", "webbed", "seeded", "cursed", "substitute", "ingrained", "power tricked", "heal blocked", "embargoed", "perishing", "levitating", "aqua ring"]
                    newstatus = {}
                    for status in user.GetStatusKeys():
                        newstatus[status] = user.Status[status]                      
                    renpy.say(None, "Pick a Pokémon to switch in.")
                    switchCommand = renpy.call_screen('switch', user.GetTrainer(), True)
                    newPokemon = user.GetTrainer().GetTeam()[switchCommand]
                    if (newPokemon.GetHealth() == 0):
                        renpy.say(None, "{} has fainted, and cannot fight!".format(newPokemon.GetNickname()))
                        DoMove(action, user, move, [user])
                        return
                    elif (newPokemon in Battlers()):
                        renpy.show_screen("battleui")
                        renpy.say(None, "{} is already in battle!".format(newPokemon.GetNickname()))
                        DoMove(action, user, move, [user])
                        return
                    team = usertrainer.GetTeam()
                    usertrainer.ShiftTeam(team.index(user), switchCommand, True)
                    posttext += "{} passed the baton to {}!".format(user.GetNickname(), newPokemon.GetNickname())
                    SwitchInEffects(newPokemon)
                    for status, count in newstatus.items():
                        newPokemon.ApplyStatus(status, count)
                    for statchange, count in statchanges.items():
                        newPokemon.ChangeStats(statchange, count)
            elif (name == "Shed Tail"):
                usertrainer = user.GetTrainer()
                newlist = []
                for mon in usertrainer.GetTeam():
                    if (mon.Health >= 1 and mon not in Battlers()):
                        newlist.append(mon)
                if (user.GetHealthPercentage() > 0.5 and not user.HasStatus("substitute") and len(newlist) > 0):
                    user.AdjustHealth(-user.GetStat(Stats.Health) / 2.0)
                    user.ApplyStatus("substitute", user.GetStat(Stats.Health) / 4.0, user)
                    statuscount = user.GetStatusCount("substitute")
                    renpy.say(None, "Pick a Pokémon to switch in.")
                    switchCommand = renpy.call_screen('switch', user.GetTrainer(), True)
                    newPokemon = user.GetTrainer().GetTeam()[switchCommand]
                    if (newPokemon.GetHealth() == 0):
                        renpy.say(None, "{} has fainted, and cannot fight!".format(newPokemon.GetNickname()))
                        DoMove(action, user, move, [user])
                        return
                    elif (newPokemon in Battlers()):
                        renpy.show_screen("battleui")
                        renpy.say(None, "{} is already in battle!".format(newPokemon.GetNickname()))
                        DoMove(action, user, move, [user])
                        return
                    team = usertrainer.GetTeam()
                    usertrainer.ShiftTeam(team.index(user), switchCommand, True)
                    posttext += "{} put up a substitute for {}!".format(user.GetNickname(), newPokemon.GetNickname())
                    SwitchInEffects(newPokemon)
                    newPokemon.ApplyStatus("substitute", statuscount)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Snatch"):
                user.ApplyStatus("snatching")
            elif (name == "Assist"):
                move.PP -= 1
                moveslist = []
                for othermon in user.GetTrainer().GetTeam():
                    if (othermon != user):
                        for move in othermon.GetMoveNames():
                            if (AssistCanCall(move)):
                                moveslist.append(GetMove(move))
                if (moveslist == []):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    newmove = random.choice(moveslist)
                    pretext += "{} called {}!".format(user.GetNickname(), newmove.Name)
                    newtargets = GetTargets(user, GetMoveRange(newmove), True)
                    if (GetMoveRange(newmove) not in [Range.AllFoes, Range.AllAlliesAndSelf, Range.AllAllies, Range.AllAdjacentFoes, Range.AllAdjacent, Range.All]):
                        newtargets = [random.choice(newtargets)]
                    DoMove(action, user, newmove, newtargets, pretext, posttext, False)
                    ActionLog.append(Action(0, user.GetStat(Stats.Speed), ActionTypes.Move, user.GetTrainer(), user, GetMove(newmove.Name), GetTrainers(newtargets), newtargets, Turn))
                    return
            elif (name in ["Revenge", "Avalanche"]):
                if (user.GetDamagedThisTurn() == Turn):
                    power *= 2
            elif (name == "Punishment"):
                power = 60
                for statchange, value in target.GetAllStatChanges().items():
                    if (value > 0):
                        power += 20 * value
                power = min(200, power)
            elif (name == "Snore"):
                if (user.HasStatus("asleep")):
                    sideeffects.append(SideEffect(user, target, "flinching", chance=0.3))
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name in ["Bug Bite", "Pluck"]):
                if (IsBerry(target.GetItem()) and not target.HasAbility("Sticky Hold")):
                    posttext += target.TakeItem()
                    UseItem(user, False, True, True)
            elif (name == "Natural Gift"):
                if (IsBerry(user.GetItem())):
                    type, power = NaturalGiftData(user.GetItem())
                    user.MarkItemUsed()
                else:
                    doDamage = False
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Recycle"):
                if (user.GetItem() == None):
                    for itemaction, item, turn in reversed(user.GetItemHistory()):
                        if (itemaction == "Used"):
                            posttext += user.GiveItem(item)
                            break
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Knock Off"):
                if (not target.HasAbility("Sticky Hold")):
                    msg = target.TakeItem()
                    if ("lost its" in msg):
                        power *= 1.5
                        posttext += msg
            elif (name == "Bestow"):
                if (target.GetItem() == None and user.GetItem() != None and not target.HasStatus("substitute")):
                    ownitem = user.GetItem()
                    posttext += user.TakeItem()
                    posttext += target.GiveItem(ownitem)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Belch"):
                consumedberry = False
                for itemaction, item, turn in reversed(user.GetItemHistory()):
                    if (itemaction == "Used" and IsBerry(item)):
                        consumedberry = True
                        break
                if (not consumedberry):
                    doDamage = False
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Discard"):
                if (user.GetItem() != None):
                    posttext += "{} discarded its item!".format(username)
                    user.MarkItemUsed()
                    posttext += user.ChangeStats(Stats.Speed, 2)
                    posttext += user.ChangeStats(Stats.Evasion, 2)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Throat Chop"):
                sideeffects.append(SideEffect(user, target, "gasping", 3))
            elif (name == "Wring Out"):
                power = max(1, target.GetHealth() / target.GetStat(Health) * 120)
            elif (name == "Stomping Tantrum"):
                lastmove = GetLastMove(ActionLog, user, returnaction=True)
                if (lastmove != None):
                    if (not lastmove.GetSuccess()):
                        power *= 2.0
            elif (name == "Sleep Talk"):
                notallowed = ["Assist", "Belch", "Beak Blast", "Bide", "Bounce", "Copycat", "Dig", "Dive", "Dynamax Cannon", "Freeze Shock", "Fly", "Focus Punch", "Geomancy", "Ice Burn", "Me First", "Metronome", "Mirror Move", "Mimic", "Phantom Force", "Razor Wind", "Shadow Force", "Shell Trap", "Sketch", "Skull Bash", "Sky Attack", "Sky Drop", "Solar Blade", "Solar Beam", "Struggle", "Uproar"]

                possiblemoves = user.GetMoveNames()
                for notmove in notallowed:
                    if notmove in possiblemoves:
                        possiblemoves.remove(notmove)

                if (not user.HasStatus("sleeping") or possiblemoves == []):
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
                else:
                    newmove = GetMove(random.choice(possiblemoves))
                    pretext += "{} called {}!".format(user.GetNickname(), newmove.Name)
                    newtargets = GetTargets(user, GetMoveRange(newmove), True)
                    if (GetMoveRange(newmove) not in [Range.AllFoes, Range.AllAlliesAndSelf, Range.AllAllies, Range.AllAdjacentFoes, Range.AllAdjacent, Range.All]):
                        newtargets = [random.choice(newtargets)]
                    DoMove(action, user, newmove, newtargets, pretext, posttext, False)
                    ActionLog.append(Action(0, user.GetStat(Stats.Speed), ActionTypes.Move, user.GetTrainer(), user, GetMove(newmove.Name), GetTrainers(newtargets), newtargets, Turn))
                    return
            elif (name == "Grudge"):
                posttext += user.ApplyStatus("begrudging")
            elif (name == "Ally Switch"):
                usertrainer = user.GetTrainer()
                newlist = []
                if (user in FriendlyBattlers() and len(FriendlyBattlers()) > 1 or user in EnemyBattlers() and len(EnemyBattlers()) > 1):
                    if (user in FriendlyBattlers()):
                        for othermon in FriendlyBattlers():
                            if (othermon != user):
                                usertrainer.ShiftTeam(user, othermon, positionswitch=True)
                    else:
                        for othermon in EnemyBattlers():
                            if (othermon != user):
                                usertrainer.ShiftTeam(user, othermon, positionswitch=True)
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Role Play"):
                if (not IsSpecialAbility(user.GetAbility()) and not IsSpecialAbility(target.GetAbility())):
                    user.ApplyStatus(".tracing", target.GetAbility())
                    posttext += "{} copied the ability {}!".format(user.GetNickname(), target.GetAbility())
                else:
                    posttext += "But it failed!"
                    action.ChangeSuccess(False)
            elif (name == "Frost Breath"):
                iscrit = True
            elif (name == "Salt Cure"):
                sideeffects.append(SideEffect(user, target, "salt cured"))
            elif (name in ["Heat Crash", "Heavy Slam"]):
                foeweight = target.GetWeight()
                selfweight = user.GetWeight()
                ratio = foeweight / selfweight
                if (ratio > 0.5):
                    power = 40
                elif (ratio > 0.3335):
                    power = 60
                elif (ratio > .2501):
                    power = 80
                elif (ratio > .2001):
                    power = 100
                else:
                    power = 120












            ###INSERT NEW MOVES HERE###############################################
            else:
                doDamage = True

            typebonus = GetTypeBonus(name, type, target, user)

            if (typebonus <= 1 and target.HasAbility("Wonder Guard")):
                typebonus = 0

            if (doDamage and math.floor(user.GetId()) == 334 and dawnbattle and len(FriendlyUnfainteds()) == 1):
                movesdodged.append(move.Name)

            if (doDamage and typebonus != 0):
                if (doDamage and not target.HasStatus("busted disguise") and target.HasAbility("Disguise")):
                    doDamage = False
                    target.AdjustHealth(-target.GetStat(Stats.Health) / 8.0)
                    target.ApplyStatus("busted disguise")
                    posttext += "{}'s disguise was busted!".format(target.GetNickname())

                if (len(sideeffects) > 0):
                    sheerforcebonus = True

                recklessbonus = recoil > 0 and user.HasAbility("Reckless")
                if (doDamage):
                    if (fixeddamage == -1):
                        if (user.HasStatus("laser focused")):
                            iscrit = True
                        if (not iscrit):
                            critodds = 0
                            if (user.HasAbility("Super Luck")):
                                critstage += 1
                            if (user.HasStatus("focused")):
                                critstage += 2
                            if (critstage == 0):
                                critodds = 1.0/24.0
                            elif (critstage == 1):
                                critodds = 1.0/8.0
                            elif (critstage == 2):
                                critodds = 1.0/2.0
                            elif (critstage >= 3):
                                critodds = 1.0

                            iscrit = random.random() <= critodds

                        if (iscrit and (target.HasAbility("Shell Armor") or target.HasAbility("Battle Armor"))):
                            iscrit = False

                        if (EffectOnOwnField(target, "lucky")):
                            iscrit = False

                    prehealth = target.GetHealthPercentage()
                    prehealthraw = target.GetHealth()

                    analyticbonus = False
                    if (action in CurrentActions and len(CurrentActions[CurrentActions.index(action):]) == 1):
                        analyticbonus = True

                    damage = DoDamage(user, move, target, type, iscrit, power, typebonus, fixeddamage, sheerforcebonus, recklessbonus, atebonus, analyticbonus, parentalbond)
                    
                    if (damage > 0 and user.HasAbility("Stench")):
                        sideeffects.append(SideEffect(user, target, "flinching", chance=0.1))
                    if (iscrit):
                        pretext += "It's a critical hit on {}!".format(target.GetNickname())
                        if (target.HasAbility("Anger Point")):
                            pretext += target.ChangeStats(Stats.Attack, 6 - target.GetStatChanges(Stats.Attack), target)
                    if (typebonus > 1 and fixeddamage == -1):
                        PlaySound("supereffective.ogg")
                        pretext += "It's super effective on {}!".format(target.GetNickname())
                    elif (typebonus < 1 and typebonus > 0 and fixeddamage == -1):
                        PlaySound("notveryeffective.ogg")
                        pretext += "It's not very effective on {}...".format(target.GetNickname())
                    elif (typebonus == 1):
                        PlaySound("normaldamage.ogg")
                    if (target.HasStatus("raging") and damage != 0):
                        posttext += "{}'s rage grows!".format(target.GetNickname())
                        posttext += target.ChangeStats(Stats.Attack, 1, target)
                    if (target.HasStatus("biding") and damage != 0):
                        if (target.HasStatus(".bidingdamage")):
                            target.ApplyStatus(".bidingdamage", (target.GetStatusCount(".bidingdamage")[0] + damage, user), overwrite=True)
                        else:
                            target.ApplyStatus(".bidingdamage", (damage, user), overwrite=True)
                    if (healthgain > 0):
                        healthgain = math.ceil(damage * healthgain)
                        user.AdjustHealth(healthgain)
                        posttext += "{} recovered HP!".format(username)
                    if (recoil > 0 and (move.Name == "Struggle" or not user.HasAbility("Rock Head"))):
                        recoil = math.ceil(damage * recoil)
                        if (user.AdjustHealth(-recoil)):
                            posttext += "{} took recoil damage!".format(username)
                    if (target.HasStatus("frozen") and type == "Fire"):
                        posttext += target.ClearStatus("frozen")
                    if (MakesContact(move) and random.random() <= 0.3 and user.HasAbility("Poison Touch")):
                        posttext += target.ApplyStatus("poisoned", 1, user)
                    if (target.GetHealth() <= 0 and (target.HasStatus("enduring") or target.HasStatus("deathless") or (prehealth == 1.0 and target.HasAbility("Sturdy")))):
                        target.AdjustHealth(1, True)
                        if (target.HasStatus("deathless")):
                            target.AdjustHealth(target.GetStat(Stats.Health) / 2.0, True)
                        posttext += "{} endured!".format(target.GetNickname())
                    if (target.GetHealth() <= 0 and math.floor(user.GetId()) == 334 and user.GetLevel() == 68 and target.GetId() == 25 and len(movesdodged) < 5 and target.HasAbility("Freelectric")):
                        if (prehealthraw > 1):
                            target.AdjustHealth(1, True)
                            posttext += "{} toughed it out so you wouldn't feel sad!".format(target.GetNickname())
                        elif (prehealthraw == 1):
                            target.AdjustHealth(0.1, True)
                            posttext += "{} toughed it out and bared a grin!".format(target.GetNickname())
                        elif (prehealthraw == 0.1):
                            target.AdjustHealth(0.01, True)
                            posttext += "{} toughed it out and took a deep breath!".format(target.GetNickname())
                        elif (prehealthraw == 0.01):
                            target.AdjustHealth(0.001, True)
                            posttext += "{} toughed it out and challenges the king!".format(target.GetNickname())
                        elif (prehealthraw == 0.001):
                            target.AdjustHealth(0.001, True)
                            posttext += "{} toughed it out and will never fall!".format(target.GetNickname())
                    if (target.GetHealth() <= 0 and target.HasStatus(".liberating")):
                        target.AdjustHealth(1, True)
                        posttext += "{} is liberated!".format(target.GetNickname())
                    if (target.GetHealth() <= 0 and name in ["False Swipe", "Hold Back"]):
                        target.AdjustHealth(1, True)
                    if (move.Category == "Physical" and target.HasAbility("Weak Armor")):
                        posttext += target.ChangeStats(Stats.Defense, -1, target)
                        posttext += target.ChangeStats(Stats.Speed, 2, target)
                    if (MakesContact(move) and (user.GetGender() == Genders.Male and target.GetGender() == Genders.Female or user.GetGender() == Genders.Female and target.GetGender() == Genders.Male) and random.random() <= 0.3 and target.HasAbility("Cute Charm")):
                        posttext += user.ApplyStatus("infatuated", 1, target)
                    if (MakesContact(move) and target.HasAbility("Iron Barbs")):
                        user.AdjustHealth(-user.GetStat(Stats.Health) / 8.0)
                        posttext += "{} was hurt by the {}!".format(username, target.GetAbility())
                    if (MakesContact(move) and target.HasAbility("Rough Skin")):
                        user.AdjustHealth(-user.GetStat(Stats.Health) / 8.0)
                        posttext += "{} was hurt by the {}!".format(username, target.GetAbility())
                    if ((target.HasStatus("gulping") or target.HasStatus("gorging")) and (target.HasAbility("Gulp Missile") or target.HasForeveral("Cramorant Foreveral"))):
                        user.AdjustHealth(-user.GetStat(Stats.Health) / 4.0)
                        if (target.HasStatus("gulping")):
                            posttext += user.ChangeStats(Stats.Defense, -1, target)
                            target.ClearStatus("gulping")
                        elif (target.HasStatus("gorging")):
                            posttext += user.ApplyStatus("paralyzed", 1, target)
                            target.ClearStatus("gorging")
                    if (name == "Fell Stinger" and target.GetHealthPercentage() <= 0):
                        posttext += user.ChangeStats(Stats.Attack, 3)
                    if (MakesContact(move) and target.GetHealth() == 0 and target.HasAbility("Aftermath") and not AbilityOnField("Damp")):
                        user.AdjustHealth(-user.GetStat(Stats.Health) / 4.0)
                        posttext += "{} was caught in the aftermath!".format(username)
                    if (target.GetHealth() == 0 and target.HasStatus("bound to destiny")):
                        posttext += "{} was bound to destiny!".format(username)
                        user.AdjustHealth(0, absolute=True)
                    if (MakesContact(move) and random.random() <= 0.3 and target.HasAbility("Flame Body")):
                        posttext += user.ApplyStatus("burned")
                    if (MakesContact(move) and random.random() <= 0.3 and target.HasAbility("Poison Point")):
                        posttext += user.ApplyStatus("poisoned")
                    if (MakesContact(move) and random.random() <= 0.3 and target.HasAbility("Static")):
                        posttext += user.ApplyStatus("paralyzed")
                    if (MakesContact(move) and target.HasAbility("Pickpocket")):
                        useritem = user.GetItem()
                        targetitem = target.GetItem()
                        if (useritem != None and targetitem == None and not user.HasAbility("Sticky Hold")):
                            posttext += user.TakeItem()
                            posttext += target.GiveItem(targetitem)
                    if (MakesContact(move) and target.HasItem("Sticky Barb")):
                        if (user.GetItem() == None):
                            posttext += user.GiveItem("Sticky Barb")
                    if (move.Category != "Status" and target.HasAbility("Cursed Body")):
                        posttext += user.ApplyStatus("disabled", 4, user)
                        user.ApplyStatus(".disabling", move.Name)
                    if (type == "Dark" and target.HasAbility("Justified")):
                        posttext += target.ChangeStats(Stats.Attack, 1)
                    if (type in ["Bug", "Dark", "Ghost"] and target.HasAbility("Rattled")):
                        posttext += target.ChangeStats(Stats.Speed, 1)
                    if (target.GetHealthPercentage() < 0.5 and target.HasAbility("Berserk")):
                        posttext += target.ChangeStats(Stats.SpecialAttack, 1)
                    if (target.GetHealthPercentage() == 0.0 and user.HasAbility("Moxie")):
                        posttext += user.ChangeStats(Stats.Attack, 1)
                    if (target.GetHealthPercentage() == 0.0 and target.HasStatus("grudging")):
                        move.PP = 0
                        posttext += "{} bore a grudge!".format(target)
                    if (target.HasStatus(".countering") and move.Category == "Physical"):
                        target.ApplyStatus(".countering", (max(1, math.floor(damage * 2.0)), user), overwrite=True)
                    if (target.HasStatus(".mirrorcoat") and move.Category == "Special"):
                        target.ApplyStatus(".mirrorcoat", (max(1, math.floor(damage * 2.0)), user), overwrite=True)
                    if (move.Category == "Physical" and target.HasAbility("Toxic Debris")):
                        if ("toxic spikes" in GetFieldEffects(user).keys()):
                            if (GetFieldEffects(user)["toxic spikes"] == 1):
                                del GetFieldEffects(user)["toxic spikes"]
                                posttext += ApplyEffect(user, "toxic spikes", 2, False)
                        else:
                            posttext += ApplyEffect(user, "toxic spikes", 1, False)
                    if (name in ["Dragon Tail", "Circle Throw"] and target.GetHealthPercentage() > 0):
                        targettrainer = target.GetTrainer()
                        newlist = []
                        for mon in targettrainer.GetTeam():
                            if (mon.Health >= 1 and mon != target):
                                newlist.append(mon)
                        if (len(newlist) != 0):
                            randpkmn = random.choice(newlist)
                            trainer = target.GetTrainer()
                            team = trainer.GetTeam()
                            trainer.ShiftTeam(team.index(target), team.index(randpkmn), True)
                            posttext += "{} was forced out!".format(randpkmn.GetNickname())
                            SwitchInEffects(randpkmn)
                    if (prehealth >= 0.5 and target.GetHealthPercentage() < 0.5 and target.GetHealth() > 0 and (target.HasAbility("Wimp Out") or target.HasAbility("Emergency Exit"))):
                        if (target.GetTrainer().GetType() != TrainerType.Enemy):
                            usertrainer = target.GetTrainer()
                            newlist = []
                            for mon in usertrainer.GetTeam():
                                if (mon.Health >= 1 and mon not in Battlers()):
                                    newlist.append(mon)
                            if (len(newlist) != 0):
                                newPokemon = FriendlyBattlers()[0]
                                while (newPokemon in Battlers() or newPokemon.GetHealth() == 0):
                                    renpy.say(None, "Pick a Pokémon to switch in.")
                                    switchCommand = renpy.call_screen('switch', usertrainer, True)
                                    if (switchCommand != "back"):
                                        newPokemon = usertrainer.GetTeam()[switchCommand]
                                        if (newPokemon.GetHealth() == 0):
                                            renpy.show_screen("battleui")
                                            renpy.say(None, "{} has fainted, and cannot fight!".format(newPokemon.GetNickname()))
                                        elif (newPokemon in Battlers()):
                                            renpy.show_screen("battleui")
                                            renpy.say(None, "{} is already in battle!".format(newPokemon.GetNickname()))
                                team = usertrainer.GetTeam()
                                usertrainer.ShiftTeam(team.index(target), switchCommand, True)
                                posttext += "{} retreated, and {} switched in!".format(target.GetNickname(), newPokemon.GetNickname())
                                SwitchInEffects(newPokemon)
                        else:                        
                            targettrainer = target.GetTrainer()
                            newlist = []
                            for mon in targettrainer.GetTeam():
                                if (mon.Health >= 1 and mon != target):
                                    newlist.append(mon)
                            if (len(newlist) != 0):
                                randpkmn = random.choice(newlist)
                                trainer = target.GetTrainer()
                                team = trainer.GetTeam()
                                trainer.ShiftTeam(team.index(target), team.index(randpkmn), True)
                                posttext += "{} retreated, and {} shifted in!".format(target.GetNickname(), randpkmn.GetNickname())
                                SwitchInEffects(randpkmn)
                    if (name == "Rapid Spin"):
                        removeeffects = ["sticky web", "toxic spikes", "stealthy rocks", "spikes"]
                        removestatus = ["wrapped", "bound", "clamped", "infested", "firespun", "whirlpooled", "seeded", "entombed", "ingrained", "anchored"]
                        statusdel = []
                        effectdel = []
                        for clearstatus in user.GetStatusKeys():
                            if (clearstatus in removestatus):
                                statusdel.append(clearstatus)
                        for clearingstatus in statusdel:
                            user.ClearStatus(clearingstatus)

                        if (user in FriendlyBattlers()):
                            for cleareffect in FriendlyEffects.keys():
                                if (cleareffect in removeeffects):
                                    effectdel.append(cleareffect)
                            for clearingeffect in effectdel:
                                del FriendlyEffects[clearingeffect]
                        else:
                            for cleareffect in EnemyEffects.keys():
                                if (cleareffect in removeeffects):
                                    effectdel.append(cleareffect)
                            for clearingeffect in effectdel:
                                del EnemyEffects[clearingeffect]
                        if (len(statusdel) + len(effectdel)):
                            posttext += "Cleared entrapments!"

            elif (doDamage and typebonus == 0):
                pretext += "It had no effect on {}...".format(target.GetNickname())
                if (name in ["Jump Kick", "High Jump Kick"]):
                    user.AdjustHealth(-user.GetStat(Stats.Health) / 2.0)
                    posttext += "{} kept going and crashed!".format(username)

            if (doDamage and typebonus != 0):
                for sideeffect in sideeffects:
                    posttext += sideeffect.Apply()

        for posteffect in posteffects:
            posttext += posteffect.Apply()

        if (len(targets) == 1 and not repeating and not repeat and doDamage and not parentalbond and user.HasAbility("Parental Bond")):
            DoMove(action, user, move, targets, pretext + posttext, "", False, True)
            return

        clearimmediately = ["airborne", "dug in", "diving", "ethereal"]
        for status in clearimmediately:
            if (user.GetStatusCount(status) == 1):
                user.ClearStatus(status)

        if (user.HasStatus("thrashing") and not doDamage):
            user.ClearStatus("thrashing")
        if (user.HasStatus("outraged") and not doDamage):
            user.ClearStatus("outraged")


        for fvl in user.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.Training):
                if (fvl == "Tyrogue Everal"):
                    if (IsPunchMove(name)):
                        user.EVs[2] = min(user.EVs[2] + 3, 255)
                        posttext += "{} trained his Defense by punching!".format(user.GetNickname())
                    elif ("Kick" in name):
                        user.EVs[1] = min(user.EVs[1] + 3, 255)
                        posttext += "{} trained his Attack by kicking!".format(user.GetNickname())
                elif (fvl == "Meditite Everal"):
                    pronouns = ("his" if user.GetGender() == Genders.Male else ("her" if user.GetGender() == Genders.Female else "its"))
                    if (type == "Fighting"):
                        user.EVs[1] = min(user.EVs[1] + 3, 255)
                        posttext += "{} trained {} Attack through physical power!".format(user.GetNickname(), pronouns)
                    elif (type == "Psychic"):
                        user.EVs[4] = min(user.EVs[4] + 3, 255)
                        posttext += "{} trained {} Special Defense through mental fortitude!".format(user.GetNickname(), pronouns)

        renpy.say(None, FormatText(pretext + posttext + ItemText))
        ItemText = ""

        if (repeat and target.GetHealth() > 0):
            DoMove(action, user, move, [target], "", "", repeat)
        elif (subtractpp):
            move.PP -= 1
            if (AbilityOnOpponentField(user, "Pressure")):
                move.PP -= 1
            if (move.PP <= 0):
                move.PP = 0

        UsingMove = False
        MoveUser = None
        ActiveMove = None