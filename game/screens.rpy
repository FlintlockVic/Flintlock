################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

style buttonhover:
    color "#000000"
    hover_color "#f0f0f0"
    font "fonts/pkmndp.ttf"

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    if (what != "{nw}"):
        if (who not in [pokedexlookup(sidemonnum, DexMacros.Name), starter_name] and not renpy.variant("small") and not hideside):
            add SideImage()

        style_prefix "say"

        window:
            id "window"

            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what"

        if (who in [pokedexlookup(sidemonnum, DexMacros.Name), starter_name] and not renpy.variant("small") and not hideside):
            add SideImage()

        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.

    else:
        text what id "what"


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 12

    adjust_spacing True

style say_portrait_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 12

    adjust_spacing True

## Input screen ################################################################
##
## This screen is used to display !. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    modal True
    use currentdate()

    style_prefix "input"

    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        at choicefade
        style "menu_window"
        xalign 0.5
        yalign 0.45

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.80)
        xmaximum int(config.screen_width * 1.00)
        yminimum int(config.screen_height * 0.80)
        ymaximum int(config.screen_height * 1.00)

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    if (not testbattle):
        ## Ensure this appears on top of other screens.
        zorder 100

        #add "gui/dialogue_frame.png" zoom 0.12 ypos 0.99 yanchor 0.5 xalign 0.5

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            if (_rollback):
                textbutton _("Back") action Rollback() text_font "fonts/pkmndp.ttf" background Frame("gui/dialogue_frame.png")
            #textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) text_font "fonts/pkmndp.ttf" background Frame("gui/dialogue_frame.png")
            #textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu() text_font "fonts/pkmndp.ttf" background Frame("gui/dialogue_frame.png")
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            #textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    
    modal True

    # The various buttons.
    imagemap:
        ground "imagemaps/Nav_Menu_Ground.png"
        idle "imagemaps/Nav_Menu_Idle.png"
        hover "imagemaps/Nav_Menu_Hover.png"
        selected_idle "imagemaps/Nav_Menu_Selected.png"
        selected_hover "imagemaps/Nav_Menu_Selected.png"
        
        hotspot (30, 240, 93, 25) action Preference("display", "any window")
        hotspot (162, 240, 115, 25) action Preference("display", "fullscreen")
        
        hotspot (28, 386, 50, 25) action Preference("text speed", 30)
        hotspot (112, 386, 72, 25) action Preference("text speed", 60)
        hotspot (222, 386, 50, 25) action Preference("text speed", 90)
        
        hotspot (28, 527, 50, 25) action SetField(config,"skip_delay",500)
        hotspot (112, 527, 72, 25) action SetField(config,"skip_delay",100)
        hotspot (222, 527, 50, 25) action SetField(config,"skip_delay",10)
        
        hotspot (101, 1018, 86, 31) action Hide("navigation", transition=dissolve)

        bar pos (141, 720) value Preference("music volume") style "pref_slider"
        bar pos (141, 808) value Preference("sound volume") style "pref_slider"
    
    vbox:
        xpos 25
        yanchor 0.5
        ypos 620
        textbutton "{b}Profanity: " + ("On" if profanity else "Off") + "{/b}" action ToggleVariable("profanity") text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#ff0000"
        textbutton "{b}Skip: " + ("All" if preferences.skip_unseen else "Seen") + "{/b}" action ToggleVariable("preferences.skip_unseen") text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#ff0000"
    
init -2 python:
    style.pref_slider.left_bar = "GUI/bar_full.png"
    style.pref_slider.right_bar = "GUI/bar_empty.png"
    style.pref_slider.ymaximum = 6
    style.pref_slider.xmaximum = 110
    style.pref_slider.thumb = None
    style.pref_slider.thumb_offset = 5
    style.pref_slider.thumb_shadow = None

    def SortDatabase():
        if (socialsort == None):
            return persondex.keys()
        elif (socialsort == "abc"):
            return sorted(persondex.keys(), key=(lambda entry : entry))
        elif (socialsort == "lv"):
            return sorted(persondex.keys(), key=(lambda entry : persondex[entry]["Value"]), reverse=True)


screen database():
    $ yvalue = 0
    $ xvalue = 0
    add "BG/Blank2.jpg" alpha 0.6
    for char in SortDatabase():
        $ person = persondex[char]
        $ pointvalue = person["Value"]
        if (person["Named"] and (pointvalue > 0 or GetMood(char) != 0)):
            $ xvalue = math.floor(yvalue/10.0)
            $ ybuffer = (yvalue % 10) * 105
            $ xbuffer = xvalue * -365
            $ chartuple = getscenes([char])[0]
            $ charname = chartuple[0]
            $ hasscene = chartuple[1]
    
            imagebutton idle "GUI/frame_battlestat.png" hover "GUI/frame_pbattlestat.png" xalign 1.0 ypos ybuffer xpos 1920 + xbuffer action NullAction() hovered Show("databasechar", Dissolve(0.5), char) unhovered Hide("databasechar", Dissolve(0.5)) at [Transform(yzoom=0.8), (tintstrobe if hasscene else Transform(matrixcolor=TintMatrix("#fff")))]
            text char pos (1570 + xbuffer, 28 + ybuffer)
            $ gendersymbol = ""
            if ("Sex" in person.values()):
                if (person["Sex"] == Genders.Male):
                    $ gendersymbol = "{color=#2b00ff}♂"
                else:
                    $ gendersymbol = "{color=#ff00b7}♀"
                
            $ valueceil = GetCharacterLevel(char)
            text gendersymbol + "{color=#000000}Lv." + str(valueceil) pos (1905 + xbuffer, 30 + ybuffer) xanchor 1.0

            $ barcolor = getCharColor(char)

            bar range GetEXPRequiredForLevel(char) value pointvalue pos (1565 + xbuffer, 65 + ybuffer) xmaximum 335 right_bar "#fff" left_bar (barcolor if pointvalue > 0 else "#fff")
            text ("EXP: " + str(pointvalue) + ("/" + str(GetEXPRequiredForLevel(char)) if pointvalue > 0 else "")) color "#fff" pos (1575 + xbuffer, 65 + ybuffer) outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
            $ yvalue += 1

    
    vbox:
        textbutton "{b}Back{/b}" action Return() xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        null height 50
        textbutton "Lv. Sort" action SetVariable("socialsort", "lv") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "ABC Sort" action SetVariable("socialsort", "abc") xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Met Sort" action SetVariable("socialsort", None) xminimum 250 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen phoneinterface(targettype = None):
    $ yvalue = 0
    $ xvalue = 0
    $ peopleadded = 0
    add "BG/Blank2.jpg" at dissolvein alpha 0.6
    for char in persondex.keys():
        $ person = persondex[char]
        $ value = person["Value"]
        if ((targettype == None or (targettype != None and char in GetStudents(targettype))) and person["Contact"]):
            $ peopleadded += 1
            $ xvalue = math.floor(yvalue/10.0)
            $ ybuffer = (yvalue % 10) * 105
            $ xbuffer = xvalue * -365
            imagebutton idle "GUI/frame_battlestat.png" hover "GUI/frame_pbattlestat.png" xalign 1.0 ypos ybuffer xpos 1920 + xbuffer action [Hide("databasechar", Dissolve(0.5)), Return(char)] hovered Show("databasechar", Dissolve(0.5), char) unhovered Hide("databasechar", Dissolve(0.5)) at Transform(yzoom=0.8)
            text char pos (1570 + xbuffer, 28 + ybuffer)
            $ gendersymbol = ""
            if ("Sex" in person.values()):
                if (person["Sex"] == Genders.Male):
                    $ gendersymbol = "{color=#2b00ff}♂"
                else:
                    $ gendersymbol = "{color=#ff00b7}♀"
                
            $ valueceil = GetCharacterLevel(char)
            text gendersymbol + "{color=#000000}Lv." + str(valueceil) pos (1905 + xbuffer, 30 + ybuffer) xanchor 1.0

            $ barcolor = getCharColor(char)

            bar range GetEXPRequiredForLevel(char) value value pos (1565 + xbuffer, 65 + ybuffer) xmaximum 335 right_bar "#fff" left_bar (barcolor if value > 0 else "#fff")
            text "EXP: " + str(value) + (("/" + str(GetEXPRequiredForLevel(char))) if value > 0 else "") color "#fff" pos (1575 + xbuffer, 65 + ybuffer) outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]
            $ yvalue += 1

    if (peopleadded == 0):
        text "No Contacts" size 40 align (0.5, 0.5) color "#fff"

    textbutton "Back" action Return("Back") xminimum 200 text_xalign .5 xalign 0.0 yalign 1.0 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"


screen databasechar(char):
    $ charcolor = getCharColor(char)
    $ finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
    $ value = persondex[char]["Value"]
    $ valueceil = GetCharacterLevel(char)
    $ charimage = char.lower()
    if (char == "Professor Cherry"):
        $ charimage = "kris"
    elif (char in ["Professor Oak", "Gramps"]):
        $ charimage = "oak"
    elif (char == "Tia" and not IsBefore(17, 4, 2004)):
        $ charimage = "tia hat"
    elif (char == first_name):
        $ charimage = "red shadow noeyes frownmouth"
    add charimage xpos ((1 * 1.25 + 1) / 10.0) - 50 matrixcolor finalmatrix
    add charimage xpos ((1 * 1.25 + 1) / 10.0)
    if (usingmoods):
        $ mood = GetMood(char)
    text "{size=80}{color=" + charcolor + "}" + char.replace(" ", "\n") + "\n{/color}{size=40}Lv." + str(valueceil) + ", EXP: " + str(value) + ("\n{/color}{size=40}Mood: " + moodtoword(mood) + " (" + str(mood) + ")" if usingmoods and GetNature(char) != TrainerNature.Special else ("\n{/color}{size=40}Mood: Stable" if usingmoods and GetNature(char) == TrainerNature.Special else "")) xpos ((1 * 1.25 + 1) / 10.0) + (1 * 0.03 - 0.1) color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at Transform(rotate=-15)

    $ classstring = "None"
    for i, classtype in enumerate(persondex[char]["ClassesKnown"]):
        if (classstring == "None"):
            $ classstring = ""
        if (i != 0):
            $ classstring += ", "
        $ classstring += classtype

    if (char == "Ethan"):
        $ classstring = "All"

    $ chartuple = getscenes([char])[0]
    $ charname = chartuple[0]
    $ hasscene = chartuple[1]
    $ posttext = ""
    if (not hasscene):
        if charname in sceneconditions.keys() and GetRelationship(charname) in sceneconditions[charname].keys():
            $ posttext = sceneconditions[charname][GetRelationship(charname)]
    else:
        $ posttext = "{gradient2=3-#f00-#0f0-33-#0f0-#00f-33-#00f-#f00-33}{b}Ready!{/b}{/gradient2}"

    $ height = 160
    if (posttext != ""):
        $ height += 35
    if (usingmoods and GetNature(char) != TrainerNature.Special):
        $ height += 105 
    add "images/GUI/readback.png" xysize (550, height) xpos 0.22 xanchor 0.5 yanchor 1.0 ypos 0.98

    vbox:
        xpos 0.22 xanchor 0.5 yanchor 1.0 ypos 0.95 spacing 5
        if (posttext != ""):
            text "{b}Next Scene:{/b} " + posttext color "#000" size 30

        if (usingmoods and GetNature(char) != TrainerNature.Special):
            $ bondchange = mooddict[max(min(10, GetMood(char)), -10)][GetNature(char)][0]
            $ moodchange = mooddict[max(min(10, GetMood(char)), -10)][GetNature(char)][1]
            text "{b}Current Mood:{/b} " + moodtoword(mood) + " (" + str(mood) + ")" color "#000" size 30
            if (bondchange == 0 and moodchange == 0):
                text "{b}Next Day:{/b} No Change" color "#000" size 30 
            else:
                text "{b}Next Day:{/b} " + ("+" if bondchange > -1 else "" ) + str(bondchange) + " Bond, " + ("+" if moodchange > -1 else "" ) + str(moodchange) + " Mood" color "#000" size 30 
            text "{b}Nature:{/b} " + str(GetNature(char)) color "#000" size 30 
        text "{b}Relationship:{/b} " + GetRelationship(char) color "#000" size 30
        text "{b}Contact Info:{/b} " + ("Acquired" if persondex[char]["Contact"] else "Unacquired") color "#000" size 30
        text "{b}Known Classes:{/b} " + classstring color "#000" size 30

init python:
    def moodtoword(points):
        if (points <= -10):
            return "Desolate"
        elif (points == -9):
            return "Heartbroken"
        elif (points == -8):
            return "Devastated"
        elif (points == -7):
            return "Sorrowful"
        elif (points == -6):
            return "Downtrodden"
        elif (points == -5):
            return "Depressed"
        elif (points == -4):
            return "Unhappy"
        elif (points == -3):
            return "Saddened"
        elif (points == -2):
            return "Irritated"
        elif (points == -1):
            return "Discontent"
        elif (points == 0):
            return "Mellow"
        elif (points == 1):
            return "Content"
        elif (points == 2):
            return "Serene"
        elif (points == 3):
            return "Happy"
        elif (points == 4):
            return "Joyful"
        elif (points == 5):
            return "Ecstatic"
        elif (points == 6):
            return "Exuberant"
        elif (points == 7):
            return "Jubilant"
        elif (points == 8):
            return "Delighted"
        elif (points == 9):
            return "Euphoric"
        elif (points >= 10):
            return "Blissful"

screen traits():
    if (playercharacter == None):
        add "red happy" xpos 0.65 ypos 1.5
    elif (playercharacter == "Ethan"):
        add "ethan closedbrow talking2mouth" xpos 0.65 ypos 1.5
    elif (playercharacter == "Blue"):
        add "blue" xpos 0.65 ypos 1.5
    elif (playercharacter == "Leaf"):
        add "leaf flirt" xpos 0.65 ypos 1.4
    add "BG/Blank2.jpg" alpha 0.6
    $ plot_values = (personalstats["Charm"] + 15, personalstats["Knowledge"] + 15, personalstats["Courage"] + 15, personalstats["Wit"] + 15, personalstats["Patience"] + 15)
    add RadarChart(
        size=800,
        values=plot_values,
        max_value=75,
        labels=[Text("{color=#b7669e}Charm\nLv. " + str(plot_values[0] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]), 
            Text("{color=#66b77d}Knowledge\nLv. " + str(plot_values[1] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]), 
            Text("{color=#ff8412}Courage\nLv. " + str(plot_values[2] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]), 
            Text("{color=#60c2f8}Wit\nLv. " + str(plot_values[3] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ]), 
            Text("{color=#e226a6}Patience\nLv. " + str(plot_values[4] - 15), outlines=[ (absolute(10), "#000", absolute(0), absolute(0)) ])],
        lines={"webs": [2, 4, 6, 8]},
        data_colour=(255, 0, 0, 255),
        line_colour=(153, 153, 153, 255),
        background_colour=(255, 255, 255, 255)) align (0.17, 0.55)

    text "TRAITS" color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] size 80 xpos .24 ypos .85
    text "PROFICIENCIES" color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] size 80 xalign .98 ypos .1

    grid 2 9:
        xalign 0.98
        yalign 0.5
        spacing 20
        for classtype in altclassdex.keys():     
            text classtype + ": " + FormatNum(classstats[classtype]) size 30 color ("#f00" if classstats[getRankStat(0)] == classstats[classtype] else "#fff") outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

    textbutton "Back" action Return() xminimum 200 text_xalign .5 xalign 0.0 yalign 1.0 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

init python:
    def SwapPositions(pos1, pos2):
        global pkmnlocked
        try:
            playerparty[pos1], playerparty[pos2] = playerparty[pos2], playerparty[pos1]
            pkmnlocked = pos2
        except:
            pkmnlocked = -1

