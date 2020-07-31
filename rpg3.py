import time,random,sys
from os import system

class master:
    enemy_objects = []

    def clear():
            _ = system('clear')


    def print_wait(string,wait,clear):
        if clear == True:
            master.clear()
            print(string)
            time.sleep(wait)
            master.clear()
        else:
            print(string)
            time.sleep(wait)

    def print_player(player):
        print("Player: Hp={}, Atk={}, Def={};".format(player.hp,player.attack,player.defense))

    def print_enemies():
        for x in master.enemy_objects:
            print("{}: Hp: {}; Atk: {}; Def: {};".format(x.name,str(x.hp),str(x.attack),str(x.defense)))
            print("")

    def choose():
        newplayer.hp = 300
        if (len(master.enemy_objects) == 0):
                master.win()
        master.clear()
        master.print_enemies()
        print("#######################################################")
        master.print_player(newplayer)
        choose_enemy = str(input("What enemy would you like to fight? "))
        for x in master.enemy_objects:
            if x.name == choose_enemy:
                master.battle(newplayer,x)
                break
        else:
            master.print_wait("That enemy does not exist",1,True)
            master.choose()

    def battle(player,enemy):
        while True:
            playercrit = random.randint(1,9)/3
            enemycrit = random.randint(1,9)/3
            player.hp = round(player.hp - (playercrit * (enemy.attack/player.defense)))
            enemy.hp = round(enemy.hp - (enemycrit * (player.attack/enemy.defense)))
            master.print_wait("Player hp: {}; {} hp: {};".format(player.hp,enemy.name,enemy.hp),0.1,True)
            if player.hp <= 0:
               master. gameover()
            elif enemy.hp <= 0:
                master.levelup(newplayer)
                master.enemy_objects.remove(enemy)
                master.choose()

    def levelup(player):
        add_atk = random.randint(0,100)
        add_def = random.randint(0,100)
        master.print_wait("Level up!",0.5,False)
        master.print_wait("+{} atk; +{} def;".format(add_atk,add_def),2,False)
        player.attack += add_atk
        player.defense += add_def
    def gameover():
        master.print_wait("You have died",1,True)
        sys.exit()
    def win():
        master.print_wait("You have won the game!",3,True)
        sys.exit()

class player:
    def __init__(self,hp,attack,defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense
    def __str__(self):
        return "hp: {}; attack: {}; defense: {}".format(self.hp,self.attack,self.defense)


class enemy:
    def __init__(self,name,hp, attack,defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        master.enemy_objects.append(self)
    def __str__(self):
        return "{}--> hp: {}; attack: {}; defense: {};".format(self.name,self.hp,self.attack,self.defense)



newplayer = player(300,300,300)
enemy("Hydra",2700,300,100)
enemy("Wurm",300,450,100)
enemy("Squid",300,1000,350)
enemy("Plant",400,525,375)
enemy("Merman",750,750,300)
enemy("Zombie",100,100,600)
enemy("Duck",700,200,300)
enemy("Chimera",200,1500,400)
enemy("Rat",300,300,300)
enemy("Cthulhu",1625,200,300)
enemy("Polysymbiote",600,975,500)
enemy("Slime",300,75,75)
enemy("Robot",600,1900,100)
enemy("Catgirl",300,2000,325)
enemy("King Blob",1000,800,400)
enemy("Amalgamation",300,800,1450)
enemy("Snake",600,600,75)
master.choose()


