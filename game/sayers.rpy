init python:
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
                    if (self.image == "libpikachu"):
                        formatcolor = GetLiberaColor()
                elif (formatname == "Blue" and persondex["Blue"]["Named"] and playercharacter != "Blue"):
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

                if (formatname in persondex.keys() and not persondex[formatname]["Named"] and not self.image == "latias"):
                    formatname = "???"

                formatcallback=callbackcontinue

                if (formatname == "You"):
                    formatwhat = "{{i}}({}){{/i}}".format(what)
                elif (formatname == ""):
                    formatwhat = ">{{cps=*0.8}}{}".format(what)
                elif (formatname == "Tia" and self.image != "latias"):
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

define defaultpersondex = {
    "Professor Oak" : {"Named" : True, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Blue" : {"Named" : True, "Value" : 0, "Contact": True, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Rival", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant},
    "Silver" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody},
    "Brawly" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Roxanne" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Falkner" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Underclassman", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody},
    "Leaf" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Devoted},
    "Ethan" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant},
    "Calem" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly},
    "Hilbert" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody},
    "Brendan" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly},
    "May" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral},
    "Flannery" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody},
    "Whitney" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly},
    "Sabrina" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant},
    "Serena" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral},
    "Cheren" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant},
    "Misty" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody},
    "Bianca" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly},
    "Dawn" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral},
    "Nate" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly},
    "Rosa" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral},
    "Bea" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Training Partner", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral},
    "Nessa" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Date", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral},
    "Hilda" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody},
    "Gardenia" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly},
    "Skyla" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly},
    "Brock" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Erika" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Friend", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant},
    "Janine" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Tool", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Tia" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Protector", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Devoted},
    "Sonia" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral},
    "Jasmine" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Friendly},
    "Grusha" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Political Rival", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Moody},
    "Victini" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Unexpected Interloper", "RelationshipRank": 0, "Events": [], "Mood": 10, "Nature": TrainerNature.Special},
    "Professor Cherry" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Distant},
    "Instructor Lenora" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Blaine" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Wallace" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Ramos" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Lieutenant Surge" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Melony" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Sensei Marshal" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Grasshopper", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Koga" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Bertha" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Will" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Burgh" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Olivia" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructrice Fantina" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Karen" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Clair" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Byron" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Valerie" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Instructor Winona" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Bruno" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Alder" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Lance" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Student", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Iris" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Female, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Dean Drayden" : {"Named" : False, "Value" : 0, "Contact": False, "ClassesKnown": [], "Sex": Genders.Male, "Relationship": "Mentor", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Yellow" : {"Named" : False, "Value" : 0, "Contact" : False, "ClassesKnown" : [], "Sex": Genders.Female, "Relationship": "Dormmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Lisia" : {"Named" : False, "Value" : 0, "Contact" : False, "ClassesKnown" : [], "Sex": Genders.Female, "Relationship": "Mentee", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Special},
    "Wally" : {"Named" : False, "Value" : 0, "Contact" : False, "ClassesKnown" : [], "Sex": Genders.Male, "Relationship": "Classmate", "RelationshipRank": 0, "Events": [], "Mood": 0, "Nature": TrainerNature.Neutral}
}
    
default first_name = "You"
default last_name = "Sugimori"
default pika_name = "Your Pikachu"
default blue_name = "Blue"

define oak = CustomCharacter("Professor Oak", "#000000", "oak")
define pikachu = CustomCharacter("Pikachu", "#fca600", "pikachu")
define libpikachu = CustomCharacter("Pikachu", "#fca600", "libpikachu")
define starter = CustomCharacter("Your Starter", "#fca600", "starterportrait")
define red = CustomCharacter("Red", "#cf0000", "red")
define redmind = CustomCharacter("You", "#cf0000", "red")
define mom = CustomCharacter("Mom", "#b7669e", "mom")

#students
define blue = CustomCharacter("Blue", "#3110dd", "blue")
define bluemind = CustomCharacter("You", "#3110dd", "blue")
define silver = CustomCharacter("Silver", "#686080", "silver")
define face = CustomCharacter("Ace Student F", "#C89BE3", "face")
define mace = CustomCharacter("Ace Student M", "#665787", "mace")
define leaf = CustomCharacter("Leaf", "#00b23f", "leaf")
define leafmind = CustomCharacter("You", "#00b23f", "leaf")
define leaftease = CustomCharacter("Leaf", "#00b23f", "leaftease")
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
define skylatease = CustomCharacter("Skyla", "#5c87b9", "skylatease")
define erika = CustomCharacter("Erika", "#34a59a", "erika")
define tia = CustomCharacter("Tia", "#C96A70", "tia")
define latias = CustomCharacter("Tia", "#C96A70", "latias")
define sonia = CustomCharacter("Sonia", "#F19272", "sonia")
define jasmine = CustomCharacter("Jasmine", "#939393", "jasmine")
define grusha = CustomCharacter("Grusha", "#00b8d0", "grusha")
define yellow = CustomCharacter("Yellow", "#f2a634", "yellow")
define wally = CustomCharacter("Wally", "#377227", "wally")
define victini = CustomCharacter("Victini", "#f57c51", "victini")

#Not technically students
define brawly = CustomCharacter("Brawly", "#467595", "brawly")
define roxanne = CustomCharacter("Roxanne", "#a2254b", "roxanne")
define falkner = CustomCharacter("Falkner", "#1d8fc5", "falkner")
define brock = CustomCharacter("Brock", "#6D211D", "brock")
define janine = CustomCharacter("Janine", "#6f4097", "janine")
define iris = CustomCharacter("Iris", "#82007e", "iris")
define lisia = CustomCharacter("Lisia", "#71BBA2", "lisia")

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
define lace = CustomCharacter("Lady Ace Trainer", "#6E7AA8", "lace")
define oldman = CustomCharacter("Old Man", "#C68C28", "oldman")

define charlist = [oak, pikachu, starter, red, mom, blue, silver, brawly, roxanne, 
    face, mace, falkner, leaf, ethan, calem, hilbert, brendan, may, flannery,
    whitney, sabrina, serena, cheren, misty, bianca, dawn, nate, rosa, bea,
    nessa, hilda, gardenia, skyla, brock, erika, janine, tia, latias, sonia, iris,
    jasmine, grusha, yellow, ethanmind, bluemind, wally,
    victini,
    lenora, blaine, wallace, ramos, surge, melony, marshal, koga, bertha, 
    winona, will, burgh, olivia, fantina, karen, clair, byron, valerie,

    bruno, alder, lance, kris, drayden,

    narrator, security, roughneck, roughneck2, roughneck3, sidemon, lace, oldman]

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