screen partyviewer():
    for i, pkmn in enumerate(playerparty):
        textbutton "" xalign 1.0 ypos 50 + 100 * i xminimum 115 yminimum 100 background Color("#d200ab" if i == pkmnlocked else "#d200ac00")
        imagebutton: 
            idle "GUI/stats_frame.png" 
            hover "GUI/stats_frame_hover.png" 
            action (SetVariable("pkmnlocked", (-1 if pkmnlocked != -1 else i)) if pkmnlocked == -1 or pkmnlocked == i else Function(SwapPositions, pkmnlocked, i))
            xalign 1.0 
            ypos 50 + 100 * i 
            hovered ([Show("mondata", Dissolve(0.5), pkmn), Show("nonbattlemoves", Dissolve(0.5), pkmn)] if pkmnlocked == -1 else NullAction()) 
            unhovered ([Hide("mondata", Dissolve(0.5)), Hide("nonbattlemoves", Dissolve(0.5)), Hide("movedata", Dissolve(0.5))] if pkmnlocked == -1 else Hide("movedata", Dissolve(0.5)))
        add "GUI/pokeballicon.webp" xanchor 1.0 xpos 1900 ypos 60 + 100 * i
        if (pkmn.GetImage() == "Pokemon/25.2.webp"):
            add "Pokemon/25.2.webp" zoom 0.2 ypos 45 + 100 * i xanchor 1.0 xpos 1925 at (monochrome if max(pkmn.GetHealth(), pkmn.GetCaught()) <= 0 else None)
            add "Pokemon/25.2-1.webp" zoom 0.2 ypos 45 + 100 * i xanchor 1.0 xpos 1925 matrixcolor TintMatrix(GetLiberaColor()) at (monochrome if max(pkmn.GetHealth(), pkmn.GetCaught()) <= 0 else None)
            add "Pokemon/25.2-2.webp" zoom 0.2 ypos 45 + 100 * i xanchor 1.0 xpos 1925 matrixcolor TintMatrix(GetLiberaColor(False)) at (monochrome if max(pkmn.GetHealth(), pkmn.GetCaught()) <= 0 else None)
        else:
            add pkmn.GetImage() zoom 0.2 ypos 60 + 100 * i xanchor 1.0 xpos 1900 at (monochrome if max(pkmn.GetHealth(), pkmn.GetCaught()) <= 0 else None)
        if (pkmn.GetItem() != None):
            add "GFX/item.png" zoom 0.3 ypos 55 + 100 * i xanchor 1.0 xpos 1915
        if (pkmn.GetForeverals() != []):
            add "GFX/foreveral.png" zoom 0.3 ypos 100 + 100 * i xanchor 1.0 xpos 1915
        if (pkmn.GetHealthPercentage() < 1):
            $ maxhealth = pkmn.GetStat(Stats.Health, triggerAbilities=False)
            $ health = max(pkmn.GetHealth(), pkmn.GetCaught())
            $ barcolor = "#00b612"
            if (health / maxhealth <= 0.25):
                $ barcolor = "#ff0000"
            elif (health / maxhealth <= 0.5):
                $ barcolor = "#fff700"
            bar range maxhealth value health pos (1910, 135 + 100 * i) xanchor 1.0 xmaximum 100 ymaximum 10 yminimum 10 right_bar "#000" left_bar barcolor

screen wallet():
    if (money > 0):
        frame:
            ypadding 10
            xpadding 15
            background Frame("GFX/DateTimeBanner.png") at Transform(xzoom=-1)
            text "$" + str('{:,}'.format(money)) size 28 color "#1c1c1c" at Transform(xzoom=-1)

screen repelwidget():
    if (activerepel != None):
        frame:
            ypos 55
            ypadding 10
            xpadding 15
            background Frame("GFX/DateTimeBanner.png") at Transform(xzoom=-1)
            text " " + activerepel + " active. Encounters left: " + str(repelstepsleft) size 28 color "#1c1c1c" at Transform(xzoom=-1)

screen inventorywidget():
    if (len(inventory) > 1):
        imagebutton: 
            idle "GUI/stats_frame.png" 
            hover "GUI/stats_frame_hover.png" 
            action [SetVariable("activemon", None), SetVariable("activeitem", None), SetVariable("invoverwrite", None), ShowTransient("fieldinventory")]
            align (1.0, 1.0)
        add "GUI/backpack.webp" align (0.99, 0.99) 

screen foreveralwidget():
    if (len(foreveralinv) > 1):
        imagebutton: 
            idle "GUI/stats_frame.png" 
            hover "GUI/stats_frame_hover.png" 
            action [ShowTransient("foreveralinventory")]
            align (1.0, 0.9)
        add "GUI/foreveralsicon.png" align (0.99, 0.89)

init python:
    def GetForeveralMonname(foreveralname, changenidoran = True):
        monname = foreveralname[:foreveralname.index(" ")]
        if ("Mime Jr." in foreveralname):
            monname = "Mime Jr."
        elif ("Mr. Mime" in foreveralname):
            monname = "Mr. Mime"
        elif (monname == "Nidoran" and changenidoran):
            monname += random.choice(["♀", "♂"])
        return monname

    def GetPlayerpartyForeverals():
        partyforeverals = []
        for mon in playerparty:
            if mon.GetForeverals() != []:
                partyforeverals.append(mon.GetForeverals())
        return partyforeverals

    def SortedForeverals():
        global foreveraldex
        if (foreveralsort == "National Dex"):
            foreveraldex.sort(reverse = foreveralsortinverse, key=(lambda entry : pokedexlookupname(GetForeveralMonname(entry[0], True), DexMacros.Id)))
        elif (foreveralsort == "Obtained"):
            foreveraldex.sort(reverse = foreveralsortinverse, key=(lambda entry : (1000000 if entry[0] not in foreveralinv else foreveralinv.index(entry[0]))))
        elif (foreveralsort == "Type"):
            foreveraldex.sort(reverse = foreveralsortinverse, key=(lambda entry : pokedexlookupname(GetForeveralMonname(entry[0], True), DexMacros.Type1)))
        elif (foreveralsort == "Category"):
            foreveraldex.sort(reverse = foreveralsortinverse, key=(lambda entry : entry[0].replace(GetForeveralMonname(entry[0], False), "")))
        elif (foreveralsort == "Alphabetical"):
            foreveraldex.sort(reverse = foreveralsortinverse, key=(lambda entry : entry[0]))

        return foreveraldex[foreveralpage * 30:foreveralpage * 30 + 30]

label giveforeveral(foreveralname):
    narrator "What would you like to do with this Foreveral?"

    python:
        hasmon = False
        foreveralheld = False
        monname = GetForeveralMonname(foreveralname, False)
        eligiblemons = []
        eligiblenames = []
        for mon in playerparty:
            if (pokedexlookup(mon.GetId(), DexMacros.Name) == monname or (monname == "Nidoran" and "Nidoran" in pokedexlookup(mon.GetId(), DexMacros.Name))):
                eligiblemons.append(mon)
                eligiblenames.append(mon.GetNickname())
                hasmon = True

        for mon in playerparty + box:
            if (foreveralname in mon.GetForeverals()):
                foreveralheld = True

        preposition = "a"
        if (monname[0] in ["A", "E", "I", "O", "U"]):
            preposition += "n"

    menu:
        ">Read Description.":
            if (not renpy.get_screen("decorativeforeveralinventory") and not renpy.get_screen("foreveralinventory")):
                show screen decorativeforeveralinventory
            call foreveraldata(foreveralname) from _call_foreveraldata

        ">Use it on [preposition] [monname].":
            if (not hasmon):
                narrator "You do not have [preposition] [monname] with you right now."
            else:
                $ chosenmon = None
                $ eligiblenames
                menu:
                    ">Use the [foreveralname] on [eligiblenames[0]].":
                        $ chosenmon = eligiblemons[0]
                    ">Use the [foreveralname] on [eligiblenames[1]]." if (len(eligiblemons) > 1):
                        $ chosenmon = eligiblemons[1]
                    ">Use the [foreveralname] on [eligiblenames[2]]." if (len(eligiblemons) > 2):
                        $ chosenmon = eligiblemons[2]
                    ">Use the [foreveralname] on [eligiblenames[3]]." if (len(eligiblemons) > 3):
                        $ chosenmon = eligiblemons[3]
                    ">Use the [foreveralname] on [eligiblenames[4]]." if (len(eligiblemons) > 4):
                        $ chosenmon = eligiblemons[4]
                    ">Use the [foreveralname] on [eligiblenames[5]]." if (len(eligiblemons) > 5):
                        $ chosenmon = eligiblemons[5]
                    "Nevermind.":
                        pass
                
                if (chosenmon != None):
                    python:
                        movenames = []
                        for moves in lookupforeveraldata(foreveralname, FVLMacros.FVLMoves):
                            movenames.append(moves)
                    menu:
                        ">Teach [movenames[0]]." if len(movenames) > 0:
                            $ chosenmon.LearnNewMove([(0, movenames[0])])

                        ">Teach [movenames[1]]." if len(movenames) > 1:
                            $ chosenmon.LearnNewMove([(0, movenames[1])])

                        ">Teach [movenames[2]]." if len(movenames) > 2:
                            $ chosenmon.LearnNewMove([(0, movenames[2])])

                        ">Swap form." if ("Diveral" in foreveralname):
                            python:
                                forms = lookupforeveraldata(foreveralname, FVLMacros.FVLTypeData)
                                if (chosenmon.GetId() == forms[0]):
                                    chosenmon.ChangeForme(forms[1])
                                else:
                                    chosenmon.ChangeForme(forms[0])

                        ">Remove form." if ("Diveral" in foreveralname):
                            $ chosenmon.ChangeForme(None, revert=True)

                        "Nevermind.":
                            pass

        ">Give it to [preposition] [monname].":
            if (not hasmon):
                narrator "You do not have [preposition] [monname] with you right now."
            else:
                $ chosenmon = None
                $ eligiblenames
                menu:
                    ">Give the [foreveralname] to [eligiblenames[0]].":
                        $ chosenmon = eligiblemons[0]
                    ">Give the [foreveralname] to [eligiblenames[1]]." if (len(eligiblemons) > 1):
                        $ chosenmon = eligiblemons[1]
                    ">Give the [foreveralname] to [eligiblenames[2]]." if (len(eligiblemons) > 2):
                        $ chosenmon = eligiblemons[2]
                    ">Give the [foreveralname] to [eligiblenames[3]]." if (len(eligiblemons) > 3):
                        $ chosenmon = eligiblemons[3]
                    ">Give the [foreveralname] to [eligiblenames[4]]." if (len(eligiblemons) > 4):
                        $ chosenmon = eligiblemons[4]
                    ">Give the [foreveralname] to [eligiblenames[5]]." if (len(eligiblemons) > 5):
                        $ chosenmon = eligiblemons[5]
                    "Nevermind.":
                        pass
                
                if (chosenmon != None):
                    $ chosenname = chosenmon.GetNickname()
                    if (chosenmon.GetForeverals() != []):
                        $ chosenmonfvl = chosenmon.GetForeverals()[0]
                        narrator "[chosenname] is currently holding the [chosenmonfvl]. Would you like to swap them?"

                        menu:
                            "Sure.":
                                $ foreveralinv.append(chosenmonfvl)
                                $ chosenmon.Foreverals = [foreveralname]
                                $ foreveralinv.remove(foreveralname)
                                $ chosenmon.RecalculateStats()

                                narrator "You swapped the [chosenmonfvl] for the [foreveralname], and put the [chosenmonfvl] back in your bag."

                            "Nevermind.":
                                pass
                    else:
                        $ chosenmon.Foreverals = [foreveralname]
                        $ foreveralinv.remove(foreveralname)
                        $ chosenmon.RecalculateStats()
                        
                        narrator "You gave [chosenname] the [foreveralname]."

        ">Use it on [pika_name].":
            if (pikachuobj not in playerparty):
                narrator "[pika_name] is not with you right now."
            else:
                python:
                    movenames = []
                    for moves in lookupforeveraldata(foreveralname, FVLMacros.FVLMoves):
                        movenames.append(moves)
                menu:
                    ">Teach [movenames[0]]." if len(movenames) > 0:
                        $ pikachuobj.LearnNewMove([(0, movenames[0])])

                    ">Teach [movenames[1]]." if len(movenames) > 1:
                        $ pikachuobj.LearnNewMove([(0, movenames[1])])

                    ">Teach [movenames[2]]." if len(movenames) > 2:
                        $ pikachuobj.LearnNewMove([(0, movenames[2])])

                    ">Swap form." if ("Diveral" in foreveralname):
                        if (pikachuobj.GetForeverals() != []):
                            narrator "Diveralizing [pika_name] will de-sync all his current Foreverals, putting them back in your inventory. Is this okay?"
                            menu:
                                "Sure.":
                                    python:
                                        for fvl in pikachuobj.GetForeverals():
                                            foreveralinv.append(fvl)
                                        pikachuobj.Foreverals = []

                                "Nevermind.":
                                    jump endgiveforeveral

                        python:
                            forms = lookupforeveraldata(foreveralname, FVLMacros.FVLTypeData)
                            if (pikachuobj.GetId() == forms[0]):
                                pikachuobj.ChangeForme(forms[1])
                            else:
                                pikachuobj.ChangeForme(forms[0])

                    ">Remove form." if ("Diveral" in foreveralname):
                        $ pikachuobj.ChangeForme(None, revert=True)

                    "Nevermind.":
                        pass

        ">Give it to [pika_name].":
            if (pikachuobj not in playerparty):
                narrator "[pika_name] is not with you right now."
            else:
                if (pikachuobj.GetFormeOverride() != None):
                    narrator "[pika_name] is currently under the influence of a Diveral. Would you like to Undiveralize [pika_name] to give him the [foreveralname]?"
                    menu:
                        "Sure.":
                            $ pikachuobj.ChangeForme(None, revert=True)
                            $ pikachuobj.RecalculateStats()

                        "Nevermind.":
                            jump endgiveforeveral

                if (pikachuobj.GetForeverals() != []):
                    $ pikafvl = pikachuobj.GetForeverals()[0]
                    narrator "[pika_name] is currently holding the [pikafvl]. Would you like to swap them?"
                    menu:
                        "Sure.":
                            $ foreveralinv.append(pikafvl)
                            $ pikachuobj.Foreverals = [foreveralname]
                            $ foreveralinv.remove(foreveralname)
                            $ pikachuobj.RecalculateStats()

                            narrator "You swapped the [pikafvl] for the [foreveralname], and put the [pikafvl] back in your bag."

                        "Nevermind.":
                            pass
                else:
                    $ pikachuobj.Foreverals = [foreveralname]
                    $ foreveralinv.remove(foreveralname)
                    $ pikachuobj.RecalculateStats()

                    narrator "You gave [pika_name] the [foreveralname]."

        "Nevermind.":
            pass

    label endgiveforeveral:

    hide screen decorativeforeveralinventory

    $ renpy.show_screen("foreveralinventory", _transient=True)

    return

label foreveraldata(foreveralname, inbattle=False):
    if (not inbattle and not renpy.get_screen("decorativeforeveralinventory") and not renpy.get_screen("foreveralinventory")):
        show screen decorativeforeveralinventory

    python:
        explainingf = True
        entry = None
        for otherentry in foreveraldex:
            if (otherentry[0] == foreveralname):
                entry = otherentry
                break
        trainer = entry[1]
        level = entry[2]
        description = entry[6]
        movesimparted = str(entry[5])
        movesimparted = movesimparted.replace("[", "").replace("]", "").replace("'", "")
        pokemontype = pokedexlookupname(GetForeveralMonname(foreveralname), DexMacros.Type1)

    narrator "This is the [foreveralname]. [pika_name] will create it when you reach a bond level of [level] with [trainer]."
    narrator "When equipped to an appropriate Pokemon, it has the following effect: [description]."
    if ("Diveral" in foreveralname):
        narrator "This Diveral can be used outside of battle to switch an appropriate Pokémon's form."
    if (len(entry[5]) > 0):
        narrator "When used on the appropriate Pokemon, it can teach the following move(s): [movesimparted]."
    if (pokemontype != "Electric"):
        narrator "When given to [pika_name], his Electric-type will be replaced by [pokemontype]."

    if (not inbattle):
        hide screen decorativeforeveralinventory

        $ renpy.show_screen("foreveralinventory", _transient=True)
        
    $ explainingf = False
    return

