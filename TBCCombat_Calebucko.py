# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:40:05 2024

@author: Caleben Jahn
"""
import TBC_Calebucko
def main():
    Character1 = TBC_Calebucko.Character()
    Character1.name = "Bungus"
    Character1.hitPoints = 40 
    Character1.hitChance = 75
    Character1.maxDamage = 10
    Character1.armor     = 5
   
    Character2= TBC_Calebucko.Character()
    Character2.name ="Flingo" 
    Character2.hitPoints = 45
    Character2.hitChance = 65
    Character2.maxDamage = 12
    Character2.armor     = 3
    
    
    Character1.printStats()
    Character2.printStats()
    
    TBC_Calebucko.fightTime(Character1, Character2)
    
    if __name__ == "__main__":
         main()