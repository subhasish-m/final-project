import random
import time
#checking where the game is being played
onlineVS = input("Are you playing online (1) or through the desktop (2)? ")
if onlineVS == "1":
  online = True
elif onlineVS == "2":
  online = False
#having different modules and clear function for online vs desktop
if online == False:
  import keyboard, os
  def clear():
    os.system('cls')
elif online == True:
  import replit
  def clear():
    replit.clear()

#what happens if you win
def victory():
  print(f"The mummy is now paralyzed forever and cannot do you any harm. Inti walks in")
  print("Inti: Congratulations child! These riches belong to my one and true descendant. Through many trials, you have proved that you are worthy. This fortune is yours.\n")
  print("'Inti,' you say 'great-great-great-great-great-great-great-great-great-great-great-great grandfather I guess. I cannot accept this treasure. I came to Peru to relax a bit. Instead, I was thrown into this adventure. I have learned so much along the way. I didn't even know there was a fortune. I appreciate your kindness, but this treasure belongs to you and the rest of the gods. It is too much for any human.")
  print("Inti smiles. 'As you wish, my child. I wish you the best on your journey in life.'\nEverything around you vanishes and you are back at the surface. It is nighttime, and there is nobody around. You wonder if all that really happened. You notice that even in the dark, you are able to see quite well around you. You smile and continue on your merry way.")
  print("YOU WON!!\n Game over.")

#what happens if you lose by the end
def death_final():
  print(f"The mummy in front of {username} begins to disintegrate. The mummy starts laughing like a manicac. {username} feels excruciating pain all over their body.")
  print("Inti walks in")
  print("Welcome my new guard. Enjoy eternity.")
  print()
  print("YOU LOST! Game over.")

#what happens when a user is unable to complete a challenge
def death_inti():
  time.sleep(0.5)
  print("\nInti:You have failed to overcome your challenge. You dare enter my temple without a bit of wit. Your little adventure is over wanderer.\n Feel the wrath of Inti!\n")
  print("Inti banished you to the surface of the Sun. \nVery unfortunate for you. \nGame over.\n")

#door open graphics to make it easier
def doorOpen():
  input("Press Enter to advance to the door...")
  clear()
  print("""
    |          |
    |          |
    |__________|
    """)
  time.sleep(2)
  clear()
  print("""
    |          |
    |          |
    |          |
    """)

#final boss fight
def fight_game():
  class Fighter:
    #characteristics for each fighter
    def __init__(self, name, hp, atk, defense, moves):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.moves = moves

    def describe(self):
        #Describe an individual fighter
        print(f"""
  {self.name}:
  - HP: {self.hp}
  - Attack: {self.atk}
  - Defense: {self.defense}""")
        return
    #use boosts while fighting
    def use_boost(self, boost_stat, boost_size):
        if boost_stat == 'atk':
            self.atk += boost_size
        if boost_stat == 'hp':
            self.hp += boost_size
        if boost_stat == 'defense':
            self.defense += boost_size
        return
    #fight method
    def fight(self, opponent):
        #A single attack
        print(f"{self.name} is attacking {opponent.name}")
        old_hp = opponent.hp
        dmg = self.atk - opponent.defense
        if dmg <= 0:
            print(f"That's not very effective... ")
            dmg = .1
        opponent.hp -= dmg
        print(f"{opponent.name} dropped from {old_hp} to {opponent.hp} HP\n")
  #final question mummy asks
  final_question= input("Who was the last Incan King? ")
  #checking for right vs wrong answer
  if final_question.lower() == 'atahualpa':
    print("Mummy: ARGHHH, You know!")
    player = Fighter('Player', 10, 7, 11, ['sucker punch', 'jump', 'scratch', 'push'])
    mummy = Fighter('Mummy', 4, 0, 5, ['kick', 'tackle','horrible breath can make u pass out oof'])
    mummy.fight(player)
    player.fight(mummy)
    mummy.fight(player)
    player.fight(mummy)
    mummy.fight(player)
    if mummy.hp == 0:
      print("Player defeated mummy")
      victory()
  else:
    print("Mummy: A descendant of Inti would know! You fraud!")
    player = Fighter('Player', 4, 0, 5,['kick', 'tackle','horrible breath can make u pass out oof'] )
    mummy = Fighter('Mummy', 10, 7, 11,['sucker punch', 'jump', 'scratch', 'push'])
    mummy.fight(player)
    player.fight(mummy)
    mummy.fight(player)
    player.fight(mummy)
    mummy.fight(player)
    if player.hp == 0:
      print("Mummy defeated Player.")
      death_final()