screen foreveralinventory:
    zorder 10
    modal True
    hbox:
        align (0.5, 0.05)
        textbutton "National Dex" action SetVariable("foreveralsort", "National Dex") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "National Dex" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Obtained" action SetVariable("foreveralsort", "Obtained") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Obtained" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Type" action SetVariable("foreveralsort", "Type") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Type" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Category" action SetVariable("foreveralsort", "Category") xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Category" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Alphabetical" action SetVariable("foreveralsort", "Alphabetical") xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Alphabetical" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
    textbutton "Page " + str(foreveralpage + 1) + "/" + str(math.floor(len(foreveraldex) / 30)) xmaximum 223 xpos 0.151 ypos .125 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
    frame:
        xpos 0.209
        yanchor 0.0
        ypos 0.124
        xysize (1118, 545)
        background "images/GUI/readback.png"
        if (invoverwrite == None):
            $ foreveralcount = 0
            grid 3 10:
                transpose True
                for foreveral in SortedForeverals():
                    $ foreveralcount += 1
                    $ color = GetTypeColor(pokedexlookupname(GetForeveralMonname(foreveral[0], True), DexMacros.Type1))
                    textbutton ("{gradient=" + color + "-" + ("#fff" if examinedf == foreveral else ("#2b2b2b" if foreveral[0] in foreveralinv else "#717171")) + "}" if foreveral[0] in foreveralinv else "") + foreveral[0][:5] + ("{/gradient}" if foreveral[0] in foreveralinv else "") + foreveral[0][5:]:
                        text_size 30
                        text_color ("#2b2b2b" if foreveral[0] in foreveralinv else "#717171") 
                        action [SetVariable("examinedf", None), (Call("giveforeveral", foreveral[0], from_current=True) if foreveral[0] in foreveralinv else Call("foreveraldata", foreveral[0], from_current=True))]
                        text_hover_color "#fff"
                        hovered SetVariable("examinedf", foreveral)
                        unhovered SetVariable("examinedf", None)
                for x in range(30 - foreveralcount):
                    null

    hbox:
        xalign .5 yalign 0.68
        textbutton "<-" action (SetVariable("foreveralpage", foreveralpage - 1) if foreveralpage > 0 else SetVariable("foreveralpage", math.floor(len(foreveraldex) / 30 - 1))) xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Back" action Hide("foreveralinventory") xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "->" action (SetVariable("foreveralpage", foreveralpage + 1) if foreveralpage < math.floor(len(foreveraldex) / 30 - 1) else SetVariable("foreveralpage", 0)) xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen decorativeforeveralinventory:
    zorder 10
    hbox:
        align (0.5, 0.05)
        textbutton "National Dex" xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "National Dex" else "#ff0000") style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Obtained" xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Obtained" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Type" xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Type" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Category" xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Category" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Alphabetical" xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if foreveralsort != "Alphabetical" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
    textbutton "Page " + str(foreveralpage + 1) + "/" + str(math.floor(len(foreveraldex) / 30)) xmaximum 223 xpos 0.151 ypos .125 text_size 40 text_xalign 0.5 text_color "#000" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
    frame:
        xpos 0.209
        yanchor 0.0
        ypos 0.124
        xysize (1118, 545)
        background "images/GUI/readback.png"
        if (invoverwrite == None):
            $ foreveralcount = 0
            grid 3 10:
                transpose True
                for foreveral in SortedForeverals():
                    $ foreveralcount += 1
                    $ color = GetTypeColor(pokedexlookupname(GetForeveralMonname(foreveral[0], True), DexMacros.Type1))
                    textbutton ("{gradient=" + color + "-" + ("#fff" if examinedf == foreveral else ("#2b2b2b" if foreveral[0] in foreveralinv else "#717171")) + "}" if foreveral[0] in foreveralinv else "") + foreveral[0][:5] + ("{/gradient}" if foreveral[0] in foreveralinv else "") + foreveral[0][5:] text_color ("#2b2b2b" if foreveral[0] in foreveralinv else "#717171") text_size 30
                    #textbutton foreveral[0] text_color ("#2b2b2b" if foreveral[0] in foreveralinv else "#717171") text_hover_color "#fff"
                for x in range(30 - foreveralcount):
                    null

    hbox:
        xalign .5 yalign 0.68
        textbutton "<-" xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Back" xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "->" xminimum 200 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

init python:
    def InvokeUseItem(partymon = None):
        renpy.invoke_in_new_context(UseItem, partymon)

screen fieldinventory(pickitem = False):
    zorder 10
    modal True
    hbox:
        align (0.5, 0.05)
        textbutton "Healing" action SetVariable("invpage", "Healing") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Healing" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Evo Items" action SetVariable("invpage", "Evo Items") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Evo Items" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Poké Balls" action SetVariable("invpage", "Poké Balls") xmaximum 224 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Poké Balls" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Battle Items" action SetVariable("invpage", "Battle Items") xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Battle Items" else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        textbutton "Misc." action SetVariable("invpage", "Misc.") xmaximum 223 text_size 40 text_xalign 0.5 text_color ("#000" if invpage != "Misc." else "#ff0000") text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
    frame:
        xpos 0.209
        yanchor 0.0
        ypos 0.124
        xysize (1118, 545)
        background "images/GUI/readback.png"
        if (invoverwrite == None):
            $ itemcount = 0
            grid 4 10:
                transpose True
                for item in inventory.keys():
                    if (invpage == InventoryCategory(item)):
                        $ itemcount += 1
                        textbutton ("" if inventory[item] == 1 else str(inventory[item]) + "x ") + item text_color "#2b2b2b" action ([SetVariable("activeitem", item), SetVariable("invoverwrite", "What would you like to do with the {}?".format(item))] if not pickitem else Return(item)) text_hover_color "#fff"
                for x in range(40 - itemcount):
                    null
        elif (invoverwrite[:4] == "What"):
            vbox:
                xfill True
                spacing 30
                null
                text invoverwrite color "#000000" size 40 xalign 0.5
                if (not TrainerItem(activeitem)):
                    textbutton ">Give to a Pokémon." action SetVariable("invoverwrite", "Which Pokémon do you want to give the {} to?".format(activeitem)) xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
                    textbutton ">Use on a Pokémon." action SetVariable("invoverwrite", "Which Pokémon do you want to use the {} on?".format(activeitem)) xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
                else:
                    textbutton ">Use the item." action Function(InvokeUseItem) xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
                textbutton "Nevermind." action [SetVariable("activeitem", None), SetVariable("invoverwrite", None)] xsize 250 xfill True text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
        elif (invoverwrite[:5] == "Which"):
            vbox:
                xfill True
                spacing 30
                null
                text invoverwrite color "#000000" size 40 xalign 0.5
                null
                grid 3 2:
                    spacing 20
                    xalign 0.5
                    for partymon in playerparty:
                        textbutton partymon.GetNickname() action (Function(InvokeUseItem, partymon) if "use" in invoverwrite else Function(GiveItem, partymon)) xsize 200 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
                    for x in range(6 - len(playerparty)):
                        null
                textbutton "Nevermind." action [SetVariable("activeitem", None), SetVariable("invoverwrite", None)] xsize 250 xfill True text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
        
        elif ("is already holding" in invoverwrite):
            vbox:
                xfill True
                spacing 30
                null
                text invoverwrite color "#000000" size 40 xalign 0.5
                null
                textbutton "Yes, swap items." action Function(SwapItems) xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        
                textbutton "Nevermind." action [SetVariable("activeitem", None), SetVariable("invoverwrite", None)] xsize 250 xfill True text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"
        else:
            vbox:
                xfill True
                spacing 30
                null
                text invoverwrite color "#000000" size 40 xalign 0.5
                null
                textbutton "Confirm" action [SetVariable("activemon", None), SetVariable("activeitem", None), SetVariable("invoverwrite", None)] xsize 250 text_xalign .5 text_size 30 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"        

    textbutton "Back" action ([SetVariable("activemon", None), SetVariable("activeitem", None), SetVariable("invoverwrite", None), (Hide("fieldinventory") if not pickitem else Return("back"))]) xminimum 200 text_xalign .5 xalign .5 yalign 0.68 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen mondata(pkmn, showtip = True):
    add "gui/button/choice_idle_background.png" xalign .5 xzoom 1.5 yzoom 15
    $ gendersymbol = ""
    if (pkmn.GetGender() == Genders.Male):
        $ gendersymbol = "{color=#2b00ff}♂"
    elif (pkmn.GetGender() == Genders.Female):
        $ gendersymbol = "{color=#ff00b7}♀"
    add pkmn.GetImage() yalign 0.25 xalign 0.5 alpha 0.2
    if (pkmn.GetImage() == "Pokemon/25.2.webp"):
        add "Pokemon/25.2-1.webp" yalign 0.25 xalign 0.5 alpha 0.2 matrixcolor TintMatrix(GetLiberaColor())
        add "Pokemon/25.2-2.webp" yalign 0.25 xalign 0.5 alpha 0.2 matrixcolor TintMatrix(GetLiberaColor(False))
    $ nick = pkmn.GetNickname()
    text nick + " " + gendersymbol + ("" if nick == pokedexlookup(pkmn.GetId(), DexMacros.Name) else "\n{size=30}{color=#000}(" + pokedexlookup(pkmn.GetId(), DexMacros.Name) + "){/size}") xminimum 550 xpos .1 yalign .05 size (70 if len(nick) < 10 else 50)
    text "Lv. " + str(pkmn.GetLevel()) xminimum 550 xalign .5 ypos .03 size 50
    text "(Cap: " + str(math.floor(pkmn.GetLevelCap())) + ", Potential: " + str(pkmn.GetMaxLevel()) + ")" xalign .5 ypos .09 size 40
    
    $ typestring = ""
    for element in pkmn.GetTypes():
        if (typestring != ""):
            $ typestring += "{color=#fff}/{/color}"
        $ typestring += "{color=" + GetTypeColor(element) + "}" + element + "{/color}"

    text typestring yalign .07 size 70 xanchor 1.0 xpos 0.85 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
    
    grid 4 7:
        xalign .5
        ypos .15
        text "{b}Stat" xminimum 300 size 40
        text "{b}Value" xminimum 300 xalign .5 size 40
        text "{b}EVs" xminimum 300 xalign .5 size 40
        text "{b}IVs" xminimum 300 xalign .5 size 40
        text "HP" xminimum 300 size 40
        text str(max(pkmn.GetHealth(), pkmn.GetCaught())) + "/" + str(pkmn.GetStat(Stats.Health)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.Health)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.Health)) + "/31" xminimum 300 xalign .5 size 40
        $ attackbonus = NatureToBonus(pkmn.GetNature(), Stats.Attack)
        text "Attack" xminimum 300 size 40 color ("#000" if attackbonus == 1 else ("#ff0000" if attackbonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.Attack, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.Attack)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.Attack)) + "/31" xminimum 300 xalign .5 size 40
        $ defensebonus = NatureToBonus(pkmn.GetNature(), Stats.Defense)
        text "Defense" xminimum 300 size 40 color ("#000" if defensebonus == 1 else ("#ff0000" if defensebonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.Defense, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.Defense)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.Defense)) + "/31" xminimum 300 xalign .5 size 40
        $ specialattackbonus = NatureToBonus(pkmn.GetNature(), Stats.SpecialAttack)
        text "Special Attack" xminimum 300 size 40 color ("#000" if specialattackbonus == 1 else ("#ff0000" if specialattackbonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.SpecialAttack, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.SpecialAttack)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.SpecialAttack)) + "/31" xminimum 300 xalign .5 size 40
        $ specialdefensebonus = NatureToBonus(pkmn.GetNature(), Stats.SpecialDefense)
        text "Special Defense" xminimum 300 size 40 color ("#000" if specialdefensebonus == 1 else ("#ff0000" if specialdefensebonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.SpecialDefense, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.SpecialDefense)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.SpecialDefense)) + "/31" xminimum 300 xalign .5 size 40
        $ speedbonus = NatureToBonus(pkmn.GetNature(), Stats.Speed)
        text "Speed" xminimum 300 size 40 color ("#000" if speedbonus == 1 else ("#ff0000" if speedbonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.Speed, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.Speed)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.Speed)) + "/31" xminimum 300 xalign .5 size 40

    text "EXP: " + str(math.floor(pkmn.GetExperience())) + ", To Next Level: " + str(math.floor(pkmn.CalculateAllExperienceNeededForLevel(pkmn.GetMaxLevel() + 1) - pkmn.GetExperience()) + 1) size 40 yalign .43 xalign 0.5

    $ status = "None"
    if (pkmn.GetHealthPercentage() <= 0.0 and pkmn.GetCaught() <= 0):
        $ status = "Fainted"
    else:
        for statustype in nonvolatiles:
            if (pkmn.HasStatus(statustype)):
                $ status = statustype
    
    hbox:
        yalign .48
        xalign .5
        spacing 30
        text "Status: " + status.title() xminimum 300 size 40 yalign .5
        if (pkmn.GetItem() == None):
            text "Item: None" xminimum 300 size 40 yalign .5
        else:
            textbutton "Item: " + pkmn.GetItem():
                xminimum 300 text_xalign .5
                ymaximum 60 text_size 40 text_color "#000" text_hover_color "#f0f" 
                style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
                action [Function(RemoveItem, pkmn)]

        text "Nature: " + NatureToString(pkmn.GetNature()) xminimum 300 size 40 yalign .5
        $ fvlability = False
        for fvl in pkmn.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                $ fvlability = True
        if (not fvlability):
            text "Ability: " + pkmn.GetAbility() xminimum 300 size 40 yalign .5
        else:
            hbox:
                text "Ability: " xminimum 300 size 40 yalign .5
                vbox:
                    text pkmn.GetAbility() xminimum 300 size 40 yalign .5
                    for fvl in pkmn.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                            for ability in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                                text "(" + ability + ")" xminimum 300 size 40 yalign .5
        if (usingforeverals):
            if (pkmn.GetForeverals() == []):
                text "Foreveral: None" xminimum 300 size 40 yalign .5
            else:
                textbutton "Foreveral: " + pkmn.GetForeverals()[0]:
                    xminimum 300 text_xalign .5
                    ymaximum 60 text_size 40 text_color "#000" text_hover_color "#f0f" 
                    style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
                    action [Function(RemoveForeverals, pkmn)]
    if (showtip):
        text ("(Click on {} to lock screen and switch Pokémon.)" if pkmnlocked == -1 else "{{u}}(Click on {} to unlock screen, or click on another Pokémon to switch positions.){{/u}}").format(pkmn.GetNickname()) xminimum 300 xalign .5 yalign .55 size 40

screen nonbattlemoves(pkmn, newmove=False, tooltips = True, ismodal=False):
    zorder 5
    grid len(pkmn.GetMoves()) 1:
        xalign .5
        yalign (.65 if tooltips else .55)
        for move in pkmn.GetMoves():
            textbutton move.Name: 
                action ([Hide("movedata", Dissolve(0.5)), Hide("nonbattlemoves", Dissolve(0.5)), Return(move)] if newmove else NullAction()) 
                xminimum 350 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" 
                text_font "fonts/pkmndp.ttf" 
                hovered ([Show("movedata", Dissolve(0.5), move), Hide("mondata", Dissolve(0.5))] if tooltips else NullAction())
                unhovered ([Hide("movedata", Dissolve(0.5)), Show("mondata", Dissolve(0.5), pkmn)] if tooltips else NullAction())

screen modalnonbattlemoves(pkmn, newmove=False, tooltips = True):
    modal True
    zorder 5
    grid len(pkmn.GetMoves()) 1:
        xalign .5
        yalign (.65 if tooltips else .55)
        for move in pkmn.GetMoves():
            textbutton move.Name: 
                action ([Hide("movedata", Dissolve(0.5)), Hide("nonbattlemoves", Dissolve(0.5)), Return(move)] if newmove else NullAction()) 
                xminimum 350 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" 
                text_font "fonts/pkmndp.ttf" 
                hovered ([Show("movedata", Dissolve(0.5), move), Hide("mondata", Dissolve(0.5))] if tooltips else NullAction())
                unhovered ([Hide("movedata", Dissolve(0.5)), Show("mondata", Dissolve(0.5), pkmn)] if tooltips else NullAction())


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

init:
    image clouds: #daytime
        "BG/sky_base.jpg"
        subpixel True
        block:
            xalign 0.0
            linear 60.0 xpos -1.0
            repeat
                
    python:
        style.mm_root.background = "clouds"

screen main_menu():
    
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        
    # The main menu buttons.
    
    imagemap:
        ground "imagemaps/Title_Still_Ground.png"
        idle "imagemaps/Title_Still_Idle.png"
        hover "imagemaps/Title_Still_Hover.png"
        
        hotspot (41, 455, 192, 55) action Start()
        hotspot (41, 391, 203, 55) action Show("load", transition=dissolve)
        hotspot (41, 588, 174, 52) action Show("navigation", transition=dissolve)
        hotspot (41, 647, 203, 52) action Show("help", transition=dissolve)
        hotspot (41, 711, 102, 52) action Quit(confirm=False)
        hotspot (41, 991, 173, 44) action Jump("credits")

    textbutton "Battle Tester" text_xalign 0.5 anchor (1.0, 1.0) pos (0.995, 0.96) action Start("randombattle") text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300

    text "Version " + config.version xalign 1.0 yalign 1.01 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
    

label credits:
    $ renpy.movie_cutscene('videos/Credits.webm')

    show screen credits

    pause 60

    hide screen credits

    call screen main_menu()

