from time import sleep

# Story theme: Life Simulator
print("It is a dark, stormy night. The sky outside of the window is filled with bright flashes of lightning and loud, crashing thunder. A family is growing impatient waiting for the baby to be born.")
sleep(9)

# Choose last name
print("What's the last name of the family?")
lastname = input("")
sleep(0.5)
print(f"You are born in the {lastname} family.")
print("")

# Choose gender
sleep(1)
print("'What's the gender of the baby?' asks your mom.")
sleep(1)
gender = input("What gender would you like to be? Reply [M] for male and [F] for female: ")

# First Loop
if gender == "M":
  # Choose name
  sleep(0.5)
  print("The baby's a boy! Now what should we call him...")
  sleep(2)
  maleName = input("Choose your name: ")
  sleep(0.5)
  print(f"That's it! Let's call the baby {maleName} {lastname}!")
  print("...")
  sleep(2)
  print("You grow up happily for a year. When you are 1 year old, your family decides to hold a birthday party for you.")
  sleep(3)
  print("You receive many presents, some big some small. They are piled up in front of you.")
  sleep(5)
  print("Your mother urges you to pick your favourite. You choose: ")
  sleep(3)
  print("1. A white crib outlined in real gold")
  sleep(1)
  print("2. A comfy, knitted, blue and white one-piece set of pyjamas")
  sleep(1)
  print("3. A stroller painted a variety of blues and greens")
  sleep(1)
  mchoice1 = input("Reply 1, 2, or 3: ")
  # Second loop
  if mchoice1 == "1":
    sleep(0.5)
    print(f"'I knew it! {maleName} loves money just like I do. He's only one year old and he already knows to pick the most expensive gift,' says your dad.")
    print("...")
    sleep(5)
    print("Your parents are setting up your new crib. In the meantime, you are crawling around filled with energy.")
    sleep(5)
    print("Suddenly, you somehow manage to stand up. Your parents do not notice. Your options are: ")
    sleep(3.5)
    print("1. Try and walk forward step by step")
    sleep(1)
    print("2. Make a noise that grabs your parents' attention")
    sleep(1)
    print("3. Sit back down and pretend nothing happened")
    sleep(1)
    mchoice2 = input("Choose 1, 2, or 3: ")
    # Third loop
    if mchoice2 == "1":
      print("You try and move your left foot forward. You end up falling and sit on the ground, stunned.")
      sleep(4)
      print("The thump you made from falling catches your parents' attention. They rush over and hold you while looking for bruises.")
      sleep(6)
      print("...")
      sleep(1)
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
    # Third loop
    elif mchoice2 == "2":
      print(f"'Oh my, look, {maleName} has stood up!' says your dad. Your mother rushes over and cries happily.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      
    # Third loop
    elif mchoice2 == "3":
      print("Sitting back down, you continue to crawl around looking for toys and fun things to do.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")

  # Second loop
  elif mchoice1 == "2":
    sleep(0.5)
    print(f"'What a cute boy, {maleName} knows to pick the coziest, warmest present,' says your mom.")
    print("...")
    sleep(5)
    print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
    

  # Second loop
  elif mchoice1 == "3":
    sleep(0.5)
    print(f"'You want to go outside huh? An outside person just like me!' says your dad.")
    print("...")
    sleep(3)
    print("Your parents are setting up your new stroller. In the meantime, you are crawling around filled with energy.")
    sleep(5)
    print("Suddenly, you somehow manage to stand up. Your parents do not notice. Your options are: ")
    sleep(3.5)
    print("1. Try and walk forward step by step")
    sleep(1)
    print("2. Make a noise that grabs your parents' attention")
    sleep(1)
    print("3. Sit back down and pretend nothing happened")
    sleep(1)
    mchoice2 = input("Choose 1, 2, or 3: ")
    # Third loop
    if mchoice2 == "1":
      print("You try and move your left foot forward. You end up falling and sit on the ground, stunned.")
      sleep(4)
      print("The thump you made from falling catches your parents' attention. They rush over and hold you while looking for bruises.")
      sleep(6)
      print("...")
      sleep(1)
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
    # Third loop
    elif mchoice2 == "2":
      print(f"'Oh my, look, {maleName} has stood up!' says your dad. Your mother rushes over and cries happily.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      
    # Third loop
    elif mchoice2 == "3":
      print("Sitting back down, you continue to crawl around looking for toys and fun things to do.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")

  # Second loop
  else:
    sleep(0.5)
    print("Aha, I see you've chosen the secret gift, a...")
    sleep(3)
    print("Thump")
    sleep(1)
    print("Thump")
    sleep(0.5)
    print("Thump")
    sleep(1)
    print("Hey you, it's time to wake up.")
    print("...")
    print("")
    sleep(2.5)
    print("GAME ENDED")
  
# First loop
elif gender == "F":
  print("The baby's a girl! Now what should we call her...")
  
  femaleName = input("Choose your name: ")
  print(f"That's it! Let's call the baby {femaleName} {lastname}!")
  print("...")
  print("You grow up happily for a year. When you are 1 year old, your family decides to hold a birthday party for you.")
  print("You receive many presents, some big some small. They are piled up in front of you.")
  print("Your mother urges you to pick your favourite. You choose: ")
  print("1. A A white crib embedded with sparkling, colourful diamonds")
  print("2. A comfy, knitted, pink and white one-piece set of pyjamas")
  print("3. A stuffed unicorn with silky, pink fur and a sparkling, gold horn")
  fChoice1 = input("Reply 1, 2, or 3: ")
  # Second Loop
  if fChoice1 == "1":
    print("")
  elif fChoice1 == "2":
    print("")
  elif fChoice1 == "3":
    print("")
  # Second loop
  else:
    sleep(0.5)
    print("Aha, I see you've chosen the secret gift, a...")
    sleep(3)
    print("Thump")
    sleep(1)
    print("Thump")
    sleep(0.5)
    print("Thump")
    sleep(1)
    print("Hey you, it's time to wake up.")
    print("...")
    print("")
    sleep(2.5)
    print("GAME ENDED")
else: 
  print("Please restart and choose a valid option")