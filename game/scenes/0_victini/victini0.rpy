label victini0:
    stop music
    show unknown at vspaz
    #show future at vspaz
    #$ renpy.transition(dissolve)
    pause 3.0


    # show victini exclaim:
    #    zoom 0.7 xpos 0.2 ypos 0.8 alpha 1.0
    #    ease 1.0 zoom 0.65 xpos 0.25 ypos 0.7 alpha 1.0 rotate 180
    #    ease 1.0 zoom 0.55 xpos 0.3 ypos 0.6 alpha 1.0 rotate -180
    #    ease 1.0 zoom 0.45 xpos 0.35 ypos 0.5 alpha 1.0 rotate 180
    #    ease 1.0 zoom 0.35 xpos 0.4 ypos 0.45 alpha 1.0 rotate -180
    #    ease 1.0 zoom 0.25 xpos 0.45 ypos 0.42 alpha 1.0 rotate 180
    #    ease 1.0 zoom 0.15 xpos 0.5 ypos 0.4 alpha 1.0 rotate -180

    show pikachu surprised:
        zoom 0.7 xpos 0.2 ypos 0.8 alpha 1.0
        ease 1.0 zoom 0.65 xpos 0.25 ypos 0.7 alpha 1.0 rotate 180
        ease 1.0 zoom 0.55 xpos 0.3 ypos 0.6 alpha 1.0 rotate -180
        ease 1.0 zoom 0.45 xpos 0.35 ypos 0.5 alpha 1.0 rotate 180
        ease 1.0 zoom 0.35 xpos 0.4 ypos 0.45 alpha 1.0 rotate -180
        ease 1.0 zoom 0.25 xpos 0.45 ypos 0.42 alpha 1.0 rotate 180
        ease 1.0 zoom 0.15 xpos 0.5 ypos 0.4 alpha 1.0 rotate -180
        ease 1.0 zoom 0.0 xpos 0.5 ypos 0.4 alpha 1.0 rotate 180

    show red surprised behind pikachu:
        zoom 0.7 xpos 0.8 ypos 0.8 alpha 1.0
        ease 1.0 zoom 0.60 xpos 0.75 ypos 0.7 alpha 1.0 rotate 60
        ease 1.0 zoom 0.50 xpos 0.7 ypos 0.6 alpha 1.0 rotate -60
        ease 1.0 zoom 0.40 xpos 0.65 ypos 0.5 alpha 1.0 rotate 60
        ease 1.0 zoom 0.30 xpos 0.6 ypos 0.45 alpha 1.0 rotate -60
        ease 1.0 zoom 0.20 xpos 0.55 ypos 0.42 alpha 1.0 rotate 60
        ease 1.0 zoom 0.10 xpos 0.5 ypos 0.4 alpha 1.0 rotate -60
        ease 1.0 zoom 0.0 xpos 0.5 ypos 0.4 alpha 1.0 rotate 60

    show time behind red
    window show dissolve

    window hide dissolve

    pause 7.0
    hide time
    hide red
    hide victini
    hide blank

    stop music
    play music "audio/music/Danger!Slow.mp3"

    scene dorm_A gray with squares

    red surprised "Urgh... what the heck just happened? I... {w=0.7} feel nauseus."
    red @talking2mouth "Did you guys feel that as well?{w=0.5} Calem?{w=0.5} Brendan?{w=0.5} Ethan?{w=0.5} ...Hilbert?"
    red confused "...Anyone?"
    $ renpy.music.play("Audio/Pokemon/pikachu_happy1.ogg", channel="altcry")
    pikachu yawn "chaaa..."
    red @talkingmouth "At least you're here, [pika_name]."
    $ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry")
    pikachu surprised "...Pika?"
    red "Yeah, I agree. This whole situation is very strange..."
    red @confused "In particular, this empty room is giving me the creeps... let's go searching to see if we can find someone around."

    scene hall_A gray with irisout

    red @talking2mouth "Helloooooo? Anyone here?"
    redmind thinking".{w=0.3}.{w=0.3}.{w=0.3}Nothing but silence. Are all of the rooms locked and empty?"
    $ renpy.music.play("Audio/Pokemon/pikachu_norm2.ogg", channel="altcry")
    pikachu neutral_4 "piiika."
    red surprised "Not even you can hear anything. [pika_name]? Then this place is truly abandoned."
    red @talkingmouth "We aren't finding any clues here... {w=.5}{nw}"
    extend @sad "No choice but to wander the academy grounds, despite there being a curfew."
    red @talkingmouth "Not like there'd be anyone around who could stop us."

    hide dorm_A gray
    scene darklands with fade
    show blank2 behind darklands

    narrator "Navigating away from the gray likeness of Relic Hall, you trek outside, and are met with a horrifying sight."
    red surprised "This isn't...{w=.5} the school I remember. What happened here?"
    $ renpy.music.play("Audio/Pokemon/pikachu_scared.ogg", channel="altcry")
    pikachu surprised "pika..."
    red @thinking "The campus was so lush and green, but now? {w=.4}Nothing but a gray darkness, as far as I can see..."
    redmind @sad "Worst of all, not a single soul in sight. It's like... {w=.5}back then."

    show pawniard as pawn1:
        xpos 1.2 ypos 0.3
        parallel:
            ease 2.0 xpos 0.5
        parallel:
            ease 0.5 rotate 5
            ease 0.5 rotate -15
            ease 0.5 rotate -5
            ease 0.5 rotate 15
            repeat
    $ renpy.music.set_volume(0.5, delay=0.0, channel="music")
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    pause 2.0

    red @happy "A Pawniard? So there is life here, after all!"
    
    $ renpy.music.play("Audio/Pokemon/pikachu_angry1.ogg", channel="altcry")
    pikachu angry_4 "Pika!"
    narrator "Tensing up, [pika_name] stood between you and the Pawniard, who was rapidly approaching, wielding a glint of malice which revealed its true intention."
    red @surprised "I guess this Pawniard isn't going to be compassionate...{nw} "
    extend @angry "Very well! Let's show it why you don't mess with us!"
    $ playerparty.append(Pokemon(25, level=6, nickname=pika_name, ivs=[3, 2, 5, 6, 3, 4], nature=Natures.Lax, gender=Genders.Male, ability="Freelectric"))

    $ pawniardobj = Pokemon(624, level=6, moves=[GetMove("Scratch")])
    $ sidemonnum = 624
    $ trainer1 = MakeRed()
    $ trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [pawniardobj], isPokemon=True)
    hide pawn1
    call Battle([trainer1, trainer2], healParty=False, specialmusic="Nothing", unrunnable=True, stopmusic=False) from _call_Battle_vic_0
    $ gymbattles["Pawniard"] = _return

    show blank2 behind darklands
    show pawniard as pawn1:
        xpos .5 ypos 0.3 rotate 0
        parallel:
            ease 4.0 xpos 1.2
        parallel:
            ease 0.5 rotate 5
            ease 0.5 rotate -15
            ease 0.5 rotate -5
            ease 0.5 rotate 15
            repeat
    pause 2.0
    #play music "audio/music/Danger!Slow.mp3"
    if gymbattles["Pawniard"] == False:
        narrator "Even though you lost, it seemed the Pawniard retreated..."
        red "No! [pika_name]!"
    else:
        narrator "After being defeated, the Pawniard slinked away."
        red "That was a tough battle... are you okay, [pika_name]?"
    
    $ renpy.music.play("Audio/Pokemon/pikachu_sad.ogg", channel="altcry")
    pikachu sad_2 "Pi...ka..!"
    red @sad "I'm sorry for making you go through this, buddy..."
    red "But... that Pawniard was acting strangely... Pokemon aren't normally so aggressive. Did it see this place as its territory?"
    red thinking "That can't be right. This is Kobukan Academy. Surely they would have dealt with wayward aggressive Pokemon...?"
    red @talkingmouth "But that all begs the question... {w=.5}What happened here? What happened to Kobukan to make it look like this?"

    show pawniard as pawn1 with vpunch:
        xpos 1.2 xanchor 0.5 zoom 0 xzoom 1 yalign 0.5 rotate 0
        parallel:
            easein 1.5 xpos .7 zoom 1.0 xzoom 1

    $ renpy.music.set_volume(0.5, delay=0.0, channel="music")
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

    $ renpy.music.play("Audio/Pokemon/pikachu_angry2.ogg", channel="altcry")
    pikachu angry_2 "Pi!"
    red surprised "The Pawniard is back... {w=0.5}already...?! Has it already recovered...? How...?"

    play music "audio/music/Danger!Fast.mp3"
    
    show pawniard as pawn2:
        xpos 1.2 xanchor 0.5 zoom 0 xzoom 1 yalign 0.8
        parallel:
            easein 1.3 xpos .80 zoom 1.0 xzoom 1
    show pawniard as pawn3:
        xpos -.2 xanchor 0.5 zoom 0 xzoom -1 yalign 0.5
        parallel:
            easein 1.5 xpos .3 zoom 1.0 xzoom -1
    show pawniard as pawn4:
        xpos -.2 xanchor 0.5 zoom 0 xzoom -1 yalign 0.8
        parallel:
            easein 1.3 xpos .20 zoom 1.0 xzoom -1
    $ renpy.music.set_volume(0.5, delay=0.0, channel="music")
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    pause 1.5
    red angry "And it brought friends."

    red "There are so many... there's no way we can hold them off."

    $ renpy.music.play("Audio/Pokemon/pikachu_scared.ogg", channel="altcry")
    pikachu sad_2 "pi...ka.."
    red @sad ".{w=0.2}.{w=0.2}.{w=0.2}"
    red @noeyes "[pika_name]. Run away as fast as you can. I'll buy some time for you, ok?"
    $ renpy.music.play("Audio/Pokemon/pikachu_norm4.ogg", channel="altcry")
    pikachu sad "pi...ka.. pika!"

    red @sad tears "You want to stay... together until the end?"
    $ renpy.music.play("Audio/Pokemon/pikachu_norm3.ogg", channel="altcry")
    pikachu bashful "Pika."

    red neutralmouth sadbrow @tears "You're the best friend I could have ever asked for."


    $ finalmatrix = ContrastMatrix(0.0)

    show pawniard as pawn1:
        zoom 1.0
        ease 1.0 xpos 0.6 zoom 1.2
    show pawniard as pawn2:
        zoom 1.0
        ease 1.0 xpos 0.7 zoom 1.2
    show pawniard as pawn3:
        zoom 1.0
        ease 1.0 xpos 0.4 zoom 1.2
    show pawniard as pawn4:
        zoom 1.0
        ease 1.0 xpos 0.3 zoom 1.2
    
    $ renpy.music.set_volume(0.5, delay=0.0, channel="music")
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/Pokemon/Cries/624.wav", channel='sound', loop=False, tight=None)
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")

    pause 1.0

    red @angry "...This is it!"

    pause 0.5
    stop music
    $ renpy.music.set_volume(0.5, delay=0.0, channel="music")
    $ renpy.sound.queue("audio/Pokemon/Cries/494.wav", channel='sound', loop=False, tight=None)
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    pause 1.2  
    # Victini appears
    show victini with hpunch:
        ypos -10.0 xpos 0.5 yzoom -1 matrixcolor finalmatrix
        parallel:
            ease 1.0 yzoom 1 ypos 0.5
    
    pause 1
    show screen songsplash("Battle! Legendary", "Zame")
    play music "Audio/Music/Battle!LegendaryUnovaZame.mp3"
    show victini:
        ypos .5 yzoom 1
        ease 0.1 ypos .49
        ease 0.1 ypos .5
        ease 0.1 ypos .51
        repeat

    show fire_attack01 as fire with dis:
        zoom 0.5 xpos 0.35 ypos 0.2 rotate 90 
        ease 0.1 ypos .19
        ease 0.1 ypos .2
        ease 0.1 ypos .21
        repeat

    pause .6   

    show fire_attack01 as fire1 with dis:
        zoom 0.5 xpos 0.55 ypos 0.4 
        ease 0.2 ypos 0.42
        repeat
        
    show fire_attack01 as fire2 with dis:
        zoom 0.5 xpos 0.55 ypos 0.2
        ease 0.2 ypos 0.22
        repeat
    show fire_attack01 as fire3 with dis:
        zoom 0.5 xpos 0.2 ypos 0.4 xzoom -1
        ease 0.2 ypos 0.42
        repeat
    show fire_attack01 as fire4 with dis:
        zoom 0.5 xpos 0.2 ypos 0.2 xzoom -1
        ease 0.2 ypos 0.22
        repeat
    
    pause 0.4

    show fire_attack01 as fire1:
        zoom 0.5 xpos 0.55 ypos 0.4 
        parallel:
            ease 1.2 xpos 1.2
    show fire_attack01 as fire2:
        zoom 0.5 xpos 0.55 ypos 0.2 
        parallel:
            ease 1.2 xpos 1.2
    show fire_attack01 as fire3:
        zoom 0.5 xpos 0.2 ypos 0.4 
        parallel:
            ease 1.2 xpos -.4
    show fire_attack01 as fire4:
        zoom 0.5 xpos 0.2 ypos 0.2
        parallel:
            ease 1.2 xpos -.4


    show pawniard as pawn1:
        ease 1.2 xpos 1.2 rotate 540
    show pawniard as pawn2:
        ease 1.2 xpos 1.2 rotate 540
    show pawniard as pawn3:
        ease 1.2 xpos -.2 rotate 540
    show pawniard as pawn4:
        ease 1.2 xpos -.2 rotate 540
    
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)

    red surprised @tears "A trainer? Out here? Wielding a... {w=1} creature of some kind that's this strong..?"
    # V-Ctrl-Del
    show pawniard as pawn1:
        xpos 1.2
        parallel:
            ease 4.0 xpos 0.7
        parallel:
            ease 0.5 rotate 5
            ease 0.5 rotate -15
            ease 0.5 rotate -5
            ease 0.5 rotate 15
            repeat
    
    show victini:
        parallel:
            ease 2.5 xpos .3
            ease 1.0 xpos .2
        parallel:
            ease 1.5 rotate 15
            ease 1.0 rotate 90
        parallel:
            ease 0.1 ypos .5
            ease 0.1 ypos .49
            ease 0.1 ypos .5
            ease 0.1 ypos .51
            repeat

    show fire_attack01 as fire:
        zoom 0.5 xpos 0.35 ypos 0.2 rotate 90
        parallel:
            ease 2.5 xpos .15
            ease 1.0 xpos .05
        parallel:
            ease 1.5 rotate 105
            ease 1.0 rotate 180
        parallel:
            ease 0.1 ypos .2
            ease 0.1 ypos .19
            ease 0.1 ypos .2
            ease 0.1 ypos .21
            repeat
    
    pause 3.5

    show victini:
        xpos 0.3 rotate 90
        parallel:
            ease .8 xpos 1.1
    
    show fire_attack01 as fire:
        xpos .05 rotate 180
        parallel:
            ease .8 xpos 0.95

    pause 0.4
    show pawniard as pawn1:
        xpos 0.7
        parallel:
            ease 0.5 ypos -.2 rotate -180
    pause 0.3

    # Pawniard Space Program
    show pawniard as pawn1:
        zoom 0.5 xpos 0.6 ypos -.2
        parallel:
            ease 0.25 rotate 90
            ease 0.25 rotate 180
            ease 0.25 rotate 270
            ease 0.25 rotate 360
            ease 0.25 rotate 450
            ease 0.25 rotate 540
            ease 0.25 rotate 630
            ease 0.25 rotate 720
            ease 0.25 rotate 810
            ease 0.25 rotate 900
            ease 0.25 rotate 990
            ease 0.25 rotate 1080
            repeat
        parallel:
            ease 3.0 ypos .5
        parallel:
            ease 0.5 zoom 0.4
            ease 0.5 zoom 0.3
            ease 0.5 zoom 0.2
            ease 0.5 zoom 0.12
            ease 0.5 zoom 0.05
            ease 0.5 zoom 0.0
        parallel:
            ease 0.5 xpos 0.57
            ease 0.5 xpos 0.54
            ease 0.5 xpos 0.51
            ease 0.5 xpos 0.48
            ease 0.5 xpos 0.46
            ease 0.5 xpos 0.45

    victini "Get outta here!"
    # Victini moves back on screen.
    show victini:
        parallel:
            ease 2.0 xpos 0.8 ypos 0.5 rotate 0 alpha 1
        parallel:
            ease 0.1 ypos .5
            ease 0.1 ypos .49
            ease 0.1 ypos .5
            ease 0.1 ypos .51
            repeat
    show fire_attack01 as fire:
        parallel:
            ease 2.0 xpos 0.65 ypos 0.2 rotate 90
        parallel:
            ease 0.1 ypos .2
            ease 0.1 ypos .19
            ease 0.1 ypos .2
            ease 0.1 ypos .21
            repeat
    
    show pawniard as pawn3:
        xpos -.2
        parallel:
            ease 6.0 xpos 0.3
        parallel:
            ease 0.5 rotate 5
            ease 0.5 rotate -15
            ease 0.5 rotate -5
            ease 0.5 rotate 15
            repeat
    
    pause 3.0
    victini "Still haven't had enough?! {w=0.5}Then have a taste of {nw}"
    # I'm far too dangerous to let fall into nefarious hands.

    # Searing Shot
    show fire_attack01 as fire2 with dis:
        zoom 0.5 xpos 0.55 ypos 0.4 xzoom -1 rotate -90
        ease 0.2 ypos 0.42
        repeat
    show fire_attack01 as fire3 with dis:
        zoom 0.5 xpos 0.55 ypos 0.00 xzoom -1 rotate -90
        ease 0.2 ypos 0.02
        repeat
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)

    extend "my {b}{color=f57c51}searing shot{/color}{/b}!"

    show fire_attack01 as fire:
        ease 1 xpos -.3 rotate 720
    show fire_attack01 as fire2:
        ease 1 xpos -.4 ypos 0.00 rotate 720
    show fire_attack01 as fire3:
        ease 1 xpos -.4 ypos 0.40 rotate -720
    
    pause 0.25

    show pawniard as pawn3:
        xpos 0.3 xzoom 1
        ease 1 xpos -.65 zoom 2.0 
    
    # Victini evade
    show pawniard as pawn1:
        xpos 1.2 ypos 0.5 zoom 1.0 rotate 0
        parallel:
            ease 0.4 xpos 0.75
            ease 1.0 xpos 0.90
        parallel:
            ease 0.5 rotate 5
            ease 0.5 rotate -15
            ease 0.5 rotate -5
            ease 0.5 rotate 15
            repeat
    hide victini with squares
    show victini angry with squares:
        zoom 1.0 xpos 0.5 ypos 0.5 alpha 1.0 rotate 0
        parallel:
            #ease 0.18 ypos .5
            #ease 0.18 ypos .49
            #ease 0.18 ypos .5
            #ease 0.18 ypos .51
            ease 0.1 ypos .5
            ease 0.1 ypos .49
            ease 0.1 ypos .5
            ease 0.1 ypos .51
            repeat
    

    victini @exclaim "Trying to get a cheapshot in on me, pawn of darkness?! I won't stand for that!"
    hide fire
    hide fire1
    hide fire2
    hide fire3
    hide fire4
    # Fire Spin
    show fire_attack01 as fire1:
        xpos .5 ypos 0.05 alignaround(.5,.4) zoom 0.25 rotate 90
        linear 1 yalign 0.05 xalign .5 clockwise circles 1
        repeat
    pause 0.125
    show fire_attack01 as fire2:
        xpos .5 ypos 0.05 alignaround(.5,.4) zoom 0.25 rotate 90
        linear 1 yalign 0.05 xalign .5 clockwise circles 1
        repeat
    pause 0.125
    show fire_attack01 as fire3:
        xpos .5 ypos 0.05 alignaround(.5,.4) zoom 0.25 rotate 90
        linear 1 yalign 0.05 xalign .5 clockwise circles 1
        repeat
    pause 0.125
    show fire_attack01 as fire4:
        xpos .5 ypos 0.05 alignaround(.5,.4) zoom 0.25 rotate 90
        linear 1 yalign 0.05 xalign .5 clockwise circles 1
        repeat
    pause 0.125
    show fire_attack01 as fire5:
        xpos .5 ypos 0.05 alignaround(.5,.4) zoom 0.25 rotate 90
        linear 1 yalign 0.05 xalign .5 clockwise circles 1
        repeat
    pause 0.125
    show fire_attack01 as fire6:
        xpos .5 ypos 0.05 alignaround(.5,.4) zoom 0.25 rotate 90
        linear 1 yalign 0.05 xalign .5 clockwise circles 1
        repeat
    pause 0.125
    show fire_attack01 as fire7:
        xpos .5 ypos 0.05 alignaround(.5,.4) zoom 0.25 rotate 90
        linear 1 yalign 0.05 xalign .5 clockwise circles 1
        repeat
    pause 0.125
    show fire_attack01 as fire8:
        xpos .5 ypos 0.05 alignaround(.5,.4) zoom 0.25 rotate 90
        linear 1 yalign 0.05 xalign .5 clockwise circles 1
        repeat
    victini happy "Let's go for a {color=f57c51}{b}spin{/b}{/color}!"
    show victini:
        parallel:
            ease 2.0 rotate 720
        parallel:
            ease 0.1 ypos .5
            ease 0.1 ypos .49
            ease 0.1 ypos .5
            ease 0.1 ypos .51
            repeat
    show fire_attack01 as fire1:
        parallel:
            ease 3.5 alignaround(1.2,.4)
        parallel:
            linear 0.5 yalign 0.05 xalign .6 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .7 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .8 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .9 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.0 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.1 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.2 clockwise circles 1
    pause 0.125
    show fire_attack01 as fire2:
        parallel:
            ease 3.5 alignaround(1.2,.4)
        parallel:
            linear 0.5 yalign 0.05 xalign .6 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .7 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .8 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .9 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.0 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.1 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.2 clockwise circles 1
    pause 0.125
    show fire_attack01 as fire3:
        parallel:
            ease 3.5 alignaround(1.2,.4)
        parallel:
            linear 0.5 yalign 0.05 xalign .6 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .7 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .8 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .9 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.0 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.1 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.2 clockwise circles 1
    pause 0.125
    show fire_attack01 as fire4:
        parallel:
            ease 3.5 alignaround(1.2,.4)
        parallel:
            linear 0.5 yalign 0.05 xalign .6 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .7 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .8 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .9 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.0 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.1 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.2 clockwise circles 1
    pause 0.125
    show fire_attack01 as fire5:
        parallel:
            ease 3.5 alignaround(1.2,.4)
        parallel:
            linear 0.5 yalign 0.05 xalign .6 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .7 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .8 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .9 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.0 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.1 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.2 clockwise circles 1
    pause 0.125
    show fire_attack01 as fire6:
        parallel:
            ease 3.5 alignaround(1.2,.4)
        parallel:
            linear 0.5 yalign 0.05 xalign .6 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .7 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .8 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .9 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.0 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.1 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.2 clockwise circles 1
    pause 0.125
    show fire_attack01 as fire7:
        parallel:
            ease 3.5 alignaround(1.2,.4)
        parallel:
            linear 0.5 yalign 0.05 xalign .6 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .7 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .8 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .9 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.0 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.1 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.2 clockwise circles 1
    pause 0.125
    show fire_attack01 as fire8:
        parallel:
            ease 3.5 alignaround(1.2,.4)
        parallel:
            linear 0.5 yalign 0.05 xalign .6 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .7 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .8 clockwise circles 1
            linear 0.5 yalign 0.05 xalign .9 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.0 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.1 clockwise circles 1
            linear 0.5 yalign 0.05 xalign 1.2 clockwise circles 1
    pause 1.5
    show pawniard as pawn1:
        ease 1.5 xpos 1.2 rotate 1080
    pause 1.5
    
    
    victini neutraleyes neutraleyesparkles smirkmouth -happy"Checkmate!{w=0.5} Anyone else want a go?{w=0.2} No? {w=.2}I thought so! {w=.2}It turned out you were all wicked weak after all!"
    victini happyeyes "Hey, wait. You there, guy in the red hat. You and your partner happy and healthy?{w=.5} Well, in this case, I suppose only the latter matters."
    narrator "Attempting to find the trainer calling out, [first_name] pivoted around, searching fruitlessly."
    hide pawn1
    hide pawn2
    hide pawn3
    hide pawn4
    hide fire1
    hide fire2
    hide fire3
    hide fire4
    hide fire5
    hide fire6
    hide fire7
    hide fire8
    show victini angry:
        zoom 1.0 xpos 0.5 ypos 0.5 alpha 1.0 rotate 0
        parallel:
            ease 2.0 xpos 0.1 ypos 0.5 alpha 1.0
            ease 4.0 xpos 0.9 ypos 0.5 alpha 1.0
        parallel:
            ease 0.1 ypos .5
            ease 0.1 ypos .49
            ease 0.1 ypos .5
            ease 0.1 ypos .51
            repeat
    red @confused "Whoever is speaking to me, could you reveal yourself, please?"
    victini done "What, can't believe your eyes nor ears? Take another view upon the glorious sight ahead!{w=0.5} ...I'm right in front of you, geez."
    show victini happy:
        parallel:
            ease 1.2 xpos 0.5 ypos 0.5 alpha 1.0
        parallel:
            ease 0.18 ypos .5
            ease 0.18 ypos .49
            ease 0.18 ypos .5
            ease 0.18 ypos .51
            repeat
    
    red @surprised "...What... {w=.5}what... is this...?"

    victini @wink talking "Erm... you good, my man? Those {b}things{/b} didn't stab you in the frontal cortex before I arrived, did they?"

    redmind @thinking "This is a living creature, maybe even a Pokemon... {w=0.5}but, I've never seen anything like it. {w=0.5}An {b}Ultra Beast{/b}... perhaps?"
    redmind "This certainly isn't in any Pokedex I've ever read... I don't know what this is. I'll need to be cautious with every word I say."

    red "If I truly am talking to who I think I am... may I ask, what exactly are you?"

    victini playfulmouth happy2eyes "Isn't it obvious? I'm a Pokemon, and the greatest there is!"

    red "I'm talking... {w=0.3}to a Pokemon? {w=.3}In English, of all languages? This night just keeps getting stranger by the minute..."

    victini neutraleyes eyesparkles @talkingmouth "Welllll--more like I'm telepathically sending word-waves directly into your mind, but potato potato!"
    victini @sadeyes frownmouth "If I actually tried to SPEAK to you, all you'd probably hear is a high-pitched voice! So I'm settling with this."
    victini @surprisedmouth "In any case, what the heck are you doing here? You don't seem {color=000000}{b}corrupted{/b}{/color}... That's a rarity around these parts!"

    red confused "Corrupted?!{w=0.3}{nw}"
    extend thinking " Is that what was going on with the Pokemon I just battled?"

    victini @exclaim "And got your ass kicked by? Who'd have done who knows what with you if I hadn't shown up in the knick of time like a hero in the storybooks of yore? Correct. Exactly. {w=.5}{size=-10}...Correctamundo? {w=.5}{size=-10} Nah, that's too corny, can't say that."

    red angry "Didn't need to phrase what just happened so casually! it was a rather serious situation.{w=1.0} But could you go into greater detail about what these ''corrupted'' are?"

    victini done "Nah. We're in the middle of a bloody battlefield, and you're going fishing for dissertations on subjects above your paygrade?"
    victini @angry "We don't have a lot of time until the next group comes. If you want to be talking, you should answer MY question first."

    red thinking "...Hmm?"

    victini angry "How did you get here? That one. I know the environment is a little dull out here, but I wasn't expecting you to match the drapes."

    red thinking "I... I'm not quite sure. I was getting some sleep, and then all of a sudden I fell into some strange space, before being plopped in this realm."
    victini @sadeyes surprisedmouth "So our stories align quite closely..."
    victini @angry "Regardless, we NEED to get out of here, immediately. We'll be spotted from a mile away if we stay here, so the nearest abandoned building will be our best bet."
    redmind @thinking "I can't help but feel that this is too good to be true, but...{w=.5} what other options do we have?"
    red talking2mouth "{size=-10}...Hey, [pika_name]. Can we trust this Pokemon?"
    narrator "At your question, [pika_name] responded by strolling toward the mysterious interloper, eventually coming to a stop and staring, to which the gaze was met in kind."
    victini normal "...Hello{w=.3}, {cps=*2}small cute yellow mouse creature.{/cps}"

    $ renpy.music.play("Audio/Pokemon/pikachu_pikapika1.ogg", channel="altcry")
    pikachu happy_3 "Pika pika!"
    victini happy "Ah...! {w=.5}A Pikachu! {size=-10}{w=.5}I've heard of that one before..."
    $ renpy.music.play("Audio/Pokemon/pikachu_excite5.ogg", channel="altcry")
    pikachu happy_2 "Pi-ka-chu!"
    victini @playfuleyes "Oh, really?{w=.5} I'd be very curious to know more, perhaps another time."
    red @thinking "...{w=0.5}Ok, I trust you. Lead the way."
    victini @normal "Hmm? I haven't a clue what you're thinking aloud, but at least now you're sensible! Let's go!"
    stop music fadeout 3.0
    show victini:
        xpos .5 ypos .5
        ease 1.0 xpos 1.2
    pause 1.0
    $ renpy.transition(dissolve)
    scene research gray with wiperight
    hide victini
    show victini with dis:
        xpos -.2 ypos .5
        ease 1.0 xpos 0.5
    pause 1.0
    show victini:
        xpos .5 ypos .5
        parallel:
            ease 0.18 ypos .5
            ease 0.18 ypos .49
            ease 0.18 ypos .5
            ease 0.18 ypos .51
            repeat
    pause 1.0
    play music "audio/music/runawayfugitives.mp3"
    narrator "Following the rather strange {w=.2}{i}Pokemon{/i}, you dash into a building with a plaque reading ''Research Center''."
    red @confused "...So this building is abandoned as well? {w=.5}Why is that so common here?"
    victini @sadeyes angrymouth "Trust me, it's better that way. The types that have the courage to enter buildings are NOT to be trifled with, even if we're packing power beyond compare. {w=0.5}{size=-10}Well, more {i}I{/i} than we, seeing as how you almost just got merc'd again on the way here."
    red @angry "You know, I can hear you, and I was {i}not{/i} almost just merc'd!"
    victini @exclaim "Sure, sure, feel free to tell yourself that next time as well. We both know it's true."
    victini normal "But first, let me just take care of a tini little thing..."
    show victini angry
    narrator "Closing its eyes briefly and theatrically pointing at the lab desks, the {i}Pokemon{/i} lifted a pair of desks with something that seemed akin to Psychic powers, placing them in front of the doors as barricades."
    victini normal "There we are. We're still screwed if we're seen through these {i}humongous{/i} windows, but at least the doors won't be an issue."
    redmind thinking "It seems as though I'm now trapped within this building, rather than the other way around... but may as well make conversation while I'm here."
    red @neutraleyes "So, you must be a Fire and Psychic typed Pokemon?"
    victini @exclaim "Good observation. Though rather obvious, based upon what you've already seen me do."
    victini @angryeyes "Anyways.{w=.5} Tell me everything about how you got here.{w=.5} All of it.{w=.5} I need to know.{w=.5} Now."
    red @normal "Well, as I said before... I was getting some rest, which from what I recall, was perfectly normal, besides the alien bed."
    victini @angry "...Alien bed?{w=.5} What, are invaders from another world purveyors of silky bedding now?"
    red @talking2mouth "I didn't mean it that way. What I meant was, this was my first night at the academy, so the bed was completely new to me."
    victini @talking "And then you said you were transported here in your sleep by a mysterious portal thinga-whatever, right?"
    red @talkingmouth "That's correct. [pika_name] was dragged along with me too, but my four roommates were nowhere to be found..."
    victini "And these roommates of yours... they around your age?"
    red @happy "Also correct. Have you seen them?"
    victini @sadeyes frownmouth ".{w=.5}.{w=.5}.{w=.5} Hmm...{w=.5} I don't believe so."
    victini "Sorry about that, don't mind me. Please continue your tale."
    red @thinking "Well... the first thing I did was search my dorm for any sign of life."
    red @sad "That failed horribly. {w=.5}So we went outside, to where the garden... {w=.3} should have been. You saw what happened next."
    victini @exclaim "Ha! So, in summary: the first night you go to school, you had the misfortune of ending up here, alone with your Pikachu?"
    victini @sadeyes frownmouth "It'd be hilarious if this place weren't so dire. You were in real danger. And so unprepared to face it."
    victini angry "To add on to that, you put [pika_name] in danger! Never fight an unknown threat alone!"
    red @surprised "Isn't that what you've been doing yourself: fighting alone?{w=.5} I don't see you with anyone."
    victini @exclaim "The difference is: I can spew fire and fly, you can't!{nw} "
    extend normal "{w=.5}Besides, even one as amazing as {i}I{/i} avoids battles when strategically condusive."
    if gymbattles["Pawniard"] == False:
        victini @angry "Also, you couldn't even beat a singular Pawniard on your own when [pika_name] was more than strong enough to take it on!"
        victini @angry "That's just pure trainer incompetence. {w=.5}Either that, or an unlucky crit, I suppose."
    red @frownmouth neutraleyebrows "Alright, I get it. Let's move on. Don't need to beat a dead ponyta."
    redmind thinking "There are so many strange things going on around here... but now that I have time to think, one particular subject is driving me crazy..."
    red @talking2mouth "Let me ask something. If I came here as I slept, wouldn't it mean that this all just a dream? So when I wake up, I'll not have to deal with this place anymore, right?"
    victini sadeyes frownmouth @eyesparkles2 "I doubt that's the case. I've been stuck here for what feels like weeks myself. Not that I can keep track of time, with how {color=808080}{b}gray{/b}{/color} everything here is at all hours."
    red @talkingmouth "Hmm...{w=.5} But if this was a dream, wouldn't you just be a figment of my imagination?"
    victini @done "That's some real ''How can the world be real if my eyes aren't real'' philosophy there. {nw}"
    extend @normal "Besides, how would you have even imagined me in the first case? You don't know what I am. You said as much earlier."
    red @confused "A subconscious doesn't need to name something that it imagines, you know..."
    victini done "Mrgrgr..."
    pause 1.0
    show victini angry
    narrator "Interrupting the conversation was a deafening stomach growl, with the discomfort on the Pokemon's face growing immense."
    red "Was that your stomach?"
    victini frownmouth playfuleyes "Yes. {w=.5} ...Urgh. That one really {cps=4}hurt{/cps}."
    red @surprised "You aren't looking too good. Don't strain yourself too much, okay?"
    show victini:
        ease 1.0 rotate 90 zoom 0.75 ypos .67
    narrator "Following your advice, the Pokemon laid itself on the lab desk at the head of the class."
    victini @talking "Good idea, I'll just rest here for a bit, can't waste any more energy..."
    $ renpy.music.play("Audio/Pokemon/pikachu_scared.ogg", channel="altcry")
    pikachu surprised "Pika..."
    narrator "Right on cue, [pika_name]'s stomach lightly grumbled as well. Quickly followed by you."
    victini sadmouth "I see. So you both are hungry as well. You're not nearly at the same desperation as myself...{w=.5} but..."
    victini sadeyes eyesparkles2 "It felt real, didn't it? {w=.5}The {b}hunger{/b}?"
    red @confused "Just as real as it would if I were awake..."
    victini sad "It's proof that this world {i}is no dream{/i}."
    victini "Despite how this world appears, if you stay here long enough, you WILL get hungry. And thirsty. Sleepy, too. {w=.5}All other bodily functions continue on as normal, if you were curious."
    victini "The true danger of this world is not just the obvious {b}corrupted{/b} that you've seen. The silent killer is our own mortal body; our own needs."
    victini closedeyes frownmouth "I've only survived this long because I had enough foresight to travel with plentiful rations. And because I'm able to easily boil my own clean water."
    victini "But even doing that, I've run out of food a few days ago. There are no supplies in this world worth salvaging. I'm running on literal fumes."
    red @surprisedmouth sadbrow "So you're saying... if we don't find a way to escape this place, we'll starve to death? {w=.5}And by fighting too much, we'd only be burning what energy we have left at a faster rate?"
    victini angryeyes frownmouth eyesparkles2 tears2 "Yeah. That sums it up. We're in a damned if you do, damned if you don't type of situation."
    red @angrybrow talking2mouth "So what should we do? What action can we take?"
    victini "...{w=.5} There's not much we can do... "
    red talking2mouth @surprisedeyes "What?! What are you saying?"
    victini @sad tears2 "I'm saying it's over for us. {w=.5}We're surrounded by a world that wants us dead, utterly devoid of sustenance. Even if we could find a way out, it'd be smashed to pieces before our eyes."
    victini @sad tears "If I'd had enough strength to escape... {w=.5}I'd have left weeks ago. {w=.5}But I couldn't manage even that. Not even at my best."
    victini sad tears cry"And look at me now. A crumpled heap. It's over."
    red @thinking ".{w=.5}.{w=.5}.{w=.5} No."
    stop music fadeout 1.0
    play music "audio/music/themeofhope.mp3" fadein 5.0
    red @happyeyebrows "...I refuse to believe that. {w=.5}{nw}"
    extend @angrymouth "I refuse to say it's over, just like that! After all, we're still alive, aren't we?"
    red @happyeyebrows "What happened to the Pokemon who proclaimed themselves as the greatest that there was?! Are you truly going to just give up?"
    red "Because while I'm still alive, I won't let us die in such pity! I'm just a powerless human, with no mastery of fire nor flight! So if I refuse to surrender, what's your excuse?"
    victini surprisedmouth ".{w=.2}.{w=.2}."
    red "There has to be a way back, and we're going to find it! Together!"
    red "You don't have to take on this world alone like you have up until now, because we'll be able to support each other! We'll shoulder this burden together!"
    $ renpy.music.play("Audio/Pokemon/pikachu_excite4.ogg", channel="altcry")
    pikachu neutral_2b "Pika!!!"
    red happy "See? [pika_name] agrees with me, too."
    red @closedbrow tears "Between the three of us, we still have hope! Hope to get back! Hope to {w=.5}{i}{cps=8}live{/i}{/cps}! {w=.5}No matter how dire, we still live, so we can still have hope!"
    victini unamusedmouth tears2".{w=.5}.{w=.5}."
    red happy tears ".{w=.5}.{w=.5}."
    victini normal -cry "...Heh. {w=.5} Heh heh."
    victini @smirkmouth angryeyes"...{w=.5}I was wrong. {w=.5} Completely wrong in my judgement of you. There's something more to you than what is visible, it seems."
    victini @talking "I don't know what I was thinking... {w=.5}you're right. We have to try. To go out like this... {w=.5}would be pathetic. I'd stain my heritage by doing such a thing."
    show victini:
        rotate 90 zoom 0.75 ypos .67
        ease 3.0 rotate 0 ypos .55
    victini happy -tears2  "Very well then! I'll choose to believe in this {i}hope{/i} of yours."
    victini happymouth "Still, hope in by itself is not a {b}plan{/b} of action. We need one, so let's get down to it."
    victini talking "...You said you arrived here through some sort of portal, right? {w=.5}That may be our only ticket out of here."
    red -tears "Yeah, and it spit me out to this strange world's version of my dorm room."
    victini winkeyes smirkmouth "Was this portal still visible after you arrived?"
    red @closedeyes talking2mouth "No... all I saw was the gray version of my room."
    victini @angry "Knew it wouldn't be so easy... {w=.5}but if that was truly where you arrived from... {w=.5}perhaps there are traces..."
    red @surprisedeyes surprisedmouth "Traces of what?"
    victini "Traces of a portal. These types of things can come in many varieties; time, space, dimensional to name a few."
    victini @talking "Some beings have adapted their entire skillset to create and travel through these portals. {w=.5}They're exceedingly rare, to the point where one could call them: {w=.5}mythical."
    victini sadeyes "My species isn't particularly known for doing this sort of thing... {w=.5}and I've never successfully done it myself."
    red "But you are saying that you think you can do it?"
    victini sadeyes frownmouth "It's... complicated. I'll try to explain."
    victini talking "Think of these portals like a densely packed path in the woods. The first one exploring will need to put in a ton of effort, and break ground on a path never traveled."
    victini neutraleyes @happymouth "But, as more traverse this path... {w=.5}the trek will become less daunting. The footsteps will create a path of dirt, and perhaps eventually, brick or stone. But it takes a long time to get to that point."
    red neutraleyes @talkingmouth "So you're concerned that the portal we're aiming for is unexplored?"
    victini @playfuleyes frownmouth "It's undoubtedly been used once, to bring you here. But to travel in the other direction? {w=.5}That may be a fresh path."
    red @talking2mouth "If you have even the slightest possibility for success, I'll do everything to help you make it happen."
    victini @normal "...Hmm. {w=.5} I dare not quantify our chances, but with me in my current condition, our chances are low. {w=1.0}{nw}"
    extend smirkmouth angryeyes "But not none."
    red @happy "Then that settles it. Our destination is decided."
    victini talkingmouth "This dorm of yours. Do you know how to get back there?"
    red @confused "I've only been on campus for a day, but I know I'd be able to recognize it. Getting there without losing my way... {w=.5}not completely sure."
    victini @sadeyes frownmouth "That hall is where all of our hope lies. {w=.5}If there's no portal there... {w=0.5}well..."
    red "It will be there. And we'll go through it. All of us."
    victini @happy "Then, what are we waiting for? We have a portal to find!"
    show blank2 with Dissolve(1.0)
    narrator "Guiding the group, you tread a path in the direction of Relic Hall."
    narrator "With the energetic Pokemon keeping an eye out for enemies, you're able to travel through the area relatively unscathed."
    narrator "Finally, you arrive to the front gate of the fated hall."
    #red neutral "...Thanks for the save."
    # "I mistook your optimism and inner strength for naivety. But even when faced with uncountable odds, you still wanted to fight. I needed a reminder."

    #victini happy "You're welcome!"
    show relichall_A gray with Dissolve(1.0)
    hide blank2
    hide victini
    # look into monochrome!
    red surprised "Hmm... if I turn this way, it should be the hall I'm looking for...{w=.5}{nw}"
    extend happy "Ah! Here it is."
    victini angryeyes unamusedmouth "So this is the hall.{w=.5} To think that I've passed by this so many times without a second thought."
    red @talking2mouth "Let's get inside, I don't want to be out here in this creepy place any longer."
    victini angrymouth "Halt! Not a step closer!"
    red @confused "Wait, what do you--{w=.5}oh. There's a Crawdaunt at the entrance. "
    $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
    $ renpy.sound.queue("audio/Pokemon/Cries/342.wav", channel='sound', loop=False, tight=None)
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    show crawdaunt with dis:
        xpos .66 ypos .5 zoom .5
        parallel:
            ease 0.5 rotate 2
            ease 0.5 rotate -6
            ease 0.5 rotate -2
            ease 0.5 rotate 6
            repeat
    pause 1.0
    victini @angry anger "Yeah, and I recognize this bastard. Hits hard, and I can't do a thing to hurt it."
    red @neutraleyebrows talking2mouth "That's probably because it being Water/Dark is a direct counter to your Fire/Psychic..."
    victini @angry sweat "Well, I was gonna say it was more because of my shellfish allergy, but you make a surprisingly good point."
    victini @sad "haaaaaa...{w=.5} really wishing I had some coverage moves right about now. In my current condition, this'd wipe me out."
    red @angrybrow talking2mouth "So what's the plan? Are we going to wait for it to leave?"
    victini angryeyes talking "No. [pika_name] is going to have to fight the Crawdaunt. [pika_name]'s Electric typing is a direct counter to ugly bubblers."
    $ renpy.music.play("Audio/Pokemon/pikachu_confused.ogg", channel="altcry")
    pikachu surprised "Pika?"
    red @surprised "...{w=.5}What?!? {w=.5}But Crawdaunt are typically level 30, based on when they evolve from Corphish... asking [pika_name] to take on a Pokemon that high level is insane!"
    victini smirkmouth "That may be so... but there's one trick up my sleeve which can turn the tides in this situation."
    victini happy "Besides, weren't you the one that said that we'd need to grasp for any possibility of success?"
    red @confused "...What's your trick?"
    victini happy2eyes "Just have [pika_name] sit tight for a moment, and all will be clear!"
    red @confusedeyebrows talkingmouth "Ok. Show me what you've got in mind!"

    victini @angry "Alright... my time to shine.{w=.5} Are you ready, [pika_name]?"
    show pikachu surprised:
        xpos .3 ypos .6 zoom .8    
    $ renpy.music.play("Audio/Pokemon/pikachu_norm4.ogg", channel="altcry")
    show victini happymouth angryeyes with squares:
        xpos .3 ypos .6 zoom 0.7
        parallel:
            ease 0.18 ypos .6
            ease 0.18 ypos .59
            ease 0.18 ypos .6
            ease 0.18 ypos .61
            repeat
    pause 1.0
    pikachu surprised "pika pika."
    victini @happy "A confused yes is still a yes!"
    victini @exclaim "...OK!"
    victini @exclaim "This is my blessing from me to you! Please, take it!"
    show victini exclaim:
        xpos 0.4 ypos .55
        parallel:
            easein_expo .5 xpos .3 ypos .8
            easeout_expo .5 xpos .4 ypos .55
            easein_expo .5 xpos .5 ypos .8
            easeout_expo .5 xpos .4 ypos .55
            repeat
    play sound "audio/Stat_Increase.wav"
    pause 0.5
    play sound "audio/Stat_Increase.wav"
    pause 0.5
    play sound "audio/Stat_Increase.wav"
    pause 0.5
    play sound "audio/Stat_Increase.wav"
    pause 0.5
    play sound "audio/Stat_Increase.wav"
    show pikachu cocky_2b
    $ renpy.music.play("Audio/Pokemon/pikachu_excite1.ogg", channel="altcry")
    pause 1.5
    pikachu cocky_2b "Pi-ka!"
    show victini:
        parallel:
            ease 2.0 xpos .3 ypos .5
        parallel:
            ease 0.18 ypos .6
            ease 0.18 ypos .59
            ease 0.18 ypos .6
            ease 0.18 ypos .61
            repeat
    victini angryeyes happymouth "{w=.5}Feel the newfound strength coursing through your veins, and vanquish the poor tortured souls who dare to oppose {i}victory{/i} in its purest form!"
    red @surprised "Wow, [pika_name], I've never seen you so energized! What did you do to him?"
    victini @happy "That's a trade secret! But let's just say..."
    victini @happy "With my power, you can't lose!"
    victini @pissed anger "No, you won't lose. We'll get back to your world, even if we need to scratch and claw for every inch!!"
    victini @exclaim "Let's boil this crawfish with shocking thunder!"
    red @angrybrow happymouth "Couldn't have said it better myself! Time to shell this fool!"
    $ attempt = 0
    label crawbattle:
        hide crawdaunt
        hide victini
        hide pikachu
        $ playerparty[0].SetVicTouched(20)
        $ crawdauntobj = Pokemon(342, level=24, moves=[GetMove("Taunt"),GetMove("Water Gun"),GetMove("Hone Claws"),GetMove("Swift")], nature="Adamamt", ivs=[0,0,0,0,0,0], ability="Hyper Cutter")
        $ sidemonnum = 342
        $ trainer1 = MakeRed()
        $ trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [crawdauntobj], isPokemon=True)
        #hide pawn1
        
        stop music
        play music "audio/music/BOSSBATTLE Remix PMD.mp3"
        call Battle([trainer1, trainer2], healParty=True, specialmusic="Nothing", unrunnable=True, gainexp=False, catchable=False, victiniwatch=True) from _call_Battle_vic_1
        $ gymbattles["Crawdaunt"] = _return
        $ playerparty[0].ResetVicTouched()

        if gymbattles["Crawdaunt"] == False:
            victini sad "How... how could you lose... even with my power..."
            if attempt is 0:
                $ ValueChange("Victini", -1, 0.2)
            if attempt is 1:
                victini @angry "Stop losing."
            if attempt is 2:
                victini @angry "You.... {w=.5}lost multiple times..."
            if attempt > 2:
                victini @angry "You.... {w=.5}lost multiple times... are you trying to lose?"
            if attempt is 9:
                victini @angry "Ten losses? {w=.5} Yeah, perhaps this Crawdaunt was too much for us."
                victini @sad "I guess we won't make it out of here after all..."
                $ renpy.quit()
            $ attempt = attempt + 1
            victini @angry "No. This time I will be the one to reject the reality in front of me! Rise again, brave warrior! Just use Thundershock! Please!"
            jump crawbattle
    play music "audio/music/themeofhope.mp3" fadein 5.0
    show victini:
        xpos 0.1 ypos 0.6 zoom 0.8
        parallel:
            ease 0.18 ypos .6
            ease 0.18 ypos .59
            ease 0.18 ypos .6
            ease 0.18 ypos .61
            repeat
    show pikachu cocky_2b:
        xpos .3 ypos .6 zoom .8   
    show crawdaunt:
        xpos .66 ypos .5 zoom .5
        parallel:
            ease 0.1 rotate 2
            ease 0.1 rotate -6
            ease 0.1 rotate -2
            ease 0.1 rotate 6
            repeat
    pause 3.0
    $ renpy.music.set_volume(0.1, delay=0.0, channel="music")
    $ renpy.sound.queue("audio/Pokemon/Cries/342.wav", channel='sound', loop=False, tight=None)
    $ renpy.music.set_volume(1.0, delay=1.0, channel="music")
    hide crawdaunt with wipeleft
    victini exclaim "Yes! You did it!"
    $ ValueChange("Victini", 1, 0.2)
    if attempt > 0:
        victini @sad "A shame it took multiple tries, though..."
    red @surprised "I can't believe you managed to take that Crawdaunt down, [pika_name]! You did great!"
    $ renpy.music.play("Audio/Pokemon/pikachu_excite1.ogg", channel="altcry")
    pikachu cocky_2b "Pika!"
    
    red @surprised "Speaking of which... did that Crawdaunt just... disappear...?"
    victini happyeyes smirkmouth "Yup. That happens a lot. {w=.5}You get used to it."
    show victini:
        zoom 0.8
        ease 1.0 xpos 0.7 ypos 0.6
    pause 1.5
    show victini done with vpunch:
        xpos 0.7 ypos 0.6
        ease .2 ypos 1.0
    victini @done "...Urgh. {w=.5}{size=-10}That took a lot more out of me than I thought it would..."
    show victini sad:
        xpos 0.7 ypos 1.0
        parallel:
            ease 2.0 ypos .5
        parallel:
            ease 0.4 xpos 0.65
            ease 0.4 xpos 0.75
            ease 0.4 xpos 0.65
            ease 0.4 xpos 0.75
            ease 0.4 xpos 0.7
    pause 2.0
    show victini normal:
        xpos 0.7
        parallel:
            ease 0.18 ypos .5
            ease 0.18 ypos .49
            ease 0.18 ypos .5
            ease 0.18 ypos .51
            repeat
    pause 1.5
    show pikachu cocky_2
    pause 0.5
    red @surprisedeyes talking2mouth "Hmm? Seems you're back to normal, [pika_name]."
    

    menu: 
        ">Ask the Pokemon about what just happened.":
            red @surprised "Whatever you did, it seems to have worn off. What was that, anyway?"
            victini @smirk "The magnificent blessing I give isn't permanent.{w=.5} But it was more than enough to win the fight, right?"
            red @talkingmouth "It was... but how did you do that...?"
            victini @talking sadeyes"Later.{w=.5} If we survive, that is."

        ">Ask if the Pokemon is alright.":
            red @talkingmouth "How are you feeling? {w=.5}Need a ride on my shoulder?"
            victini @angryeyes smirk "As much as I want to rest... I'll be fine. {w=.5}Something this tini won't bring me down!"
            red happymouth @happyeyes "Ok, I'll hold to you that!"
            victini "{size=-10}...{w=.5}Thanks."

    red @talking2mouth "Anyways, now that the entrance is clear, we shouldn't have an issue with any Pokemon inside, right?"
    victini @sadeyes frownmouth "That's what I'm hoping, at least."
    victini @angry "If we get unlucky, prepare yourself for close-quarters combat. Peer around every corner."
    red @talkingmouth angrybrow "Okay, be ultra-vigilant. Got it."
    # "How... how could you lose..."
    # -1 point
    # "No. This time I will be the one to reject the reality in front of me! Rise again, brave warrior! Just use Thundershock! Please!"
    # Woah, don't eat so fast! You'll get refeeding syndrome.
    scene hall_A gray with irisout
    red @thinking "Hmm... I think this is the right hallway. {w=.5}Ah, this here says ''Men's Baseball Changing Rooms''. I must be on the right track, but I still don't understand why these rooms are placed here..."
    victini playfuleyes smirkmouth"Am I missing some context here...? {w=.5}Or do you always light your way based upon changing rooms?"
    red @angry "Please, don't say one word more about changing room lights."
    victini @winkeyes surprisedmouth "?????"
    victini @exclaim "Okay, now I'm just curious! You've gotta let me in on this!"
    red @talking2mouth surprisedeyes "I'd really rather not."
    victini @angry "Fine then, keep your secrets! And continue being no fun while you're at it as well!"
    red happyeyebrows talking2mouth "As opposed to you, who has only revealed that you are simply a Pokemon?"
    victini neutraleyes @happymouth "Yes, the best Pokemon. Isn't that self-explanatory to what I am? It's more than enough context!"
    red "It really isn't. Especially when such a thing is subjective."
    victini @normal "Ah, whatever. In good news, this building is completely empty. No threats are around. Still, keep your guard up."
    victini @sadeyes "Anyways... are we just gonna keep walking down this hall aimlessly, or---"
    red neutraleyes surprisedmouth "Ah, here's my room!"
    victini @done "Okay, what lovecraftian horrors does your room have in store?"
    $ renpy.sound.queue("audio/Door_Open1.mp3", channel='sound', loop=False, tight=None)
    scene dorm_A gray with squares
    show victini normal:
        zoom 1 xpos 0.5 ypos 0.5
        parallel:
            ease 0.18 ypos .5
            ease 0.18 ypos .49
            ease 0.18 ypos .5
            ease 0.18 ypos .51
            repeat
    pause 1.0
    $ renpy.sound.queue("audio/Door_Close1.mp3", channel='sound', loop=False, tight=None)
    victini angryeyes neutralmouth "So this is your room? Not as bad as I thought it would be. But doesn't look very lived in. Even accounting for the lack of color."
    red happy "Well, I did say I just moved in today, so I can't argue with that. But it's certainly got potential! If it weren't so gray, as you say."
    victini sadeyes @talking "With the amount of beds in this place, I'll begrudgingly believe it. Five people in this place has GOT to be cramped."
    red @neutral "Land in Kobukan is pretty expensive, I'd reason?"
    victini angry "What the heck is a Kobukan?? Some sort of fruit snack? {w=.5}Actually, later, we're wasting time here."
    red @talking2mouth "So, any portal here? {w=.5}Maybe it's hiding in the wardrobe...? {nw}"
    $ renpy.sound.queue("audio/Door_Open1.mp3", channel='sound', loop=False, tight=None)
    extend @frownmouth "{w=1.0}Nope, nothing. Guess this isn't like ''The Pyroar, the Delphox, and the Wardrobe'' story, then."
    $ renpy.sound.queue("audio/Door_Close1.mp3", channel='sound', loop=False, tight=None)
    red @happy "Hmm... {w=.5}I'm out of ideas. Got anything?"
    victini @angry "Yeah, give me a minute and some quiet. {w=.5} Hmmm... if I'm looking for a portal, there should be some sort of irregular pattern of energy..."
    victini @angryeyes poutmouth "Let's see here... feel the concentration of energy in the air..."
    victini @exclaim "Yes! There's something here!"
    show victini normal:
        zoom 1 xpos 0.5 ypos 0.5
        ease 2.0 zoom .4 xpos 0.5 ypos 0.38
    pause 2.0
    victini "It's somewhere around this corner of the room! That's where it's concentrating."
    red @confused "Really? I don't see anything out of the ordinary."
    victini smirkmouth angryeyes "Perhaps not yet... as the energy is latent, and not bonded to an extent where a normal human could see. {size=-10}That's you, by the way."
    red @angry "Yeah, I know..."
    victini talking "But now, if I channel a discharge of energy... it should appear to one less blessed in the senses as well."
    show time behind victini with dis:
        zoom 0.05 xpos .38 ypos .38
    red @surprised "Woah!"
    victini @sadeyes frownmouth "Okay, so that's definitely a portal. But now comes the difficult part: opening it. Hooooo boy, this is not gonna be fun, best case."
    stop music
    play music "audio/music/portal_open0.wav"
    show time behind victini
    victini @angry "Let's begin."
    pause 1.0
    victini @angryeyes unamusedmouth eyesparkles2 "Oh, portal of mystery! Feast upon my energy, and grow into a vessel for our party's safe voyage across oceans thought uncrossable for all but a select few!"
    red @surprised "A hymm of some kind?"
    victini @smirkmouth "Who knows?"
    show blank
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    pause 1.0
    hide blank
    show time behind victini:
        zoom 0.05 xpos .37 ypos .36
        parallel:
            ease .5 rotate -20
            ease .5 rotate 40
            ease .5 rotate -60
            ease .5 rotate 80
            repeat
    pause 1
    show blank
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    pause 1.0
    hide blank
    pause 1
    show blank
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    pause 1.0
    hide blank

    red @surprised "That's really loud!"
    victini @neutraleyes happymouth "This is actually a lot easier than I thought it would be! We'll be out of this hellscape in a flash!"

    stop music
    play music "audio/music/portal_open1.wav"
    show victini angry with hpunch:
        zoom .4 xpos 0.5 ypos 0.38
        parallel:
            ease .1 rotate -5 xpos 0.5
            ease .1 rotate 5 xpos 0.51
            ease .1 rotate -5 xpos 0.5
            ease .1 rotate 5 xpos 0.49
            repeat
    show time behind victini with dis:
        zoom 0.05 xpos .37 ypos .36
        parallel:
            ease .1 rotate -20
            ease .1 rotate 40
            ease .1 rotate -60
            ease .1 rotate 80
            repeat
    
    victini @surprised "Huh?!?"
    show blank2 with squares
    victini angry "Urgh...! It's fighting me! My control is slipping!"
    red @surprised "What's going on?! {w=.5}I can't see a thing!"
    victini "No, no, no! Shit, shit, shit!"
    red @confused "That tone worries me!? It doesn't sound like you're wrangling the issue well!"
    victini "I'm having a hard time here, okay!!? I don't really know what I'm doing! At all!"
    red @surprisedeyes talking2mouth "Is there a way to wrest back control?! Or are we all going to explode?!"
    victini "Give me an explanation of where you wish to return to! If I can visualize it, maybe that will help a ton!"
    red @surprisedeyes talking2mouth "Well, it looks just like here, except it is vibrant, full of life, and color!"
    red @surprisedeyes talking2mouth "There's four other people who should be in there: my roommates!"
    red @surprisedeyes talking2mouth "And right outside the hall is a view of a large, lush school campus, filled with students and professors from around the world!"
    
    hide blank2 with Dissolve(1.5)
    show time behind victini with dis:
        zoom 0.05 xpos .38 ypos .38 rotate 0
    show victini normal:
        zoom .4 xpos 0.5 ypos 0.38 rotate 0
    stop music
    play music "audio/music/portal_open0.wav"
    victini @surprisedmouth neutraleyes "Was that enough... did I manage to calm it down...?"
    show time behind victini with dis:
        zoom 0.05 xpos .37 ypos .36
        parallel:
            ease .1 rotate -20
            ease .1 rotate 40
            ease .1 rotate -60
            ease .1 rotate 80
            repeat
    stop music
    play music "audio/music/portal_open0.wav"
    show victini surprised with vpunch:
        ease 0.3 ypos .3 xpos .76
    $ renpy.sound.queue("audio/Body Crash.ogg", channel='sound', loop=False, tight=None)
    pause .3
    show victini dizzy surprised2mouth with hpunch:
        ypos .3 xpos .76
        ease 1.2 ypos .44
    $ renpy.sound.queue("audio/Body Roll.ogg", channel='sound', loop=False, tight=None)
    pause 1.5
    victini @poutmouth "Owowow! What the heck, that didn't work?!"
    show victini angry:
        xpos .76 ypos .44 
        parallel:
            ease 2.0 xpos .5 rotate 0
        parallel:
            ease 0.5 ypos .40
            ease 0.45 ypos .36
            ease 0.40 ypos .40
            ease 0.35 ypos .36
            ease 0.3 ypos .38
    pause 3.0
    victini vcreate frownmouth angryeyes @anger "Fine then, if you're going to be this way, I'll just have to use force!"
    # Have victini get mad and use v-create, then teleport to right bed.
    # Fine then, I'll use force!
    show victini with hpunch:
        alpha 1.0 xpos .5 ypos .38
        ease .4 xpos .3
    pause 0.8
    hide victini with squares
    show victini angry with squares:
        xpos .76 ypos .6 zoom .5
    victini -vcreate "Take cover!"
    red @surprised "Wha--"
    show blank2
    stop music
    pause 3.0
    red @surprised "{w=.5}It's quiet...?"
    red confused "Am...{w=.5} I dead...?"
    victini "No, you just closed your eyes."
    victini "And whatever I did stopped the tantrum the portal was having, apparently."
    red "Oh."
    hide time
    hide blank2 with Dissolve(1.0)
    show time behind victini:
        zoom 0.05 xpos .37 ypos .36 rotate 0
    red @angry "You aren't one for exact science, are you? That brash action could have killed all of us!"
    victini smirkmouth winkeyes "But it didn't. {w=.7}So that just means I'm a mad genius."
    red @talking2mouth "{i}Emphasis{/i} on the mad."
    victini happymouth "But still a genius!"
    red @thinking "Pat yourself on the back {i}after{/i} we find a way out, please."
    victini poutmouth angryeyes "You're all about the results, and leave no interest for the process! {w=.5}A shame, for the scientific method centers around process."
    show victini:
        xpos .76 ypos .6 zoom .5
        ease 1.5 xpos .6 ypos .38 zoom .4
    victini @talking "Fine then. I also want to get out of here."
    stop music
    play music "audio/music/portal_open0.wav"
    victini @angrymouth "I'm gonna blast this thing with energy til it opens!"
    show blank
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    victini "Take this!"
    hide blank
    pause 1
    show blank 
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    victini "And that!"
    hide blank
    pause 1
    show blank
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    victini "And just for good measure, a three more shots of victory!"
    hide blank
    show time behind victini:
        zoom 0.3 xpos .2 ypos .1
    red @surprised "It's larger!"
    victini @talking "And stable! {w=.5} Just needs one more push..."
    victini @surprisedmouth "On my go, get ready to jump in!"
    red @surprised "What about you?"
    victini @frownmouth "I can't hold a whatever-this-door-is open and go in before you. I'll go after!"
    red @angry "OK!"
    victini @angry "Here... {w=.5}we... hng..!{w=.5} go...!"
    hide screen currentdate
    show blank
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    $ renpy.sound.queue("audio/BurnDamage.wav", channel='sound', loop=False, tight=None)
    pause 1.0
    stop music
    play music "audio/music/portal_open2.wav"
    pause 2.0
    #red @surprised "Woah!"
     
    stop music
    play music "audio/music/HoldOnTight.mp3"
    scene time with Dissolve(2.0)
    hide blank
    show victini exclaim:
        zoom 0.15 xpos 0.48 ypos 0.4 alpha 1.0
        parallel:
            ease 1.0 zoom 0.25 xpos 0.45 ypos 0.42 alpha 1.0 rotate 180
            ease 1.0 zoom 0.35 xpos 0.4 ypos 0.45 alpha 1.0 rotate -180
            ease 1.0 zoom 0.45 xpos 0.35 ypos 0.5 alpha 1.0 rotate 180
            ease 1.0 zoom 0.55 xpos 0.3 ypos 0.6 alpha 1.0 rotate -180
            ease 1.0 zoom 0.65 xpos 0.25 ypos 0.7 alpha 1.0 rotate 180
            ease 1.0 zoom 0.7 xpos 0.2 ypos 0.8 alpha 1.0 rotate -180
        parallel:
            ease 6.0 rotate 1080

    show pikachu surprised:
        zoom 0.15 xpos 0.48 ypos 0.4 alpha 1.0
        ease 1.0 zoom 0.25 xpos 0.45 ypos 0.42 alpha 1.0 rotate 180
        ease 1.0 zoom 0.35 xpos 0.4 ypos 0.45 alpha 1.0 rotate -180
        ease 1.0 zoom 0.45 xpos 0.35 ypos 0.5 alpha 1.0 rotate 180
        ease 1.0 zoom 0.55 xpos 0.3 ypos 0.56 alpha 1.0 rotate -180
        ease 1.0 zoom 0.65 xpos 0.25 ypos 0.63 alpha 1.0 rotate 180
        ease 1.0 zoom 0.7 xpos 0.2 ypos 0.7 alpha 1.0 rotate -180

    show red surprised: #behind victini:
        zoom 0.10 xpos 0.52 ypos 0.4 alpha 1.0
        ease 1.0 zoom 0.20 xpos 0.55 ypos 0.42 alpha 1.0 rotate 60
        ease 1.0 zoom 0.30 xpos 0.6 ypos 0.45 alpha 1.0 rotate -60
        ease 1.0 zoom 0.40 xpos 0.65 ypos 0.5 alpha 1.0 rotate 60
        ease 1.0 zoom 0.50 xpos 0.7 ypos 0.6 alpha 1.0 rotate -60
        ease 1.0 zoom 0.60 xpos 0.75 ypos 0.7 alpha 1.0 rotate 60
        ease 1.0 zoom 0.7 xpos 0.8 ypos 0.8 alpha 1.0 rotate -60

    
    window show dissolve

    window hide dissolve

    pause 8.0
    stop music fadeout 2.0
    hide time
    hide red
    hide victini
    hide pikachu

    $ timeOfDay = "Early Morning"

    call calendar(1) from _call_calendar_v

    show earlymorning at vspaz

    pause 3.5    

    #queue music "Audio/Music/Road to Viridian City.ogg"

    scene dorm_A with Dissolve(2.0)
    $ renpy.transition(dissolve)
    #show screen currentdate

    $ renpy.pause(1.0, hard=True)

    #hide blank2
    #scene dorm_A

    show victini
    victini happy "That's all for now! But here's some expressions!"

    victini tongue dizzyeyes "test"
    victini talking surprisedeyes "test"
    victini surprised "test"
    victini happymouth neutraleyes neutraleyesparkles "test"
    victini happymouth tears "test"
    victini happymouth tears2 "test"
    victini happymouth closedeyes -tears2 "test"
    victini happymouth sweat "test"
    victini exclaim -sweat "test"
    victini pout angryeyes eyesparkles2 -tears "test"
    victini pout angryeyes neutraleyesparkles "test"
    victini unamusedmouth angryeyes eyesparkles2 "test"
    victini smirkmouth playfuleyes "test"
    victini embarrassedmouth sadeyes "test"
    victini frownmouth sadeyes eyesparkles2 "test"
    victini surprised2mouth sadeyes "test"
    victini angrymouth angryeyes "test"

    victini smirkmouth "Back to the normal game. If things break, not my fault."
    #jump day010405