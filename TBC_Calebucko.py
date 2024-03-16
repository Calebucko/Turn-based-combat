# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:21:13 2024

@author: Caleben Jahn
"""


import random



class Character(object):
 
    def __init__(self):
        self.name = "Anonymous"
        self.hitPoints = 40
        self.hitChance = 75
        self.maxDamage = 10
        self.armor     = 5
        
    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter 
    def hitPoints(self, value):
        value = self.testInt(0, 100, 0)
        self.__hitPoints = value
        
    @property 
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter 
    def hitChance(self, value):
        value = self.testInt(0,100,0)
        self.__hitChance = value
        
    def hitTime(self, enemy):
        if random.randint(1, 100)<self.hitChance:
            print(f"{self.Name} hits {enemy.Name}")
        damage = random.randint(1, self.maxDamage)
        print(f"{enemy.name} takes {damage} points of damage")
        damage-= self.armor
        if damage <0:
            damage = 0
        if enemy.armor> 0:
            print(f"But {enemy.name} armor blocked {enemy.armor} points of damage ")
        enemy.hitPoints-=damage
        
        
            
        
        
    def fightTime(Character1, Character2):
        keepgoing = True
        while(keepgoing):
            Character1.hitTime(Character2)
            Character2.hitTime(Character1)
        if Character1.hitPoints <= 0:
            print(f"{Character2.name} reigns victorious. Huzzah")
            keepgoing = False
        elif Character2.hitPoints <= 0:
            print(f"{Character1.name} reigns victorious. Hurray.")
            keepgoing = False
            input("press any key to continue the fight")
            
        
            
        
        def printStats(self):
            f"""
            {self.name}
            Hit Points:   {self.hitPoints}
            Hit Chance:   {self.hitChance}
            Max Damage:   {self.maxDamage}
            Armor rating: {self.armor}
            """
    
    def testInt(self, value, min = 0, max = 100, default = 0):
        """ takes in value 
            checks to see if it is an int between
            min and max.  If it is not a legal value
            set it to default """
    
        out = default
    
        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")
    
        return out

     
        
    
        
    
    
        
        
    