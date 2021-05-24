# The imported class contains functions for adding and removing
# items to the inventory, the player character's mind, the game world,
# and evergreen lists for each of them.

from Dimensions.Dimensions import DimensionStruct 

# These functions are events happening in spaces throughout the game.
# Depending on player choice, the lists inventory, mind, and world
# get added to (add_item) or subtracted from (remove_item).
# N.B. that environment = DimensionStruct() in def main.
# Checks for items in any combination of those three lists
# will determine the outcome and availability of player choices
# and eventually the end of the storyline.


def door1(environment):
    print('''
    There's a giant bear with a gold tooth here eating a cheese cake.
    What do you do?

    1. Take the cake.
    2. Scream at the bear.
    3. Get out of here.''')

    if 'cleaver' in environment.inventory:
        print('''    4. Attack the bear with the meat cleaver.''')
    else:
        print('''    4. <OPTION LOCKED – GOT NO CLEAVER>''')
    
    if 'fish' in environment.inventory:
        print('''    5. Throw the bear a fish.''')
    else:
        print('''    5. <OPTION LOCKED – GOT NO FISH>''')
    
    door1_act1 = input('''
    > ''')

    if door1_act1 == '1' and 'faceless' not in environment.mind:
        bear_fight(environment)
    elif door1_act1 == '1' and 'faceless' in environment.mind:
        print('''
    As much as you remain tempted to steal the bear's meal
    from under its nose, you have direly little of your face left
    to spare it.''')
    elif door1_act1 == '2':
        print('''
    The bear eats your legs off. Good job!
        
    YOU GOT ENDING 1/16. Thank you for playing.
    ''')
        quit()
    elif door1_act1 == '3':
        print('''
    Deeming it a miracle you've yet to void your bladder in fear,
    you promptly make for the exit.''')
        return main()
    elif door1_act1 == '4' and 'cleaver' in environment.inventory:
        print('''
    You run at the bear and slice it in half
    with the meat cleaver. Seems those hours in the gym
    paid off. You were beginning to think we'd evolved
    past the need for brute force to survive. Who were you
    kidding?''')
        environment.add_item('dead_bear', 'world')
        environment.add_item('cake', 'world') 
        return door1_clear(environment)
    elif door1_act1 == '5' and 'fish' in environment.inventory:
        print('''
    You throw the fish in the furthest corner of the room and
    the bear immediately gives chase. It gobbles down the fish
    and falls asleep with a thunderous thump.''')
        environment.add_item('sleeping_bear', 'world')
        environment.add_item('cake', 'world')
        return door1_clear(environment)
    else:
        print('''
    Please enter only a valid number.''') 
    
    return door1(environment)
    # Above could be one big while-True-loop instead?

def bear_fight(environment):
    
    print('''
    Before you reach it, the bear eats your face off. Good job!
    But you won't impress people at the dance this way. What now?

    1. Run away and close the door behind you.
    2. Attempt to tear the bear's face off with your bare hands.
    3. Ask the bear for advice.''')
    environment.add_item('faceless', 'mind')

    door1_act1a = input('''
    > ''')

    if door1_act1a == '1':
        print('''
    You deem flight a far more suitable solution than fight,
    and you're back where you started, door shut behind you,
    faster than you could say 'deformed for life'.''')
            
        return main()

    if door1_act1a == '2':
        print('''
    Somehow hoping to defy aeons of perfectly good physics,
    you run at the bear and clump its cheeks in your palms.
        Your last thought is that you must look more like
    an old lady greeting her grandchild than a gladiator
    of legend denouncing weaponry by principle.
        The bear's claw leaves a gaping hole clean through
    your torso and you drop to the floor rather slowly,
    blessed with your very first look at your own real
    live viscerae at work, though your brain is too busy
    conjuring a death trip to make sense of it.
    
    YOU GOT ENDING 2/16. Thank you for playing.
    ''')
        quit()
    
    if door1_act1a == '3':
        print('''
    You open your mouth to speak and the beast immediately
    lunges at you, missing by a hair's breadth.
    Without the element of choice, you dart out of
    the room and shut the door.''')
            
        return main()

    else:
        print('''
    Please enter only a valid number.''')
            
    return bear_fight(environment)


