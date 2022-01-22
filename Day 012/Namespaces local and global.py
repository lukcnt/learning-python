#Scope
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local scope
def drink_potion():
    potion_strenght = 2
    print(potion_strenght)

drink_potion()

#Global scope
player_health = 10

def drink_potion():
    potion_strenght = 2
    print(player_health)

dring_potion()
print(player_health)