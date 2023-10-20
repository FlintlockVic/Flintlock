############################################################################################################################################################################################################################
# FIRST DAY ON CAMPUS: PLAYER MEETS HALL GUIDE, PROCEEDS TO LOOK FOR POTENTIAL ROOMMATE MATCH, MEETS BLUE, THEN HAS CHOICE OF ROOMMATE BETWEEN BRENDAN, CALEM, CHEREN AND TIERNO.
# PATH DIVERGES UPON SELECTING ROOMMATE, PLAYER SEPARATES FROM ROOMMATE, GETS LOST AND MEETS LEAF, REUNITES WITH ROOMMATE, THEN PROCEEDS TO THE ORIENTATION.
# PLAYER SEES ROXANNE AT ORIENTATION, ALTERNATIVE DIALOGUE DEPENDING ON ROOMMATE, PLAYER RETURNS TO ROOM WITH ROOMMATE AND SELECTS TYPE ELECTIVE CLASSES.

label day010402:    
    $ renpy.pause(1.0, hard=True)
    scene lobby with dissolve

    show falkner uniform with dis
        
    pause 0.5

    falkner @talkingmouth "Hello. Welcome to Relic Hall, one of the three residence halls of this esteemed academy."
    
    hide relichall_A
    hide blank
    
    falkner @closedbrow talking2mouth "Are you here to reserve a dorm? If so, may I have your name? First and last."
    
    red happy "Sure, it's [first_name] [last_name]! And I think I'm here to reserve a dorm. That's what Brawly said to do."
    falkner @closedbrow talkingmouth "Hm. You met Brawly, then."
    red -happy "You know him?"
    $ BecomeNamed("Falkner")
    falkner @talking2mouth "Yes. I'm Falkner, and we work together on the Student Council.{w=0.5} ...Though work may be too strong a word, in his case."

    red closedeyes angryeyebrows frownmouth "I've been hearing that a lot about Brawly, but he seems great, to me."

    falkner @closedbrow happymouth "I'm sure he appreciates that."
    falkner @talkingmouth "In any case, suites are first-come, first-serve. If you have permission from the school to dorm with someone in particular, let me know. Otherwise, I can assign you a suite."
    falkner @sad "...I can also ensure that you don't dorm with someone you'd rather not spend a year with."

    red happy "If you could make sure I don't dorm with 'Blue Oak,' then I'm good with anyone else!"

    falkner @closedbrow talking2mouth "Very well. You'll be in Dorm... 151. Carry on down this hallway, take a left at the Tranquill Wing's exit and continue diagonally past the skywalk." 
    falkner @talkingmouth "After you drop off your luggage, you may want to head to the lobby. To... 'mingle.'"
    
    red "Will do.{w=0.5} Thanks!"

    hide falkner with dis

    pause 1.0
    
    red @surprised "Okay, the way he just said 'mingle' was mega-weird."
    red "But whatever, it's time to head to my dorm!"

stop music fadeout 1.5
$ renpy.pause(1.5, hard=True)
scene hall_A2b with Dissolve(1.0)
pause 1.0

show hall_A2:
    xalign 0.0 yalign 1.0 xpos 0 ypos 1080 zoom 0.625
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -300 ypos 1120
    parallel:
        ease 1.0 zoom 0.8
        