screen abortbattletester:
    textbutton "Leave Battle Tester" text_xalign 0.5 align (0.5, 1.0) action MainMenu(confirm=False) text_font "fonts/pkmndp.ttf" style "menu_choice_button" xmaximum 300

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu():
    
    modal True
    
    imagemap:
        ground "imagemaps/Menu_Ground.png"
        idle "imagemaps/Menu_Idle.png"
        hover "imagemaps/Menu_Hover.png"
        
        hotspot (26, 194, 146, 40) action [Hide("game_menu", transition=dissolve), SetVariable("yvalue", 1.0), ShowMenu("text_history", transition=dissolve)]
        
        hotspot (25, 306, 169, 50) action Show("navigation", transition=dissolve)
        hotspot (25, 368, 101, 50) action Show("save", transition=dissolve)
        hotspot (25, 427, 101, 50) action Show("load", transition=dissolve)
        
        hotspot (25, 607, 147, 50) action [Hide("game_menu", transition=dissolve), Show("traits", transition=dissolve), Hide("database", transition=dissolve)]
        hotspot (25, 545, 148, 50) action [Hide("game_menu", transition=dissolve), Hide("traits", transition=dissolve), Show("database", transition=dissolve)]
        hotspot (24, 782, 223, 43) action MainMenu()
        
        hotspot (101, 1018, 86, 31) action [Hide("game_menu", transition=dissolve), Return()]

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

init python:
    def RenameFile(slot):
        global save_name
        if (inbattle):
            renpy.invoke_in_new_context(renpy.say, None, "You cannot save in the middle of a battle!")
            return
        savename = FileSaveName(slot)
        if ("{size=30}" in savename and "{/size}" in savename 
        and "Afternoon" not in savename
        and "Morning" not in savename
        and "Evening" not in savename
        and "Noon" not in savename
        and "Night" not in savename):
            savename = savename[savename.index("{size=30}") + len("{size=30}"):savename.index("{/size}")]
        else:
            savename = timeOfDay
        save_name = renpy.invoke_in_new_context(renpy.input, "Type a name for the save.", default=savename, length=16, exclude="{}[[]%<>",)
        if (save_name.strip() == ""):
            save_name = timeOfDay
        save_name = "{}, {} {}\n{}".format(getRWDay(0), str(calendar.month_name[calDate.month]), getRDay(0), "{size=30}" + save_name + "{/size}")
        
screen save():
    imagemap:
        ground "imagemaps/Save_Load_Ground.png"
        idle "imagemaps/Save_Load_Idle.png"
        hover "imagemaps/Save_Load_Hover.png"
        selected_idle "imagemaps/Save_Load_Selected.png"
        selected_hover "imagemaps/Save_Load_Hover.png"
        if int(persistent._file_page) > 6:
            hotspot (6, 997, 38, 38) clicked SetVariable("persistent._file_page", str(int(persistent._file_page) - 5))
        else:
            hotspot (6, 997, 38, 38) clicked SetVariable("persistent._file_page", "1")

        hotspot (53, 997, 38, 38) clicked If(int(persistent._file_page) > 1, SetVariable("persistent._file_page", str(int(persistent._file_page) - 1)))
        hotspot (33, 953, 38, 38) clicked FilePage(1)
        hotspot (82, 953, 38, 38) clicked FilePage(2)
        hotspot (132, 953, 38, 38) clicked FilePage(3)
        hotspot (181, 953, 38, 38) clicked FilePage(4)
        hotspot (207, 997, 38, 38) clicked FilePage(int(persistent._file_page) + 1), SetVariable("persistent._file_page", str(int(persistent._file_page) + 1))
        hotspot (254, 997, 38, 38) clicked FilePage(int(persistent._file_page) + 5), SetVariable("persistent._file_page", str(int(persistent._file_page) + 5))

        hotspot (20, 84, 261, 150) clicked ([Function(RenameFile, 1), FileSave(1)] if not inbattle else Function(RenameFile, 1)):
            use load_save_slot(number=1)
        hotspot (20, 255, 261, 150) clicked ([Function(RenameFile, 2), FileSave(2)] if not inbattle else Function(RenameFile, 2)):
            use load_save_slot(number=2)
        hotspot (20, 435, 261, 150) clicked ([Function(RenameFile, 3), FileSave(3)] if not inbattle else Function(RenameFile, 3)):
            use load_save_slot(number=3)
        hotspot (20, 615, 261, 150) clicked ([Function(RenameFile, 4), FileSave(4)] if not inbattle else Function(RenameFile, 4)):
            use load_save_slot(number=4)
        hotspot (20, 794, 261, 150) clicked ([Function(RenameFile, 5), FileSave(5)] if not inbattle else Function(RenameFile, 5)):
            use load_save_slot(number=5)

        hotspot (101, 1018, 86, 31) action Hide("save", transition=dissolve), Hide("extra_load")
        $ str_page = "Pg. " + persistent._file_page
        text str_page xpos 200 ypos 1042

        hotspot (33, 1040, 40, 40) action Show("extra_load")

screen load():
    
    modal True

    #This ensures that any other menu screen is replaced.
    #tag menu

    imagemap:
        ground "imagemaps/Save_Load_Ground.png"
        idle "imagemaps/Save_Load_Idle.png"
        hover "imagemaps/Save_Load_Hover.png"
        selected_idle "imagemaps/Save_Load_Selected.png"
        selected_hover "imagemaps/Save_Load_Hover.png"
        cache False
        if int(persistent._file_page) > 6:
            hotspot (6, 997, 38, 38) clicked SetVariable("persistent._file_page", str(int(persistent._file_page) - 5))
        else:
            hotspot (6, 997, 38, 38) clicked SetVariable("persistent._file_page", "1")
        
        hotspot (53, 997, 38, 38) clicked If(int(persistent._file_page) > 1, SetVariable("persistent._file_page", str(int(persistent._file_page) - 1)))
        hotspot (33, 953, 38, 38) clicked FilePage(1)
        hotspot (82, 953, 38, 38) clicked FilePage(2)
        hotspot (132, 953, 38, 38) clicked FilePage(3)
        hotspot (181, 953, 38, 38) clicked FilePage(4)
        hotspot (230, 953, 38, 38) clicked FilePage(5)
        hotspot (207, 997, 38, 38) clicked FilePage(int(persistent._file_page) + 1), SetVariable("persistent._file_page", str(int(persistent._file_page) + 1))
        hotspot (254, 997, 38, 38) clicked FilePage(int(persistent._file_page) + 5), SetVariable("persistent._file_page", str(int(persistent._file_page) + 5))

        hotspot (20, 84, 261, 150) clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot (20, 255, 261, 150) clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot (20, 435, 261, 150) clicked FileLoad(3):
            use load_save_slot(number=3)
        hotspot (20, 615, 261, 150) clicked FileLoad(4):
            use load_save_slot(number=4)
        hotspot (20, 794, 261, 150) clicked FileLoad(5):
            use load_save_slot(number=5)
            
        hotspot (101, 1018, 86, 31) action Hide("load", transition=dissolve), Hide("extra_load")
        $ str_page = "Pg. " + persistent._file_page
        text str_page xpos 200 ypos 1042

        hotspot (33, 1040, 40, 40) action Show("extra_load")

screen extra_load:
    frame:
        #xysize (300,200) 
        style "menu_choice_button"
        xpos 0.38
        ypos 0.9
        #xmaximum .4
        vbox:
            hbox:
                text "{size=+2}Travel to page:"
                button:
                    id "input_1"
                    xysize (250,25)
                    action NullAction()
                    add Input(hover_color="#808080",size=40, color="#000", default=int(persistent._file_page), changed=file_page_func, length=10, button=renpy.get_widget("extra_load","input_1")) yalign 0 
            hbox:
                textbutton "{b}Enter{/b}" style "buttonhover" action Hide("extra_load")

init python:
    def file_page_func(newstring):
        if newstring.isdigit() and int(newstring) > 0:
            persistent._file_page = newstring

screen load_save_slot:
    $ file_text = "{color=#ffffff}{font=fonts/pkmndp.ttf}{size=22}%s\n\n\n%s{/size}{/font}{/color}" % (FileSaveName(number),
                        FileTime(number, format='%m/%d/%Y - %H:%M', empty=_("Empty Slot"))) 

    add FileScreenshot(number) xpos 1 ypos 2 zoom 0.7
    text file_text xpos 10 ypos 10 outlines [ (3, "#000") ] line_spacing 0.75 line_leading 1.0 kerning 2.0
    
    key "save_delete" action FileDelete(number)

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu

    # Include the navigation.
    use navigation

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help: 
    
    modal True
    
    imagemap:
        ground "GFX/Help1.png"        
        hotspot (0, 0, 1920, 1080) action Hide("help", transition=dissolve)

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    modal True

    if message == layout.QUIT:
        imagemap:
            ground 'GUI/Quit_Idle.png'
            hover 'GUI/Quit_Hover.png'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action
            
    if message == layout.OVERWRITE_SAVE:
        imagemap:
            ground 'GUI/Overwrite_Idle.png'
            hover 'GUI/Overwrite_Hover.png'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action
    
    if message == layout.DELETE_SAVE:
        imagemap:
            ground 'GUI/Delete_Save_Idle.png'
            hover 'GUI/Delete_Save_Hover.png'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action
        
    if message == layout.LOADING:
        imagemap:
            ground 'GUI/Load_Idle.png'
            hover 'GUI/Load_Hover.png'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action
        
    if message == layout.MAIN_MENU:
        imagemap:
            ground 'GUI/Return_Menu_Idle.png'
            hover 'GUI/Return_Menu_Hover.png'
       
            hotspot (834, 510, 130, 76) action yes_action
            hotspot (978, 510, 130, 76) action no_action


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "fonts/DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

##USER-CREATED SCREENS

screen battleui():
    if (not hidebattleui):
        for i, playermon in enumerate(FriendlyBattlers()):
            $ originali = i
            $ i = len(FriendlyBattlers()) - i - 1
            $ isprojecting = playermon.GetFormeOverride() != None and playermon.GetImage() == "Pokemon/25.2.webp"

            if (playermon.GetImage() != "Pokemon/25.2.webp" and playermon.GetImage() != "Pokemon/25.webp"):
                add playermon.GetImage() at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) xpos 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)
            elif (playermon.HasAbility("Freelectric", False) and len(freelectricphases) < 2):
                add "images/expressions/pikachu/pikachu_face_angry.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) xpos 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) yanchor 1.0 ypos 1.0 - .15 * i xzoom 1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1)
            else:
                add "Pokemon/25.2-4.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) xpos (75 if isprojecting else 0) + 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0) 
                add "Pokemon/25.2-1.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) matrixcolor TintMatrix(GetLiberaColor()) xpos (75 if isprojecting else 0) + 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)

                if (isprojecting):
                    add "Pokemon/{}.webp".format(playermon.GetId()) at (hoverfloat) matrixcolor SaturationMatrix(2.0) alpha 0.8 xpos -75 + 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) ypos -0.05 + 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1)

                add "Pokemon/25.2-3.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) xpos (75 if isprojecting else 0) + 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)
                add "Pokemon/25.2-5.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) matrixcolor TintMatrix(GetLiberaColor()) xpos (75 if isprojecting else 0) + 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)
                add "Pokemon/25.2-2.webp" at (hovering if originali == BattlerIndex and len(FriendlyBattlers()) > 1 else None) matrixcolor TintMatrix(GetLiberaColor(False)) xpos (75 if isprojecting else 0) + 250 * i + 200 * (len(FriendlyBattlers()) == 1) + 100 * (len(FriendlyBattlers()) == 2) * i + 50 * (len(FriendlyBattlers()) == 2) yanchor 1.0 ypos 1.0 - .15 * i xzoom -1.0 / (i * 0.25 + 1) yzoom 1.0 / (i * 0.25 + 1) zoom (0.8 if isprojecting else 1.0)

        for i, enemymon in enumerate(EnemyBattlers()):
            $ i = len(EnemyBattlers()) - i - 1
            add enemymon.GetImage() xanchor 1.0 xpos 1920 - (250 * i + 200 * (len(EnemyBattlers()) == 1) + 100 * (len(EnemyBattlers()) == 2) * i + 50 * (len(EnemyBattlers()) == 2)) yanchor 1.0 ypos 1.0 - .15 * i zoom 1.0 / (i * 0.25 + 1)

        for i, trainer in enumerate(FriendlyTrainers()):
            if (trainer.HasMons() and not trainer.GetIsPokemon()):
                for j, mon in enumerate(trainer.GetTeam()):
                    add "GUI/Pokeball_indicator.png" xpos 380 + j * 40 ypos 20 + 40 * i matrixcolor SaturationMatrix(mon.GetHealth() > 0)

        for i, trainer in enumerate(EnemyTrainers()):
            if (trainer.HasMons() and not trainer.GetIsPokemon()):
                for j, mon in enumerate(trainer.GetTeam()):
                    add "GUI/Pokeball_indicator.png" xpos 1920 - 420 - j * 40 xzoom -1 ypos 20 + 40 * i matrixcolor SaturationMatrix(mon.GetHealth() > 0)

        $ ylevels = 0
        if (CurrentWeather != None):
            add "GUI/frame_pbattlestat.png" ypos 8 + 40 * ylevels at Transform(yzoom=0.3) xalign 0.5
            text CurrentWeather[0].title() ypos 18 + 40 * ylevels xalign 0.5
            $ ylevels = 1

        for effect in BattlefieldEffects:
            add "GUI/frame_pbattlestat.png" ypos 8 + 40 * ylevels at Transform(yzoom=0.3) xalign 0.5
            text effect ypos 18 + 40 * ylevels xalign 0.5
            $ ylevels += 1

        #left side, your stuff
        $ ylevels = 0
        for i, mon in enumerate(FriendlyBattlers()):
            $ health = mon.GetHealth()
            $ maxhealth = mon.GetStat(Stats.Health)
            $ ybuffer = i * 106 + ylevels * 35
            add "GUI/frame_pbattlestat.png" ypos ybuffer yzoom .8 xanchor .03
            if (mon.GetForeverals() != []):
                imagebutton:
                    idle Transform("gfx/foreveral.png", matrixcolor=InvertMatrix(0), zoom=0.2)
                    hover Transform("gfx/foreveral.png", matrixcolor=InvertMatrix(), zoom=0.2)
                    ypos ybuffer + 30
                    xpos 0.115
                    action (Hide("stats"), Call("foreveraldata", mon.GetForeverals()[0], inbattle=True, from_current=True) if not explainingf else NullAction())
            text mon.GetNickname() pos (17, 30 + ybuffer) size 35 - (1.5 * max(0, (len(mon.GetNickname()) - 10)))
            $ gendersymbol = ""
            if (mon.GetGender() == Genders.Male):
                $ gendersymbol = "{color=#2b00ff}♂"
            elif (mon.GetGender() == Genders.Female):
                $ gendersymbol = "{color=#ff00b7}♀"
            text gendersymbol + "{color=#000000}Lv." + str(mon.GetLevel()) xanchor 1.0 pos (350, 30 + ybuffer)

            $ barcolor = "#00b612"
            if (health / maxhealth <= 0.25):
                $ barcolor = "#ff0000"
            elif (health / maxhealth <= 0.5):
                $ barcolor = "#fff700"

            bar range maxhealth value health pos (12, 65 + ybuffer) xmaximum 335 right_bar "#fff" left_bar barcolor
            text (str(health) + "/" + str(maxhealth)) color "#fff" pos (17, 65 + ybuffer) outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ]

            if (mon.IsTerad()):
                add "GUI/frame_pbattlestat.png" xanchor .1 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}Terastalized {/gradient2}" + mon.GetTeraType() xpos 15 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                $ ylevels += 1

            for status in mon.GetStatusKeys():
                if (status[0] != "."):
                    add "GUI/frame_pbattlestat.png" xanchor .1 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                    if (status in ["diveralized", "mega evolved", "minigigamaxed"]):
                        text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}" + status.title() + "{/gradient2}" xpos 15 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    else:
                        text status.title() xpos 15 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    $ ylevels += 1

            for change in mon.GetAllStatChanges().keys():
                add "GUI/frame_pbattlestat.png" xanchor .1 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                text StatToString(change) xpos 15 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                text ("+" if mon.GetStatChanges(change) > 0 else "" ) + str(mon.GetStatChanges(change)) xpos 325 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                $ ylevels += 1
        
        for effect in FriendlyEffects:
            $ yceiling = len(FriendlyBattlers()) * 105 + 10 + ylevels * 35
            add "GUI/frame_pbattlestat.png" xanchor .03 ypos yceiling at Transform(yzoom=0.3)
            text effect.title() xpos 15 ypos yceiling + 8
            $ ylevels += 1

        #right side, their stuff
        $ ylevels = 0
        for i, mon in enumerate(EnemyBattlers()):
            $ health = mon.GetHealth()
            $ maxhealth = mon.GetStat(Stats.Health)
            $ ybuffer = i * 106 + ylevels * 35
            add "GUI/frame_pbattlestat.png" ypos ybuffer yzoom .8 xanchor .97 xpos 1.0
            text mon.GetNickname() pos (1920-345, 30 + ybuffer) size 35 - (1.5 * max(0, (len(mon.GetNickname()) - 10)))
            $ gendersymbol = ""
            if (mon.GetGender() == Genders.Male):
                $ gendersymbol = "{color=#2b00ff}♂"
            elif (mon.GetGender() == Genders.Female):
                $ gendersymbol = "{color=#ff00b7}♀"
            text gendersymbol + "{color=#000000}Lv." + str(mon.GetLevel()) xanchor 1.0 pos (1920-10, 30 + ybuffer)

            $ barcolor = "#00b612"
            if (health / maxhealth <= 0.25):
                $ barcolor = "#ff0000"
            elif (health / maxhealth <= 0.5):
                $ barcolor = "#fff700"

            bar range maxhealth value health pos (1920-12, 65 + ybuffer) xmaximum 335 right_bar barcolor left_bar "#fff" bar_invert True xanchor 1.0
            #text (str(health) + "/" + str(maxhealth)) color "#fff" pos (1920-17, 65 + ybuffer) outlines [ (absolute(5), "#000", absolute(0), absolute(0)) ] xanchor 1.0

            if (mon.IsTerad()):
                add "GUI/frame_pbattlestat.png" xanchor .9 xpos 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}Terastalized {/gradient2}" + mon.GetTeraType() xpos 1920-15 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                $ ylevels += 1

            for status in mon.GetStatusKeys():
                if (status[0] != "."):
                    add "GUI/frame_pbattlestat.png" xanchor .9 xpos 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                    if (status in ["diveralized", "mega evolved", "minigigamaxed"]):
                        text "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}" + status.title() + "{/gradient2}" xpos 1920-15 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    else:
                        text status.title() xpos 1920-15 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                    $ ylevels += 1

            for change in mon.GetAllStatChanges().keys():
                add "GUI/frame_pbattlestat.png" xanchor .9 xpos 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 at Transform(yzoom=0.3)
                text StatToString(change) xpos 1920-325 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                text ("+" if mon.GetStatChanges(change) > 0 else "" ) + str(mon.GetStatChanges(change)) xpos 1920-15 xanchor 1.0 ypos (i + 1) * 105 + 10 + ylevels * 35 + 8
                $ ylevels += 1
        
        for effect in EnemyEffects:
            $ yceiling = len(EnemyBattlers()) * 105 + 10 + ylevels * 35
            add "GUI/frame_pbattlestat.png" xanchor .97 xpos 1.0 ypos yceiling at Transform(yzoom=0.3)
            text effect.title() xpos 1920-15 xanchor 1.0 ypos yceiling + 8
            $ ylevels += 1