#introducing the last barrier
def fifth_barrier():
  print(f"Inti: You have come a long way {username}")
  print(f"Inti:But the treasure that you seek is defended by a mummy.Try not to end up like him.")
  print()
  time.sleep(1)
  print("Inti vanishes. Before you is a room full of gold, silver, crystals, and riches beyond comprehension. This is the inheritance of the descendant of Inti.")
  print("From a dark corner, you hear the growls and cries of an awakening mummy")
  print("Mummy: Who dares to enter? Why if it isn't another foolish child trying to get something that isn't theirs")
  print("Mummy: I did the same as you. I made it to this very room. And there was a mummy waiting for me inside. He asked me a question that I didn't know the answer to.")
  print("The mummy defeated me. I thought there was no worse punihsment than death but I was wrong. The old mummy disintegrated and I became this. Cursed to guard a treasure that I can't even touch.")
  print("I must defeat you. I can no longer carry this burden. So I will ask you the same question that monster asked me...")
  fight_game()

#the fourth barrier
def fourth_barrier():
  #introducing the dancing game
  print("A now-familiar thud sounds behind you after you step through. You don't see anybody in this room, and are confused. Was this the end? A bit of movement catches your eye. On the wall is a little dancing picture. A voice sounds, and you soon realize it's coming from the figure on the wall itself. This has been a strange day, but this was definitely the most surreal thing you had experienced\n")
  clear()
  print("""

      o
     <|>
     / \\
    """)
  print("'Hello! I'm just here to dance. Copy my dance moves and you'll be able to pass through. Mess up, and Inti will burn you alive. How fun! Press the arrow key corresponding to the direction my arms are pointing. Press space when I jump. Be quick, or else you'll lose quick!")
  input("Press Enter to play")
  #each of the possible dance moves
  #ascii graphics:key on keyboard
  danceStates = {
      """

      \\o/
       |
      / \\
      """:"up",
      """

       o__
      <|
      / \\
      """:"right",
      """

     __o
       |>
      / \\
      """:"left",
      """

       o
      /|\\
      / \\
      """:"down",
      """
     __o__
       |
      / \\
      """:"space"
      }
  #list of all the dictionary keys (ascii graphics)
  keys = list(danceStates.keys())
  #setting counter for number of rounds
  n = 0
  #setting counter for dancing streak as well as score
  streak = 0
  score = 0
  #main while loop of the game
  while n < 6:
    clear()
    print("""

       o
      <|>
      / \\
      """)
    time.sleep(0.3)
    clear()
    print("""

       o
      <|\\
      / \\
      """)
    time.sleep(0.3)
    clear()
    print("""

       o
      /|>
      / \\
      """)
    time.sleep(0.3)
    clear()
    print("""

       o
      <|>
      / \\
      """)
    print("I'm warmed up, get ready!")
    time.sleep(2)
    clear()
    move = keys[random.randint(0,4)]
    print (move)
    #giving people 10 seconds to select a move
    now = time.time()
    end = now + 10
    while time.time() < end:
      if keyboard.is_pressed(danceStates[move]):
        pressDelay = round(time.time() - now,3)
        print("Good job!")
        print(pressDelay)
        time.sleep(1)
        streak+=1
        score+=(streak+1)*(2-pressDelay)
        break
      elif keyboard.read_key() != danceStates[move]:
        print("bad job")
        time.sleep(1)
        streak = 0
        break
      n+=1
  clear()
  if score > 30:
    print("Nice dancing! I guess no burning for you this time!")
    doorOpen()
    fifth_barrier()
  else:
    print("Dang, I guess they don't teach you how to dance, huh fumblefoot?")
    death_inti()