def door1_clear(environment):

    print('''
    You stand in the bear's room.
    
    1. Leave the room.''')
    
    if 'cake' in environment.world:
        print('''    2. Eat the cake.''')
    
    else:
        print('''    2. <OPTION LOCKED – DAMN, THAT TASTED GOOD>''')
    
    if 'dead_bear' in environment.world:
        print('''    3. Check on the bear's corpse.''')
        
    else:
        print('''    3. <OPTION LOCKED – BEAR'S NOT DEAD>''')
    
    if 'sleeping_bear' in environment.world:
        print('''    4. Approach the sleeping bear.''')
    
    else:
        print('''    4. <OPTION LOCKED – BEAR ISN'T SLEEPING>''')
    
    door1_act2 = input('''
    > ''')
    
    if door1_act2 == '1':
        print('''
    You walk back through the door.''')
        
        return main()
    
    elif door1_act2 == '2' and 'cake' in environment.world:
        print('''
    It's pretty stale but you're hungry enough to finish
    the whole thing in a matter of minutes. Remembering
    you're never hungry first thing in the morning, you
    wonder how long you've been asleep.
        As you bite into the last slice you feel something papery
    in your mouth. It's a note saying:
    
        CONGRATULATIONS. THERE'S A BOARDED-UP DOOR IN THE FIRST ROOM.
        FEEBLE ENOUGH TO RIP OFF WITH YOUR BARE HANDS.
        HURRY UP.
    ''')
        environment.add_item('note', 'inventory')
        environment.remove_item('cake', 'world')
    
    elif door1_act2 == '3' and 'dead_bear' in environment.world:
        
        dead_bear_approach(environment)

    elif door1_act2 == '4' and 'sleeping_bear' in environment.world:
        
        sleeping_bear_approach(environment)
    
    else:
        print('''
    Please enter only a valid number.''')
    
    return door1_clear(environment)


def dead_bear_approach(environment):
    
    print('''
    Looks pretty dead.
        
    1. Leave the corpse be.''')
    
    if 'tooth' not in environment.inventory and 'necklace' not in environment.inventory:
        print('''    2. Force out the bear's gold tooth.''')
            
    elif 'tooth' in environment.inventory or 'necklace' in environment.inventory:
        print('''    2. <LOCKED OPTION – ALREADY HAVE TOOTH>''')
    
    if 'faceless' in environment.mind:
        print('''    3. Cut the bear's face off and wear it.''')
    
    elif 'faceless' not in environment.mind:
        print('''    3. <LOCKED OPTION – YOU HAVE A FACE, OR YOU'RE FACELESS BUT HAVE NO CLEAVER,
       OR YOU ALREADY TOOK THE BEAR'S FACE FOR YOUR OWN>''')
    
    door1_act2a = input('''
    > ''')
        
    if door1_act2a == '1':  
        print('''
    You decide not to touch the gross corpse.''')
        
        return door1_clear(environment)
        
    elif door1_act2a == '2' and ('tooth' not in environment.inventory and 'necklace' not in environment.inventory):
            
        if 'cleaver' in environment.inventory:
            print('''
    With the proverbial pommel end of the cleaver you bash out
    the glimmering little masticator and pocket it.''')
    
            environment.add_item('tooth', 'inventory')
                
            if 'wire' in environment.inventory:
                print('''
    There's a hole in the tooth. You slip the wire through it
    and hang it around your neck. It's a suave necklace.''')
                environment.remove_item('wire', 'inventory')
                environment.remove_item('tooth', 'inventory')
                environment.add_item('necklace', 'inventory')
    
        elif 'wire' in environment.inventory:
        
            print('''
    You use the wire to file away at the bear's gum until the
    gold tooth comes loose, then you pocket it.
    
    There's a hole in the tooth. You slip the wire through it
    and hang it around your neck. It's a suave necklace.''')
            environment.remove_item('wire', 'inventory')
            environment.add_item('necklace', 'inventory')
        
    elif door1_act2a == '3' and 'faceless' in environment.mind:
        print('''
    You slice the bear's face off to replace your own.
    You must look like a monster. Luckily, it stops some
    of the bleeding.''')
        environment.remove_item('faceless', 'mind')
        environment.add_item('bear_face', 'mind')

    else:
        print('''
    Please enter only a valid number.''')
    
    return dead_bear_approach(environment)