define longtext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Terastalize! {/size}{/gradient2}"
define shorttext = "Terastalize"
define longlibtext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Liberize! {/size}{/gradient2}"
define longdivtext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Diveralize! {/size}{/gradient2}"
define longmegatext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Mega Evolve! {/size}{/gradient2}"
define longminigigatext = "{gradient2=3-#f00-#0f0-11-#0f0-#00f-11-#00f-#f00-11}{size=60} Minigigamax! {/size}{/gradient2}"

screen battle(currentMon=None):
    if (not renpy.get_screen("battleui")):
        use battleui()

    $ showteraoption = False
    if (currentMon != None and "Tera Orb" in inventory.keys()):
        $ showteraoption = True
        for allymon in currentMon.GetTrainer().GetTeam():
            if (allymon.IsTerad() and (allymon != currentMon or allymon == currentMon and allymon.GetTerastalized() != Turn)):
                $ showteraoption = False

    $ hasdiveral = False
    if (currentMon != None):
        for fvl in currentMon.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.FormSwap):
                $ hasdiveral = True

    vbox:
        xalign .5
        yalign .5
        if (currentMon != None):
            if (showteraoption):
                textbutton "[terabuttontext]" action Return(value='tera') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button" hovered SetVariable('terabuttontext', (longtext if not currentMon.IsTerad() else shorttext)) unhovered SetVariable('terabuttontext', (shorttext if not currentMon.IsTerad() else longtext))
            if (movesdodged.count("Dragon Pulse") >= 4 and dawnbattle):
                textbutton "[longlibtext]" action Return(value='lib') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button"
            if (hasdiveral and GimmickCost > 0):
                textbutton "[longdivtext]" action Return(value='div') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button"
            if (currentMon.GetItem() != None and currentMon.GetItem()[-3:] == "ite" and GimmickCost > 0):
                textbutton "[longmegatext]" action Return(value='mega') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button"
            if (currentMon.GetItem() != None and "Minigiga" in currentMon.GetItem() and GimmickCost > 0):
                textbutton "[longminigigatext]" action Return(value='giga') text_font "fonts/pkmndp.ttf" xmaximum 360 text_xalign .5 text_size 60 text_color "#4b4b4b" top_padding 17 style "menu_choice_button"
        textbutton " Fight " action Return(value='fight') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#9b5151" text_hover_color "#d03b3d" style "menu_choice_button"
        textbutton "  Bag  " action Return(value='bag') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#826926" text_hover_color "#c98022" style "menu_choice_button"
        textbutton "Pokémon" action Return(value='pokemon') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#437128" text_hover_color "#459426" style "menu_choice_button"
        textbutton "  Run  " action Return(value='run') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#295272" text_hover_color "#256799" style "menu_choice_button"
        if (len(CurrentActions) > 0):
            textbutton " Back " action Return(value='back') text_font "fonts/pkmndp.ttf" xmaximum 270 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button"

screen choosetarget(move, attacker):
    if (not renpy.get_screen("battleui")):
        use battleui()

    if (move != Range.Any):
        if (isinstance(move, int)):
            $ range = move
        else:
            $ range = GetMoveRange(move)


        $ groupselection = False
        if (range == Range.AllAdjacentFoes
            or range == Range.AllAdjacent
            or range == Range.AllAllies 
            or range == Range.AllFoes
            or range == Range.All
            or range == Range.AllAlliesAndSelf):
            $ groupselection = True
    else:
        $ groupselection = False
        $ range = Range.Any

    if (groupselection):
        vbox:
            align (0.5, 0.5)
            xanchor 1.0
            for trainer in FriendlyTrainers():
                for mon in trainer.GetLead():
                    if (mon != None):
                        textbutton "" xminimum 350 yminimum 90 background Color("#d200ab" if mon in GetTargets(attacker, range) else "#d200ac00")
        vbox:
            align (0.5, 0.5)
            xanchor 0.0
            for trainer in EnemyTrainers():
                for mon in trainer.GetLead():
                    if (mon != None):
                        textbutton "" xminimum 350 yminimum 90 background Color("#d200ab" if mon in GetTargets(attacker, range) else "#d200ac00")
    vbox:
        align (0.5, 0.5)
        xanchor 1.0
        for trainer in FriendlyTrainers():
            for mon in trainer.GetLead():
                $ istarget = mon in GetTargets(attacker, range)
                $ returnable = GetTargets(attacker, range) if groupselection else [mon]
                if (mon != None):
                    textbutton mon.GetNickname() action (Return(returnable) if istarget else NullAction()) text_font "fonts/pkmndp.ttf" xmaximum 340 text_xalign .5 text_size (60 if len(mon.GetNickname()) < 11 else 50 - (2 * (len(mon.GetNickname()) - 10))) text_color ("#000" if istarget else "#616161") style "menu_choice_button"

    vbox:
        align (0.5, 0.5)
        xanchor 0.0
        for trainer in EnemyTrainers():
            for mon in trainer.GetLead():
                $ istarget = mon in GetTargets(attacker, range)
                $ returnable = GetTargets(attacker, range) if groupselection else [mon] 
                if (mon != None):
                    textbutton mon.GetNickname() action (Return(returnable) if istarget else NullAction()) text_font "fonts/pkmndp.ttf" xmaximum 340 text_xalign .5 text_size (60 if len(mon.GetNickname()) < 11 else 50 - (2 * (len(mon.GetNickname()) - 10))) text_color ("#000" if istarget else "#616161") style "menu_choice_button"
    grid 1 1:
        xalign .5
        ypos .658
        textbutton "Back" action Return(value='back') xminimum 400 text_xalign .5 xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"


screen moves(mon):
    if (not renpy.get_screen("battleui")):
        use battleui()
    $ Moves = mon.GetMoves()
    $ NumMoves = len(Moves)

    if (HasValidMoves(mon)):
        grid 2 2:
            xalign .5
            ypos .5

            for i, move in enumerate(Moves):
                $ hovercolor = "#f0f"
                $ bodycolor = "#000"
                $ name = move.Name
                if (not MoveValid(mon, move)):
                    $ hovercolor = "#000"
                    $ bodycolor = "#616161"
                    $ name = "{s} " + name + " {/s}"
                textbutton name action [Hide("movedata", Dissolve(0.5)), Return(value=i)] xminimum 400 text_xalign .5 text_size 60 text_color bodycolor text_hover_color hovercolor style "menu_choice_button" text_font "fonts/pkmndp.ttf" hovered Show("movedata", Dissolve(0.5), move) unhovered Hide("movedata", Dissolve(0.5))
                
            for i in range(4 - NumMoves):
                null
    else:
        grid 1 1:
            xalign .5
            ypos .5
            textbutton "Struggle" action [Hide("movedata", Dissolve(0.5)), Return(value='Struggle')] xminimum 400 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" hovered Show("movedata", Dissolve(0.5), struggle) unhovered Hide("movedata", Dissolve(0.5))  

    grid 1 1:
        xalign .5
        ypos .658
        textbutton "Back" action Return(value='back') xminimum 400 text_xalign .5 xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen movedata(move):
    add Frame("GUI/character_frame.png", 10, 10, xmaximum=1150, ymaximum=300, xalign=.5, ypos=.07)
    text move.Name xminimum 550 xalign .5 yalign .1 size 100
    grid 3 2:
        xalign .5
        ypos .2
        text "Category: " + move.Category xminimum 300 xalign .5 size 40
        text "Type: " + "{color=" + GetTypeColor(move.Type) + "}" + move.Type xminimum 300 xalign .5 size 40
        text "PP: " + str(move.PP) + "/" + str(move.MaxPP) xminimum 300 xalign .5 size 40
        if (move.Power in [0, "-", "", "—"]):
            text "Power: ---" xminimum 300 xalign .5 size 40
        else:
            text "Power: " + str(move.Power) xminimum 300 xalign .5 size 40
        null
        if (str(move.Accuracy) in ["-", "", "—"]):
            text "Accuracy: Can't miss" xminimum 300 xalign .5 size 40
        elif (move.Accuracy in ["?", "~"]):
            text "Accuracy: Variable" xminimum 300 xalign .5 size 40
        else:
            text "Accuracy: " + str(math.floor(move.Accuracy * 100)) + "%" xminimum 300 xalign .5 size 40
        
    text move.Description xminimum 300 xalign .5 yalign .3 size 40   

screen stats(pkmn):
    if (not renpy.get_screen("battleui")):
        use battleui()
    
    add "gui/button/choice_idle_background.png" xalign .5 xzoom 1.5 yzoom 15
    $ gendersymbol = ""
    if (pkmn.GetGender() == Genders.Male):
        $ gendersymbol = "{color=#2b00ff}♂"
    elif (pkmn.GetGender() == Genders.Female):
        $ gendersymbol = "{color=#ff00b7}♀"
    add pkmn.GetImage() yalign 0.25 xalign 0.5 alpha 0.2
    if (pkmn.GetImage() == "Pokemon/25.2.webp"):
        add "Pokemon/25.2-1.webp" yalign 0.25 xalign 0.5 alpha 0.2 matrixcolor TintMatrix(GetLiberaColor())
        add "Pokemon/25.2-2.webp" yalign 0.25 xalign 0.5 alpha 0.2 matrixcolor TintMatrix(GetLiberaColor(False))
    $ nick = pkmn.GetNickname()
    text nick + " " + gendersymbol + ("" if nick == pokedexlookup(pkmn.GetId(), DexMacros.Name) else "\n{size=30}{color=#000}(" + pokedexlookup(pkmn.GetId(), DexMacros.Name) + "){/size}") xminimum 550 xpos .1 yalign .05 size (70 if len(nick) < 10 else 50)
    text "Lv. " + str(pkmn.GetLevel()) xminimum 550 xalign .5 ypos .03 size 50
    text "(Cap: " + str(math.floor(pkmn.GetLevelCap())) + ", Potential: " + str(pkmn.GetMaxLevel()) + ")" xalign .5 ypos .09 size 40
    
    $ typestring = ""
    for element in pkmn.GetTypes():
        if (typestring != ""):
            $ typestring += "{color=#fff}/{/color}"
        $ typestring += "{color=" + GetTypeColor(element) + "}" + element + "{/color}"

    text typestring yalign .07 size 70 xanchor 1.0 xpos 0.85 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
    
    grid 4 7:
        xalign .5
        ypos .15
        text "{b}Stat" xminimum 300 size 40
        text "{b}Value" xminimum 300 xalign .5 size 40
        text "{b}EVs" xminimum 300 xalign .5 size 40
        text "{b}IVs" xminimum 300 xalign .5 size 40
        text "HP" xminimum 300 size 40
        text str(max(pkmn.GetHealth(), pkmn.GetCaught())) + "/" + str(pkmn.GetStat(Stats.Health)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.Health)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.Health)) + "/31" xminimum 300 xalign .5 size 40
        $ attackbonus = NatureToBonus(pkmn.GetNature(), Stats.Attack)
        text "Attack" xminimum 300 size 40 color ("#000" if attackbonus == 1 else ("#ff0000" if attackbonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.Attack, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.Attack)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.Attack)) + "/31" xminimum 300 xalign .5 size 40
        $ defensebonus = NatureToBonus(pkmn.GetNature(), Stats.Defense)
        text "Defense" xminimum 300 size 40 color ("#000" if defensebonus == 1 else ("#ff0000" if defensebonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.Defense, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.Defense)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.Defense)) + "/31" xminimum 300 xalign .5 size 40
        $ specialattackbonus = NatureToBonus(pkmn.GetNature(), Stats.SpecialAttack)
        text "Special Attack" xminimum 300 size 40 color ("#000" if specialattackbonus == 1 else ("#ff0000" if specialattackbonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.SpecialAttack, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.SpecialAttack)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.SpecialAttack)) + "/31" xminimum 300 xalign .5 size 40
        $ specialdefensebonus = NatureToBonus(pkmn.GetNature(), Stats.SpecialDefense)
        text "Special Defense" xminimum 300 size 40 color ("#000" if specialdefensebonus == 1 else ("#ff0000" if specialdefensebonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.SpecialDefense, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.SpecialDefense)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.SpecialDefense)) + "/31" xminimum 300 xalign .5 size 40
        $ speedbonus = NatureToBonus(pkmn.GetNature(), Stats.Speed)
        text "Speed" xminimum 300 size 40 color ("#000" if speedbonus == 1 else ("#ff0000" if speedbonus == 1.1 else "#0000ff"))
        text str(pkmn.GetStat(Stats.Speed, triggerAbilities=False, absolute=True)) xminimum 300 xalign .5 size 40
        text str(pkmn.GetEV(Stats.Speed)) + "/255" xminimum 300 xalign .5 size 40
        text str(pkmn.GetIV(Stats.Speed)) + "/31" xminimum 300 xalign .5 size 40

    text "EXP: " + str(math.floor(pkmn.GetExperience())) + ", To Next Level: " + str(math.floor(pkmn.CalculateAllExperienceNeededForLevel(pkmn.GetMaxLevel() + 1) - pkmn.GetExperience()) + 1) size 40 yalign .43 xalign 0.5

    $ status = "None"
    if (pkmn.GetHealthPercentage() <= 0.0 and pkmn.GetCaught() <= 0):
        $ status = "Fainted"
    else:
        for statustype in nonvolatiles:
            if (pkmn.HasStatus(statustype)):
                $ status = statustype
    
    hbox:
        yalign .48
        xalign .5
        spacing 30
        text "Status: " + status.title() xminimum 300 size 40 yalign .5
        if (pkmn.GetItem() == None):
            text "Item: None" xminimum 300 size 40 yalign .5
        else:
            text "Item: " + pkmn.GetItem() xminimum 300 size 40 yalign .5

        text "Nature: " + NatureToString(pkmn.GetNature()) xminimum 300 size 40 yalign .5
        $ fvlability = False
        for fvl in pkmn.GetForeverals():
            if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                $ fvlability = True
        if (not fvlability):
            text "Ability: " + pkmn.GetAbility() xminimum 300 size 40 yalign .5
        else:
            hbox:
                text "Ability: " xminimum 300 size 40 yalign .5
                vbox:
                    text pkmn.GetAbility() xminimum 300 size 40 yalign .5
                    for fvl in pkmn.GetForeverals():
                        if (lookupforeveraldata(fvl, FVLMacros.FVLType) == ForeveralTypes.AddAbility):
                            for ability in lookupforeveraldata(fvl, FVLMacros.FVLTypeData):
                                text "(" + ability + ")" xminimum 300 size 40 yalign .5
        if (usingforeverals):
            if (pkmn.GetForeverals() == []):
                text "Foreveral: None" xminimum 300 size 40 yalign .5
            else:
                text "Foreveral: " + pkmn.GetForeverals()[0] xminimum 300 size 40 yalign .5
    
    textbutton "Back" action [Hide("stats", Dissolve(0.5)), Show("switch", Dissolve(0.5), pkmn.GetTrainer())] xminimum 300 yalign .7 xalign .6 text_xalign .5 text_size 40 text_color "#800000" text_hover_color "#FF0000" background Frame("gui/button/choice_idle_background.png")
    textbutton "Select" action [Hide("stats", Dissolve(0.5)), Return(value=(pkmn.GetTrainer().GetTeam().index(pkmn)))] xminimum 300 yalign .7 xalign .4 text_xalign .5 text_size 40 text_color "#228B22" text_hover_color "#00FF00" background Frame("gui/button/choice_idle_background.png")

    use battlemoves(pkmn)