$ renpy.pause(1.2, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -300 ypos 1120 zoom 0.8
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -100 ypos 1200
    parallel:
        ease 1.0 zoom 0.85
        
$ renpy.pause(1.4, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -100 ypos 1200 zoom 0.85
    parallel:
        ease 1.2 xalign 0.0 yalign 1.0 xpos -550 ypos 1300
    parallel:
        ease 1.0 zoom 0.9

$ renpy.pause(1.5, hard=True)

show hall_A2:
    xalign 0.0 yalign 1.0 xpos -550 ypos 1300 zoom 0.9
    ease 1.0 xalign 0.0 yalign 1.0 xpos -480 ypos 1250 zoom 0.85

red ".{w=0.25}.{w=0.25}."

red happy "Yep. I'm lost."

redmind closedeyes frownmouth "I guess my lucky streak of running into every single Student Council member had to end eventually."
redmind "I must've left the area where the dorms are, though. When I was there, there were tons of students around, but now it's just me."
red happy "Well. If I just pick a direction and run, then, I bet I'll find my way back to where I was!"
red -happy "Just going to tighten my laces, and then..."

pause 1.0

show hall_A2:
    xalign 0.0 xpos -480 ypos 1250 zoom 0.85
    ease 1.5 xpos -530 ypos 1120 zoom 0.8

pause 1.0

red sadeyes sadeyebrows frownmouth "...Actually... Maybe I should hold off. I don't want to knock a vase over or anything."

show hall_A2:
    xpos -530 ypos 1120 zoom 0.8

"{color=#00b23f}Female Voice{/color}" "{size=28}{i}Hey, buddy. What do you think you're doing?{/i}{/size}"

show hall_A2 with vpunch:
    xalign 0.0 xpos -530 ypos 1120 zoom 0.8
    ease 0.1 xpos -100 ypos 1100 zoom 0.7

show leaf surprised:
    alpha 0.0 xpos 0.5
    ease 0.75 alpha 1.0

red surprised "Gah!"

$ renpy.music.queue("Audio/Music/Pallet Town A.ogg", channel='music', loop=True, fadein=1.0, tight=None)

show hall_A2:
    xpos -100 ypos 1100 zoom 0.7

red closedeyes talking2mouth "Geez, talk about heart attacks..."

show leaf -surprised frownmouth with dis

red happy "Sorry, you scared the hell out of me! You make a habit of skulking up behind people and whispering in their ears?"

leaf talkingmouth "{i}I'm{/i} the one skulking?{w=0.5} Do you have {i}any{/i} idea where you are?"

red -happy frownmouth "Um..."
red "Just... just a random set of dorms, right?"

show hall_A2:
    xalign 0.0 xpos -100 ypos 1100
    ease 1.0 xpos 0 ypos 1175
        
show leaf flirt:
    subpixel True
    xpos 0.5 ypos 1.0
    ease 1.0 xpos 0.6 ypos 1.1

red "Oh, wait, there's something on the sign here..."

show leaf happy with dis
    
red talking2mouth "{cps=12}'Cheer Squad's Changing Rooms'{/cps}{w=0.5}"

pause 1.5

red "Huh. Okay, so, I guess I'm {i}very{/i} lost."

pause 1.0

red frownmouth closedeyes "Ah, damn it.{w=0.5} You're not going to spread weird rumors about me, are you?"

show hall_A2:
    xalign 0.0 yalign 1.0 xpos 0 ypos 1175
    ease 1.0 xpos -100 ypos 1100
        
show leaf happy:
    subpixel True
    xpos 0.6 ypos 1.1
    ease 1.0 xpos 0.5 ypos 1.0

red sadeyes sadeyebrows frownmouth "Seriously, I just wandered up here by accident. It's obvious, right? And it's pretty dumb for the cheer squad to have their changing rooms so far away from the fields."

show leaf happy:
    xpos 0.5 ypos 1080

leaf -happy "I'm going to be honest, I feel like I'm watching a Growlithe chase its own tail."
leaf flirt "It's kinda cute."

red surprised "C-cute?"

leaf happybrow talking2mouth "Yeah, I've always thought that a shitty sense of direction was a massive turn-on."

red angrybrow frownmouth ".{w=0.25}.{w=0.25}."
red "Well, great. Glad I could do that for you. Mind pointing me in the right direction, now?"

leaf -happybrow -talking2mouth "I don't think the brochure's that hard to follow.{w=0.5}{nw}"
leaf surprised "I don't think the brochure's that hard to follow.{fast} I mean, the design of the dorm's wings are laid out in a grid, so it should be really easy to navigate."
leaf -surprised "Here, let me see yours."

show leaf:
    xpos 0.5 ypos 1.0
    ease 1.0 zoom 1.2 ypos 1.1 xpos 0.6

red -angrybrow closedeyes frownmouth "I... don't have one of those."
red "Though, now that you mention it, I vaguely remember some other students carrying around some small leaflets... Damn. Guess I missed the boat on that one."

leaf surprisedbrow sadmouth "You {i}seriously{/i} went all this time without a map?{w=0.5} And then you made it all the way here from the main hall?"

leaf fullblush -surprisedbrow -sadmouth "I have to say, your sense of direction is amazing.{w=0.7} Uh, wait, no it's not.{w=0.5}{nw}"
leaf happy "I have to say, your sense of direction is amazing. Uh, wait, no it's not.{fast} It's just hopeless!"
    
show leaf happy:
    zoom 1.2 ypos 1.1 xpos 0.6
    ease 1.0 zoom 1.0 xpos 0.5 ypos 1.0

extend " Ha ha ha!"
$ renpy.music.set_volume(1.0, delay=0.0, channel="ctc")
    
red "You're not winning any points with me, personality-wise, right now..."

leaf flirtbrow -fullblush talking2mouth "Oh, so I'm winning points in other ways? Maybe it's my fashion sense?"

red "Sure, let's go with that. Now, are you just going to keep laughing or are you going to point me out of here?"

leaf -flirt "Since you asked so nicely, I'll take you up on that offer."

show leaf happy:
    alpha 1.0 xpos 0.5
    parallel:
        ease 1.0 alpha 0.0
    parallel:
        ease 1.2 xpos 0.4
        
leaf "Ha ha ha! Ha ha ha ha ha!"

red "Hey! You--"

"Female Student" "{size=20}--y{/size}{size=22}eah{/size}{size=24}, sh{/size}{size=26}e wa{/size}{size=28}s to{/size}{size=29}tal{/size}{size=30}ly{/size} {size=31}dit{/size}{size=32}ch{/size}{size=33}ing{/size} {size=34}us t{/size}o go shop--"

red angrybrow frownmouth "Ah, great. More. Sounds like I'll have to explain myself to a whole group, now. Maybe if I just keep my head down, I can walk on by."

show leaf surprised blush:
    alpha 0.0 xpos 0.4
    ease 0.6 alpha 1.0 xpos 0.5

pause 0.6

show leaf surprised blush:
    xpos 0.5 alpha 1.0
    
show hall_A2:
    xalign 0.0 xpos -100 ypos 1100 zoom 0.7
    ease 2.5 xpos -2000 ypos 2640 zoom 2.0 
show leafintro_A:
    alpha 0.0 xalign 0.5 yalign 0.5 zoom 1.08
    pause 1.5
    ease 1.25 zoom 1.0 alpha 1.0
        
show leaf surprised blush:
    alpha 1.0
    pause 1.5
    ease 1.0 alpha 0.0

red -angrybrow surprised "Gah! Jeez, that's a firm grip."
red closedeyes "Hey, I appreciate it, but you don't need to bail me out here.{w=0.5} I can just explain to them what happ--"

hide leaf

leaf surprised "I'm not bailing you out! I'm bailing myself out. I don't want rumors spreading that I'm hanging out with the cheerleader changing room skulker before I've even had my first class!"
red frownmouth "And here I was, briefly having the thought that maybe you were doing something selfless."
red -closedeyes "Thanks for clearing that up for me."

play sound "Audio/GenericDoorOpen.ogg"
leaf -surprised "Oh, stop whining. Just stay here!"

play sound "Audio/GenericDoorClose.ogg"
red "...She just went into the women's restroom."
red ".{w=0.25}.{w=0.25}."
red happy "This is going to be so dumb."

pause 1.0

play sound "Audio/GenericDoorOpen.ogg"
leaf happy "Okay, hide in here. I'll come get you when the coast is clear."

red -happy "Didn't think I'd have to point this out to you, but that's the women's room."

play sound "Audio/GenericDoorClose.ogg"
leaf firtbrow talkingmouth "Yeah, I have eyes, too. It's the only room that's not locked in this hallway, so get in before they see us!"

red closedeyes ".{w=0.25}.{w=0.25}.{w=0.25}I'm struggling to find the words necessary to explain why this is not going to happen." 
leaf angrybrow talkingmouth"What's your problem? It's just a girls' bathroom, not some kind of private sanctuary! Believe me, you're {i}definitely{/i} not going to defile it with {i}your{/i} male presence."
red angrybrow frownmouth ".{w=0.25}.{w=0.25}.{w=0.25}Okay, I don't like how you emphasized the 'your' there. I promise you, I'm definitely male."
leaf angrybrow angrysmilemouth "Really? Because you're being a total girl right now."
red angrybrow "That's sexist."
leaf angry "Just get in the damn bathroom!"

if (profanity):
    menu:
        ">Get in the damn bathroom.":        
            red -angrybrow "Okay, I'll do it. But I'm covering my eyes while I'm in there."
            
            show leafintro_happy:
                alpha 0.0
                ease 0.5 alpha 1.0
            
            leaf happy "What a gentleman you are."

            pause 1.0
            
            leaf -happy "Now, not a peep from you while I'm gone."
            
            play sound "Audio/GenericDoorOpen.ogg"
            
            leaf flirt "Ladies first."
            
            red angrybrow "Ha. Ha."
            
        ">Don't get in the damn bathroom.":        
            red -angrybrow "Fat chance. I've never been inside of a women's bathroom for eighteen years and I'm not about to start now. {w=0.25}That goes against everything I stand for.{w=0.5} Besides, what if someone else is in there?{w=0.5} Then we'd really be in trouble."
            
            leaf angry "You got memory problems? I {i}just{/i} checked!"

            red surprisedeyes surprisedeyebrows talking2mouth "Yeah, but... someone could've come in since then. I mean, we've been watching the door, but there's windows on the inside."
            
            show leafintro_mad:
                alpha 0.0
                ease 0.5 alpha 1.0

            red "So someone could've, like... {cps=20}climbed up from outside, and... {cps=15}gone in there..."
            
            leaf ".{w=0.25}.{w=0.25}.{w=0.25}"
            leaf "{cps=12}{i}Through the window!?{/i}"
            
            play sound "Audio/GenericDoorOpen.ogg"
            
            red closedeyes -surprisedeyebrows "Yeah, you know what, I can hear it now. I'll just go in."
            
        ">Jump out the damn window.":
            $ leafwindowjump = True
            
            red -angrybrow "Fat chance. I've never been inside of a women's bathroom for eighteen years and I'm not about to start now. {w=0.25}That goes against everything I stand for.{w=0.5} Besides, I've got a better idea."
            
            leaf surprised "You do? What?"

            red closedeyes frownmouth "Okay, we're on the second floor, right? And it's all grass on the ground outside."

            show leafintro_mad:
                alpha 0.0
                ease 0.5 alpha 1.0

            leaf ".{w=0.25}.{w=0.25}.{w=0.25}"

            red -closedeyes -frownmouth "I should be able to survive a two-story fall if I just go through the window."
            
            leaf angrysmilemouth angrybrow ".{w=0.25}.{w=0.25}.{w=0.25}"
            leaf "{cps=12}{i}Through the window!?{/i}"
            
            play sound "Audio/GenericDoorOpen.ogg"
            
            red closedeyes -surprisedeyebrows "Yeah, you know what, I can hear it now. I'll just go in."
else:
    menu:
        ">Get in the **** bathroom.":        
            red -angrybrow "Okay, I'll do it. But I'm covering my eyes while I'm in there."
            
            show leafintro_happy:
                alpha 0.0
                ease 0.5 alpha 1.0
            
            leaf happy "What a gentleman you are."

            pause 1.0
            
            leaf -happy "Now, not a peep from you while I'm gone."
            
            play sound "Audio/GenericDoorOpen.ogg"
            
            leaf flirt "Ladies first."
            
            red angrybrow "Ha. Ha."
            
        ">Don't get in the **** bathroom.":        
            red -angrybrow "Fat chance. I've never been inside of a women's bathroom for eighteen years and I'm not about to start now. {w=0.25}That goes against everything I stand for.{w=0.5} Besides, what if someone else is in there?{w=0.5} Then we'd really be in trouble."
            
            leaf angry "You got memory problems? I {i}just{/i} checked!"

            red surprisedeyes surprisedeyebrows talking2mouth "Yeah, but... someone could've come in since then. I mean, we've been watching the door, but there's windows on the inside."
            
            show leafintro_mad:
                alpha 0.0
                ease 0.5 alpha 1.0

            red "So someone could've, like... {cps=20}climbed up from outside, and... {cps=15}gone in there..."
            
            leaf ".{w=0.25}.{w=0.25}.{w=0.25}"
            leaf "{cps=12}{i}Through the window!?{/i}"
            
            play sound "Audio/GenericDoorOpen.ogg"
            
            red closedeyes -surprisedeyebrows "Yeah, you know what, I can hear it now. I'll just go in."
            
        ">Jump out the **** window.":
            $ leafwindowjump = True
            
            red -angrybrow "Fat chance. I've never been inside of a women's bathroom for eighteen years and I'm not about to start now. {w=0.25}That goes against everything I stand for.{w=0.5} Besides, I've got a better idea."
            
            leaf surprised "You do? What?"

            red closedeyes frownmouth "Okay, we're on the second floor, right? And it's all grass on the ground outside."

            show leafintro_mad:
                alpha 0.0
                ease 0.5 alpha 1.0

            leaf ".{w=0.25}.{w=0.25}.{w=0.25}"

            red -closedeyes -frownmouth "I should be able to survive a two-story fall if I just go through the window."
            
            leaf angrysmilemouth angrybrow ".{w=0.25}.{w=0.25}.{w=0.25}"
            leaf "{cps=12}{i}Through the window!?{/i}"
            
            play sound "Audio/GenericDoorOpen.ogg"
            
            red closedeyes -surprisedeyebrows "Yeah, you know what, I can hear it now. I'll just go in."

        
show bathroom_light with splitfadefast
$ renpy.pause(0.75, hard=True)

hide leafintro_A
hide leafintro_mad
hide leafintro_happy

red "Oh, yeah, shut the lights off, too. That's not creepy at all."

leaf angrysmilemouth angrybrow "Just be good and sit there. I'll be right back."

play sound "Audio/GenericDoorClose.ogg"
show bathroom_dark with splitfadefaster

red sadeyes sadeyebrows frownmouth "I really... didn't think this is what Kobukan was going to be like.{w=0.5} Shut up in the women's bathroom,{nw}"
play sound "Audio/fading_footsteps.ogg"
extend " and the girl who did it is running away."

pause 1.0

red thinking "I'll give her five minutes to come back, then I'm going through the window."

pause 1.0

play sound "Audio/GenericDoorOpen.ogg"
hide bathroom_dark with splitfadefast

leaf happy "Okay, come on out."

window hide
hide leaf
    
show hall_A2:
    xalign 0.0 xpos -480 ypos 1250 zoom 0.85
    ease 1.5 xpos -100 ypos 1100 zoom 0.7
    
hide bathroom_light with splitfade
$ renpy.pause(1.0, hard=True)

show leaf:
    alpha 0.0 xpos 0.5
    ease 0.75 alpha 1.0

red -thinking "That was fast. What'd you say to them?"
    
leaf happy "I just told them that I saw a shiny Eevee in the tall grass on the opposite side of the building. That should keep them busy for a while."
red surprised "That's almost cruel! Even if I was ninety-nine percent sure that you were lying, I'd have to take that chance."
leaf flirtbrow "I've never seen a group of people turn heel and run so fast before.{w=0.5}{nw}" 
leaf sad "I've never seen a group of people turn heel and run so fast before.{fast} I'll admit, I felt a bit guilty, too."
red thinking ".{w=0.25}.{w=0.25}."
leaf -sad "Okay, over it. {w=0.25}Now, before I forget, {w=0.25}here, I took one of brochures they dropped."

show leaf at getcloser

pause 1.0
    
leaf happy "If I recall, you really need it."

red -thinking "Thanks, I guess. I'm not sure any of that really needed to be done, but you did it... {w=0.5}{nw}"
red sadeyebrows sadeyes "Thanks, I guess. I'm not sure any of that really needed to be done, but you did it... {fast}well...?"

leaf angrysmilemouth flirtbrow "You'd be a lot cuter if you'd ended that sentence after 'thanks.'"
red "I'll keep that in mind the next time a girl shoves me into the women's bathroom to preserve her reputation from high-school level rumors."

show leaf at getfurther

leaf closedbrow happymouth "You'll thank me. Trust me, I know {i}all{/i} about navigating social intrigue." 
leaf frownmouth "But you know, despite everything that happened, it was...{w=0.6} kind of.{w=0.25}.{w=0.25}."

$ renpy.pause(2.0, hard=True)

leaf sadbrow blush -frownmouth "...a lot of fun.{w=0.5} Probably the most fun I've had in a while."
leaf happy "Let's do this again sometime!"

red closedeyes frownmouth "I'm going to do my best to avoid that, but if I can't...{w=0.5}{nw}"
red happy "I'm going to do my best to avoid that, but if I can't...{fast} sure."

show leaf happy:
    alpha 1.0 xpos 0.5 zoom 1.0 ypos 1.0
    parallel:
        ease 1.5 xpos 1.0 zoom 1.35 ypos 1.5
    parallel:
        pause 0.5
        ease 1.0 alpha 0.0
    
show hall_A2:
    xalign 0.0 xpos -100 ypos 1100 zoom 0.7
    ease 2.0 xpos -220 ypos 1100 zoom 0.7

pause 2.0

red -happy "...She seemed nice."

window hide
$ renpy.pause(1.5, hard=True)

redmind "Oh. I forgot to ask her name."

hide leaf
hide leafintro_A

window hide
stop music fadeout 2.5

scene blank2 with Dissolve(1.5)
$ renpy.pause(1.5, hard=True)

queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

show dorm_empty_A with Dissolve(1.0):
    zoom 1.0 xpos 0 ypos 0 xanchor 0 yanchor 0
    ease 4.0 zoom 1.18 xpos -170 ypos -180

play sound "Audio/Door_Open1.mp3"

red "Huh. So this is my room."

pause 1.0

red "For the next year..."

pause 1.0

red surprised "Hm, wasn't this meant to be a suite? I don't see anyone else's stuff here, though, even though there are four more beds."

$ renpy.music.set_volume(0.0, delay=0.5, channel="music")

play sound "Audio/Chime.mp3"

"Roxanne's Voice" "{color=#e70000}Attention, new students. The time is now 2:00 p.m. There will be an orientation taking place in the auditorium of Relic Hall starting in one hour. All new students are advised to attend.{/color}"

$ renpy.music.set_volume(1.0, delay=1.5, channel="music")

red thinking "Maybe I'm just the first of my dormmates to get here? They're cutting it a bit close, though."

play sound "Audio/Door_Open1.mp3"
pause 1.0

show dorm_empty_A:
    zoom 1.18 xpos -170 ypos -180 xanchor 0 yanchor 0
    ease 0.4 zoom 1.0 xpos 0 ypos 0

"{color=#c1861e}Young Voice" "\"{size=20}...cutting {/size}{size=22}it {/size}{size=24}a bit {/size}{size=26}close, {/size}though.\""

show ethan with dis:
    xpos 1.5
    ease 1.0 xpos 0.5

show red happy at Transform(xpos=0.08, yanchor=0.35)
show ethan happybrow talkingmouth with dis
"{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}" "\"Oh, hey!\""

show ethan surprised -talkingmouth with dis
show red surprised with dis
red "..."
ethan "..."

show red -surprised with dis
show ethan talkingmouth -surprised with dis
"{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}" "\"Do you want to talk first?\""

show ethan happybrow talkingmouth with dis
show red happy with dis
"{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}" "\"Hey, sorry about this, it's so weird.\""

show ethan angrybrow frownmouth with dis
show red angrybrow frownmouth with dis
"{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}" "\"Here, go ahead.\""

show ethan surprised with dis
show red -angrybrow surprised with dis
"{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}" "\"...\""

show ethan angrybrow surprisedmouth with dis
show red angrybrow with dis
"{color=#cf0000}[first_name]{/color} & {color=#c1861e}???{/color}" "\"Oogabooga!\""

pause 1.0

hide red at Transform(xpos=0.08, yanchor=0.35) with dis

pause 1.0

hide red

ethan happy "Ethan."

red thinking "Oh, thank god, we broke the curse. Who's Ethan?"

$ BecomeNamed("Ethan")

ethan -happy "I am. Looks like I'm one of your dormmates, too."

red -thinking "Cool. Nice to meet you. My name's [first_name] [last_name]."

ethan talkingmouth "So, hey, what's your story?"

red "Well, I'm from Pallet Town in Kanto. {w=0.5}...That's pretty much it."

ethan talking2mouth "Pallet? Oh, I know that place! That's where Professor Oak lives, right? I went to his lab once on a field trip. I'm from New Bark Town in Johto."

red surprised "...Sorry, Professor Oak? You mean Old Man Oak?"

ethan thinking "You're kidding, right? Yeah, sure, maybe he's a bit old, but he's a world-famous Pokémon researcher. He's a bit more than 'Old Man Oak.'"

red "Huh."
red -surprised "To me, he was just my neighbor."

ethan "Wow, you lived next to him? Wait..."
ethan surprised "Shit, I remember you! You nearly ran our teacher over while we were walking through the center of town! You were carrying a fat Pikachu, right?"
red happy "I don't remember that, but that sounds like me, alright!"

ethan "Huh. Small world."

show ethan -surprised with dis
red -happy "Looks like we arrived at pretty much the same time. You want to grab these two beds? We can unpack our stuff now."
ethan thinking "Sure! Wondering who the other three'll be, though."
red thinking "Hopefully, we don't go through the whole talking-at-the-same-time routine with the other three as well."
red happy "With all five of us talking at once, we'd blow the ears out of a Loudred."
ethan happy "Haha, yeah."
pause 1.0
ethan sadbrow happymouth "A what?"
show ethan surprised with dis
red "Oh, it's a Pokémon from Hoenn. Normal-type. Has two big ears that can both recieve and emit sound. Most of them are completely immune to sound-based attacks."
ethan "Dude... you just know that?"
red sadeyes sadeyebrows "Well... yeah. I've studied a bit."
ethan happy "Pretty impressive, [first_name]. I think I know who I'm going to want to have as a study partner."
red happy "Well, let's handle that after we finish setting up our room."

play sound "Audio/Door_Open1.mp3"

show ethan surprised with dis

pause 1.0

show calem with dis:
    xpos 1.5
    ease 1.0 xpos 0.66

show ethan: 
    xpos 0.5
    ease 1.0 xpos 0.33

calem "Yes, this looks like the right spot."

$ BecomeNamed("Calem")
calem talking2mouth "The name's Calem. What's yours?"

ethan happy "Hey, Calem! I'm Ethan, and this guy here is [first_name]."

red "Nice to meet you!"

calem happymouth "Likewise. Getting to my dorm was one of my top priorities, but it looks like I was a bit late."

ethan -happy "Don't worry about it, [first_name] and I were just about to unpack."
ethan talking2mouth "Hey, is that a Kalosian accent?"

calem closedbrow talkingmouth "Yes, that's right. I'm from Vaniville town, in the southeast of Kalos."
ethan happy "Man, you probably get mad luck with the ladies, then! I know they go crazy for a sexy Kalosian accent."
show ethan surprised with dis
calem angrybrow talking2mouth "It's a curse. I can't step outside without drowning in the amount of panties that are spontaneously ripped off in my presence."

pause 1.0

ethan "Dude. You serious...?"
show ethan -surprised with dis
calem closedbrow smilemouth "Who can say?"

pause 1.0

red "Well, do you have any preferences where you bed down?"

calem -closedbrow talking2mouth "I prefer not to sleep too close to any other men. I'll take that fifth bed off to the side."

ethan "Cool. Let's just get our stuff unpacked, then--"

play sound "Audio/Door_Open1.mp3"

ethan angrybrow surprisedmouth "Oh, what now!?"
show ethan surprised with dis
show calem surprised with dis

show hilbert with dis:
    xpos 1.5
    ease 1.0 xpos 0.75

show calem:
    xpos 0.66
    ease 1.0 xpos 0.5

show ethan: 
    xpos 0.33
    ease 1.0 xpos 0.25

pause 2.0

hilbert angrybrow "Well? What are you staring for?"

calem closedbrow talking2mouth "I'm assuming by the way you walked in here you're one of our dormmates, yes? Your first priority, then, should be giving us your name."

ethan happy "Yeah, I'm Ethan, this guy's [first_name], and this dude's Karen!"

calem "{size=30}Calem, actually.{/size}"

show calem angry with dis
show ethan angry with dis
hilbert sadbrow talkingmouth "...I don't remember asking. And I definitely don't care."

show hilbert:
    xpos 0.75
    linear 1.0 xpos 0.375

pause 1.0

show dorm_empty_A at vpunch

show calem surprised with dis
show ethan surprised with dis
show hilbert angrybrow with dis
red angry "Tell us your name, or we're calling you 'Edgelord' for the next year."

pause 1.0 

hilbert "..."

red frownmouth "..."

"{color=#353535}Edgelord" "\"...\""

red "..."

$ BecomeNamed("Hilbert")

hilbert "...Hilbert."
hilbert "And I'm taking the bed over there."

show hilbert:
    xpos 0.375
    ease 1.0 xpos -0.5

pause 1.0

calem closedbrow talkingmouth "{size=30}That was going to be my bed... {/size}Well, whatever. Nicely handled, [first_name]."
ethan happy "Yeah, that was pretty cool!"
ethan sad "...I guess we're spending the next year with Hindenburg, then, huh..."
calem closedbrow talking2mouth "{size=30}Pretty sure it was 'Hilbert.'{/size}"
calem -closedbrow "Anyway, with a school as prestigious as this, I can understand if someone isn't in a particular mood to forge friendships."
calem angry "The competitive nature of our environment is absolutely no excuse for poor manners, though."
red "Yeah, he reminds me of this guy I met this morning. Although I think that guy was just very awkward."
ethan happy "Right? It's like, okay dude, we get that you were the toughest guy in your high school. You can chill out."
red -frownmouth -angrybrow "Well, hopefully whoever our last dormmate is is... not like that."

pause 1.0

play sound "Audio/Door_Open1.mp3"

pause 1.0

calem surprisedbrow "{i}En parlant du loup...{/i}"
ethan happy "You said it, Karen!"
show calem angrybrow with dis

pause 1.0

calem happybrow "Calem, Ethan. It's Calem."

show brendan happy with dis:
    xpos 1.5
    ease 1.0 xpos 0.75

brendan "Hey, dudes!"
$ BecomeNamed("Brendan")
brendan -happy "Brendan's the name and Pokémon's my game! What's goin' on?"
show calem angry with dis
ethan happy "Now that's more like it! Hey, Brendan! I'm Ethan, this guy's [first_name], Mr. Sexy Accent is Karen, and short, dark and brooding over there is Hildegard."

pause 2.0

calem angry "Why do we continually allow Ethan to introduce us? And why does he only get your name right?"
red "Yeah, uh, this guy's Calem, and that guy's Hilbert. Nice to meet ya, Brendan!"

show brendan at getcloser, rightside

show ethan surprised with dis
show calem surprised with dis
brendan surprised "Bro! You and I, we're kindred spirits. I can tell!"
red surprisedeyes talking2mouth "Oh yeah...?"
brendan happy "Your thighs, man! They're hella toned. You run a lot, right?"
show calem closedbrow smilemouth with dis
show ethan -surprised with dis
red happy "Oh. Uh, yeah. All the time, actually. Once a day, if I can."

show brendan at getfurther, rightside

brendan -happy talking2mouth "Sick. You and I, we'll run together, then. You can make sure I don't skip leg day."
red -happy "That's quite a responsibility, but I'll do what I can."
ethan happymouth "Guys, you see what this means? All five of us are here now! The five roomates that'll spend the next year together! Isn't that incredible?"
calem happybrow "It certainly does seem like the start of something rather excellent. I look forward to learning about, and perhaps even befriending, all of you."
brendan happy "Likewise, guys! Hey, if any of you need any help with anything, or you want to work out, you just let me know. Brendan's here for friendin'!"
show brendan angry with dis
show calem closedbrow sadmouth with dis
show ethan angry with dis

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.8

show hilbert sad with dis:
    xpos -0.5
    ease 1.0 xpos 0.2

show calem:
    xpos 0.5
    ease 1.0 xpos 0.6

show ethan: 
    xpos 0.25
    ease 1.0 xpos 0.4

stop music fadeout 1.0

hilbert "...Pathetic."

$ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

ethan "What the hell's your problem, man?"
hilbert angrybrow talkingmouth "You're all talking about friendship and camaraderie, and {i}working together{/i}. Don't you realize what this school is going to put you through?"
calem "Whatever it puts us through, handling it with allies is certainly a better strategy than going it alone."
hilbert sad "You have to go it alone. You, red. You know what I'm talking about. Explain it to them."
red angrybrow frownmouth "..."
ethan surprised "Wait, [first_name]? Do you know what he's talking about?"
red -angrybrow sadeyes talking2mouth "...Kobukan Academy has an enforced 80 percent graduation rate. The students in the bottom 20 percent aren't permitted to graduate. You're allowed to try again, but..."
show brendan surprised with dis
red closedeyes "...But you aren't eligibile for financial aid if you ever failed to graduate, so in practice, if you don't graduate once, you never will, unless you're ridiculously wealthy."
calem "This is possible only due to Kobukan's unique one-year curriculum. If Kobukan were a standard three-year program, then students would spend far more time and money before being told they're not permitted to graduate."
show ethan sad with dis
show calem sad with dis
show brendan sad with dis

pause 2.0

hilbert angrybrow talkingmouth "See what I'm saying? One out of every five students won't graduate. There's five of us here."
hilbert angrymouth "Do the math."

show hilbert:
    ease 1.0 xpos 1.5

pause 1.0

play sound "Audio/Door_Slam.mp3"

show calem -sad with dis
show brendan -sad with dis
ethan happy "W-well, uh, let's all do so well that Himbo's the one who gets kicked out instead of any of us!"
red happy "That's the spirit, Ethan!"
ethan "Yeah!"
ethan "..."
ethan sadbrow "Okay, I'll be real with you guys, I {i}did not know{/i} that, and I'm kinda freaking out about it."
calem talkingmouth "We should certainly be aware of our odds, but there is little a clear mind and a defined set of priorities cannot solve."
brendan angrybrow happymouth "Yeah! I didn't sign all those papers and do all those tests just to get scared off by previous years' stats! Heck, maybe we'll be so good that this year, they'll decide to bin the 80 percent acceptance rate thing!"
red happy "Heck yeah. Don't worry. I may have just met you, Ethan, but I bet that you'll graduate just as easily as any of us. And near the end of the year, when Hilbert begs us to help him study, maybe we'll be gracious and say yes."

stop music fadeout 1.0

ethan "Alright..."

queue music "Audio/Music/SoaringIllusions_Intro.ogg" noloop
queue music "Audio/Music/SoaringIllusions.ogg"

ethan happy "Alright! I'm not giving up yet! Not before things have even begun!"
show calem happy with dis
show brendan happy with dis
red "Right on."
$ renpy.music.set_volume(0.3, delay=3.0, channel="music")

pause 3.0
redmind thinking "I knew those stats before, but... even though I somehow got in, I'm still in the bottom tenth percentile."
redmind "If I want to make it through the year, I'm going to need to work harder than I ever have before..."
redmind happy "But that's fine! I'm going to be a Champion someday, and I always knew I'd have to work insanely hard to make that happen. Might as well start now!"

$ renpy.music.set_volume(1.0, delay=1.0, channel="music")

show ethan -happy with dis
show brendan -happy with dis
calem closedbrow "I originally planned on unpacking before the orientation, but we're running a bit short on time. Perhaps we should attend orientation, then come back?"
ethan "Sure, sounds like a plan."

stop music fadeout 1.0
$ renpy.pause(1.25, hard=True)

queue music "Audio/Music/Kalos_Start.ogg" noloop
queue music "Audio/Music/Kalos_Loop.ogg"

scene orientation with dissolve
$ renpy.pause(1.0, hard=True)

$ renpy.music.play("Audio/school_crowd.ogg", channel='crowd', loop=True, fadein=1.0)

red surprised "Wow. It's impressive how many students are crammed in here."

show calem closedbrow with dis

calem closedbrow "One has to wonder how many students this school would have if it were a standard three-year academy. Seems as though it has its hands full, as-is."

red -surprised "You don't seem fazed."
calem -closedbrow talking2mouth "I do my best not to. I assure you, though, I'm quite impressed. But I have spent quite some time in Lumiose City, which exceeds even Inspira in size."

pause 1.0

show brendan sad at rightside with dis

brendan "Huh... I don't see her."

show ethan happy at leftside with dis

ethan "Who ya looking for, Brendan?"
calem angry "{size=30}What, you got his name right?{/size}"
brendan "My girlfriend. She said she'd meet up with me during orientation."
show calem surprised with dis
ethan surprised "Damn, dude! You have a girlfriend here already!?"
brendan happy "Oh, nah, dude, you got it wrong. She's my friend from childhood. We enrolled here together."
show calem closedbrow smilemouth with dis
ethan -surprised "Ohhhhh, okay. I was going to say, man, that's scary fast."
brendan -happy -sweat "Hah, it would be, wouldn't it? {w=0.5}{nw}"
brendan happy "Hah, it would be, wouldn't it? {fast}Oh, wait, there she is!"

show calem:
    xpos 0.5
    ease 1.0 xpos 0.8

show ethan:
    xpos 0.25
    ease 1.0 xpos 0.6

show brendan:
    xpos 0.75
    ease 1.0 xpos 0.4

show may happy:
    xpos -0.5 alpha 0.0
    ease 1.0 xpos 0.2 alpha 1.0

may "Hey, sweetheart!"

show ethan at getcloser:
    xpos 0.6

ethan surprised "{size=30}Holy shit, she's so cute!{/size}"
red angrybrow frownmouth "{size=30}Yeah, and she's our roommate's girlfriend, so keep it in your pants.{/size}"
ethan sad "{size=30}Er... of course, hah hah...{/size}"

show ethan at getfurther:
    xpos 0.6

$ BecomeNamed("May")
brendan "Guys, this is May. We grew up in Littleroot Town together."
ethan -sad "Oh, I know that place. That's where Professor Birch lives. Hoenn, right?"
may happy "Oh, you know about it? Yep, that's right!"
brendan @surprisedbrow "Huh, you know about May's old man?"
ethan @surprised "Old man...? Wait, you mean...!"
may -happy sadbrow "Yep! May Birch is my full name."
ethan thinking "Huh. [first_name] knows Professor Oak, Brendan knows Professor Birch, I know Professor Elm..."
calem thinking "...It might be worth mentioning that I worked as Professor Sycamore's intern for a couple years."
ethan surprised "What the heck...?{w=0.5} So we all, except for Hickey, have a personal connection with a prominent Professor from our region?"
show ethan -surprised with dis
brendan closedbrow talkingmouth "I mean, we don't know whether he does or not. Probably wouldn't tell us, anyway."
may sadbrow talkingmouth "What're you talking about?"
calem thinking "..."
brendan -closedbrow -talking2mouth "I wonder if...{w=0.5} nah, it's nothing."
brendan @talkingmouth "Anyway, babe, how's your suite? You got some dudes as cool as the guys I ended up with?"
may angrybrow happymouth "Well, they're a bit less dude-ish, but yeah, I think they're some pretty cool people!"
calem @talkingmouth "I would have preferred if we could pick our roommates directly, but at least things largely seemed to turn out well."
may -angrybrow happy "Oh, I just love the randomness of it! Even if we could pick, I would've gone random, just to see who I ended up with."
brendan happy "Yeah, May always loved leaving things up to chance! Heck, the first time I asked her out, she decided whether or not to accept on a coinflip!"
may sadbrow frownmouth "...I wouldn't mind if you stopped telling people that..."
calem surprised "!"
show may -sadbrow -frownmouth with dis
calem thinking "Oh, look up at the stage. I believe the speaker's about to start. We should find some seats."
redmind thinking "Hm. He saw that moment of awkwardness and immediately changed the subject. Pretty slick."
ethan "Yeah, let's go."

stop music

play sound "Audio/Mic_Feedback.mp3"
$ renpy.music.stop(channel='crowd', fadeout=0.5)

show orientation:
    parallel:
        xalign 0.0
        ease 0.02 xpos -30
        ease 0.02 xpos 30
        ease 0.02 xpos 0
        repeat 40
    parallel:
        yalign 0.0
        ease 0.02 ypos -15
        ease 0.02 ypos 15
        ease 0.02 ypos 0
        repeat 40

show calem surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.8
        ease 0.02 xpos 0.85
        ease 0.02 xpos 0.75
        ease 0.02 xpos 0.8
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40
    
show brendan surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.4
        ease 0.02 xpos 0.45
        ease 0.02 xpos 0.35
        ease 0.02 xpos 0.4
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show may surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.2
        ease 0.02 xpos 0.25
        ease 0.02 xpos 0.15
        ease 0.02 xpos 0.2
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show ethan surprisedmouth deadbrow at monochrome:
    parallel:
        xpos 0.6
        ease 0.02 xpos 0.65
        ease 0.02 xpos 0.55
        ease 0.02 xpos 0.6
        repeat 40
    parallel:
        yalign -0.11
        ease 0.02 ypos 25
        ease 0.02 ypos -25
        ease 0.02 ypos 0
        repeat 40

show red:
    xpos -0.5

red "{cps=0}Oh, GOD. {size=44}WHY?{w=0.5} HOLY CRAP.{/size}{/cps} This noise! {cps=120}It's like a thousand Pokémon got together and used Screech and Supersonic at the same time!{w=0.5} I can't tell if I'm screaming from the pain or if it's still the feedback!{/cps}"

window hide

show calem at monochrome:
    xpos 0.8 ypos 1.0
    ease 0.5 xpos 0.78 ypos 1.1 rotate -10.0
show ethan at monochrome:
    xpos 0.6 ypos 1.0
    ease 0.5 xpos 0.62 ypos 1.1 rotate 10.0
show brendan at monochrome:
    xpos 0.4 ypos 1.0
    ease 0.5 xpos 0.38 ypos 1.1 rotate -10.0
show may at monochrome:
    xpos 0.2 ypos 1.0
    ease 0.5 xpos 0.22 ypos 1.1 rotate 10.0
$ renpy.pause(0.5, hard=True)
show calem at monochrome:
    xpos 0.78 ypos 1.1 rotate -10.0
    ease 0.5 xpos 0.8 ypos 1.2 rotate 10.0
show ethan at monochrome:
    xpos 0.62 ypos 1.1 rotate 10.0
    ease 0.5 xpos 0.6 ypos 1.2 rotate -10.0
show brendan at monochrome:
    xpos 0.38 ypos 1.1 rotate -10.0
    ease 0.5 xpos 0.4 ypos 1.2 rotate 10.0
show may at monochrome:
    xpos 0.22 ypos 1.1 rotate 10.0
    ease 0.5 xpos 0.2 ypos 1.2 rotate -10.0
$ renpy.pause(1.0, hard=True)
hide calem
hide ethan
hide brendan
hide may
with moveoutbottom
show orientation at vpunch

hide red
play sound "Audio/Thud2.ogg"
play sound "Audio/Thud.ogg"
$ renpy.pause(0.5, hard=True)

play sound "Audio/Complaining.ogg"
    
red angrybrow surprisedmouth "What kind of terrible speaker makes a sound like that!?"

play sound "Audio/Mic_Feedback2.mp3"

roxanne @angry "--telling you this stupid thing won't work!"    
roxanne @surprised ".{w=0.25}.{w=0.25}.{w=0.5}{nw}"

queue music "Audio/Music/Kalos_Start.ogg" noloop
queue music "Audio/Music/Kalos_Loop.ogg"

roxanne @happy "...{fast}Oh, there we go!"

redmind -angrybrow thinking "I don't think she's aware half the people in this room are still brain dead on the floor after that uproar..."
redmind "If my ears had eyes, they'd be crying."
    
mace "What was that!?{w=0.5} Some kind of hazing ritual!?"
face "Please, no more!"
    
show flannery furious veins:
    xpos 0.5 ypos 1.6
    ease 0.25 xpos 0.5 ypos 1.0

show whitney surprisedbrow sadmouth:
    xpos 0.75 ypos 1.6 rotate -15.0
    pause 0.75
    ease 0.25 xpos 0.65 ypos 1.0 rotate -15.0

flannery "{size=45}I'LL KILL YOU!{/size}{w=0.75}{nw}"

$ BecomeNamed("Flannery")

whitney "Flannery!{nw}"

show flannery angry:
    subpixel True
    xpos 0.5
    ease 0.5 xpos 0.4

show whitney:
    subpixel True
    xpos 0.65 rotate -15.0
    ease 0.5 xpos 0.55 rotate -15.0
    
extend " Not here!{w=1.5}{nw}"

show flannery:
    subpixel True
    xpos 0.4
    ease 0.7 xpos 0.3
        
show whitney thinking:
    subpixel True
    xpos 0.55 rotate -15.0
    ease 0.7 xpos 0.45 rotate -15.0

whitney "Unf!{w=1.0}{nw}"

show flannery:
    subpixel True
    xpos 0.3
    ease 0.5 xpos 0.2
        
show whitney surprisedbrow sadmouth:
    subpixel True
    xpos 0.45 rotate -15.0
    ease 0.5 xpos 0.35 rotate -15.0
    
whitney "You need to lay off the Lava Cookies, girl!"

show flannery:
    subpixel True
    xpos 0.2 
    ease 0.8 xpos -0.3
        
show whitney thinking:
    subpixel True
    xpos 0.35 rotate -15.0
    ease 0.8 xpos -0.15 rotate -15.0
        
show hilbert:
    alpha 0.0 xpos 1540
    ease 0.5 xpos 1540 alpha 1.0
    
pause 0.5

hide flannery
hide whitney

hilbert ".{w=0.25}.{w=0.25}.{w=0.6}{nw}"

show hilbert angry

extend "Try that again."

hide hilbert angry
with moveoutright

show sabrina:
    xpos 0.5 ypos 1.8
    ease 1.5 xpos 0.75 ypos 1.0

pause 2.5 

sabrina neutralpowered poweredbrow ".{w=0.25}.{w=0.25}."

show sabrina neutralpowered poweredbrow:
    xpos 0.75 alpha 1.0
    ease 1.5 xpos 1.5 alpha 0.0

$ renpy.pause(1.75, hard=True)

show orientation
with vpunch

hide sabrina

roxanne @angry "{size=44}Come on now, we're on a schedule! GET MOVING!{/size}"

red "Eeesh. I only met Roxanne for a moment, but I'm not exactly... endeared by her, right now."

show ethan sad:
    ypos 2.0 xpos 0.5 rotate 10.0
    ease 2.0 ypos 1.2 xpos 0.75 rotate 10.0

pause 1.0

ethan "Who's... Roxanne?"

show roxie_orientation behind ethan with dis

pause 1.0

red "The one on the microphone up there."

show ethan closedbrow sadmouth:
    ypos 1.2 xpos 0.75 rotate 10.0
    ease 2.0 ypos 2.0 xpos 0.75 rotate 0.0

ethan "Ohhhhh..."

window hide

show calem thinking:
    ypos 2.0 xpos 0.65
    ease 2.0 ypos 1.2 xpos 0.65

calem "There are better places to take a nap than on the ground, you know."

hide ethan

calem "Here, grab my hand."

show calem:
    ypos 1.2 xpos 0.65 rotate 0.0
    ease 1.0 ypos 1.4 xpos 0.65 rotate 10.0
    pause 1.0
    ease 1.0 ypos 1.0 xpos 0.65 rotate 0.0

show ethan:
    ypos 2.0 xpos 0.75 rotate 10.0
    pause 2.0
    ease 1.0 ypos 1.0 xpos 0.75 rotate 0.0

pause 3.0

ethan happy "Thanks, Kallen!"
calem closedbrow smilemouth "Well, it's closer than Karen."
calem surprised ".{w=0.25}.{w=0.25}.{w=0.25}{nw}"

pause 1.0

show calem:
    xpos 0.65
    ease 0.25 xpos 0.25

calem -surprised "...Personal space, please."
ethan surprised "Huh? Oh, uh, sure."

show brendan angry:
    xpos 0.5 ypos 2.0
    ease 0.25 xpos 0.6 ypos 1.0

show may angry:
    xpos 0.5 ypos 2.0
    ease 1.0 xpos 0.4 ypos 1.0

brendan "What's the big idea, blowing a guy's ears out like that!"
may "Seriously! Just to get our attention? She's louder than a Loudred!"
ethan happy "Hey, I know what that is!"
calem surprised "..."
calem thinking "Good for you."

show roxie_orientation:
    zoom 1.0 xpos 0 ypos 0 xanchor 0 yanchor 0
    ease 5.0 zoom 1.1 xpos -80 ypos 0

stop music fadeout 1.5
    
$ renpy.music.play("Audio/Music/Hoenn_Start.ogg", channel='music', loop=None, fadein=1.5, tight=None)
$ renpy.music.queue("Audio/Music/Hoenn_Loop.ogg", channel='music', loop=True, tight=None)

roxanne @happy "Good evening, our new friends!{w=4.0}{nw}"

show roxspeech with Dissolve(2.0):
    subpixel True
    zoom 1.25 xalign 0.5
    ease 40.0 zoom 1.0

roxanne uniform @talkingmouth "I am Roxanne, and to start I would like to thank the academy staff here for allowing the council to hold this special event."
roxanne @closedbrow talkingmouth "I hope you will all make the most out of this occasion and grant me the opportunity to officially welcome every one of you to this prestigious establishment."
roxanne @happy "Everyone...{w=0.5} welcome to the Kobukan Academy of Advanced Pokémon Arts & Sciences."
roxanne @teachingmouth "While we are calling this event an orientation, I'd like to ask for your patience in this initial assembly before you all return to socializing or attending your personal agendas."

red thinking "It's coming.{w=0.5} This is gonna be one of those long, insomnia-curing speeches."

roxanne @talkingmouth"For the first thing I'd like to mention, I hope you've all managed to reserve your own suites in one of the three student residential halls."
roxanne @talking2mouth "The one here is {color=#0048ff}Relic Hall{/color} and the other two, {color=#0048ff}Pledge Hall{/color} and {color=#0048ff}Aura Hall,{/color} are located east and west, respectively, from this location."
roxanne @teachingmouth "Another important item to cover is class scheduling."
roxanne @angrybrow talkingmouth "All of you here will follow a preset class schedule of six periods per day.{w=0.5} Pay close attention, because you'll be doing this for the next year."
hide roxie_orientation
hide calem
hide ethan
hide may
hide brendan

red "This is it."

calem happy "I'm taking notes."
    
roxanne @closedbrow talkingmouth "{color=#0048ff}The first period of each day is homeroom,{/color} lasting two hours. Core subjects will be covered here by your professor."

brendan surprised "Two hours!?"
calem thinking "I know. Two hours is hardly enough time to cover all the material."
may sad "Especially since we only have a year..."
ethan surprised "Uh, that's not what he was implying, guys."
red happy "I spent two hours in Mt. Moon with no repels once. Can't be any worse than that."
ethan angry "Oh, god, Zubat everywhere, right? You know, they're an invasive species--Kanto has a lot to answer for, for letting them cross the border and mess up Johto like they have."
red -happy "What're we supposed to do, shoot them down?"

roxanne "{color=#0048ff}Following homeroom will be an hour of one Pokémon type elective{/color} of your choice.{w=0.5} You'll be able to select {color=#0048ff}{i}two{/i} out of the eighteen known Pokémon types{/color} to focus your studies on for each individual day."

ethan surprised "Whoa, hold up."
ethan "Are we specializing in two Pokémon types?{w=0.5} Only two out of eighteen?"
calem -thinking "Not quite. You can certainly take only the same two electives every day, if you wish, but you're permitted to switch between electives at will."
brendan surprised "Huh!? How does that work?"
calem @talkingmouth "Due to the high teacher-to-student ratio Kobukan boasts, instructors are able to adjust the curriculum to be appropriate to any student's level, even if they've never taken that class before."
red @talkingmouth "That's another advantage of Kobukan's unique one-year program. We have to work three times as hard, and three times as fast, as other schools, but students can customize their education."
redmind thinking "I know a lot of Kobukan students, especially the ones that went on to excel, focused on two to three electives. Mastering all eighteen types in one year just doesn't seem feasible."
redmind "Even an amazing student could probably only handle {color=#0048ff}six{/color} electives."

show roxspeech:
    ease 0.75 zoom 1.0

roxanne @talkingmouth "In addition to your elective classes, you will each also have a period of gym and lunch."
roxanne @closedbrow teachingmouth "Your last class will end at 3 p.m."
roxanne @talkingmouth "After that, those of you taking part in research or extracurricular activities are free to use our campus buildings, which close at 6 p.m. sharp."
roxanne @happymouth "We'll be implementing a strict curfew this year, so any individuals who are seen outside their dorms after 8 p.m. are subject to severe disciplinary action."

show roxspeech:
    zoom 1.0

red "8 p.m.?{w=0.5} That's--"

show roxspeechmad:
    alpha 0.0 zoom 1.0 xalign 0.5
    ease 0.33 alpha 1.0

brawly uniform @surprised "That's so early! This wasn't on the morning memo!{w=0.3} How am I supposed to do my nightly runs now?"

roxanne @angrybrow talking2mouth "{i}Ahem{/i}... And don't think you can just sneak out, too!{w=0.5} There are security cameras on every floor in every building."
roxanne @closedbrow frownmouth "Unless you have a special notice from a staff member, there will be no exceptions to--"

brawly @angrybrow talking2mouth "Hey, did you know about this curfew thing?"

falkner uniform @talkingmouth "Yes."

brawly @sad "Wha--{w=0.25} Why does everyone know except me!?"

roxanne @angry "Will you {i}shut up!?{/i} We're in the middle of an assembly right now!"
roxanne @closedbrow angrymouth "It's your own fault you didn't show up to the meeting when we discussed this! Maybe now you'll start taking your job more seriously!"

redmind sad "Oh, poor Brawly. To get tongue-lashed like this in front of the entire auditorium..."

falkner @closedbrow talkingmouth "Roxanne. Your speech."

roxanne @angrybrow talking2mouth "When this is over, we're going to have a little talk, you and I!"
    
show roxspeechmad:
    alpha 1.0
    ease 0.33 alpha 0.0

roxanne @closedbrow frownmouth "{i}Ahem{/i}... Where was I?"
roxanne @happy "Oh, yes. As I was saying, it is a privilege to be a part of this great school we call Kobukan Academy.{w=0.4} Now is the opportunity of a lifetime to open a new door!"

calem surprised "She switched gears that easily?{w=0.5} That's formidable."

roxanne @talkingmouth "Only by working together can we realize our goals and foster our talents.{w=0.5} But in the end, it will be up to you to find your own path and seize the day with your own hands!"

play sound "Audio/Big Applause.ogg"

roxanne @happy "And with that, I formally welcome you to Kobukan Academy!"

window hide

hide roxspeedmad

show roxspeech:
    alpha 1.0
    ease 2.0 alpha 0.0

show orientation:
    zoom 1.1 xpos -80 ypos 0 xanchor 0 yanchor 0
    ease 4.0 zoom 1.0 xpos 0 ypos 0   

$ renpy.pause(2.5, hard=True)

roxanne @closedbrow teachingmouth "Have a great rest of the day, everyone. And don't forget to get those signups done!"

show brendan happy:
    alpha 0.0 xpos 0.2
    ease 0.5 alpha 1.0

show may happy:
    alpha 0.0 xpos 0.4
    ease 0.5 alpha 1.0

show ethan happy:
    alpha 0.0 xpos 0.6
    ease 0.5 alpha 1.0

show calem happy:
    alpha 0.0 xpos 0.8
    ease 0.5 alpha 1.0
    
$ renpy.pause(0.5, hard=True)

show brendan -happy with dis
show may -happy with dis
show ethan -happy with dis
show calem -happy with dis

calem "Well, what did you think, everyone?"

brendan "About what? The speech?"

calem @thinking "Well, I guess that's something, too."
calem talkingmouth "But I'm more focused on the class scheduling part."
calem "We're completely set on the room situation so there's nothing left for us to do there."

calem talking2mouth "It'll be tough picking two type electives out of eighteen. {color=#0048ff}And we'll have different instructors and classmates depending on the types we choose...{/color}"
calem -talking2mouth "Even though we have the freedom to swap between electives at any time, many students will choose instead to focus on two or three types for the entire year."
redmind "That might work for other students, but if I want to become a Champion, {color=#0048ff}I should probably swap between electives depending on what kind of Pokémon I'm trying to raise.{/color}"
calem thinking "A large decision awaits us when we come back to our room, I believe. Handling that should be our first priority."
brendan happy "Great!"
brendan "I'll tell you what, [first_name], I'm gonna pick the same electives as you!"
brendan "Then we'll be class buddies, too! It'll be great!"
red surprisedeyes surprisedeyebrows sadmouth "I.{w=0.25}.{w=0.25}."
may happy "Imagine if you two also get the same homeroom teacher?{w=0.5} Then you guys'll look like a couple!"
red thinking "I'm not sure how I should feel about that."
brendan -happy "Aw, jokes, dude! I'm just messin'."
brendan "I haven't decided on which two electives yet, so if I do end up pickin' the same ones as you, it's totally by chance!"
may -happy "I know one of my choices will be Fire, so if you also decide to choose Fire, you'll have at least one familiar face there."
red "I think I'll probably swap between electives."
show may surprised with dis
show calem surprised with dis
show brendan surprised with dis
ethan surprised "Really!? I heard that's really tricky to do right, though!"
red sadeyes sadeyebrows talkingmouth "So have I. But almost all the Champions that graduated from Kobukan did it. I wouldn't be the first."
show may -surprised with dis
show calem -surprised with dis
show brendan -surprised with dis
ethan happy "Huh. Well, I'm not going to tell you to stop! I was going to do the same thing."
red surprised "Oh, really?"
ethan "Yeah! Only downside is, I guess if we're both hopping between electives, we're probably not going to have too many classes together."
red happy "Well, when we do, we'll appreciate them even more." 
brendan "Wanna come with us and decide on electives, May?"
may @sadbrow happymouth "I'll have to pass, boys,{w=0.5}{nw}"
extend " I already agreed to meet with Leaf later."
red -happy "Leaf?"
brendan "One of her dormmates."
brendan "I met up with all of them before I actually got to our room!{nw}"
brendan sadbrow "I met up with all of them before I actually got to our room!{fast} What, uh, what were their names, again?"
may sadbrow frownmouth "...You weren't listening?"
brendan "N-no, I totally was!{w=0.5} I'm just, uh, so bad with names.{w=0.5} Isn't that right, Erick?"
ethan angry "..."
ethan "It's Ethan. That's pretty inconsiderate of you, to get my name so wrong, Brantham."
calem "Let's get back on topic. May, what are your dormmates' names?"
may "Well... there's me, Leaf, then a girl from Unova named Hilda--"

show orientation with hpunch

show brendan surprised:
    xpos 0.2
    ease 0.5 xpos 0.5

show may surprised:
    xpos 0.4
    ease 0.5 xpos 0.6

show ethan surprised:
    xpos 0.6
    ease 0.5 xpos 0.7

show calem surprised

show hilbert angry:
    xpos -0.5
    ease 0.25 xpos 0.2

hilbert "What!? Hilda!?"

pause 1.0

calem thinking "Personal space, please."

show calem:
    xpos 0.8
    ease 1.0 xpos 0.1

pause 1.0

calem "{w=0.25}.{w=0.25}.{w=0.25}."
calem sad "Nevermind, this is far worse."

show calem:
    xpos 0.1
    ease 1.0 xpos 0.8

pause 1.0

hilbert "Did you say Hilda!? Answer me!"

show brendan:
    xpos 0.5
    ease 0.5 xpos 0.4

brendan angry "Hey, man, back off."
may sad "Y-yeah...? Hilda's her name. Um, do you know her?"
hilbert ".{w=0.25}.{w=0.25}.{w=0.25}"
hilbert sad "Probably not. It's a common name."
hilbert "Nevermind."

show hilbert:
    xpos 0.2
    ease 1.0 xpos -0.5

calem thinking "...What an unpleasant man. Let him serve as a reminder of how not to react. Please, May, continue."
may "U-uh... well, after Hilda is this Kalosian girl named Serena--"

show orientation with hpunch

show brendan surprised:
    xpos 0.4
    ease 0.5 xpos 0.2

show may surprised:
    xpos 0.6
    ease 0.5 xpos 0.3

show ethan surprised:
    xpos 0.7
    ease 0.5 xpos 0.4

show calem surprised

calem "WHAT!?"
ethan angry "Oh, what now!?"
calem "Please, describe her to me!"
show ethan surprised with dis
may "Um, well, she's got flawless skin, a massive chest, really long legs--"
calem thinking "Sunglasses? Does she have sunglasses?"
show brendan happy with dis
may happy "Oh, yes! They kinda make her look like a Hoothoot. She laughed when I said that."
calem closedbrow "...That cannot be. {cps=*0.2}She's not meant to..."
show may sadbrow frownmouth with dis
show brendan sadbrow frownmouth with dis
show ethan sadbrow frownmouth with dis

pause 1.0

red sadeyebrows sadeyes talking2mouth "Hey. Calem. You good?"

calem "Yes... except for the sinking realization that I made the hardest decision of my life for absolutely naught."
ethan "...Translation?"
calem "One often meets their destiny on the road to avoid it."
ethan angry "Calem! Dude! None of us know what that means!"

show brendan surprised:
    xpos 0.2
    ease 1.0 xpos 0.5

show may surprised:
    xpos 0.3
    ease 1.0 xpos 0.6

show ethan surprised:
    xpos 0.4
    ease 1.0 xpos 0.7

show calem thinking

show serena:
    xpos -0.5
    ease 1.5 xpos 0.2

serena "Excuse me, did you say 'Calem?'"

redmind surprised "{cps=*0.2}...{/cps}Well, she certainly fits the description May gave, vague as it was. With those sunglasses and that accent, I'm pretty sure that's Serena."

$ BecomeNamed("Serena")
calem "Oh, hello, Serena."

show ethan closedbrow:
    xpos 0.7
    ease 10.0 xpos 1.5

show may:
    xpos 0.6 ypos 1.0
    ease 3.0 xpos 0.1
    pause 2.0
    ease 2.0 rotate -5.0 ypos 1.1
    pause 1.0
    ease 1.0 xpos -0.5

show brendan:
    xpos 0.5
    ease 2.0 xpos -0.5
    pause 5.0
    ease 1.0 xpos 0.05
    pause 1.0
    ease 1.0 xpos -0.5

calem "Uh..."
calem happybrow -frownmouth "I had no idea you were enrolled here."

serena "Same for me.{w=0.5} I didn't think I'd find you here."
serena "So, since we've managed to find each other, are you busy?"

pause 1.0

show calem thinking:
    xzoom 1 xpos 0.8
    ease 0.5 xzoom -1

pause 2.0

redmind frownmouth angrybrow "Calem gestured towards me without a word."

show calem thinking:
    xzoom -1 xpos 0.8
    ease 0.5 xzoom 1

pause 2.0
    
show serena at getcloser:
    xpos 0.2

pause 2.0

serena sadbrow "Oh? And who might you be?"

red -angrybrow surprised "Me? Oh, uh, I'm [first_name], and..."

menu:
    "I'm Calem's homeroom teacher!":
        show serena surprised with dis
        calem surprised ""          
        red happy "I'm Calem's homeroom teacher. A pleasure to meet you."
        serena happymouth "Goodness, I didn't know we were assigned our homerooms already!{w=0.5} But you're so young!{w=0.5} What do you teach, Professor?"
        calem angrybrow "What? No, he's not a teacher.{w=0.5} And we haven't been assigned our homerooms yet.{w=0.5} Don't take him so seriously."
        serena pout "Oh, it was a joke?{w=0.6} How disappointing..."
        redmind thinking "Well, that's one way to embarrass yourself."      
        
    "With those glasses, I bet people mistake you for a Hoothoot.":
        show calem surprised with dis
        show serena surprised with dis
        red happy "With those glasses, I bet people mistake you for a Hoothoot."

        pause 2.0
        
        redmind thinking "Calem and Serena are peering deeply into the fathoms of my soul."        
        serena closedbrow -surprisedmouth "Hee... Hee..."
        redmind sadbrow -frownmouth "She's either crying or laughing."
        serena happy "Heeheeheehahahahaha!"
        $ ValueChange("Serena", 1, 0.2)
        serena "That's actually the second time I've heard that today! It's true, isn't it?"
        serena -happy "Would you believe me if I told you they were a present from my parents?"
        serena happy "Everyone thinks they're silly-looking, but I think they're adorable!"
        
        show calem at getcloser:
            xpos 0.8

        calem thinking "{size=30}You noticed what May said earlier, and you knew Serena would be fine with that joke, so this was... fine. Still, do be aware some people would take offense at that.{/size}"
        red happy "{size=30}Yeah, I know. Wouldn't have said it if I knew it wouldn't be fine.{/size}"
        calem happymouth "{size=30}...Of course.{/size}"

        show calem at getfurther:
            xpos 0.8
        
    "It's a pleasure to meet you.":        
        red -surprised "It's a pleasure to meet you."

        serena happy "And the same to you, I'm sure."

pause 1.0

serena surprised "Oh my, look at the time!"

show serena at getfurther:
    xpos 0.2

serena sadbrow "I have to get going. I'm going to run some errands with a few girls I met earlier today."

serena happy "But it's really great to see you here!"
serena -happybrow "Let's catch up later!"
calem happy "Sure, I'll see you around."

show serena:
    alpha 1.0 xpos 0.2
    ease 1.25 alpha 0.0 xpos 1.5
    
pause 1.0

show calem sad with dis

show calem:
    xpos 0.8
    ease 0.5 xpos 0.5

stop music fadeout 3.0

red "And she's gone."

pause 1.0

red angrybrow frownmouth "...And, so, apparently, is everyone else."

pause 1.0

red -angrybrow "Hey, seriously, Calem, are you alright?"
calem "{cps=*0.2}...{/size}No, but I will be."

pause 1.0

red -angrybrow -frownmouth "Alright. But you know, I'm here to talk. Might need to get a lunch or two together, get a better feel for each other, you know, but I {i}am{/i} here."

calem happy "Thank you for your concern. I assure you my friendship does not normally involve so much drama."

hide serena

$ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, fadein=3.0, tight=None)

red "Friend of yours?"
calem -happy "You can say that."
calem thinking "We were neighbors. As you've doubtlessly gathered, though, I was not made aware she would be enrolling here. I wonder why.{w=0.25}.{w=0.25}."

calem surprised "Ah.{w=0.75}{nw}"
extend -surprised smilemouth " Since we're going to be dormmates, we should exchange contact information. You know, in case we need to call each other if there's an emergency."
red "Oh yeah. Good thinking."

$ BecomeContacted("Calem")

calem "All right. It appears that we've been ditched, so I'm going to resolve a few errands."
calem "I have some personal business to take care of at the registration office. Something about my recommendation letters, if I remember correctly."
calem "I'm suspecting other students are probably there for other reasons, so I'd like to get there before it closes."

red "Okay, cool. Need me to come with you?"
calem -smilemouth "No, it's all right."
calem happy "I believe that androgynous Student Council member recommended we head to the lobby to mingle. Why don't you head there?"
calem -happy "You never know what connections you might make."
red angrybrow smilemouth "Oh, so it's really just about making contacts you can leverage later?"
calem sadbrow "You think so little of me? I'm not Hilbert, you know. No, I think forming bonds with other people is genuinely fun. Regardless of what boons they may come with."
red happy -angrybrow "Relax, I know you're not like that. Anyway, I'll catch you later?"
calem happy "Yes, give me a call if you need anything."
calem -happy smilemouth "{i}Au revoir.{/i}"

show calem:
    xpos 0.5
    ease 1.0 xpos 1.5

pause 2.0

redmind thinking "Alright, time to find that lobby! Let's see... if I just start running in a random direction, then..."

show hall_A2b at sepia with dis
show flashback with dis

$ renpy.pause(1.0, hard=True)

show leaf angrybrow angrysmilemouth at sepia, dissolvein behind flashback

pause 0.5

leaf "Hey, did I give you that brochure for nothing? Use it, dummy!"

show blank with splitfade

hide leaf
hide hall_A2b
hide flashback
hide blank with dis

redmind "Oh, great, now there's two of them in my head. Fine, I'll use the brochure!"
red surprised ".{w=0.25}.{w=0.25}.{w=0.25}"
redmind thinking "Huh. This is actually super-easy to follow. Maybe that girl had a point."
red angrybrow happymouth "Okay! Lobby time. Let's go!"

$ renpy.pause(1.0, hard=True)
    
$ renpy.music.play("Audio/mediumcrowdloop.ogg", channel='crowd', loop=True, fadein=1.0)

scene lounge:
    alpha 0.0 zoom 1.0
    ease 3.0 alpha 1.0 zoom 1.1 ypos -100

show orientation behind lounge

$ renpy.pause(2.5, hard=True)

redmind "Huh, looks like most people are discussing the orientation."
redmind "I imagine a lot of people are coordinating their type electives, and figuring out their schedules."

show lounge:
    zoom 1.1 ypos -100 alpha 1.0
    ease 0.75 zoom 1.0 ypos 0

redmind "I don't see any of my dormmates around here...{w=0.5} but that's fine. I think I'd like to start a conversation with someone new, anyway."

show lounge:
    zoom 1.0
    parallel:
        xalign 0.0
        ease 0.03 xpos -15
        ease 0.03 xpos 15
        ease 0.03 xpos 0
        repeat 3
    parallel:
        yalign 0.0
        ease 0.03 ypos -30
        ease 0.03 ypos 30
        ease 0.03 ypos 0
        repeat 3

stop music fadeout 1.0
$ cap_player = first_name.upper()
"{color=#3110dd}???{/color}" "\"{size=45}[cap_player]!!{/size}\""

red surprisedeyes surprisedbrow happymouth "Whoa! That guy has the right idea!"

show lounge:
    yalign 1.0 xalign 0.5

show blue angry with dis:
    xpos 720

pause 0.5
play music "Audio/Music/RivalTune.mp3" noloop
$ renpy.music.queue("Audio/Music/Show Me Around.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    
$ renpy.pause(0.5, hard=True)

red angrybrow frownmouth "Oh. I should've known."

blue "What the hell are you stalking me for?{w=0.25} Wait, how'd you even get in here?"

show blue talkingmouth:
    zoom 1.0 ypos 1.0
    ease 0.5 zoom 1.25 ypos 1.1 xpos 600

blue "Did you sneak in just to follow me around!? That's creepy as shit!"
blue "You better scram before I call security on your ass!"

red "Give me a break.{w=0.5} I've got an invitation, just like you, [blue_name]."

show blue:
    zoom 1.25 ypos 1.1 xpos 600
    ease 0.5 zoom 1.0 ypos 1.0 xpos 720

blue sweat angrymouth "You...{w=0.5} got an invitation?"

show blue surprised with dis
red "Yeah, last month.{w=0.5} Actually, we thought it was yours, at first, but--"

show blue angry:
    zoom 1.0 ypos 1.0
    ease 0.25 zoom 1.25 ypos 1.1 xpos 600

blue -sweat "Bullshit! Let me see it!"
    
show letter at itemgive

red "Sure, if it'll make you feel better."
red angry "...But don't you dare even think about so much as folding it roughly."

show letter:
    alpha 1.0
    ease 0.5 alpha 0.0

pause 1.5

hide letter
    
blue -angry surprisedmouth ".{w=0.4}.{w=0.4}."

red -angrybrow talking2mouth "Hey. Earth to [blue_name]. Are you happy now?"

blue surprised "..."

show blue:
    zoom 1.25 ypos 1.1 xpos 600
    ease 0.5 zoom 1.0 ypos 1.0 xpos 720

blue sad "This means...{w=0.5} then why didn't Gramps...?"
blue "...That makes no sense.{w=0.5}{nw}"
blue angry "...That makes no sense.{fast} Why are you here? You're the last guy in the world that should be in here!"
red angrybrow "...And yet I am, just as much as you are. So what does that say about you?"
blue "You're such a waste of space, it's disgusting that Gramps recommended you.{w=0.5} He must've just felt bad that you didn't have any friends!"

show blue closedbrow:
    xpos 720
    ease 0.5 xpos 500

blue "Psh, talking about this with you is a waste of time."

blue angry "Whatever happens, just quit holding me up and we won't have a problem, got it, [first_name]?"

blue -angry "Now excuse me, I got things to do.{w=0.5}{nw}"

show blue:
    xpos 500 alpha 1.0
    ease 0.4 xpos 0 alpha 0.0

blue happybrow angrymouth "Smell ya, loser!"

pause 2.0

redmind -angrybrow sad "That was utterly miserable. I'll just see if there's someone else to talk to, then I'm out."

cheren "Pardon me."
red "Oh, hey."

show cheren with dis

cheren disappointed "On the behalf of my classmate, I'd like to apologize for his disastrous conduct."
red happy "Hah, what? You don't need to apologize for [blue_name]. It's him, and only him, that's responsible for how he acts."
cheren sad "Nevertheless, to have some of your first moments at this prestigious academy marred by that man's atrocious manners..."
red -happy "It's fine, really. I know how to roll with the punches."
red "Anyway, I appreciate your concern, but, uh, how are you involved in this? You're a normal student, right?"
cheren -sad "For now. I aim to join the Student Council shortly, though."
red surprised "Oh, yeah? Actually, that reminds me of a question I had. This school's got a one-year curriculum. How does the Student Council work? How can there be one before the school year's even started?"
cheren happy "It'd be my pleasure to explain! Last year's students can elect to remain with the school after graduation."
cheren -happy sadmouth "They take on a supervisory role for a number of months, ensuring the incoming class becomes acclimated." 
cheren thinking "However, a month after the year begins, a new election is held to determine this year's Student Council. From there, the Council votes internally to determine who their president will be."
red "Wow, so you only have a month to start up a campaign, and get people to vote for you?"
cheren sad "That's the sum of it, yes."
red happy "Well, what are your positions? Convince this voter."
cheren surprised "Oh? Er, then... my positions, yes..."

pause 1.0

red sadeyes sadeyebrows smilemouth "You good?"

pause 1.0

cheren disappointedbrow happymouth "{i}...Absolutely.{/i}"

pause 1.0

cheren angry "My positions are thus: The introduction of co-ed dorms. Raises for non-academic staff. Repeal of the school's frankly absurd curfew! We are adults, after all."
cheren disappointedbrow "Furthermore, the benefits granted by tenure in this school allow for far too much 'creativity' in how classes are run. On the other hand, the staff should absolutely be permitted to unionize."
cheren "Even further more, financial aid ought to be dispersed towards those who need it most, not those who are most well-connected."
cheren angry "Finally, the number of highly suspicious stories about how this school decides admission must be looked into, resolved, and, if necessary, terminated."

redmind surprised "...Oh, crap, this guy's intense."
redmind frownmouth closedbrow "And I think he's looking into something that could cause some serious problems for me."
red -closedbrow surprisedmouth "That's pretty ambitious. Does the Student Council have the authority to do all that? A lot of it sounds like stuff the staff would want to handle themselves."
cheren "It certainly is. But what is politics, if not the wresting of power from those who wish to hold it evermore?"
cheren sad "Regrettably, what I can promise is limited, given the scope of my ambition. And many have overscoped themselves into an early grave."
cheren angrybrow happymouth "But I assure you, if you elect me to the Student Council, I'll never stop fighting for a more egalitarian, just, and modernized Kobukan Academy."

pause 2.0

cheren disappointed "Oh, and also, we'll put five-ply toilet paper in the washrooms."
cheren "That's a very popular request amongst a certain lobby, so{cps=*0.2}..."

pause 1.0

red happy "Well, you've got my vote. Who am I voting for?"
$ BecomeNamed("Cheren")
cheren surprised "Oh! Of course. My name is Cheren, of Aspertia City. In Unova."
red "Sounds good. Hope you succeed."
cheren happy "I very much appreciate your support. Good day."

hide cheren with dis

redmind thinking "...Well, he seems nice. I'm worried about what he might find, though. But... given what he says he wants to do, surely he won't actually make enough progress to find anything out about me, right?"
redmind sadeyes sadeyebrows "{cps=*0.2}Right...?{/cps}"

$ renpy.music.stop(channel='crowd', fadeout=2.0)

show blank2 with dis:
    alpha 1.0

pause 2.0

redmind "Alright. I still haven't unpacked my stuff yet, so I should probably run back to my room now."

show blank2:
    alpha 1.0
    ease 1.5 alpha 0.0

show hall_B behind blank2:
    xpos 960 xalign 0.5 ypos 1080 yalign 1.0 zoom 0.9
    ease 0.5 zoom 0.95

$ renpy.pause(0.5, hard=True)

show hall_B:
    alpha 1.0 zoom 0.95
    ease 1.2 zoom 1.0
    block:
        ease 0.03 xpos 940 ypos 1060
        ease 0.03 xpos 980 ypos 1100
        ease 0.03 xpos 960 ypos 1080
        repeat 2

show misty surprised:
    xpos -0.5 zoom 1.0 ypos 1.0
    pause 1.1
    ease 0.3 zoom 1.5 ypos 1.3 xpos 0.5
    ease 0.7 rotate 45.0 ypos 3.0

$ renpy.pause(1.2, hard=True)

stop music fadeout 1.0

play sound "Audio/Body Crash.ogg"
$ renpy.pause(0.4, hard=True)

misty "{size=48}UWAAHHH!{/size}"
misty "{size=48}HEY! WATCH IT!{/size}"

hide blank2
    
red surprised "Whuh?"

queue music "Audio/Music/CeruleanCity.mp3"

show misty angry:
    ypos 3.0 rotate 45.0 zoom 1.0
    ease 1.5 ypos 1.0 rotate 0.0
        
misty "Don't 'whuh' me! What's with that dumbass look on your face?"
misty "Are you deaf or just stupid!? Don't just stand there and stare! At least admit you weren't paying attention!{w=0.25} 'Cause clearly you weren't!"

menu:
    "I'm very sorry.":
        show misty surprisedbrow -angrymouth with dis
        red sadeyes sadeyebrows -surprisedmouth "I'm very sorry."
        red "I was in kind of a hurry and turned the corner too quickly. Are you okay?"      
            
        misty closedbrow "{i}*sigh*{/i}"
        
        misty talkingmouth "I'm fine."
        
        misty angry "I'm fine!{w=0.6} It's fine!"
        misty closedbrow "Just try to not run over any more girls on the way to...{w=0.5}{nw}"
        misty -closedbrow -angrymouth "Just try to not run over any more girls on the way to...{fast} wherever you're going."
        
        show misty:
            alpha 1.0 xpos 0.5
            ease 1.0 xpos -0.5 alpha 0.0
            
        stop music fadeout 2.0
        
        redmind thinking "Yeah. Okay. Tear my head off, then strut out without even giving your name. Nice."
        redmind sadmouth "Ugh, groveling like that left a bad taste in my mouth..."

    "You ran into me!":
        show misty surprised with dis
        red angry "You ran into me!"
        red "Lay off the insults for a second, and maybe you'd realize that this was totally your fault."

        $ ValueChange("Misty", -1, 0.5)

        misty "You...{w=0.7}{nw}"
        misty angry "You... {fast} JERK!"
        
        show misty angry:
            zoom 1.0 ypos 1.0 xpos 960
            ease 0.5 zoom 1.25 ypos 1.2 xpos 720
        
        $ renpy.pause(1.0, hard=True)
        play sound "Audio/Slap.ogg"
        pause 0.1
        
        show misty angry:
            xpos 720 ypos 1.2 zoom 1.25 rotate 0
            ease 0.1 xpos 520 ypos 1.1 zoom 1.33 rotate -3
        
        show hall_B at hall_move1
        
        pause 1.0
        
        show misty angry:
            xpos 520 ypos 1.1 zoom 1.33 rotate -3
            ease 0.2 xpos 360 ypos 1.0 zoom 1.25 rotate 0
        
        show hall_B at hall_move2
        
        redmind "Ow."
        
        show misty angry:
            zoom 1.25 xpos 360 ypos 1.0 alpha 1.0
            parallel:
                pause 0.5
                ease 0.5 alpha 0.0
            parallel:
                ease 1.0 xpos -200
        
        stop music fadeout 2.0
        
        pause 1.0
        
        red angry "Ugh. Has anyone ever told you... {size=40}you don't take criticism too well!?{/size}"

    "My bad, but tone it down.":
        show misty surprisedbrow -angrymouth with dis
        red sadeyes sadeyebrows -surprisedmouth "My bad, but tone it down."
        red "I was just figuring out what to say. So, sorry, alright? No need to blow up like that. Now, are you okay?"
        
        $ ValueChange("Misty", 1, 0.5)        
            
        misty closedbrow "{i}*sigh*{/i}"
        
        misty talkingmouth "I'm fine."
        
        misty angry "I'm fine!{w=0.6} It's fine!"
        misty closedbrow "Just try to not run over any more girls on the way to...{w=0.5}{nw}"
        misty -closedbrow -angrymouth "Just try to not run over any more girls on the way to...{fast} wherever you're going."
        
        show misty:
            alpha 1.0 xpos 0.5
            ease 1.0 xpos -0.5 alpha 0.0
            
        stop music fadeout 2.0
        
        redmind thinking "Yeah. Okay. Tear my head off, then strut out without even giving your name. Nice."

pause 1.0

scene hall_A with dissolve    

queue music "Audio/Music/CeruleanCity.mp3"

$ renpy.pause(1.5, hard=True)

pause 1.5

red surprised "Uh."

show misty:
    xpos 860 alpha 0.0
    ease 0.5 alpha 1.0

pause 1.0
    
misty surprised "Seriously? Didn't I {i}just{/i} see you?"
misty "{w=0.5}.{w=0.5}.{w=0.5}."
misty angry "You're the guy that ran me over earlier."

if (persondex["Misty"]["Value"] > 0):
    misty -angrybrow talkingmouth "But at least you were a decent enough human being and apologized."
    misty sad "Not many people own up to their mistakes.{w=0.5}{nw}"
    misty closedbrow "Not many people own up to their mistakes.{fast} I, uh, appreciated it."

$ renpy.pause(1.5, hard=True)
misty -angry -closedbrow -sadmouth "Tch. Whatever. I won't hold it against you."
$ renpy.pause(1.5, hard=True)

$ BecomeNamed("Misty")
misty "...Well? Introduce yourself. I'm Misty."

if (persondex["Misty"]["Value"] > 0):
    red happy "I'm [first_name]. Nice to meet you."
else:
    red happy "I think we got off on the wrong foot. Let's start over. I'm [first_name], and it's nice to meet you."

if first_name in ["John", "Johnny", "Jonathan", "Jon", "Joe", "Joseph", "Joey", "Michael", "Mike", "Mikey", "Robert", "Rob", "James", "Will", "William", "Bill", "Billy", "David", "Dave", "Richard", "Rich", "Richie", "Charles", "Charlie", "Chuck", "Chuckie", "Chucky", "Thomas", "Tom", "Tommy", "Timothy", "Timmy", "Tim", "Christopher", "Chris", "Daniel", "Danny", "Dan", "Paul", "Mark", "Donald", "Donny", "Don", "George", "Kenneth", "Kenny", "Ken", "Steven", "Stephen", "Stephan", "Steve", "Edward", "Edwin", "Eddie", "Eddy", "Ed", "Brian", "Ronald", "Ronny", "Ron", "Anthony", "Tony", "Kevin", "Kev", "Jason", "Jay", "Matthew", "Matt", "Larry", "Jeffrey", "Jeff", "Geoffrey", "Frank", "Frankie", "Scott", "Erik", "Eric", "Andrew", "Andy", "Drew", "Raymond", "Ray", "Gregory", "Greg", "Joshua", "Josh", "Jerry", "Jeremy", "Dennis", "Denny", "Walter", "Walt", "Patrick", "Pat", "Patty", "Pattie", "Peter", "Harry", "Harold", "Jack", "Jackie", "Jacky", "Roger", "Carl", "Henry", "Justin", "Terry", "Samuel", "Sam", "Nicholas", "Nick", "Nicky", "Nickie", "Adam", "Benjamin", "Ben", "Benny", "Brandon", "Phillip", "Philip", "Phil", "Sean", "Fred", "Freddy", "Freddie"]:
    misty surprised "'[first_name]?' For real?{w=0.5} That sounds so basic."
    red thinking "I stand corrected."
    misty surprised "Uhh, I just mean I didn't expect your name to be so normal, is all!"

else:
    misty "'[first_name]?' For real?{w=0.5} What kind of name is that?"
    red thinking "I stand corrected."
    misty surprised "Uhh, I just mean I don't know many people named that, is all!"

misty sadbrow sweat "I'm not implying it's weird or anything, honest!"

redmind "Go on. Keep digging."
misty -sweat sad "{size=28}{i}Ugh, why am I always so...{/i}{/size}"
show misty surprised with dis

red angrybrow talking2mouth "You're going to have to speak up a bit. You started trailing off on that last sentence."
misty angry "I didn't say anything!"

pause 1.0

redmind thinking "Tch, she's tenser than a coiled spring. I'm not sure if this conversation is even worth the minefield, but..."

menu:
    "Do you live here?":
        red -angrybrow "This is your room, right here?"
        misty surprised "Yeah, it is."

        $ renpy.pause(1.0, hard=True)

        misty closedbrow -surprisedmouth "Oh, great. Now you know where I live."
        misty angry "Don't get any funny ideas, buster!"
        red "Hey, I'm a nice guy.{w=0.5} I wouldn't dream of doing anything like that."
        misty -angrymouth "Hmmm."
        
        show misty norm2
        misty -angrybrow "I guess I can trust you.{w=0.75}{nw}"
        misty angrybrow "I guess I can trust you.{fast} Just be sure to watch where you're going when classes start!"
        red thinking "You can drop that anytime, you know..."
        
    "How was your day?":
        red -angrybrow -talking2mouth "So, how was your first day here?"
        misty "Other than you tackling me to the ground?{w=0.5} Just peachy."
        red thinking "You can drop that anytime, you know..."

    "Is that a Cerulean outfit?":
        red -angrybrow -talking2mouth "I recognize those clothes. Are you from Cerulean City, by any chance?"
        $ renpy.music.set_volume(1.0, delay=0.0, channel="ctc")
        
        $ ValueChange("Misty", 1, 0.5)

        misty happy "You know Cerulean City?"
        
        red "Sure! My mom and I used to go to their water parks all the time when I was a little kid."
        red sadeyes sadeyebrows "Though, those Gyarados rides always scared the pants off me back then."
        misty sadbrow "Aw, no way!{w=0.5} Where are you from?"
        
        red "I'm from Pallet Town.{w=0.5} It's not the most well-known place in Kanto but I'm sure you've heard of it."
        
        misty closedbrow -happymouth "What town? Pewter?"
        
        red "Uh, no. Pallet Town?{w=0.5} You know, the one with all the trees and grass?{w=0.5} South of Viridian?{w=0.5}"
        red sad "Does any of this ring a bell?"

        misty -closedbrow "Nope. Sorry."        
        redmind thinking "Damnit! I was so close to a full conversation! Curse me and my humble upbringing!"

show misty surprised with dis
red happy "Anyway, I need to unpack my stuff. I shouldn't keep holding you up."

red "Here, let me take your bags in for you. To make up for earlier."
red surprised "...Huh. These are some awfully fancy bags. And what does that name tag say? Something about a gym...?"

misty angry "Don't touch those!"

show misty:
    xpos 860 ypos 1080 zoom 1.0
    ease 0.4 zoom 1.2 ypos 1250 xpos 780
    
$ renpy.pause(0.5, hard=True)

red surprised "Uh, okay. Looks like you got it."

show misty angry:
    xpos 780 ypos 1250 zoom 1.2
    ease 0.5 zoom 1.0 ypos 1080 xpos 820

misty "You-- inconsiderate, pigheaded-- you--"

show misty angry:
    xpos 820 zoom 1.0

misty "Don't go around touching a girl's things!"

show misty angry:
    xpos 820 alpha 1.0
    ease 0.33 xpos 200 alpha 0.0
    
pause 0.33

play sound "Audio/Door_Slam.mp3"
show hall_A:
    yalign 0.0
    ease 0.03 ypos -10
    ease 0.03 ypos 10
    ease 0.03 ypos 0
    repeat 3

red "..."

if (persondex["Misty"]["Value"] == 2):
    redmind happy "Nope, you're not turning me off that easily. I'm gonna be your friend, and there's nothing you can do about it."
elif (persondex["Misty"]["Value"] == -1):
    redmind thinking "...Ugh. I'm so done with her."
else:
    redmind thinking "I sense I've committed some sort of faux pas..."

hide misty

stop music fadeout 1.5

$ renpy.pause(1.5, hard=True)
    
show dorm_empty_B with dis:
    alpha 1.0

play sound "Audio/Door_Open1.mp3"

$ renpy.pause(2.5, hard=True)

hide blank2

redmind -thinking "...?"

red thinking "Something... is off."

redmind "It's like one of those games I played as a kid where I tried to spot the difference between two similar pictures."
redmind "Something is definitely out of place, but I can't put my finger on it."

play sound "Audio/Door_Close1.mp3"

show calem at rightside with dis
show brendan at leftside with dis
show ethan at centerside with dis

calem "Is something wrong, [first_name]?"
red -closedeyes "I'm... not sure."
calem "Have you been drinking water? With all the excitement, it's easy to forget.{w=0.5} Dehydration is a killer."
brendan surprised "Oh, crap. Does your head hurt? Stomachache, maybe?{w=0.5} Gimme a sec, I think May dropped some Lum Berries off in my bag!"

red "In your bag{w=0.25}.{w=0.25}.{w=0.25}.?"
red "...bag."

pause 2.0

show dorm_empty_B:
    parallel:
        xalign 0.0
        ease 0.03 xpos -15
        ease 0.03 xpos 15
        ease 0.03 xpos 0
        repeat 3
    parallel:
        yalign 0.0
        ease 0.03 ypos -30
        ease 0.03 ypos 30
        ease 0.03 ypos 0
        repeat 3

queue music "Audio/Music/Found It.ogg" noloop
$ renpy.music.queue("Audio/Music/Sneaking Again.ogg", channel='music', loop=True, tight=None)

red angry "{size=42}My bag is gone!{/size}"


ethan surprised "What! That black and yellow one, right?"
calem thinking "Yes, I saw it too. Where was it last...?"
red -angrybrow sad "Damn it, I need that! It's got pretty much everything except my clothes in it!"
brendan angry "Someone must've stolen it! I'll beat that asshole inside out!"
calem -thinking talkingmouth "Be calm. Only us five and the staff can get in here."
red confusedeyebrows "...Us {i}five?{/i}"
ethan angry "Wait a minute... Hitandrun isn't here!"
calem surprised "...That's truly baffling."
calem thinking "In any case, he might not be, but all his luggage is. It doesn't make sense for him to abscond with your backpack and leave all his stuff here at our mercy."
brendan "Huh... that Roxanne chick. She said that all the hallways have security cameras, right?"
red angrybrow happymouth "Yeah, that's right! Good thinking. I'm going to the security office right now."

pause 1.0

show calem sad with dis
show ethan sad with dis
show brendan sad with dis
red -angrybrow sad "Er..."

pause 1.0

calem "Am I right in assuming that none of us know where the security office is?"

pause 1.0

red closedeyes "Yep... But..."
show ethan happy with dis
show brendan happy with dis
show calem surprised with dis
red angrybrow happymouth "If we pick a direction and just start running, we're bound to run into it eventually!"
ethan "Hell yeah!"
brendan "Leg day, here we go!"

show brendan:
    xpos 0.25
    ease 0.4 xpos 1.5

show ethan:
    xpos 0.5
    ease 0.4 xpos 1.5

pause 0.4

play sound "Audio/Door_Slam.mp3"

pause 2.0

calem "That's... that's not how geometry works..."
calem "..."
calem happy "Oh, whatever. Wait up!"

show calem:
    xpos 0.75
    ease 1.0 xpos 1.5

pause 0.5

show blank2 with splitfadefast

$ renpy.pause(1.0, hard=True)

show lobby_night behind blank2
hide dorm_empty_B

$ renpy.pause(0.5, hard=True)
$ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

hide blank2 with splitfadefast

red talking2mouth "Wha... an uproar? What's going on here?"

show face surprised at dissolvein:
    xpos 0.6

face "I-I don't know!{w=0.3} I was just minding my own business here, a-and then..."
face angry "...It's like a giant bug!{w=0.5} Except, like, it shocked me with some kinda taser! Like, what the hell, man!"

red surprisedeyes confusedeyebrows "...What?"

show mace at dissolvein:
    xpos 0.4

hide brendan

mace "There was something skittering around the lobby a few minutes ago.{w=0.5} Whenever it touched someone, it blasted them with some kind of electricity."
red "What could that be? A Galvantula? Or a Charjabug?"
mace closedbrow "It couldn't have been a Charjabug since it moved too fast...{w=0.5} My money's on a Galvantula. In which case, I definitely intend to add it to my team!"

show brendan thinking:
    alpha 0.0 xpos 0.75
    ease 0.5 alpha 1.0
    
brendan "Huh. That's a pretty big coincidence."

hide calem

show mace surprised with dis
show face surprised with dis
if (profanity):
    red "Coincidence, my ass!{w=0.5} What's my bag doing running around the lobby floor!?"
else:
    red "Coincidence, my ***!{w=0.5} What's my bag doing running around the lobby floor!?"

show calem thinking:
    alpha 0.0 xpos 0.25
    ease 0.5 alpha 1.0

calem "...Interesting.{w=0.5} What did you say you packed in your bag again, [first_name]?"

show calem surprised with dis
red "I didn't pack a Galvantula, I'll tell you that much!{w=0.5} Whatever's going on, all I know is that I need that bag back!"
red "Which way did you say it went?"

hide ethan

mace surprisedbrow "Down the hallway.{w=0.5} If you want to get your bag back, you should hurry. There's already a bunch of other students trying to catch it and I'm sure security's on the way, too."

show mace at dissolveaway:
    xpos 0.4
show face at dissolveaway:
    xpos 0.6
show ethan with dis

brendan angry "Aw, hell no. That's your bag, right, [first_name]?{w=0.5} If you let those other guys get it before you, there's no tellin' what's gonna happen to your stuff!"
brendan sad "I'm not entirely sure what's happenin' right now, but if something really weird {i}is{/i} in your bag, aren't you gonna be in huge trouble if they find out it's yours?"
calem "Arguably, we'd be in more trouble for interfering in the operations of the school's security team..."
ethan surprised "Uh... I'll pass here. Whatever you think we should do is probably best."

$ goafter = True

menu:
    ">Let security handle it.":
        $ goafter = False     
        red -angrybrow thinking "Even though I'm a little hesitant to just let my bag run free with all those other guys chasing it, I'm sure the school's security will do a far better job looking for it than me."        
        red happy "Besides, if it's as dangerous as they say, maybe I shouldn't go around messing with it."

        calem thinking "Right. This situation's simply out of our control."
        calem -thinking "And this {i}is{/i} Kobukan Academy we are talking about.{w=0.5} If there's any school with competent security, it'd be this one."
        calem "Anyway, let's go to the lost and found and file a missing report for your bag."
        
        brendan thinking "I dunno, man.{w=0.5} I still feel like it's a little weird letting other people handle stuff that isn't theirs."
        brendan "But in the end it's your bag.{w=0.5} If you think it's a good idea, I'm all for it."
        
        show blank2 with splitfade
        
        $ renpy.pause(1.5, hard=True)
        
        show text "{color=#ffffff}.{/color}" as text1:
            alpha 1.0
            pause 0.5
            ease 0.0 alpha 0.0
        show text "{color=#ffffff}..{/color}" as text2:
            alpha 0.0
            pause 0.5
            block:
                ease 0.0 alpha 1.0
                pause 0.5
                ease 0.0 alpha 0.0
        show text "{color=#ffffff}...{/color}" as text3:
            alpha 0.0
            pause 1.0
            block:
                ease 0.0 alpha 1.0
                pause 1.5
                ease 1.0 alpha 0.0
        
        $ renpy.music.stop(channel='crowd', fadeout=1.5)
        
        $ renpy.pause(3.0, hard= True)
        
        hide blank2 with splitfade
        
        $ renpy.pause(1.5, hard= True)
        
        red closedeyes "Looks like my bag hasn't turned up yet. Not that I was really expecting it to."
        
        hide text1
        hide text2
        hide text3
        
        red @talking2mouth "{i}*sigh*{/i}"
        red -closedeyes frownmouth "Well, nothing left to do but wait for someone to bring it here.{w=0.5} Let's go back."
        brendan surprised "So, like, is there anything weird in your bag or does it normally do stuff like this?"
        
        red "Definitely not! It was completely normal all the way here, and I had it on me this entire time. It only started acting weird when I left it alone."
        red "The only thing I can thin--"
        
        show brendan surprised with dis
        show calem surprised with dis
        show ethan surprised with dis

        "Security" "\"You there! Watch out!\""

        red surprised "Wha?"

        show backpack:
            alpha 0.0 yalign 1.0
            ease 1.0 alpha 1.0
            
        pause 0.5
            
        play sound "Audio/Pokemon/Moves/Paralyzed.ogg"

        $ renpy.pause(1.0, hard=True)

        ethan "Hey, isn't that your--"
    
    ">Go after it.":        
        red "Whatever it is, that's still my bag out there, and I want it back."
        red "The situation's gone a little crazy, but that's all the more reason why I have to take care of it myself."
        calem "If you say so.{w=0.5} I won't question your choice, so if you think this is for the best, then I'll follow along."
        calem happy "Anyway, somebody has to make sure you don't do something silly."
        brendan happy "Hell yeah! That bag's yours and we're not lettin' nobody touch it with their grubby hands!"
        brendan angry "You lead the way, [first_name]!{w=0.4} I'll be right behind you!"
        ethan happy "Allons-y!"
        
        show blank2 with splitfade
        
        $ renpy.pause(1.5, hard=True)
        
        show text "{color=#ffffff}.{/color}" as text1:
            alpha 1.0
            pause 0.5
            ease 0.0 alpha 0.0
        show text "{color=#ffffff}..{/color}" as text2:
            alpha 0.0
            pause 0.5
            block:
                ease 0.0 alpha 1.0
                pause 0.5
                ease 0.0 alpha 0.0
        show text "{color=#ffffff}...{/color}" as text3:
            alpha 0.0
            pause 1.0
            block:
                ease 0.0 alpha 1.0
                pause 1.5
                ease 1.0 alpha 0.0
        
        $ renpy.music.stop(channel='crowd', fadeout=1.5)
        
        hide lobby_night
        
        $ renpy.pause(3.0, hard= True)
        
        show hall_B_night behind brendan:
            subpixel True
            xalign 0.5 yalign 1.0 zoom 1.0
            ease 2.5 xalign 0.5 yalign 1.0 zoom 1.07
        
        hide blank2 with splitfade
        
        $ renpy.music.play("Audio/hall_crowd.ogg", channel='crowd', loop=True, fadein=1.5)

        $ renpy.pause(1.5, hard= True)
        
        show calem surprised with dis
        show ethan surprised with dis
        show brendan surprised with dis

        red "I can hear people yelling.{w=0.5} We have to be getting close!"
        
        show hall_B_night:
            xpos 960 ypos 1080 zoom 1.07
        
        hide text
        hide text1
        hide text2
        hide text3

        ethan "Hey, over there, I see your bag!{w=0.5} It's.{w=0.25}.{w=0.25}.{w=0.5} really moving by itself!?"
        calem "Obviously not. Whatever's inside it must be propelling its locomotion."
        
        show backpack:
            alpha 0.0 yalign 1.0
            ease 1.0 alpha 1.0
            
        pause 0.5
        
        play sound "Audio/Pokemon/Moves/Paralyzed.ogg"
        
        $ renpy.pause(1.0, hard=True)
        
        show backpack:
            alpha 1.0
        
        redmind thinking "Sure enough, my bag's darting between people's legs like it's some kind of small Pokémon.{w=0.5} The bigger problem, though, are all the people trying to grab it...!"
        red angry "Hey, stop! That's mine!"
        
        "Greedy Student" "\"No way, I saw it first!\""
        "Rude Student" "\"Yeah, right! Finder's keepers, idiot!\""
        
        red "No, I mean it's {i}literally{/i} mine! It's got my name on it!"

        brendan happymouth angrybrow "Don't worry, [first_name], I got it!{w=0.5} I've dealt with this kind of thing b--"

play sound "Audio/thunder.ogg"
show blank:
    alpha 0.5
    pause 0.1
    alpha 0.0
    pause 0.1
    repeat 5

show backpack:
    parallel:
        xalign 0.0
        ease 0.03 xpos -20
        ease 0.03 xpos 20
        ease 0.03 xpos 0
        repeat 8
    parallel:
        yalign 0.0
        ease 0.03 ypos -20
        ease 0.03 ypos 20
        ease 0.03 ypos 0
        repeat 8

if (goafter):
    show hall_B_night:
        parallel:
            xalign 0.0
            ease 0.03 xpos -20
            ease 0.03 xpos 20
            ease 0.03 xpos 0
            repeat 7
        parallel:
            yalign 0.0
            ease 0.03 ypos -20
            ease 0.03 ypos 20
            ease 0.03 ypos 0
            repeat 7

else:
    show lobby_night:
        parallel:
            xalign 0.0
            ease 0.03 xpos -20
            ease 0.03 xpos 20
            ease 0.03 xpos 0
            repeat 7
        parallel:
            yalign 0.0
            ease 0.03 ypos -20
            ease 0.03 ypos 20
            ease 0.03 ypos 0
            repeat 7

show calem surprisedmouth deadbrow at leftside, monochrome behind backpack
show ethan surprisedmouth deadbrow at monochrome behind backpack
show brendan surprisedmouth deadbrow at rightside, monochrome behind backpack

"Dormies" "\"{size=48}AaaaarrrRGBLRLBLRBLLBR{/size}\""

hide blank

show backpack:
    alpha 1.0
    ease 0.75 alpha 0.0

$ renpy.pause(1.0, hard=True)

show calem:
    ypos 1.0 xpos 0.25
    ease 1.0 ypos 1.1 rotate 5.0
show ethan:
    ypos 1.0
    ease 1.0 ypos 1.2 rotate -5.0
show brendan:
    ypos 1.0 xpos 0.75
    ease 1.0 ypos 1.15 rotate 7.0

$ renpy.pause(1.5, hard=True)

red angry "Hey, guys!{w=0.5} Get a hold of yourselves!"

show calem:
    ypos 1.1 rotate 5.0 xpos 0.25
    ease 0.5 ypos 2.0 rotate 30.0
show ethan:
    ypos 1.2 rotate -5.0
    ease 0.5 ypos 2.0 rotate -30.0
show brendan:
    ypos 1.15 rotate 7.0 xpos 0.75
    ease 0.5 ypos 2.0 rotate 35.0

$ renpy.pause(0.5, hard=True)

play sound "Audio/Body Roll.ogg"
if (goafter):
    show hall_B_night with vpunch
else:
    show lobby_night with vpunch

$ renpy.pause(1.5, hard=True)

stop music
show flashback with dis

$ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

redmind thinking "Okay. Something's in my bag. Almost certainly an electric type. Fast, small. Not powerful, but determined to do whatever it's doing..."
redmind "Not a Rotom, because my bag's non-mechanical. It's staying on the ground, so it can't fly or levitate. It's able to see where it's going, so its head must be low to the ground--it runs on all fours."
redmind "Less than twenty inches long. Base speed of--at this tilt--somewhere in the range of eighty to one hundred."
redmind "Then... it could be a Pachirisu, a Minun, a Togedemaru, or even a--"

stop music
hide flashback
if (goafter):
    show hall_B_night with vpunch
else:
    show lobby_night with vpunch

security "Watch out, kid!"

red surprised "Gwaah!"

if (goafter):
    show hall_B_night with vpunch
else:
    show lobby_night with vpunch

red "{size=42}Can't dodge--!{/size}"

stop music fadeout 1.0

red thinking ".{w=0.25}.{w=0.25}.{w=0.75}Huh?"

red -closedeyes "It's...{w=0.5} not doing anything."

red "..."
red happy "Well, why don't we just open you up and see what's happening here, huh?"

security "H-Hey, kid! Don't make any sudden movements!{w=0.5} That thing's dangerous!"

play sound "Audio/Pokemon/Unzip Pikachu.ogg"
$ renpy.pause(3.0, hard=True)

$ renpy.music.queue("Audio/Music/New_Adventure_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/New_Adventure_Loop.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

red surprised "This is...!{w=0.75}{nw}"

show redpika01:
    alpha 0.0 zoom 1.1 yalign 1.0 xalign 0.5
    ease 1.0 zoom 1.0 yalign 1.0 xalign 0.5 alpha 1.0

extend ""

red "[pika_name]!?{w=0.5} What... How--"

play sound "Audio/Pokemon/pikachu_happy3.ogg"

hide pikachu

pikachu happy_3 "Pika! Pika Pikachu!"

hide calem
hide ethan
hide brendan

calem thinking "...You brought a Pikachu?{w=0.5} You didn't mention that when I asked you what was in the bag."

red "No! I left him with my mom and...{w=0.25} how did you get here?{w=0.5} Did you stow away in my suitcase!?"

pikachu neutral_2 "Pikachu! Pi-Pikachu!"

red angry "Didn't I tell you to stay with Mom? Does she even know you're here right now?{w=0.5} What if I'd put you in the baggage hold? You could've frozen, you furry idiot!"

pikachu neutral_4 "P-Pika...{w=0.5}{nw}"

extend pikachu neutral_2b " Pikachu!"

red sad "...You wanted to see me that badly, huh?"
red happy "Oh, how could I say no to you?{w=0.5} Welcome back, [pika_name]!"

play sound "Audio/Pokemon/pikachu_excite3.ogg"

pikachu happy_3 "Pika pika!"

show redpika01:
    alpha 1.0
    ease 1.0 alpha 0.0

pause 1.0   
     
stop music fadeout 2.0

redmind "Alright! All's well that ends well. Except for...{w=0.5} one problem."

$ renpy.music.queue("Audio/Music/Littleroot_Start.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/Littleroot_Loop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

pause 1.0

security "So, this is what's causing all the commotion.{w=0.5} Young man, is that your Pokémon?"

red sad "Yes, sir. He is."
    
security "Young man, allowing your Pokémon to freely roam the residence hall is one thing, but endangering the students and faculty in this hall?"
security "I'm afraid I'm going to have to ask you and your Pokémon to come with me to the office."

show calem at leftside with dis

calem "Pardon, sir, but I don't think that's very fair for [first_name] or his Pikachu."
calem "We can't blame him for being frightened by an unfamiliar environment.{w=0.5} He was only trying to reach [first_name] before everyone here began to aggravate him."
    
show brendan at rightside with dis

brendan angry "Yeah, wait a sec! What's the big deal?{w=0.5} Pikachu was just tryin' to find [first_name] like any Pokémon would its Trainer!"
brendan "You guys were the ones chasin' him around all over the place and freakin' him out so of course he's gonna shock some people!"

show ethan angry with dis

ethan "Yeah!{w=0.5} [first_name] didn't even know his Pikachu was in his bag."
calem thinking "That being the case, isn't it sensible to assume the fault here lies somewhere, perhaps... closer to home?"
brendan closedbrow "Right?{w=0.5} What kinda security system do you have where someone can {i}accidentally{/i} bring a whole-ass Pikachu in here?"    
security "Hmph. {w=0.5}I see what you're doing, boys, but the rules are very clear here. I'll need to take this young man to the office, and if you interfere, I'll have to report you, too."
show calem surprised with dis
show brendan surprised with dis
ethan "R-report us!? For what!? Standing up for a friend?"
red happy "Hey, guys, chill. Don't worry, I'll figure something out. Don't get in trouble for me."
show calem sad with dis
show brendan sad with dis
ethan sad "B-but..."

pause 1.0

security "That's better. Now, young man, come along and--"

show hilbert:
    xpos -0.5 zoom 1.0 ypos 1.0
    ease 0.5 xpos 0.3 zoom 1.2 ypos 1.1

show ethan surprised:
    xpos 0.5
    ease 0.5 xpos 0.8

show brendan surprised:
    xpos 0.75
    ease 0.5 xpos 0.9

show calem surprised:
    xpos 0.25
    ease 0.5 xpos 0.7

if (goafter):
    show hall_B_night with vpunch
else:
    show lobby_night with vpunch

stop music

$ renpy.music.queue("Audio/Music/DragonDenStart_B.ogg", channel='music', loop=False, fadein=1.0, tight=None)
$ renpy.music.queue("Audio/Music/DragonDenLoop.ogg", channel='music', loop=True, fadein=0.0, tight=None)

hilbert "{size=42}Pathetic.{/size}"

security "Y-young man...?"

hilbert "I live in the dormitory this bag came from. I was there before anyone else. I saw everything."

pause 1.0

hilbert angry "What I saw was {i}pathetic{/i}. 'Security Team?' Don't make me laugh. You and your band of incompetents couldn't secure a pizza."
hilbert @talkingmouth "When was the last time {i}any{/i} of you passed a physical? And your communication? Laughable. I heard you arguing over which 'code' this was for five minutes."
hilbert "You're direly lucky this was just a Pikachu. If it was anything bigger, people could have {i}died.{/i} Would that make you realize how unqualified you are to keep {i}anyone{/i} safe? Or will you just quit now?"

pause 1.0

hilbert sad "Get out of my sight."

show hilbert:
    alpha 1.0 xpos 0.3 ypos 1.1
    ease 1.5 alpha 0.0 xpos 0.0

pause 2.0

stop music 

show ethan:
    xpos 0.8
    ease 0.5 xpos 0.5

show brendan -surprised:
    xpos 0.9
    ease 0.5 xpos 0.75

show calem -surprised:
    xpos 0.7
    ease 0.5 xpos 0.25

$ renpy.music.queue("Audio/Music/New_Adventure_Start.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/New_Adventure_Loop.ogg", channel='music', loop=True, tight=None)

red surprised "H-holy shit..."
ethan "Dude.{w=0.5} Was Hitcher actually going easy on us before...?"

pause 1.0

red sad "Uh, if it makes you feel any better, sir, I don't think you did that bad a job...?"
red "..."
red angrybrow -sadmouth "Wait, where'd he go?"
calem thinking "Ran off that way.{w=0.5} Crying, I believe."

red -angrybrow "Well, I guess we should start heading back to our room?{w=0.5} It's getting close to curfew, and Cheren hasn't become president yet, so..."
ethan sadbrow -surprisedmouth "Who?"
red happy "Oh, he's great. He's this guy who's running for Student Council, and..."

pause 1.5

window hide
show blank2 with splitfade
stop music fadeout 1.5
$ renpy.pause(2.0, hard=True)

hide calem
hide ethan
hide brendan

$ renpy.music.queue("Audio/Music/SoaringIllusions_Intro.ogg", channel='music', loop=None, tight=None)
$ renpy.music.queue("Audio/Music/SoaringIllusions.ogg", channel='music', loop=True, tight=None)

$ renpy.pause(1.0, hard=True)

show phone_B behind blank2
show phone_A behind blank2
with fadeinbottom

show mom behind phone_A:
    xalign 0.5 zoom 0.95

mom sad "{i}Oh, I'm sorry, honey!{w=0.5} When he decided to follow you, I just couldn't bring myself to stop him!{/i}"
mom -sad "{i}I meant to call you, but I don't think airplanes get reception when they're in the air!{/i}"
    
show dorm_empty_B behind phone_B

hide blank2 with dis

red sad "Then what about after I landed?"
mom "{i}Well, by the time I remembered, I figured you would've already found him.{/i}{w=0.5}{nw}"
mom happy "{i}Well, by the time I remembered, I figured you would've already found him. {fast}In fact, I was more surprised that you didn't call me first!{/i}"
hide blank2

show mom surprised with dis
red thinking "Ugh, Mom... you're lucky my roommate was there to cover for me or I would've been in big trouble!"

mom happymouth "{i}Oh, how{/i} is {i}your roommate?{w=0.5} Is he a nice boy? Where is he from? What does he look like?{/i}"
hide hilbert
show mom surprised with dis
red "Well, actually, I have four of them. But the one who covered for me was called Hilbert. He's, uh... a character." 
red -thinking "Anyway, I'll tell you all about them tomorrow.{w=0.5} I still have some stuff to sort out before heading to bed."
show mom -surprised with dis
red "Getting ready for the first day of classes on Monday and all that."
mom happy "{i}Oh, of course!{w=0.5} Good night, my beloved Champion! Talk to you tomorrow!{/i}"

show phone_B:
    ypos 1.0
    ease 1.0 ypos 3.0
        
show mom:
    parallel:
        ypos 1.0
        ease 1.0 ypos 3.0
    parallel:
        alpha 1.0
        ease 0.25 alpha 0.0
        
show phone_A:
    ypos 1.0
    ease 1.0 ypos 3.0

$ renpy.pause(2.0, hard=True)  


show hilbert with dis:
    xpos 0.2

show ethan with dis:
    xpos 0.4

show brendan with dis:
    xpos 0.6

show calem with dis:
    xpos 0.8

ethan "So, hey, [first_name] and I are going to be swapping between electives, but what about you guys? Where will you be?"

$ KnowClasses("Brendan", ["Bug", "Grass", "Ground"])
brendan angrybrow happymouth "Grass and Ground for me! I've got lots of experience with those, back home in Hoenn."

pause 1.0

brendan happybrow angrymouth "Oh, and... May forced me into taking Bug class with her... They kinda freak me out, but she likes 'em, so..."
$ KnowClasses("Calem", ["Fighting", "Flying", "Fairy"])
calem "Fighting, Flying, and Fairy are my preferences. I may dabble in another elective or two, for variety, but I imagine I'm largely set."

pause 1.0

ethan angrybrow frownmouth "I was asking you, too, Hutchinson."
hilbert sad "It's Hilbert."
hilbert "..."
$ KnowClasses("Hilbert", ["Steel", "Ice", "Ghost"])
hilbert -sad "And I'll be in Steel, Ice, and Ghost."

show hilbert at dissolveaway:
    xpos 0.2

pause 2.0

ethan happy "Of course he will. What an edgelord!"

show hilbert angry:
    xpos 0.2

show dorm_empty_B at vpunch

pause 1.0

show ethan surprised with dis
show brendan surprised with dis
show calem surprised with dis
hilbert "It's nothing like that! Ice is the most powerful offensive type, and steel is the most powerful defensive type! Choosing those two is just logical, and Ghost covers their Fighting weaknesses!"

pause 1.0

hilbert sad "Tch. I don't need to explain myself to you."

show hilbert at dissolveaway:
    xpos 0.2

pause 2.0

show calem thinking with dis
show ethan thinking with dis
brendan sad "Is... is that true? Are Ice and Steel the best types?"
calem "That depends on what you're looking for. Certainly, Steel types are known for their high defenses, and Ice types are known for their strong elemental advantages."
calem -thinking "But Grass and Ground types can do many things that the average Steel type or Ice type entirely lacks."
ethan happy "What he's saying is...{w=0.5} don't worry about it! No matter what you pick, you can't screw your education up {i}too{/i} badly."
calem "As long as you restrict yourself to two or three types, that is. It's certainly possible to 'screw yourself over' by spreading yourself too thinly."
ethan sad "Er...{w=0.5} yeah." 
ethan happy "Hahaha.{w=0.5} I know that. Don't worry, I've got plans!"

red happy "So do I! My plan right now, though, is to go to sleep!"
red -happy "You ready for bed, [pika_name]?"

$ renpy.sound.play("Audio/Pokemon/pikachu_excite2.ogg", channel="altcry", loop=None)

pikachu happy_2 "Pika!"

calem surprised "You're not going to keep him in his Poké Ball?"

red confusedeyebrows "No, why?"

stop music fadeout 2.0

calem thinking "I...{w=0.5} Well, where do you usually put him before you go to bed?"
queue music "Audio/Music/Opening_Intro.ogg" noloop

red sadeyebrows sadeyes "Right here with me.{w=0.5} Is that weird?"

calem happy "No, I suppose not."
brendan happy "I think it's weird!{w=0.5} But if you don't get shocked, then I guess it's fine?"
ethan "It's not weird! My Pichu back home does that exact same thing."
ethan -happy "If I ever try to put her in her Pokeball when I go to sleep, I wake up with her on my face at four in the morning."
brendan thinking "Huh! Maybe I'm the weird one, then."
brendan -thinking "Whatever. I'm gonna hit the hay now, dudes.{w=0.5} Night, [first_name], Calem, Ethan, Hilbert, and [pika_name]!"

show brendan at dissolveaway:
    xpos 0.6

calem happy "Yes, goodnight, all."

show calem at dissolveaway:
    xpos 0.8

ethan happy "See y'all tomorrow!"

show ethan at dissolveaway:
    xpos 0.4
    
    
red -sadeyebrows -sadeyes "Goodnight, guys."
red "Let's get some sleep, [pika_name].{w=0.5} We've got plenty of things to do this weekend before classes start."

pikachu neutral_2b "Pika Pi!"

window hide

show blank2 with Dissolve(1.0)
$ renpy.pause(1.0, hard=True)

show relichall_B with dis:
    alpha 1.0

redmind closedeyes "I'll admit. I'm a little scared that if I go to sleep now, I'll wake up and realize that getting into Kobukan Academy, which was always my dream, was just that--a dream."
redmind "But now I know it's real.{w=0.5} My subconscious isn't clever enough to have [pika_name] hitch a ride to Kobukan in my luggage. Even my wildest fantasies of getting into Kobukan didn't have that."
redmind happy "I'm glad he's here."
redmind thinking "...But we {i}really{/i} need to work on his patience."

window hide

scene blank2 with transball

stop music fadeout 1.0
$ renpy.pause(1.0, hard=True)

hide calem
hide brendan
hide ethan
hide hilbert

hide dorm_empty_B

$ renpy.pause(1.0, hard=True)

show text "{color=#ffffff}{size=40}Pokémon Academy Life{/size}{/color}":
    alpha 1.0 yalign 0.5 xalign 0.5
    pause 3.0
    linear 1.0 alpha 0.0
    
$ renpy.pause(4.0, hard=True)

$ renpy.movie_cutscene('videos/Intro.webm')
    
$ renpy.pause(2.0, hard=True)

jump victini0