def sleeping_bear_approach(environment):

    print('''
    Not even babies look this cute while asleep.
    
    1. Leave the beast to its slumber.''')
    
    if 'wire' in environment.inventory:
        print('''    2. Choke the bear to death with the wire.''')
        
    elif 'wire' not in environment.inventory:
        print('''    2. <OPTION LOCKED – YOU HAVE NO WIRE>''')
        
    door1_act2b = input('''
    > ''')
        
    if door1_act2b == '1':
        print('''
    You'd be an arse to stir it from such blissful oblivion.''')
        
        return door1_clear(environment)
        
    elif door1_act2b == '2' and 'wire' in environment.inventory:
        print('''
    Taking a last mental photograph of cuteness, you slip the wire
    around its neck and trap every mote of good oxygen in its lungs
    for what feels like the longest minute of your life as it claws
    the air in confusion.''')
        environment.remove_item('sleeping_bear', 'world')
        environment.add_item('dead_bear', 'world')
        
        return dead_bear_approach(environment)

    else:
        print('''
    Please enter only a valid number.''')
    
    return sleeping_bear_approach(environment)


def door2(environment):
    
    print('''
    You enter a room with two objects on the floor:
    a fresh fish and a key. Each item lies on a pressure
    plate, although through the murk you can't
    distinguish what they might trigger. On the floor
    lies a note saying,
    
        YOUR CHOICES WILL DETERMINE YOUR FUTURE, SO
        DON'T BE DAFT, YOU FOOL.
    
    1. Take the key.
    2. Take the fish.
    3. Leave.''')
    
    door2_act1 = input('''
    > ''')
    
    if door2_act1 == '1':
        print('''
    You kneel down by the key and gently lift it from
    the metallic surface. A clear metal clangour sends
    you bolting back. You spin around in time to see
    a cage crash down over the fish.''')
        environment.add_item('key', 'inventory')
        environment.add_item('cage', 'world')
        
        return door2_cage(environment)

    elif door2_act1 == '2':
        print('''
    You hunch next to the fish and lift your face
    to dampen the strong smell. As you lift it slowly
    off the pressure plate a clangour sends you
    darting a few paces back. You see a huge cage
    crashing down over the key.''')
        environment.add_item('fish', 'inventory')
        environment.add_item('cage', 'world')
        
        return door2_cage(environment)
        
    elif door2_act1 == '3':
        print('''
    You turn around and leave.''')
        
        return main()
        
    else:
        print('''
    Please enter only a valid number.''')
    
    return door2(environment)


def door2_cage(environment):
    
    print('''
    The cage menacingly covers the prize
    you did not reach for.
    
    1. Attempt to lift the cage.
    2. Leave.''')
    
    door2_cage_act1 = input('''
    > ''')
    
    if door2_cage_act1 == '1':
        print('''
    No luck. Feels heavier than your car.
    (Yes, you did drunkenly try to lift your
    car once.)''')
    
    elif door2_cage_act1 == '2':
        print('''
    You skedaddle.''')
        
        return main()

    else:
        print('''
    Please enter only a valid number.''')

    return door2_cage(environment)
    

def door3_dark(environment):
    
    print('''
    You contemplate your next move in the room behind
    the third door.
    
    1. Reach around with your arms.
    2. Inspect the hard object.
    3. Leave the room.''')
    
    if 'wire' in environment.mind:
        print('''    4. Pull the wire.''')
        
    elif 'wire' not in environment.mind:
        print('''    4. <OPTION LOCKED – SECRET>''')
    
    door3_act1 = input('''
    > ''')
    
    if door3_act1 == '1':
        print('''
    As you reach out you feel cold stone under your palm: a wall.
    The room is the size of a broom closet. Your elbow bumps
    into a steel wire dangling in the musty air.''')
    
        if 'wire' not in environment.mind:
            environment.add_item('wire', 'mind')
    
    elif door3_act1 == '2':
        print('''
    It feels rectangular and wooden. It has a steel loop
    with a steel square dangling from it.''')
    
    elif door3_act1 == '3':
        print('''
    You return to the room from whence you came.''')
        
        return main()
    
    elif door3_act1 == '4' and 'wire' in environment.mind:
        print('''
    A naked ceiling bulb pulses on with a weak whirring noise,
    illuminating the room.''')
        environment.add_item('light', 'world')
        
        return door3_light(environment)
        
    else:
        print('''
    Please enter only a valid number.''')
    
    return door3_dark(environment)