screen battlemoves(pkmn):
    grid len(pkmn.GetMoves()) 1:
        xalign .5
        yalign .57
        for move in pkmn.GetMoves():
            textbutton move.Name action NullAction() xminimum 350 text_xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" hovered Show("movedata", Dissolve(0.5), move) unhovered Hide("movedata", Dissolve(0.5)), Show("stats", Dissolve(0.5), pkmn)

screen rememberablemoves(pkmn):
    $ rememberablemoves = GetRememberableMoves(pkmn)

    grid 5 6:
        align (0.5, 0.75)
        for move in rememberablemoves:
            textbutton move:
                xmaximum 280 text_size 40 text_xalign 0.5 text_color "#000" ymaximum 70
                text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
                action [Hide("rememberablemoves", Dissolve(0.5)), Hide("movedata", Dissolve(0.5)), Return(move)] 
                hovered Show("movedata", Dissolve(0.5), GetMove(move)) 
                unhovered Hide("movedata", Dissolve(0.5))

        for i in range(30 - len(rememberablemoves)):
            null

    textbutton "Back" action [Hide("movedata", Dissolve(0.5)), Hide("rememberablemoves", Dissolve(0.5)), Return("Back")] xminimum 300 yalign .4 xalign .5 text_xalign .5 text_size 40 text_color "#800000" text_hover_color "#FF0000" background Frame("gui/button/choice_idle_background.png")

screen SelectMon():
    if (not renpy.get_screen("partyviewer")):
        use partyviewer()
        
    $ team = playerparty
    $ numMons = len(team)

    grid 3 2:
        xalign .5
        ypos .2

        for i, mon in enumerate(team):
            textbutton mon.GetNickname() + " {size=30}Lv." + str(mon.GetLevel()) action [Hide("SelectMon", Dissolve(0.5)), Return(mon)] xminimum 400 text_xmaximum 400 yminimum 140 ymaximum 140 text_xalign .5 text_yalign 0.3 text_size (60 if len(mon.GetNickname()) <= 10 else 40)  style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f"
        for i in range(6 - numMons):
            null 

    grid 3 2:
        xalign .5
        ypos .29
        yspacing 100
        xspacing 12

        for i, mon in enumerate(team):
            $ maxhealth = mon.GetStat(Stats.Health, triggerAbilities=False)
            $ health = max(mon.GetHealth(), mon.WasCaught)
            $ barcolor = "#00b612"
            if (health / maxhealth <= 0.25):
                $ barcolor = "#ff0000"
            elif (health / maxhealth <= 0.5):
                $ barcolor = "#fff700"
            bar range maxhealth value health xmaximum 388 right_bar "#fff" left_bar barcolor
        for i in range(6 - numMons):
            null 

    textbutton "Back" action Return(value='back') xminimum 400 text_xalign .5 xalign .5 yalign .75 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"    

screen SendToPC():
    if (not renpy.get_screen("partyviewer")):
        use partyviewer()
        
    $ team = playerparty
    $ numMons = 7

    grid 3 3:
        xalign .5
        ypos .2

        for i in range(numMons):
            textbutton team[i].GetNickname() + " {size=30}Lv." + str(team[i].GetLevel()) action ([Hide("SendToPC", Dissolve(0.5)), Return(team[i])] if team[i] != pikachuobj else NullAction()) xminimum 400 text_xmaximum 400 yminimum 140 ymaximum 140 text_xalign .5 text_yalign 0.3 text_size (60 if len(team[i].GetNickname()) <= 10 else 40)  style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f"
            if (i == 5 or i == 6):
                null

    grid 3 3:
        xalign .5
        ypos .29
        yspacing 100
        xspacing 12

        for i in range(numMons):
            $ maxhealth = team[i].GetStat(Stats.Health, triggerAbilities=False)
            $ health = max(team[i].GetHealth(), team[i].WasCaught)
            $ barcolor = "#00b612"
            if (health / maxhealth <= 0.25):
                $ barcolor = "#ff0000"
            elif (health / maxhealth <= 0.5):
                $ barcolor = "#fff700"
            bar range maxhealth value health xmaximum 388 right_bar "#fff" left_bar barcolor
            if (i == 5 or i == 6):
                null      

screen switch(trainer, hideback = False):
    if (not renpy.get_screen("battleui")):
        use battleui()
    
    python:
        team = trainer.GetTeam()
        numMons = len(team)
    
    grid 3 2:
        xalign .5
        ypos .2

        for i in range(numMons):
            textbutton team[i].GetNickname() + " {size=30}Lv." + str(team[i].GetLevel()) action [Hide("switch", Dissolve(0.5)), Show("stats", Dissolve(0.5), team[i])] xminimum 400 text_xmaximum 400 yminimum 140 ymaximum 140 text_xalign .5 text_yalign 0.3 text_size (60 if len(team[i].GetNickname()) <= 10 else 40) style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f"
                
        for i in range(6 - numMons):
            null

    grid 3 2:
        xalign .5
        ypos .29
        yspacing 100
        xspacing 12
        
        python:
            team = trainer.GetTeam()
            numMons = len(team)

        for i in range(numMons):
            if (taughtmove == None):
                $ maxhealth = team[i].GetStat(Stats.Health, triggerAbilities=False)
                $ health = team[i].GetHealth()
                $ barcolor = "#00b612"
                if (health / maxhealth <= 0.25):
                    $ barcolor = "#ff0000"
                elif (health / maxhealth <= 0.5):
                    $ barcolor = "#fff700"
                bar range maxhealth value health xmaximum 388 right_bar "#fff" left_bar barcolor
            else:
                hbox:
                    null width 110
                    text (("{color=#00b612}Can Learn{/color}" if MonCanLearn(team[i], taughtmove) else "{color=#ff0000}Can't Learn{/color}") if taughtmove not in team[i].GetMoveNames() else "{color=#ff0000}Learned{/color}") xalign 0.5
                    null width 110
            
        for i in range(6 - numMons):
            null

    if (not hideback and not mustswitch):
        grid 1 1:
            xalign .5
            ypos .658
            textbutton "Back" action Return(value='back') xminimum 400 text_xalign .5 xalign .5 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

##############################################################################
# Calendar
#
screen currentdate():
    use partyviewer()
    use wallet()
    use repelwidget()
    if (usinginventory):
        use inventorywidget()
    if (usingforeverals):
        use foreveralwidget()

    frame:
        left_padding 10
        right_padding 25
        xpadding 15
        background Frame("GFX/DateTimeBanner.png",0,0)
        xalign 1.0
        vbox:
            text "{size=28}{font=fonts/Microgramma-D-OT-Bold-Extended.ttf}[timeOfDay] -{/font}{/size} {size=28}"+getRWDay(0)+", "+str(calendar.month_name[calDate.month])+" "+getRDay(0)+"{/size}" color "#1c1c1c"

##############################################################################
# Class Electives Selection
#
# Types screens.

screen electives():
    use currentdate()

    grid 3 6:
        xpos 0.41
        yalign 0.5
        spacing 20
        for keyname in altclassdex.keys():
            if (lastclass != keyname):
                $ lowerkey = keyname.lower()
                imagebutton: 
                    idle "imagemaps/{}_still.png".format(lowerkey)
                    hover "imagemaps/{}_hover.png".format(lowerkey)
                    action Return(keyname) 
                    hovered Show("classmates", Dissolve(0.5), keyname)
                    unhovered Hide("classmates", Dissolve(0.5))
            else:
                null

screen studyfocus():
    use currentdate()

    grid 3 6:
        xalign 0.5
        yalign 0.5
        spacing 20
        for keyname in altclassdex.keys():
            $ lowerkey = keyname.lower()
            imagebutton: 
                idle "imagemaps/{}_still.png".format(lowerkey)
                hover "imagemaps/{}_hover.png".format(lowerkey)
                action Return(keyname)
    
    textbutton "Back" action Return("Back") xminimum 200 text_xalign .5 xalign .5 yalign .9 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen picktype:
    grid 3 6:
        xalign 0.5
        yalign 0.5
        spacing 20
        for keyname in altclassdex.keys():
            $ lowerkey = keyname.lower()
            imagebutton: 
                idle "imagemaps/{}_still.png".format(lowerkey)
                hover "imagemaps/{}_hover.png".format(lowerkey)
                action Return(keyname)

screen inventory():
    if (not renpy.get_screen("battleui")):
        use battleui()
    frame:
        xpos 0.209
        yanchor 0.0
        ypos 0.124
        background "images/GUI/readback.png"
        $ itemcount = 0
        grid 4 10:
            transpose True
            for item in inventory.keys():
                if (InventoryCategory(item) in ["Healing", "Poké Balls"] or item == "Poké Doll"):
                    $ itemcount += 1
                    textbutton ("" if inventory[item] == 1 else str(inventory[item]) + "x ") + item text_color "#2b2b2b" action Return(item) text_hover_color "#fff"
            for x in range(40 - itemcount):
                null

    textbutton "Back" action Return("Back") xminimum 200 text_xalign .5 xalign .5 yalign .75 text_size 60 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf"

screen classmates(type):
    for i, character in enumerate(GetStudents(type)):
        $ charcolor = getCharColor(character)
        $ iteration = (1.25 if len(GetStudents(type)) == 3 else 1.0)
        $ suffix = ""
        if (character == "Tia" and not IsBefore(17, 4, 2004)):
            $ suffix = " hat" 
        if (character in persondex.keys() and "Named" in persondex[character].keys() and persondex[character]["Named"]):
            $ value = persondex[character]["Value"]
            $ valueceil = GetCharacterLevel(character)
            add character.lower() + " uniform" + suffix xpos ((i * iteration + 1) / 10.0) - (0 if len(GetStudents(type)) == 3 else 0.05)
            $ specialnature = GetNature(character) == TrainerNature.Special
            $ mood = GetMood(character)
            text "{size=50}{color=" + charcolor + "}" + character + "\n{/color}{size=30}Lv." + str(valueceil) + ", EXP: " + str(value) + ("\n{/color}{size=30}Mood: " + moodtoword(mood) + " (" + str(mood) + ")" if usingmoods and not specialnature else ("\n{/color}{size=30}Mood: Stable" if usingmoods and specialnature else "")) xpos ((i * iteration + 1) / 10.0) - (.05 if len(GetStudents(type)) == 3 else 0.1) + (0 if len(GetStudents(type)) == 3 else 0.01) * i color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at Transform(rotate=-15) ypos 0.1#(0.0 if i % 2 == 0 else 0.1)
        else:
            $ finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
            add character.lower() + " uniform" + suffix xpos ((i * iteration + 1) / 10.0) - (0 if len(GetStudents(type)) == 3 else 0.05) matrixcolor finalmatrix

    text type + "{size=80} - Lv. " + FormatNum(classstats[type]) color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] size 120 xcenter 0.25 ypos 0.85

