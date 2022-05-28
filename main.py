import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

delay_print("Welcome to the pokemon battles")
print(" ")
time.sleep(2)

class Pokemon:
  def __init__(self, name, type, health):
    self.name = name
    self.type = type
    self.health = health
    self.fainted = False
    self.attacks = {}
    
  def add_attacks(self, Name, Damage):
    self.attacks[Name] = Damage   
    
  def set_health(self, newHP):
    if newHP <= 0:
      self.health = 0
      self.fainted = True
  
    else:
      self.health = newHP

p1 = Pokemon("Zygarde", "Dragon, Ground", 130) 
p1.add_attacks("rumble", 20)
p1.add_attacks("raging blade", 60)
p1.add_attacks("lands attack", 130)

print("Player 1 " + p1.name + " attacks:")
for key in p1.attacks:
  print(key, p1.attacks[key])
time.sleep(2)
p2 = Pokemon("Eternatus", "Dragon, Poison", 220) 
p2.add_attacks("power accelerator", 30)
p2.add_attacks("dread end", 30)
p2.add_attacks("dynamax cannon", 120)

print(" ")

print("Player 2 " + p2.name + " attacks:")
for key in p2.attacks:
  print(key, p2.attacks[key])

print(" ")

attack = input("Enter an attack player 1:\n")
time.sleep(1)
print(p1.attacks[attack])
print("damage")

print(" ")
time.sleep(2)
attack = input("enter an attack player 2:\n")
time.sleep(1)
print(p2.attacks[attack])
print("damage")