def door3_light(environment):

    print('''
    The bare bulb casts light onto a chest securely shut
    with a sturdy lock hanging from the latch.
    
    1. Leave the room.''')
    
    if 'open_chest' not in environment.world:
        
        print('''    2. Attempt to force open the lock.''')
        
    else:
    
        print('''    2. <LOCKED OPTION – WHY FORCE AN ALREADY-OPEN CHEST?>''')
    
    if 'wire' not in environment.inventory and 'necklace' not in environment.inventory:
    
        print('''    3. Tug at the wire.''')
    
    else:
    
        print('''    3. <LOCKED OPTION – ALREADY GOT THE WIRE>''')
    
    if 'key' in environment.inventory and 'open_chest' not in environment.world:
    
        print('''    4. Use the key on the chest.''')
    
    else:
    
        print('''    4. <LOCKED OPTION – KEY NOT IN INVENTORY OR CHEST ALREADY OPEN>''')
        
    if 'open_chest' in environment.world and 'cleaver' not in environment.inventory:
    
        print('''    5. Take the meat cleaver.''')
        
    else:
    
        print('''    5. <LOCKED OPTION – ITEM ALREADY IN INVENTORY OR CHEST NOT OPEN>''')
    
    door3_act2 = input('''
    > ''')
    
    if door3_act2 == '1':
        print('''
    You leave the room.''')
    
        return main()
        
    elif door3_act2 == '2' and 'open_chest' not in environment.world:
        print('''
    Pry as you might, there's no way this
    heavy duty lock will budge without a flamethrower,
    chainsaw, or help of a locksmith.
        And being a rebellious teenager, all the money
    you could have used on a locksmith already went
    into cigarettes and marijuana.''')
        
    elif door3_act2 == '3' and ('wire' not in environment.inventory and 'necklace' not in environment.inventory):
        print('''
    You tug at the wire, it breaks off, and you keep it.''')
        environment.add_item('wire', 'inventory')
        if 'tooth' in environment.inventory:
            print('''
    You remember the gold tooth had a hole in it. You take it out
    and slip the wire through it, turning it into a necklace, which
    you hang around your neck.''')
            environment.remove_item('wire', 'inventory')
            environment.remove_item('tooth', 'inventory')
            environment.add_item('necklace', 'inventory')
    
    elif door3_act2 == '4' and ('key' in environment.inventory and 'open_chest' not in environment.world):
        
        print('''
    The chest swings open revealing a meat cleaver glistening in the light.''')
        environment.add_item('open_chest', 'world')
        
    elif door3_act2 == '5' and 'cleaver' not in environment.inventory:
        print('''
    You take the very grotesque weapon.''')
        environment.add_item('cleaver', 'inventory')
    
    else:
        print('''
    Please enter only a valid number.''')
        
    return door3_light(environment)


def hallway(environment):
    
    if 'faceless' in environment.mind:
        
        print('''
    Your face has bled out so much you fail to register what is
    behind the door, collapsing in a puddle of your own blood,
    thoroughly deceased.
    
    YOU GOT ENDING 3/16. Thanks for playing.''')
        quit()
    
    else:

        print('''
    You're in the school hallway. The clock says you're five
    minutes late for the dance! But what just happened is worth
    reporting as soon as possible. What do you do?
    
    1. Screw unexpected circumstances – just go to the dance!
    2. Better safe than sorry – report incident to Mrs Duchamp.''')
    
        hallway_act = input('''
    > ''')
        
        if hallway_act == '1':
            
            print('''
    You jog lightly to the auditorium, where a slew of decor
    covers its usually bland interior for the annual occasion.
    Most of the year group is already thronging here and minutes
    pass before you find Angela.''')
    
            auditorium(environment)
    
        elif hallway_act == '2':
            
            classroom(environment)