screen pickpokemon(choices):
    $ lesschosen = (chosenindex - 1) % len(choices)
    $ morechosen = (chosenindex + 1) % len(choices)
    $ modchosen = chosenindex % len(choices)
    $ totalstats = pokedexlookup(choices[modchosen], DexMacros.Total)
    $ potential = pokedexlookuppos(getevolution(choices[modchosen]), DexMacros.Total)

    text "(Click or use keyboard to change selection.)" size 40 align (0.5, 0.1) color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
    
    add "GUI/double-arrow.png" align (0.5, 0.5) at Transform() 

    imagebutton idle "Pokemon/" + str(choices[lesschosen]) + ".webp" yalign 0.5 xanchor 0.5 xpos 0.15 action SetVariable("chosenindex", lesschosen)
    key "K_LEFT" action SetVariable("chosenindex", lesschosen)
    add "Pokemon/" + str(choices[lesschosen]) + ".webp" yalign 0.5 xanchor 0.5 xpos 0.15 at Transform(alpha=0.6, matrixcolor=BrightnessMatrix(-1))
    
    imagebutton idle "Pokemon/" + str(choices[modchosen]) + ".webp" align(0.5, 0.4) at Transform(zoom=1.5) action Return(choices[modchosen])
    key "K_RETURN" action Return(choices[modchosen])
    text pokedexlookup(choices[modchosen], DexMacros.Name) size 80 align (0.5, 0.75) color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
    
    $ secondcolorstring = pokedexlookup(choices[modchosen], DexMacros.Type2)
    if (secondcolorstring == None):
        $ secondcolorstring = ""
    else:
        $ secondcolorstring = "{color=#fff}/{/color}{color=" + GetTypeColor(secondcolorstring) + "}" + secondcolorstring
    text pokedexlookup(choices[modchosen], DexMacros.Type1) + secondcolorstring size 40 align (0.5, 0.8) color GetTypeColor(pokedexlookup(choices[modchosen], DexMacros.Type1)) outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

    grid 4 2:
        align (0.5, 0.91)
        xspacing 15
        yspacing 25
        bar value pokedexlookup(choices[modchosen], DexMacros.Health) range 120 xmaximum 300 top_bar "#FF0000" bottom_bar "#A60000"
        bar value pokedexlookup(choices[modchosen], DexMacros.Attack) range 120 xmaximum 300 top_bar "#F08030" bottom_bar "#9C531F"
        bar value pokedexlookup(choices[modchosen], DexMacros.Defense) range 120 xmaximum 300 top_bar "#F8D030" bottom_bar "#A1871F"
        bar value pokedexlookup(choices[modchosen], DexMacros.SpecialAttack) range 120 xmaximum 300 top_bar "#6890F0" bottom_bar "#445E9C"
        bar value pokedexlookup(choices[modchosen], DexMacros.SpecialDefense) range 120 xmaximum 300 top_bar "#78C850" bottom_bar "#4E8234"
        bar value pokedexlookup(choices[modchosen], DexMacros.Speed) range 120 xmaximum 300 top_bar "#F85888" bottom_bar "#A13959"
        bar value potential range 700 xmaximum 300 top_bar "#FF00E4" bottom_bar "#710066"
        bar value potential / totalstats range 2.5 xmaximum 300 top_bar "#00FFF8" bottom_bar "#00827e"

    grid 4 2:
        align (0.5, 0.9)
        text "Health: " + str(pokedexlookup(choices[modchosen], DexMacros.Health)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Attack: " + str(pokedexlookup(choices[modchosen], DexMacros.Attack)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Defense: " + str(pokedexlookup(choices[modchosen], DexMacros.Defense)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Special Attack: " + str(pokedexlookup(choices[modchosen], DexMacros.SpecialAttack)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Special Defense: " + str(pokedexlookup(choices[modchosen], DexMacros.SpecialDefense)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Speed: " + str(pokedexlookup(choices[modchosen], DexMacros.Speed)) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Final BST: " + str(potential) size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]
        text "Potential: " + str(math.floor(potential / totalstats * 100)) + "%" size 40 color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

    imagebutton idle "Pokemon/" + str(choices[morechosen]) + ".webp" yalign 0.5 xanchor 0.5 xpos 0.85 action SetVariable("chosenindex", morechosen)
    key "K_RIGHT" action SetVariable("chosenindex", morechosen)
    add "Pokemon/" + str(choices[morechosen]) + ".webp" yalign 0.5 xanchor 0.5 xpos 0.85 at Transform(alpha=0.6, matrixcolor=BrightnessMatrix(-1))

screen abilitysplashleft(ability):
    zorder 100
    $ username = ability[0]
    $ ability = ability[1] + "\n{size=60}activated!"
    add "GUI/double-arrow.png" yalign 0.5 at swipeinleft, Transform(yzoom = 0.3, xzoom=-0.3)
    text "{size=60}" + username + "'s{/size}\n" + ability color "#fff" yalign 0.5 size 80 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleft
    timer 2.0 action Hide("abilitysplashleft")

screen abilitysplashright(ability):
    zorder 100
    $ username = ability[0]
    $ ability = ability[1] + "\n{size=60}activated!"
    add "GUI/double-arrow.png" yalign 0.5 xalign 1.0 at swipeinright, Transform(zoom = 0.3)
    text "{size=60}" + username + "'s{/size}\n" + ability color "#fff" yalign 0.5 size 80 xalign 1.0 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinright
    timer 2.0 action Hide("abilitysplashright")

screen itemsplashleft(itemname):
    zorder 100
    $ username = itemname[0]
    $ item = itemname[1] + "\n{size=60}was used!"
    add "GUI/itemarrow.png" yalign 0.5 at swipeinleft, Transform(yzoom = 0.3, xzoom=-0.3)
    text "{size=60}" + username + "'s{/size}\n" + item color "#fff" yalign 0.5 size 80 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleft
    timer 2.0 action Hide("itemsplashleft")

screen itemsplashright(itemname):
    zorder 100
    $ username = itemname[0]
    $ item = itemname[1] + "\n{size=60}was used!"
    add "GUI/itemarrow.png" yalign 0.5 xalign 1.0 at swipeinright, Transform(zoom = 0.3)
    text "{size=60}" + username + "'s{/size}\n" + item color "#fff" yalign 0.5 size 80 xalign 1.0 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinright
    timer 2.0 action Hide("itemsplashright")

screen songsplash(song, artist):
    zorder 100
    text "{size=60}♪ " + song + "{/size}\nby " + artist color "#fff" yalign 0.5 size 80 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at swipeinleftslow
    timer 10.0 action Hide("songsplash")

screen tables():
    zorder 5
    $ validtables = []
    grid 3 2:
        yalign .95
        xalign .5
        spacing 20
        $ tables = ["Angry Table", "Cheerful Table", "Busy Table", "Romantic Table", "Calm Table", "Quiet Table"]
        if (IsDate(20, 4, 2004) and GetRelationship("Nessa") == "Date"):
            $ tables = ["Angry Table", "Cheerful Table", None, "Romantic Table", "Calm Table", "Quiet Table"]
        for table in tables:
            if (table == None):
                null
            else:
                $ description = ""
                $ npcs = GetCharsInTable(table)
                if (table == "Angry Table"):
                    $ description = "This table is filled with students loudly arguing with each other. Despite the hostile atmosphere, they seem to be enjoying their anger."
                elif (table == "Cheerful Table"):
                    $ description = "This table is filled with students chatting and gossiping. Rumors are born and killed at this table."
                elif (table == "Busy Table"):
                    $ description = "This table is filled with students multi-tasking. They're all carrying on two conversations at once, phones to their ears. They frequently mention how they \"need to take this for their job.\""
                elif (table == "Romantic Table"):
                    $ description = "This table is filled with students unabashedly flirting. Cloth doilies cover the table, and there are rose petals scattered about. Someone's lit a candle-- No, wait. That's a Litwick."
                elif (table == "Calm Table"):
                    $ description = "This table is filled with students talking seriously. They discuss their school schedules, grades, extra curriculars, and plans for the future. You note they aren't discussing their social lives."
                elif (table == "Quiet Table"):
                    $ description = "This table is filled with students refusing to make eye contact with each other, and a Professor trying desperately to get them to. It's peaceful, though."
                    if (not IsBefore(11, 4, 2004)):
                        $ classtype = RandomChoice(list(altclassdex.keys()), True)
                        $ description += "\n{b}Professor Cherry can tutor you on the " + classtype + " type.{/b}"

                $ tablevalid = True
                for i, character in enumerate(npcs):
                    $ value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
                    if (value < 1):
                        $ tablevalid = False
                if (tablevalid):
                    $ validtables.append(table)
                textbutton table action ([Hide("tabledescriptions", Dissolve(0.5)), Return(table)] if tablevalid else NullAction()) xminimum 400 text_xalign .5 text_size 60 style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color ("#000" if tablevalid else "#616161") text_hover_color ("#f0f" if tablevalid else "#616161") hovered Show("tabledescriptions", Dissolve(0.5), description, npcs) unhovered Hide("tabledescriptions", Dissolve(0.5))
    
    if (len(validtables) == 0):
        textbutton "Sleeping Table" action [Hide("tabledescriptions", Dissolve(0.5)), Return("Sleeping Table")] xminimum 400 text_xalign .5 align (0.0, 0.0) text_size 60 style "menu_choice_button" text_font "fonts/pkmndp.ttf" text_color "#000" text_hover_color "#f0f" hovered Show("tabledescriptions", Dissolve(0.5), "Ethan is sleeping here, by himself...", ["Ethan"]) unhovered Hide("tabledescriptions", Dissolve(0.5))

screen tabledescriptions(description, npcs):
    for i, character in enumerate(npcs):
        $ charcolor = getCharColor(character)
        $ value = (persondex[character]["Value"] if character in persondex.keys() and "Value" in persondex[character].keys() else 0)
        $ valueceil = GetCharacterLevel(character)
        $ xposition = 1.0 / (len(npcs) + 1) * (i + 1) - 0.05
        if (len(npcs) == 1):
            $ xposition = 0.5
        if (character in persondex.keys() and "Value" in persondex[character].keys() and persondex[character]["Value"] > 0):
            if (character == "Tia" and not IsBefore(17, 4, 2004)):
                add "tia uniform hat" xpos xposition + 0.05
            elif (character != "Professor Cherry"):
                add character.lower() + " uniform" xpos xposition + 0.05
            else:
                add "kris" xpos xposition + 0.05
        else:
            $ finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
            if (character == "Tia" and not IsBefore(17, 4, 2004)):
                add "tia uniform hat" xpos xposition + 0.05
            elif (character != "Professor Cherry"):
                add character.lower() + " uniform" xpos xposition + 0.05 matrixcolor finalmatrix
            else:
                add "kris" xpos xposition + 0.05 matrixcolor finalmatrix

        text "{size=80}{color=" + charcolor + "}" + (character if character in persondex.keys() and persondex[character]["Named"] else "???").replace(" ", "\n") + "\n{/color}{size=40}Lv." + str(valueceil) + ", EXP: " + ('{color=#ff0000}' if value < 1 else "") + str(value) xpos xposition color "#fff" outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ] at Transform(rotate=-15)

    textbutton description xalign 0.5 ypos 0.65 xmaximum 1500 text_color "#000" background Frame("gui/button/choice_idle_background.png") xpadding 80

init python:
    def liberize(element):
        renpy.hide_screen("liberizemessage")
        global libtypes
        if (element in libtypes):
            libtypes.remove(element)
        else:
            libtypes.append(element)
            if (len(libtypes) > (2 if dawnbattle else libtypesnum)):#libtypesnum set to 2 if dawnbattle
                libtypes = libtypes[:len(libtypes) - 1]
                renpy.show_screen("liberizemessage", "You do not have the freedom to\nliberize into another type{w=0.5}\nyet.")
            else:
                libtype1 = libtypes[0]
                libtype2 = libtypes[0]
                if (len(libtypes) > 1):
                    libtype2 = libtypes[1]
                renpy.show_screen("liberizemessage", liberizefirstsentence[libtype1] + "\n" + liberizesecondsentence[libtype2])

transform liberize_scroll:
    ypos 1.0 yanchor 0.0
    ease 0.25 yalign 0.7
    ease 2.0 yalign 0.6
    ease 0.25 ypos 0.0 yanchor 1.0

screen liberizemessage(msg):
    vbox at liberize_scroll:
        xpos 0.65
        yalign 1.0
        text msg

    timer 2.5 action Hide()

screen liberize:
    add "imagemaps/libera_tail.webp" at liberizemovein
    imagemap at liberizefadein:
        idle "imagemaps/libera_idle.webp"
        hover "imagemaps/libera_hover.webp"
        alpha False 

        hotspot (278, 155, 127, 109) action Function(liberize, "Grass")#grass 
        hotspot (452, 192, 103, 129) action Function(liberize, "Fire")#fire
        hotspot (625, 249, 85, 123) action Function(liberize, "Water")#water
        hotspot (798, 308, 79, 123) action Function(liberize, "Electric")#electric
        hotspot (939, 367, 130, 109) action Function(liberize, "Fighting")#fighting
        hotspot (1114, 420, 111, 110) action Function(liberize, "Psychic")#psychic
        hotspot (206, 399, 117, 116) action Function(liberize, "Dark")#dark
        hotspot (373, 442, 123, 119) action Function(liberize, "Steel")#steel
        hotspot (547, 479, 112, 128) action Function(liberize, "Dragon")#dragon
        hotspot (710, 525, 122, 126) action Function(liberize, "Fairy")#fairy
        hotspot (880, 570, 120, 118) action Function(liberize, "Normal")#normal
        hotspot (1053, 615, 110, 122) action Function(liberize, "Ghost")#ghost
        hotspot (116, 673, 129, 97) action Function(liberize, "Flying")#flying
        hotspot (295, 685, 117, 114) action Function(liberize, "Poison")#poison
        hotspot (452, 722, 133, 91) action Function(liberize, "Ground")#ground
        hotspot (636, 748, 121, 107) action Function(liberize, "Rock")#rock
        hotspot (814, 755, 106, 124) action Function(liberize, "Bug")#bug
        hotspot (975, 785, 127, 124) action Function(liberize, "Ice")#ice

    for element in libtypes:
        add "imagemaps/libera{}.webp".format(element.lower()) at liberizeactivefadein

    textbutton "Finish" xminimum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" xalign 1.0 yalign 1.0 action [Hide("liberize", Dissolve(0.5)), Return("liberaconfirm")]

screen map_UI():
    if (not renpy.get_screen("currentdate")):
        use currentdate()

    zorder -5
    imagemap:
        ground "BG/Map.jpg"
        idle "BG/Map.jpg"
        hover "imagemaps/Map_Hover.jpg"
        
        hotspot (161, 121, 429, 230) action Show("map_confirm", Dissolve(0.5), "Battle Hall") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Battle Hall"), (161, 121, 429, 230)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (658, 107, 609, 214) action Show("map_confirm", Dissolve(0.5), "Academy") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Academy"), (658, 107, 609, 214)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (88, 343, 331, 275) action Show("map_confirm", Dissolve(0.5), "Recreation Center") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Recreation Center"), (88, 343, 331, 275)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (88, 621, 464, 384) action Show("map_confirm", Dissolve(0.5), "Aura Hall") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Aura Hall"), (88, 621, 464, 384)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (1451, 347, 376, 250) action Show("map_confirm", Dissolve(0.5), "Research Center") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Research Center"), (1451, 347, 376, 250)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (733, 566, 475, 220) action Show("map_confirm", Dissolve(0.5), "Garden") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Garden"), (733, 566, 475, 220)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (581, 780, 757, 258) action Show("map_confirm", Dissolve(0.5), "Relic Hall") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Relic Hall"), (581, 780, 757, 258)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (734, 312, 500, 249) action Show("map_confirm", Dissolve(0.5), "Student Center") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Student Center"), (734, 312, 500, 249)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (1456, 140, 419, 200) action Show("map_confirm", Dissolve(0.5), "Baseball Field") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Baseball Field"), (1456, 140, 419, 200)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (232,0, 1594, 111) action [Hide("map_people", Dissolve(0.5)), Return("Town")]
        hotspot (1367, 618, 473, 385) action Show("map_confirm", Dissolve(0.5), "Pledge Hall") hovered Show("map_people", Dissolve(0.5), GetCharsInPlace("Pledge Hall"), (1367, 618, 473, 385)) unhovered Hide("map_people", Dissolve(0.5))
        hotspot (0, 964, 362, 116) action [Hide("map_people", Dissolve(0.5)), Return("Fields")]

screen egghunt():
    if (not renpy.get_screen("currentdate")):
        use currentdate()

    zorder -5
    imagemap:
        ground "BG/Map.jpg"
        idle "BG/Map.jpg"
        hover "imagemaps/Map_Hover.jpg"
        
        hotspot (161, 121, 429, 230) action Return("Battle Hall") #Tyrogue
        hotspot (658, 107, 609, 214) action Return("Academy") #Smoochum
        hotspot (88, 343, 331, 275) action Return("Recreation Center") #Mantyke
        hotspot (88, 621, 464, 384) action Return("Aura Hall") #Togepi
        hotspot (1451, 347, 376, 250) action Return("Research Center") #Toxel
        hotspot (733, 566, 475, 220) action Return("Garden") #Happiny
        hotspot (581, 780, 757, 258) action Return("Relic Hall") #Magby
        hotspot (734, 312, 500, 249) action Return("Student Center") #Wynaut
        hotspot (1456, 140, 419, 200) action Return("Baseball Field") #Larvesta
        hotspot (1367, 618, 473, 385) action Return("Pledge Hall") #Bonsly
        hotspot (0, 964, 362, 116) action Return("Outside")

screen makeup():
    if (not renpy.get_screen("currentdate")):
        use currentdate()

    zorder -5
    imagemap:
        ground "BG/Map.jpg"
        idle "BG/Map.jpg"
        hover "imagemaps/Map_Hover.jpg"
        
        hotspot (161, 121, 429, 230) action [Hide("map_people", Dissolve(0.5)), Return("Battle Hall")] #Returns a failure message
        hotspot (1451, 347, 376, 250) action [Hide("map_people", Dissolve(0.5)), Return("Research Center")] hovered Show("map_people", Dissolve(0.5), ["Bea", "Nate"], (1451, 347, 376, 250)) unhovered Hide("map_people", Dissolve(0.5))#Bea & Nate talking about violence
        hotspot (88, 343, 331, 275) action [Hide("map_people", Dissolve(0.5)), Return("Recreation Center")] hovered Show("map_people", Dissolve(0.5), ["Rosa", "Nessa"], (88, 343, 331, 275)) unhovered Hide("map_people", Dissolve(0.5))#Rosa & Nessa #talking about fame, and how it's ruined them
        hotspot (88, 621, 464, 384) action [Hide("map_people", Dissolve(0.5)), Return("Aura Hall")] hovered Show("map_people", Dissolve(0.5), ["Bianca", "Hilda", "May", "Serena"], (88, 621, 464, 384)) unhovered Hide("map_people", Dissolve(0.5))#Leaf's Roommates
        hotspot (581, 780, 757, 258) action [Hide("map_people", Dissolve(0.5)), Return("Relic Hall")] hovered Show("map_people", Dissolve(0.5), ["Brendan", "Calem", "Hilbert"], (581, 780, 757, 258)) unhovered Hide("map_people", Dissolve(0.5))#Roommates
        hotspot (1367, 618, 473, 385) action [Hide("map_people", Dissolve(0.5)), Return("Pledge Hall")] hovered Show("map_people", Dissolve(0.5), ["Cheren", "Silver", "Skyla"], (1367, 618, 473, 385)) unhovered Hide("map_people", Dissolve(0.5))#Disciplinary Committee
        hotspot (1456, 140, 419, 200) action [Hide("map_people", Dissolve(0.5)), Return("Baseball Field")] hovered Show("map_people", Dissolve(0.5), ["Flannery", "Whitney"], (1456, 140, 419, 200)) unhovered Hide("map_people", Dissolve(0.5))#Flannery & Whitney's Dorm
        hotspot (232,0, 1594, 111) action [Hide("map_people", Dissolve(0.5)), Return("Inspira")] hovered Show("map_people", Dissolve(0.5), ["Jasmine", "Grusha"], (232,50, 1594, 161)) unhovered Hide("map_people", Dissolve(0.5)) #The First Aid Squad (Grusha, Jasmine, Wally(?))
        hotspot (0, 964, 362, 116) action [Hide("map_people", Dissolve(0.5)), Return("Outside")]