#Mama Quilla's challenge
def rps_game():
  #nested dictionary determines outcome
  who_won = {
    'stone': {
      'stone': 'You tied with Mama Quilla!\n',
      'cloth': 'you lose!\n',
      'blade': 'you win!',

    },
    'cloth': {
      'stone': 'you win!',
      'cloth': 'You tied with Mama Quilla!\n',
      'blade' : 'you lose!\n ',

    },
    'blade' : {
      'stone': 'you lose!\n',
      'cloth': 'You win!',
      'blade': 'You tied with Mama Quilla\n',}
  }

  #nested dictionary tells user why they tied, lost, or won the round
  why_lose = {
    'stone':{
      'stone':'stones are buddies u fool\n',
      'cloth':'cloth covers stone sadly\n',
      'blade':'u crushed them blades boii\n',
    },
    'cloth':{
      'cloth': 'at least now you have a blanket?\n',
      'blade': 'blade slashes through cloth real quick\n',
      'stone': 'you won that wrap battle\n',
    },
    'blade':{
      'blade': 'blades are sisters!\n',
      'stone': 'stone beats blade with a quick tap\n',
      'cloth': 'blade slashes though cloth real quick\n',
    },
  }
  #score board dictionary
  score= {
    'player_1':{
      'player_wins': 0,
      'player_losses' : 0,
      'player_ties': 0},
    'computer':{
      'computer_wins': 0,
      'computer_losses' : 0,
      'computer_ties': 0 }
      }
  #welcome the player to the game
  print("Welcome to a game of Stone, Cloth, Blade! You will have one round with Mama Quilla, and because she believes in you, if you tie wth her she will still let you pass. But if you fail...Good luck! \n")
  time.sleep(0.5)
  #determine the outcome of the game + tracks score each round
  def outcome(player_1, computer_choice):
    print(who_won[player_1][computer_choice])
    print(why_lose[player_1][computer_choice])
    #checking logic for who won using score dict
    if 'win' in who_won[player_1][computer_choice]:
      score['player_1']['player_wins'] +=1
      score['computer']['computer_losses'] +=1
      print('player has\n',score['player_1']['player_wins'],'wins\n',score['player_1']['player_losses'],'losses\n and',score['player_1']['player_ties'],'ties\n')
      doorOpen()
      if online == True:
        fifth_barrier()
      else:
        fourth_barrier()
    elif 'lose' in who_won[player_1][computer_choice]:
      score['player_1']['player_losses'] +=1
      score['computer']['computer_wins'] +=1
      print('player has\n',score['player_1']['player_wins'],'wins\n',score['player_1']['player_losses'],'losses\n and',score['player_1']['player_ties'],'ties\n')
      print("You have failed Mama Quilla")
      death_inti()
    else:
      score['player_1']['player_ties'] +=1
      score['computer']['computer_ties'] +=1
      print('player has\n',score['player_1']['player_wins'],'wins\n',score['player_1']['player_losses'],'losses\n and',score['player_1']['player_ties'],'ties\n')
      print("You may pass on to the next room")
      print("Excellent...your cleverness is worthy of Inti's descendant.")
      doorOpen()
      if online == True:
        fifth_barrier()
      else:
        fourth_barrier()
  #game function:
  def game():
    options = ['stone','cloth', 'blade']
    computer_choice = random.choice(options)
  #take in user input
    player_1 = input("stone, cloth, blade?\n").lower()
    options = ['stone','cloth', 'blade',]
    #gives player chance to input a valid answer
    while player_1 not in options:
      player_1 = input("Pick a valid option imbecile\n")
  #generate computer choice
    print("SCB SHOOT!...\n")
    print(player_1, 'vs',computer_choice)
    time.sleep(0.5)
    outcome(player_1, computer_choice)

  #asks player if they know how to play
  how_to=  input("Do you know how to play?\n")
  if how_to== 'yes':
    print("")
    game()
  #tells player the rules:
  else:
    print("\nThe rules are simple. Cloth covers stone and is cut by the blade. Stone beats the blade.\n")
    game()