def auditorium(environment):

    if 'bear_face' in environment.mind and 'necklace' in environment.inventory:
                
        print('''
    Angela's saucepan eyes dart between your evidently alpha-male
    bear face and the stylish gold tooth hanging from your neck,
    at a loss for words.
    
    You make to greet her and she all but swoons in your arms.
    She is with a man who has slain a bear and lived to tell
    the tale – well-dressed to boot – what more could a teenage girl
    ask for?
    
    Your nemesis since primary school, Brett, eyeballs you callowly
    from a distance, irreverence too demped by your overall
    cool to dare call out the slightly out-of-place nature of it
    all.
    
    Even before the dance officially starts, Angela has fallen madly
    in love with you. The two of you sneak out and make love in her
    room.
    
    You awaken then next morning with a knife lodged in your abdomen,
    Angela's father scornfully looking down at you.
    
    'Despite all the obstacles I've set in your path, you still
    managed to defy my will,' he says. 'No matter – the strongest
    always wins in the end.'
    
    Your last thought is the terrified shriek of Angela, oblivious
    to its implications for her continued life.
    
    YOU GOT ENDING 4/16. Thanks for playing.
    ''')
        quit()
        
    elif 'bear_face' in environment.mind and 'necklace' not in environment.inventory:
                
        print('''
    'Good God,' says Angela. 'Your face . . . are you okay?'
    She relaxes when you say it's just a costume. Seems a bit more
    responsive to your quips and jokes than she'd otherwise have
    been, though, as if irresponsiveness would confirm her fears.
        
    It makes the date so easy you start thinking you'll get lucky,
    despite the glares you get for your inappropriate attire.
        
    'Hey, dickwad,' says Brett, your nemesis since primary school.
    'This isn't the Hallowe'en party.'
        
    He rips off the bear's face before you could make to stop him,
    revealing your facelessness underneath.
        
    You are promptly taken to a hospital.
        
    Angela is so traumatised, she is put in a mental ward. Though
    she is eventually released, she spends the rest of her life as
    a cat lady.
        
    The person who kidnapped you is revealed to be her father, a fact
    which causes Angela to double her cat collection and move over-
    seas with a drug lord sugar daddy.
        
    YOU GOT ENDING 5/16. Thanks for playing.
    ''')
        quit()
                    
    elif 'bear_face' not in environment.mind and 'necklace' in environment.inventory:
                
        print('''
    Angela immediately notices the shiny golden necklace
    and she smiles. Must be glad you made some effort to look good
    for the dance.
    
    You dance and socialise the night away. When most have left
    the auditorium, you're still there, and you offer to drive her
    home.
    
    Outside her home you kiss her on the lips and arrange a second
    date. When you are done punching her number into your phone
    you look up only to see a hole in her head.
    
    You run like your life depends on it. Later, you find out that
    the shooter was her father, and that you were supposed to be his
    target, but his aim was off. The gun was a silenced sniper rifle
    kept from his days in the Grens Oorlog.
    
    Her father also confesses to having kidnapped you before the
    dance. He receives a becoming prison sentence.
    
    The trauma fades with the years and you gain hope that your
    chances for love and redemption are not lost – otherwise,
    why were you spared?
    
    YOU GOT ENDING 6/16. Thanks for playing.
        ''')
        quit()
        
    elif 'dead_bear' in environment.world and not ('bear_face' in environment.mind or 'necklace' in environment.inventory):
                
        print('''
    Angela is unimpressed with the lack of effort
    made to your appearance, while her outfit is clearly
    superior to that of every other girl in the building.
    
    Still, love is blind, and at the end you ask her out
    again. She accepts in a manner so forcefully polite
    it makes your stomach twist.
    
    Meanwhile, you report your strange experience in the dark room
    to the headmaster who gets the police to investigate.

    Then you follow up with Angela about a
    second date. She puts it off a number of times and
    eventually tells you, much like an older sister,
    that's she's generally not interested in dating
    right now.
    
    Investigation reveals that the person who kidnapped you
    was none other than Angela's father. She switches schools
    the next day and you never see her again.
    
    The only good thing you get out of the experience is your
    survival and the court payout for damages. Here we come,
    new computer!
    
    YOU GOT ENDING 7/16. Thanks for playing.
        ''')
        quit()
        
    elif 'sleeping_bear' in environment.world:
                
        print('''
    Angela does not like your outfit. Not one bit.
    
    Much as you try to woo her, she seems distracted.
    As if she expected more. Especially as she would
    definitely have won the award for best-dressed at the
    dance had there been one.
    
    What saves you from the quiet awkwardness, however,
    is rather something you would have done without.
    
    'Bear!' someone shouts. 'There's a goddamn bear
    on the dancefloor.'
    
    The bear seems to remember you for having fooled it,
    and lunges at you.''')
    
        if 'wire' in environment.inventory:
            print('''
    You dive out of the way, and spin around just in time to
    see the bear about to chomp Angela's upper body off.
    
    In the split seconds that follow, instinct seems to
    automate your actions.
    
    You pull the wire out of your pocket and span it around the bear's
    neck in a single movement, somehow summoning the strength
    to pull its maw away from your beloved's golden locks.
    
    The act of heroism is so wonder-inducing that even when
    Angela finds out her father was the one who kidnapped you,
    she remains so in love with you it's as if the rest of the
    universe doesn't exist.
    
    Having newfound confidence in your physical prowess you
    become a successful farmer and settle down on the outskirts
    of town with Angela and your new family.
    
    YOU GOT ENDING 8/16. Thanks for playing.
    ''')
            quit()
    
        else:
            print('''
    You dive out of the way just in time – and Angela
    has but a split second to shriek before the bear
    chomps off her whole upper body, leaving behind only
    an attractive pair of legs with a not-so-attractive
    bleeding gash on top.
    
    You tell the police everything that night. That
    such a young beauty was so easily terrorised makes
    the police force redouble its efforts and the weekend
    is not over before Angela's father is revealed to be
    the one who kidnapped you.
    
    The bear's escape and mutilation of his daughter weighs
    too heavily on his heart, and he hangs himself before he
    can be sentenced to the appropriate punishment.
    
    Some of that guilt carries over to you, and many years
    pass for its mollification, replacing it gradually with
    a glimmer of hope to find love again.
    
    YOU GOT ENDING 9/16. Thanks for playing.
    ''')
        quit()
        
        