screen map_people(people, location):
    $ values = {(0, 1): 0, (0, 2): -50, (1, 2): 50, (0, 3): -100, (1, 3): 0,
        (2, 3): 100, (0, 4): -150, (1, 4): -50, (2, 4): 50, (3, 4): 150}
    for i, person in enumerate(people):
        $ centerpos = (location[0] + location[2] / 2.0 + values[(i, len(people))], location[1] + location[3])
        $ charcolor = getCharColor(person)
        $ finalmatrix = TintMatrix(charcolor) * BrightnessMatrix(1.0) * ContrastMatrix(0.0)
        $ personsprite = person.lower()
        if (person == "Professor Cherry"):
            $ personsprite = "kris"
        elif (person == "Tia" and not IsBefore(17, 4, 2004)):
            $ personsprite = "tia hat"
        add personsprite at (hovering if getscenes([person])[0][1] else None) matrixcolor finalmatrix xpos math.floor(centerpos[0]) ypos math.floor(centerpos[1]) zoom 0.21
        if (persondex[person]["Named"]):
            add personsprite at (hovering if getscenes([person])[0][1] else None) xpos math.floor(centerpos[0]) ypos math.floor(centerpos[1]) zoom 0.2

screen map_confirm(location):
    modal True
    vbox:
        align (0.5, 0.5)
        if (location == "Academy" and (calDate.day > 11 or calDate.month > 4 or calDate.year > 2004)):
            textbutton "{b}Study{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("Study")]
        if (location == "Student Center"):
            textbutton "{b}Heal Party{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Function(HealParty)]
        if (location == "Baseball Field" and "Gardenia" in GetCharsInPlace("Baseball Field") and not IsBefore(25, 4, 2004) and (getRWDay(0) == "Sunday" or getRWDay(0) == "Saturday" or timeOfDay == "Evening")):
            textbutton "{b}Talk Business{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("Business")]
        if (location == "Battle Hall" and "Janine" in GetCharsInPlace("Battle Hall") and not IsBefore(26, 4, 2004) and (getRWDay(0) == "Sunday" or getRWDay(0) == "Saturday" or timeOfDay == "Evening")):
            textbutton "{b}Check Levels{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("LevelCheck")]
        if (location == "Garden" and "Professor Cherry" in GetCharsInPlace("Garden") and GetRelationshipRank("Professor Cherry") != 0):
            textbutton "{b}Check Critical Capture Rate{/b}" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return("CriticalCheck")]
        for chartuple in getscenes(GetCharsInPlace(location)):
            $ charname = chartuple[0]
            if (persondex[charname]["Named"]):
                $ hasscene = chartuple[1]
                $ posttext = ""
                if (not hasscene):
                    if charname in sceneconditions.keys() and GetRelationship(charname) in sceneconditions[charname].keys():
                        $ posttext = " - Next Scene: " + sceneconditions[charname][GetRelationship(charname)]
                textbutton ("{b}[[RANK UP!]{/b} " if hasscene else "") + ">Find " + charname + posttext xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color getCharColor(chartuple[0]) style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return(chartuple[0])]
        textbutton "Back" xminimum 800 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("map_confirm", Dissolve(0.5)), Return ("Back")]

screen evolution(oldid, newid, liberize=False):
    $ oldimage = "images/Pokemon/" + str(oldid) + ".webp"
    $ newimage = "images/Pokemon/" + str(newid) + ".webp"
    add "BG/Blank2.jpg" at dissolvein
    add "GFX/speedlines.jpg" at speedlines
    add newimage xzoom (-1 if liberize else 1) at evolvein
    if (liberize):
        add "images/Pokemon/25.2-1.webp" xzoom -1 at evolvein
        add "images/Pokemon/25.2-2.webp" xzoom -1 at evolvein
    add oldimage xzoom (-1 if liberize else 1) at evolveaway

    if (not liberize):
        hbox:
            yalign .95
            xalign .5
            spacing 300
            textbutton "Skip!" text_xalign 0.5 xmaximum 300 text_color "#000" text_hover_color "#0f0" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("evolution"), Return(True)]    
            textbutton "Abort!" text_xalign 0.5 xmaximum 300 text_color "#000" text_hover_color "#f00" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("evolution"), Return(False)]

    timer 25 action [Hide("evolution", Dissolve(2.0)), Return(True)]

screen shopkeep(items):
    vbox:
        xalign .5
        yalign .85
        for i in range(math.ceil(len(items) / 5)):
            hbox:
                for item in items[i * 5: i * 5 + 5]: #item is (name, cost, description)
                    textbutton item[0] + " - $" + str(item[1]) text_xalign 0.5 xmaximum 300 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Show("itemdetails", Dissolve(0.5), item)]
        textbutton "Back" xalign .5 xminimum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("itemdetails", Dissolve(0.5)), Return("Back")]

screen itemdetails(item):
    $ itemname = item[0]
    $ itemcost = item[1]
    $ itemdescription = item[2]

    add "gui/button/choice_idle_background.png" xalign .5 xzoom 1.5 yzoom 15 ypos -.05

    text "{b}" + itemname + "{/b}" xcenter 0.5 yalign .1 size 120
    text itemdescription xcenter 0.5 yalign .2
    text "$" + str(itemcost) + " x" + str(boughtitems) + " = $" + str(itemcost * boughtitems) xcenter 0.5 yalign 0.3
    text "Inventory: " + str(GetNumItems(itemname)) xcenter 0.5 yalign 0.4

    hbox:
        xalign .25
        yalign .5
        textbutton "-10" xmaximum 100 text_xalign 0.5 text_color "#700" text_hover_color "#f00" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("boughtitems", max(1, boughtitems - 10))
        textbutton "-1" xmaximum 100 text_xalign 0.5 text_color "#700" text_hover_color "#f00" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("boughtitems", max(1, boughtitems - 1))
    
    vbox:
        align (0.5, 0.5)
        textbutton "Buy!" xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f"  style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("itemdetails", Dissolve(0.5)), Return(item)]
        textbutton "Back" xmaximum 250 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action [Hide("itemdetails", Dissolve(0.5))]
    
    hbox:
        xalign .75
        yalign .5
        textbutton "+1" xmaximum 100 text_xalign 0.5 text_color "#070" text_hover_color "#0f0" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("boughtitems", min(99, boughtitems + 1))
        textbutton "+10" xmaximum 100 text_xalign 0.5 text_color "#070" text_hover_color "#0f0" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("boughtitems", min(99, boughtitems + 10))

init python:
    def swapPokemonLocation(pkmn):
        global box
        global playerparty
        global currentbox
        pkmn.Heal()
        if (pkmn in playerparty):
            if (len(playerparty) == 2):
                renpy.invoke_in_new_context(renpy.say, None, "You need to keep at least two Pokémon in your party!")
            elif (pkmn != pikachuobj):
                playerparty.remove(pkmn)
                box.append(pkmn)
            else:
                if (not IsDate(5, 5, 2004)):
                    renpy.hide_screen("partymons")
                    renpy.jump("nopikachu")
        elif (pkmn in box and len(playerparty) < 6):
            box.remove(pkmn)
            playerparty.append(pkmn)
        else:
            renpy.invoke_in_new_context(renpy.say, None, "Your party is full!")

        if (currentbox > math.floor((len(box) - 1) / 30)):
            currentbox -= 1

screen partymons:
    zorder 0
    grid 3 2:
        xalign 0.5
        yalign 0.1
        for mon in playerparty:
            textbutton mon.GetNickname() + " {size=20}Lv." + str(mon.GetLevel()) xmaximum 310 text_size 40 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action Function(swapPokemonLocation, mon)
        for i in range(6 - len(playerparty)):
            null
    textbutton "Back" align (0.5, 0.4) xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action Return()
    
    add "gui/button/choice_idle_background.png" xalign .5 xzoom 0.35 yalign 0.56 yzoom 2.5
    text "Box #" + str(currentbox + 1) align (0.5, 0.57) color "#fff" size 120 outlines [ (absolute(10), "#000", absolute(0), absolute(0)) ]

    hbox:
        spacing 20
        align (0.5, 0.57)
        textbutton ("{b}" if currentsort == "level" else "") + "Lv. Sort" + ("" if currentsort != "level" else " " + ("↓" if reversesort else "↑")) xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action (SetVariable("currentsort", "level") if currentsort != "level" else ToggleVariable("reversesort"))
        textbutton ("{b}" if currentsort == "abc" else "") + "ABC Sort" + ("" if currentsort != "abc" else " " + ("↓" if reversesort else "↑")) xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action (SetVariable("currentsort", "abc") if currentsort != "abc" else ToggleVariable("reversesort"))
        null width 350
        textbutton ("{b}" if currentsort == "dex" else "") + "Dex Sort" + ("" if currentsort != "dex" else " " + ("↓" if reversesort else "↑")) xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action (SetVariable("currentsort", "dex") if currentsort != "dex" else ToggleVariable("reversesort"))
        textbutton "Stop Sorting" xmaximum 300 text_xalign 0.5 text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" action SetVariable("currentsort", None)

init python:
    def SortedBox():
        global box
        if (currentsort == "level"):
            box.sort(reverse = reversesort, key=(lambda entry : entry.GetLevel()))
        elif (currentsort == "abc"):
            box.sort(reverse = reversesort, key=(lambda entry : entry.GetNickname()))
        elif (currentsort == "dex"):
            box.sort(reverse = reversesort, key=(lambda entry : entry.GetId()))
        return box[currentbox * 30:currentbox * 30 + 30]

label pokemonextraoptions(pkmn):
    $ nick = pkmn.GetNickname()
    "What would you like to do with [nick]?"

    menu:
        "Rename it.":
            $ newnick = renpy.input("What would you like to nickname it?", default=nick, exclude="{}[[]%<>", length=12)
            if (newnick == ""):
                $ newnick = pokedexlookup(pkmn.GetId(), DexMacros.Name)
            $ pkmn.Nickname = newnick
            "The Pokémon has been renamed to [newnick]."

        "Relieve it. (Of its item.)" if (pkmn.GetItem() != None):
            $ RemoveItem(pkmn)

            "You do so."

        "{color=#FF0000}Release it.{/color}" if (pkmn != starterobj):
            "Are you absolutely certain? There is no getting it back without reloading a save. (Or using rollback.)"

            menu:
                "Do it.":
                    $ box.remove(pkmn)
                    if (currentbox > math.floor((len(box) - 1) / 30)):
                        $ currentbox -= 1
                    "The Pokémon runs away sadly..."

                "No.":
                    pass

        "Nevermind.":
            pass
return

screen pokemonswap:
    zorder 6    
    if (len(box) > 30):
        textbutton "<-": 
            xmaximum 100 yminimum 200 align (0.01, 0.83) text_xalign 0.5 
            text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
            action SetVariable("currentbox", (currentbox - 1 if currentbox != 0 else math.ceil(len(box) / 30) - 1))
    if (len(box) > 30):
        textbutton "->": 
            align (.99, 0.83) xmaximum 100 yminimum 200 text_xalign 0.5 
            text_color "#000" text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
            action SetVariable("currentbox", (currentbox + 1 if currentbox != math.ceil(len(box) / 30) - 1 else 0))

    grid 6 5:
        xalign 0.5
        yalign 0.9
        for mon in SortedBox():
            textbutton mon.GetNickname() + " {size=20}Lv." + str(mon.GetLevel()):
                xmaximum 280 text_size 40 text_xalign 0.5 text_color "#000" ymaximum 70
                text_hover_color "#f0f" style "menu_choice_button" text_font "fonts/pkmndp.ttf" 
                action [Hide("nonbattlemoves"), Hide("mondata"), Function(swapPokemonLocation, mon)] 
                hovered [Show("mondata", None, mon, False), Show("nonbattlemoves", None, mon, tooltips=False, _zorder=5)] 
                unhovered [Hide("mondata"), Hide("nonbattlemoves")]
                alternate [Hide("partymons"), Hide("nonbattlemoves"), Hide("mondata"), Call("pokemonextraoptions", mon)]
        for i in range(30 - len(SortedBox())):
            null

transform credits_scroll():
    yalign 0.0
    linear 50 yalign 1.0

screen credits:
    add "BG/Blank2.jpg"
    vbox at credits_scroll:
        xalign 0.5
        yalign 0.1
        spacing 50
        null height 1080

        vbox:
            text "Project Recreator" size 80 color "#fff"
            text "Freudian Creations" size 40 color "#fff"

        vbox:
            text "CG Artists" size 80 color "#fff"
            text "Dahlia Wilder" size 40 color "#fff"
            text "Wolff Steel" size 40 color "#fff"

        $ spriteartists = ["Iustinus Tempus", "Chayma", "KBunink", "Dantalion", "Anthos", "Wolff Steel", "SquishyBird22", "Ken Sugimori"]
        vbox:
            text "Sprite Artists" size 80 color "#fff"
            for name in spriteartists:
                text name size 40 color "#fff"

        $ specialthanks = ["Drunk Old Man", "imainmeleekirby", "JumboXtraLarge", "Bartre God Dio", "Novemball"]
        vbox:
            text "Special Thanks" size 80 color "#fff"
            for name in specialthanks:
                text name size 40 color "#fff"
        
        $ topstudents = ["Drunk Old Man [[Lisia's grandpa]", 'Leirbag15 (Pikmin Trainer)', 'nmorrow', 'denial___', 'Calem le français', 'cinnaburh', 'seanmac317', "JXL- Tia's ICE/Astrid's Superego", 'torait21', 'caerulight', 'Lexel (Bea Simp)', 'Q1justin [[Blue Deserves Love]', 'Adamthenoob1 (#1 Simp for Hilda)']
        vbox:
            text "Teaching Assistants" size 80 color "#fff"
            for name in topstudents:
                text name size 40 color "#fff"

        $ teachingassistants = ['kingsting', 'shinzeka', 'Based Squire (Krok)', "Drunk Old Man [[Lisia's grandpa]", 'kingslayer3765', 'pestofettuccine', 'Leirbag15 (Pikmin Trainer)', 'velmidos9021', 'nmorrow', 'prettymiggy', 'Based King 🤴🏾 (Christian)', 'nicksaulnier', 'kogasaka', 'denial___', 'weez1ng', 'Raion [[Lyra and Serena Simp]', 'tiggyxtaggy', 'Calem le français', 'carpechaz', 'kenjinava', 'myname_jonas', "FlanneryHildaAreMY#1's", 'tgasf', 'microe', 'Pesto', 'Orion', 'inferno6703', 'Horny [[Champion Enjoyer]', 'cinnaburh', 'zajinho2b', '-Leaf simp~', 'seanmac317', 'rhaykou', 'FAKE', 'thepridefulcynicist', "JXL- Tia's ICE/Astrid's Superego", 'torait21', 'Cobra - #1 Leaf Fan', 'caerulight', 'Lexel (Bea Simp)', 'Bartre God Dio', 'himdave', 'Q1justin [[Blue Deserves Love]', 'Adamthenoob1 (#1 Simp for Hilda)', 'alurayune', 'Toop']
        vbox:
            text "Top Students" size 80 color "#fff"
            for name in teachingassistants:
                text name size 40 color "#fff"

        $ commissioners = ["Drunk Old Man [[Lisia's grandpa]", 'Leirbag15 (Pikmin Trainer)', 'jwillicus_', 'Ethan (EL PAPUCHO DE ANTHOS)', 'nathanrose.', 'moka6803', 'Horny [[Champion Enjoyer]', 'SerenaSimpInc-HopingforaHappyEnd', 'Bartre God Dio', 'crippledjoe', 'flintlocksq']
        vbox:
            text "Commissioners" size 80 color "#fff"
            for name in commissioners:
                text name size 40 color "#fff"

        vbox:
            text "Backgrounds" size 80 color "#fff"

            text "Love Ribbon by Razzart Visual" size 40 color "#fff"
            text "Backgrounds by Minikle" size 40 color "#fff"

            null height 50

            text "Your Diary by CUBE" size 40 color "#fff"
            text "Artworks by Kantoku, and Suimya" size 40 color "#fff"

            null height 50

            text "The Quintessential Quintuplets the Movie: Five Memories of My Time with You by MAGES. GAME" size 40 color "#fff"
            text "Backgrounds by Fukuda Tomonori, and Nagai Taketo" size 40 color "#fff"

            null height 50

            text "Backgrounds by Sai Gakai (増助彩)/Kimagure After (きまぐれアフター)" size 40 color "#fff"

            null height 50

            text "Backgrounds by Min-Chi (みんちり)" size 45 color "#fff"
            text "Taken from みんちりえ (https://min-chi.material.jp/) and みんちりのfanbox (https://min-chi.fanbox.cc/)" size 25 color "#fff"

        
        null height 1080