#introducing the third challenge with story
def third_barrier():
  print(f"You walk through, a little more confident now. The door shuts behind you once again. This room has jewelry scattered on the floor. There is a ghostly woman facing away from you on the floor")
  time.sleep(1)
  print("Woman: I am Mama Quilla, goddess of the moon and wife of Inti the Sun God. You wear on your neck my moon penchant. When I first gave it to the king of my people, I told him to pass it on to every generation. From you comes an internal light, a mark of a descendant of Inti.")
  time.sleep(0.5)
  print("You realize the light you noticed was coming from yourself. This is mildly disconcerting, but you don't have time to ponder it as Mama Quilla speaks again.")
  time.sleep(1)
  print("That's why I'll make this easy for you.")
  time.sleep(0.5)
  print("The easiest game I know is Stone, Cloth, Blade. A descendant of Inti should have plenty of enough luck to win such a silly game.\nHer smile doesn't exactly comfort you")
  time.sleep(0.5)
  print("Mama Quilla: But don't worry. I like you. If we tie, I will still let you pass on to your final challenge.")
  rps_game()

#Pachamama's challenge, a few riddles
def riddle_game():
  #logic for getting riddles right or wrong
  riddle1= input("Pachamama:\nWhat has roots as nobody sees\nIs taller than trees\nUp, up it goes\nAnd yet never grows?\n")
  if riddle1.lower() == "mountain":
    print("Good job.")
    riddle2 = input("Pachamama:\nVoiceless it cries\nWingless flutters\nToothless bites\nMouthless mutters.\n")
    if riddle2.lower() == "wind":
      print("Excellent...your cleverness is worthy of Inti's descendant.")
      doorOpen()
      third_barrier()
    else:
      print("try a different riddle")
      riddle3= input("Pachamama:\nIt cannot be seen, cannot be felt, Cannot be heard, cannot be smelt.\nIt lies behind stars and under hills, And empty holes it fills.\nIt comes first and follows after, Ends life, kills laughter.\n")
      if riddle3.lower() == "dark" or "darkness":
        print("Excellent...your cleverness is worthy of Inti's descendant.")
        doorOpen()
        third_barrier()
      else:
        print("You have gotten too many wrong.")
        death_inti()
  else:
    print("Try a different riddle")
    riddle2_= input("Pachamama:\nVoiceless it cries\nWingless flutters\nToothless bites\nMouthless mutters.\n")
    if riddle2_.lower() == "wind":
      print("Good job. Try one more.")
      riddle3_= input("Pachamama:\nIt cannot be seen, cannot be felt, Cannot be heard, cannot be smelt.\nIt lies behind stars and under hills, and empty holes it fills.\nIt comes first and follows after, Ends life, kills laughter.\n")
      if riddle3_.lower() == "dark" or "darkness":
        print("Good job.You may pass")
        third_barrier()
      else:
        print("You are wrong. You got more than 1 wrong. Game over.")
        death_inti()
    else:
      print("You are wrong. You got more than 1 wrong. Game over.")
      death_inti()