def classroom(environment):
            
    print('''
    'Mrs Duchamp!' you say as you enter the biology teacher's
    classroom.

    In her usual immortal way, she's marking papers at this
    hour, which doesn't seem to change for any occasion.

    Only her eyes move in your direction. 'What do you want?'

    You blurt out everything that just transpired. Somewhere
    in the midst of your narrative, her expression changes
    from bored obligation to terrified awe.

    'Come with me this instant,' she says.''')

    if 'cleaver' in environment.inventory:
        
        print('''
    Mrs Duchamp leads you out of the room. However, just as
    you exit she turns at a speed belying her age and shoves
    you back into the room, locking it.

    'You think I don't see anything conspicious like, oh, I
    don't know, that giant meat cleaver you're carrying? I'm
    calling your bluff.' ''')

        if 'bear_face' in environment.mind:
        
            print('''
    'Wait until the police see that hideous bear face
    you're wearing,' she says. 'I always suspected you of
    being a no-gooder. Now, finally, I'll be proved right.'

    When the police find you have replaced your face with
    that of a bear, they consider the rest of your story
    made up: the real kidnapper is never thoroughly investigated.

    You are put in a hospital, then an asylum for psychopathy.''')

            return asylum(environment)
        
        else:
        
            print('''
    'I'm calling the police,' she says. 'We'll see what
    they think about a student carrying around a deadly
    cutting tool.'

    The police arrive, and luckily they're less rash
    decision makers than Mrs Duchamp, although they do
    confiscate your meat cleaver.

    You repeat the story to them and they ask you to
    show them to the mysterious rooms.

    When you get there, the officer walking in front
    is immediately seized by a giant of a man, who puts
    a gun to the cop's head. 'Don't anyone move,' he says,
    'or he gets a hot, hard piece of lead in the thinker.'

    You entered the room at about the same time as the cop,
    however, and managed to slip past. You stand behind the
    man and he doesn't seem to have noticed you.''')
            environment.remove_item('cleaver', 'inventory')
            
            return rooms_return_father(environment)
    
    else:
    
        print('''
    Mrs Duchamp leads you out of the room. She rushes fast
    ahead and you're out of breath in your efforts to catch
    up. Didn't expect that given her age!''')
    
    return rooms_return_bear(environment)


