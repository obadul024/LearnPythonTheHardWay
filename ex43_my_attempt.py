from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print "this scene is not yet configured. Subclass it and implement enter()"
        exit (1)


class Engine (object):
    def __init__(self, scene_map):
        self.scene_map = scene_map


    def play (self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n\n------------------------------------------------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)



class Death(Scene):

    quips = [

        "You Died and also suck at this",
        "Your mama so fat, she slowed down time when she walked passed me",
        "And that's why programming sucks",
        "Good Bye MOTHAFAKAH"

    ]



    def enter(self):
        print Death.quips[randint(0, len(self.quips) - 1 )]
        exit(1)




class Central_Corridor(Scene):

    def enter(self):
        print "Vogons from the planet Vogosphere have invaded your ship"
        print "After killing every one of your crew they are looking for you"
        print "the only way to survive is to take an escape pod to the planet below"
        print "Your mission should you choose to accept it, is to find that neutron bomb in the armoury"
        print "plant it in the ship and escape to the planet below"
        print "Fade In"
        print "INTR.  CENTRAL CORRIDOR - 2300 hrs"
        print "You are running down the corridor to the armoury when"
        print "a vogon jumps out from a corridor to the left"
        print "right in front of you"
        print "he's blocking the door to the armoury. "
        print "and about to pull a weapon to blast you "
        print "what do you do [shoot! , dodge! , tell a 'YO MAMA' joke ]"

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Vogon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into a rage and blast you repeatedly in the face until"
            print "you are blasted to bits , after which he recites a poem for you."
            return 'death'

        elif action == "dodge!":
            print "Like a world-class boxer you dodge, weave, slip and slide right"
            print "as the Vogon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Vogon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == "tell a 'YO MAMA' joke":
            print "Lucky for you they made you learn YO MAMA JOKES in the academy."
            print "You tell the one Vogon joke you know:"
            print " >> yo mamma so dumb she failed a blood test <<"
            print "The Vogon stops, tries not to laugh, then busts out laughing and can't move."
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'




class Laser_Weapon_Armory (Scene):

    def enter (self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Vogons that might be hiding. It's dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."

        code = "%d%d%d" % (randint(1,1), randint(1,1), randint(1,1))
        guess = raw_input("[Keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:

            print " BUZZ ALERT !"
            guesses += 1
            guess = raw_input("[Keypad]> ")

        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return  "the_bridge"

        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Vogons blow up the"
            print "ship from their ship and you die."
            return 'death'

class The_Bridge (Scene):

    def enter (self):
        print "You burst onto the Bridge with the neutron destruct bomb"
        print "under your arm and surprise 5 Vogons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."
        print "You can do one of these actions [ throw the bomb, slowly place the bomb] "

        action = raw_input(">")

        if action == 'throw the bomb':
            print "In a panic you throw the bomb at the group of Vogons"
            print "and make a leap for the door. Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
        elif action == "slowly place the bomb":

            print "You point your blaster at the bomb under your arm"
            print "and the Vogons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Vogons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'
        else:

            print "DOES NOT COMPUTE!"
            return "the_bridge"

class Escape_Pod(Scene):

  def enter(self):

        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes. It seems like"
        print "hardly any Vogons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #] >")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return "death"
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"
            
            return "finished"







class Map(object):
    scenes = {

        'central_corridor': Central_Corridor(),
        'laser_weapon_armory': Laser_Weapon_Armory(),
        'the_bridge': The_Bridge(),
        'escape_pod': Escape_Pod(),
        'death': Death()

    }

    # whatever is given to this class is stored in the self var as startscene
    # when this class is called this func runs and stores start scene
    def __init__(self, start_scene):
        self.start_scene = start_scene

    # when this is called with scene name it stores scene in self var
    # that takes name from the scene dict. using key
    def next_scene(self, scene_name):
        return self.scenes.get(scene_name)

    # when this is called, it calls next_scene func
    # with start_scene
    def opening_scene (self):
        return self.next_scene(self.start_scene)










a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()