#starting the second challenge
def second_barrier():
  print( f"You continue through the door, not really seeing any other choice. It shuts behind The room is full of shattered pots and colorful tapestry. Once again, there seems to be light coming from nowhere. The figure of a woman in the tapestry in front of you begins to take form.\n" )
  print()
  print("Woman: So you have met Inti. He rules over the Sun, and I the Earth. Our people took care of the soil that made them. You modern age children only destroy it. I will not make this easy for you.")
  print(f"You ask for her name")
  time.sleep(2)
  print("Woman: I am Pachamama, Mother Earth.")
  time.sleep(1)
  print("Pachamama: You will play a riddle game with me. I will give you three riddles. If you get two out of three riddles correct you may pass. If you get more than one wrong, you will meet Inti sooner than you'd like.")
  time.sleep(2)
  ready=input("Are you ready to play? 1 for yes and 2 for no\n")
  if ready == '1' :
      print("You will have to try 2-3 riddles!")
      riddle_game()
  elif ready == '2' :
      print("Too bad, we are getting started anyway!")
      riddle_game()


#the first challenge (a hangman game)
def first_barrier():
  ready=input("Are you ready? 1 for yes and 2 for no\n")
  if ready == '1' :
      print("Brave! You have 8 tries!")
  elif ready == '2' :
      print("Nobody is ever really ready. Unfortunately in this case you don't have a choice. You do have 8 tries though.")
  #hangman ascii art
  hangman= (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   -|-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-/
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-/
     |    |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-/
     |    |
     |    |
     |   |
     |   |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |  /-|-/
     |    |
     |    |
     |   | |
     |   | |
     |
    ----------
  """)
  #computer generates random word
  secret_word = "inti"
  #some motivating words for the player when they guess correctly
  motivation=("Wow!","Well done!", "You are doing a fantastic job!")
  #when user guesses right, the length of the secret word reduces by 2 each time
  max_=len(secret_word)+4
  #should print out underscores for each letter in computer generate word
  sofar= (" _ ") * len(secret_word)
  #empty list to store the guesses used by player
  used = []
  #counter for the number of wrong guesses
  wrong= 0
  guesses=0
  guesses_left=8
  input("Press Enter to begin the game!")
  print("\n H A N G M A N \n")
  #set limit of amount of tries
  while wrong < max_ and sofar != secret_word:
    print()
    #print hangman graphics
    clear()
    print(hangman[wrong])
    #shows user how many letters are left to guess
    print(f"The secret word so far: {sofar}")
    #shows user the letters they used
    print(f"Letters used so far: {used}")
    #tells user to guess a letter
    guess = input("Guess a letter \n")
    time.sleep(0.5)
    print()
    #if they guess the same letter, tell user they already used that letter
    while guess in used:
      print("Hey you already used this letter, try again!")
      guess=input("Guess a letter:")
      time.sleep(0.5)
      print()

    #add every guess to the empy list called used, as a storage list
    used.append(guess)
    #give user motivation to keep on guessing
    if guess in secret_word :
      print(random.choice(motivation),"...time to update the word!")
      new = ""
      for i in range(len(secret_word)):
        if guess == secret_word[i]:
          new += guess
        else:
          new += sofar[i]
      sofar=new
      guesses+=1
      guesses_left -=1
    elif len(guess) > 1:
      print("One character at a time please, you filthy cheater.")
    else:
      wrong += 1
      guesses += 1
      guesses_left-=1
      print(f"Wrong guess foolish wanderer! You have {guesses_left} guesses left")
  print("Calculating result from your input...")
  time.sleep(0.5)
  #checks if the user has won or not
  if wrong == max_ :
    print(f"Oof,you're out of tries. You guessed {guesses} times. Prepare to meet Inti.")
    death_inti()
  else:
    print("Inti")
    print(f" You have done well {username}. You guessed {guesses} times")
    print()
    print()
    #unlocking the door
    input("Press Enter to reach the door...")
    clear()
    print("""
  |          |
  |          |
  |__________|
  """)
    print(f"{username} put in 'Inti' as the code")
    time.sleep(3)
    clear()
    print("""
  |          |
  |          |
  |          |
  """)
    #going to the second challenge
    second_barrier()



#introductory story
print("\n||DESCENDANTS||\n")
print("You are on vacation in Peru. You came here just by yourself to unwind and relax. Hiking up the mountain, you shiver a little bit and pull your wool blanket your mother gave you a little closer. It's June, the peak of summer back at home, but this area was submerged deep into winter.\nThere are ruins around you, and every once in a while you take a note of something in your notebook. Walking along the path, you spot an old man sitting on the side who doesn't look like your average tourist. He makes eye contact, and holds his gaze. You feel uncomfortable, but at the same time something urges you closer to him.")
oldMan = input("Do you go over to him (1), or keep walking (2)? ")
if oldMan != "1":
  print("You make your way along the path, ostensibly ignoring his existence. Your mind seems unsure of itself. The rest of your vacation is relatively uneventful, but you can't shake the feeling you missed out on something.")
elif oldMan == "1":
  print("You make your way over to him, following some strange feeling in your head. He smiles as you come closer, standing up in place. He is of shorter stature, much like the Quechua-speaking Incas you had met earlier. 'Tell me child, what is your name?' he asks.")
  username = input("What is your name?\n")
  print(f"'{username},' you answer.\nThe old man smiles as if the name means something. '{username}, do you know where we are?\n'Machu Picchu, of course,' you answer, thinking that was a strange question to ask.\n'Yes, Machu Picchu. A place as old as any on Earth. It's inhabitants, the Incas, worshipped the sun god Inti. Their king, their god, the Sapa Inka, ruled over them from dynasty to dynasty, starting from the son of Inti himself, Manco Capac, all the way to the last one, Atahualpa.'\nAll of this sounds strangely familiar to you. 'Why are you telling me this?' you ask.\n'You are special.' He reaches for the penchant in the shape of the moon around your neck, the one your mother gave you. 'Yes, you are special.'\nYou turn away for a second as a condor overhead catches your eye, and the old man is gone. You assume he slipped into one of the many side streets. That was definitely a strange experience.")
  follow = input("Do you try to follow him to find out more but risk losing your way (1), or continue up the mountain (2)? ")
  if follow == "1":
    print("You dive into the alleys, hoping to find the old man and ask him more about his identity and maybe even yours. It does not take long before you are hopelessly lost, however. Suddenly, on your next step, the seemingly solid floor under you slips away as you fall into a wide chamber.")
  elif follow == "2":
    print("Shrugging it off, you continue up the mountain. Although there were many people milling up and down before, it seems in your time with the man all of them had gone. You plod up through the path. Suddenly, on your next step, the seemingly solid floor under you slips away as you fall into a wide chamber.")
  print("Strangely, you are not hurt, even if a fall of that height could've broken a leg or two. There is no discernible source of light, yet you can see everything around you just fine, as if illuminated by some glow.")
  print(f"Voice: Welcome {username}! I know what it is you seek. But you don't know me, and I don't help strangers. The door is locked and only by knowing the code will you be able to pass your first barrier.")
  print("""
  |          |
  |          |
  |__________|
  """)
  print("You have no idea what he is talking about.")
  stayAndDie = int(input("Do you decide to go along (1), or try to find your way out (2)? "))
  if stayAndDie == 1:
    guess_wanted = input("You will play a simple game of Hangman to find out the code with a total of 8 tries. Win or lose you will face me again. Do you wish for a hint?\n")
    if guess_wanted.lower() == "yes" or "y":
        print("I rule over fire rolled in a ball.\nPowerful and ancient, I watched my great empire fall. \nMy people loved me the most until they saw ghosts coming from the sea. \nThe mortal deceived them, made them think he was me.")
    elif guess_wanted.lower() == "no" or "n":
        print("No? How disgustingly proud. Fare as you will on your own luck.")
    else:
      print("I understand not what you said, but I wish you the best of luck.")
    time.sleep(0.1)
    first_barrier()
  else:
    print("You decide to ignore the voice. You claw your way around the rocks, but find no way out. Fairly soon, you realize you are probably going to die here. At least you don't have any friends to wonder what happened.")