def asylum(environment):
    
    print('''
    It doesn't take more than a day at the asylum
    to convince you you don't belong here. People speak
    in their own made-up languages and the drugs are
    terrible.
    
    1. Spend your time in misery.''')
    
    if 'tooth' in environment.inventory or 'necklace' in environment.inventory:
        print('''    2. Bribe a staff member to sneak you out using the gold tooth you snuck in.''')
    
    else:
        print('''    2. <LOCKED OPTION – TOOTH OR NECKLACE NOT IN INVENTORY>''')
    
    if 'wire' in environment.inventory or 'necklace' in environment.inventory:
        print('''    3. Use the wire you snuck in to choke out the night patrol.''')
    
    else:
        print('''    3. <LOCKED OPTION – WIRE OR NECKLACE NOT IN INVENTORY>''')
    
    asylum_act = input('''
    > ''')
    
    if asylum_act == '1':
    
        print('''
    You're told you're insane so many times you start
    to believe it. Instead of acting out about it, however,
    you become more reserved, and keep your head down.
    
    Somewhere in the midst of the tedious banality
    you start thinking to yourself that there is more
    to life than mere normality and abnormality in human
    behaviour.
    
    One day, Angela visits to find out whether the guy
    who stood her up at the dance is truly insane.
    
    However, your philosophical ramblings have become
    all but incomprehensible crypticism.
    
    Angela decides you're not worth the risk of a
    relationship with insanity, and though you've
    become impeccable at putting up the front of
    sombre peacefulness, you wonder if your expression
    belies the sting inside this time.
    
    Your new synthetic face doesn't add much to your charm,
    either.
    
    Years later you go on your honeymoon with a
    markedly less interesting partner than Angela,
    so chosen likely because all that time being scolded
    for your avant garde nature finally convinced you
    you shouldn't be yourself.
    
    It won't be long until your divorce.
    
    YOU GOT ENDING 10/16. Thanks for playing.
    ''')
        quit()
    
    if asylum_act == '2' and ('tooth' in environment.inventory or 'necklace' in environment.inventory):
    
        print('''
    You wait until nightfall and sneak to the lobby
    where the security guard is stationed.
    
    'Pssst,' you say.
    
    He lifts his walkie-talkie to call for back-up;
    and freezes when you proffer the gold tooth.
    
    'Holy shit,' he says. 'This is solid gold, and it's
    huge.'
    
    Needless to say, you persuade him, and you are let
    out of the asylum with very little attention drawn to you.
    
    You steal a bicycle and stop only on the border of town,
    at Angela's farmhouse. Unfortunately, you can't convince
    her to come with, because you stood her up at the dance.
    
    Maybe it also has something to do with your new synthetic
    face.
    
    It's a bummer at first, but deeply you know that freedom
    has always been more important to you than companionship,
    and it's not long before you start to whistle a jolly melody
    as you cycle along the highway into the great and exciting
    unknown.
    
    YOU GOT ENDING 11/16. Thanks for playing.
    ''')
        quit()
    
    if asylum_act == '3' and ('wire' in environment.inventory or 'necklace' in environment.inventory):
    
        print('''
    You wait for it to get dark and sneak along the hallways
    until you reach the lobby where a security guard does his
    patrol.
    
    When he turns his back you sneak up behind him and choke
    him to death.
    
    You grab his keyring and make a run for it. You throw a 
    brick through the window of a bicycle store and make off
    with their finest model.
    
    It's not long before you hear sirens behind you. They thought
    you were cuckoo last time – now they'll think you're a
    dangerous psycho.
    
    The thought of it rouses you to pedal faster in spite of
    their commands to do the contrary. The sound of a gunshot
    thunders through the frigid air and you fall face-first
    on the icy tar.
    
    Oh man, first you got your real face ripped off, now
    your new synthetic face is busted up. The bullet in your
    back doesn't add much good to your mood, either.
    
    The last thing you see is the unwelcome face of an
    embittered police officer hovering over you as he goes
    about 'another day at the office.'
    
    YOU GOT ENDING 12/16. Thanks for playing.
    ''')
        quit()
    
    else:
        print('''
    Please enter only a valid number.''')
    
    return asylum(environment)
    
def rooms_return_father(environment):

    if 'wire' in environment.inventory or 'necklace' in environment.inventory:
        print('''
    But wait! You still have that wire.
    
    And since it is clear the culprit wants to put a hole
    in the cop's head no matter the response,
    you act before you give yourself time to think,
    slipping the wire around his neck and choking him to death.
    
    Your antics prove not only life-saving but worthy of film.
    Newspapers announce your ballad with the headline: 'Young
    Teen Chokes Dead His Own Kidnapper; Saves Cop.'
    
    At school you become more popular than ever before,
    except among Angela and her friends. Why? Because the man
    you killed was also her father. And though she can't deny
    he was a psychopath for doing what he did, she can't at
    all accept that people have turned your actions into such
    a blown-up fable.
    
    She decides never to speak to you, and though you gain
    the interest of many a groupie with your new reputation,
    you find that although the sex is good, the shared interests
    are shallow.
    
    YOU GOT ENDING 13/16. Thanks for playing.
    ''')
        quit()
    
    else:
        print('''
    You stand by helplessly as another officer steps forward
    and the thug puts a hole in the hostage's skull.
    
    The thug is knocked down and cuffed up. He is later
    revealed to be none other than Angela's father. It takes
    her some time to process it – she is not seen at school
    for weeks.
    
    When she does return, she defies all your expectations
    by approaching you and extending her empathy, saying
    that although she was traumatised by the event, her father
    must have put you through far worse, being so close to death.
    
    She assumes you no longer have interest in her, in light
    of the psychotic genes in her family, and in that moment
    you vevaciously insist the contrary.
    
    However, as time passes, you realise you cannot rub out
    the image of her father's twisted face as he pulled the
    trigger on that noble police officer – a face which is
    just about the spitting image of Angela's.
    
    Eventually you can take it no more and call off the
    relationship, making peace with the thought that at least
    you got out of the drama with your skin intact.
    
    YOU GOT ENDING 14/16. Thanks for playing.
    ''')
        quit()


