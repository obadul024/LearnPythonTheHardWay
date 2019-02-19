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
        current_scene = self.scene_map.openning_scene()

        while True:
            print "/n---------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)



class Death(scene):

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

        if action == "shoot!"
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









