print('''  *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************

''' )

print("Welcome to Treasure Island,Your mission is to find the treasure")
choice_left_or_right = input('You\'re at a cross road. where do you want to go? type "left" or "right :')

if choice_left_or_right == "left":
  choice_swim_or_wait = input('''You\' have come to a lake. There is a island in the middle of the lake.
                              Type wait to wait for a boat. Type swim to swim across :''')
  if choice_swim_or_wait == "wait":
     choice_red_door_or_blue_door = input(''' You arrived at the island unharmed. There is a house with 3 doors : red, yellow and blue. Wich color do you choose ?''')
     if choice_red_door_or_blue_door == "red":
       print("Burned by fire. Game Over.")
     elif choice_red_door_or_blue_door == "blue":
       print("Eaten by beasts.Game Over.")
     elif choice_red_door_or_blue_door == "yellow":
       print("you win")
     else:
       print("Game over")      
  else:
    print("Attacked by trout. Game Over.") 
else:
  print("Fall into a hole. Game Over.")
  