def rooms_return_bear(environment):
   
    print('''
    You watch in awe as Mrs Duchamp wrestles the bear and
    kills it by ripping its heart out.
    
    You are about to celebrate when you realise her
    frenzy is not done. She pounds her chest like a
    barbarian might do and sets her sight on you,
    murderous intent in her eyes.
    
    The fight with the bear has driven her insane.''')
   
    if 'wire' in environment.inventory:
    
        print('''
    Luckily she lunges over you, then you jump on her back and
    choke her to death with the wire.
    
    When the police arrive, the death of Mrs Duchamp is
    so pressing, the matter of your kidnapping is given
    little attention.
    
    But Mrs Duchamp's family history shows a pattern of
    anger management issues. Charges are waived and the
    kidnapper is later found to be Angela's father.
    
    The court cases gain you some attention at school.
    But Angela does not like what you're known for,
    because she does not want to be remembered as the
    child of a sociopath.
    
    Not seeing her at the dance gave you little chance
    to build familiarity with her 'before' her father's
    true nature was revealed, now she doesn't know you
    well enough to deem changing her mind worthwhile.
    
    Between the fleeting flings with numerous news groupies
    you eventually forget your fantasies of what could
    have been with the profound woman and instead
    spend your days musing about your next claim to fame.
    
    YOU GOT ENDING 15/16. Thanks for playing.
    ''')
        quit()
        
    else:

        print('''
    Horrified, you shield your face with your arms as
    she lunges at you. The result is a number of deep and
    ugly gashes and bruises on you arms and body before help
    arrives in the form of a janitor whose hobby is bodybuilding.
    
    Having been assaulted gives you an odd reputation of fragile
    cargo among staff and overly traumatised, even for a teenager,
    among your peers.
    
    You are also given empathic and dutiful attention by the police
    who listen to the story of your kidnapping. Associating it
    first with the case of Mrs Duchamp's anger management problems,
    rife in her family history, it takes extra time before they trace
    the incident to Angela's father.
    
    Thus, Angela doesn't want any of the attention you've gained and
    having missed you at the dance she's not aware enough of your redeeming
    characteristics to change her mind.
    
    For her, it is enough of a challenge to deal with the newfound
    psychopathy in her elder and his subsequent incarceration.
    
    You never thought that your fame in the newspapers would be that of
    victim rather than hero. Though it has its perks in that people
    don't give you trouble, it has its downfall in that they don't give
    you reverence.
    
    It becomes terribly lonely. The good things that arise out of this
    loneliness are gratitude for still being alive and interest in
    improving at your craft.
    
    YOU GOT ENDING 16/16. Thanks for playing.
    ''')

    
def main():

# The main function starts the player off in a dark room
# and can branch into combinations of the above functions.

    environment = DimensionStruct()
    
    print('''
    You see some doors.
    
    1. Enter door 1.
    2. Enter door 2.
    3. Enter door 3.''')
    
    if 'note' in environment.inventory:
        print('''    4. Remove panels from door 4 and advance.''')
    
    door = input('''
    > ''')

    if door == '1' and 'cake' not in environment.world:
        return door1(environment)
        
    elif door == '1' and 'cake' in environment.world:
        return door1_clear(environment)
        
    elif door == '2' and 'cage' not in environment.world:
        return door2(environment)
    
    elif door == '2' and 'cage' in environment.world:
        return door2_cage(environment)
    
    elif door == '3' and 'light' not in environment.world:
        return door3_dark(environment)

    elif door == '3' and 'light' in environment.world:
        return door3_light(environment)

    elif door == '4' and 'note' in environment.inventory and 'panel_off' not in environment.world:
        print('''
    The boarded-up door is easy enough to find by running your palm
    along the wall. The panel is loosened with a few hard jerks.
    You thank the universe for giving you the will not to miss
    arms day.
        You make your way through the mysterious exit.''')
        environment.add_item('panel_off', 'world')
        return hallway(environment)

    elif door == '4' and 'note' in environment.inventory and 'panel_off' in environment.world:
        print('''
    You leave through the fourth door.''')
        return hallway(environment)

    else:
        print('''
    Please enter only a valid number.''')
        return main()

# The game opens with a string that prints only once.

print('''
    You are Gary Pfeiffer, impending high school graduate.
    You wake up thinking it's time to prepare for the farewell dance.
    The most attractive girl in history, Angela, said yes to your request to go as a pair.
        Mustering the courage for that was a test of your valour, and now it would seem
    that test is not over, because you wake up in a strange dark room instead of your bedroom.
        Surely it's a dream.
        Then again, have you ever thought that while you truly dreamt?
        Better find a way out – still have to get your tuxedo
    from the suit hire shop.''')

# After that, go to main, which branches into all other functions.

main()