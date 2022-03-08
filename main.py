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

if gender == "M":
  # First name
  sleep(0.5)
  print("The baby's a boy! Now what should we call him...")
  sleep(2)
  firstName = input("Choose your name: ")
  sleep(0.5)
  print(f"That's it! You are called {firstName} {lastname}!")
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
  choice1 = input("Reply 1, 2, or 3: ")
  # 1 Year old Gift Choice -> Crib
  if choice1 == "1":
    sleep(0.5)
    print(f"'I knew it! {firstName} loves money just like I do. He's only one year old and he already knows to pick the most expensive gift,' says your dad.")
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
    choice2 = input("Choose 1, 2, or 3: ")
    # Male Choice 1
    if choice2 == "1":
      sleep(0.5)
      print("You try and move your left foot forward. You end up falling and sit on the ground, stunned.")
      sleep(4)
      print("The thump you made from falling catches your parents' attention. They rush over and hold you while looking for bruises.")
      sleep(6)
      print("...")
      sleep(1)
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of boys playing soccer on the field")
      sleep(2)
      print("2. Join some kids sitting in the classroom reading a storybook")
      sleep(2)
      print("3. Stay with your parents")
      sleep(1)
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        sleep(2)
        print("GAME ENDED")
      
    # Male Choice 1
    elif choice2 == "2":
      sleep(0.5)
      print(f"'Oh my, look, {firstName} has stood up!' says your dad. Your mother rushes over and cries happily.")
      sleep(5)
      print("...")
      sleep(1)
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of boys playing soccer on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")
        
    # Male Choice 1
    elif choice2 == "3":
      sleep(0.5)
      print("Sitting back down, you continue to crawl around looking for toys and fun things to do.")
      sleep(4)
      print("...")
      sleep(1)
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of boys playing soccer on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")

  # 1 Year old Gift Choice -> Pyjamas
  elif choice1 == "2":
    sleep(0.5)
    print(f"'What a cute boy, {firstName} knows to pick the coziest, warmest present,' says your mom.")
    print("...")
    sleep(5)
    print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
    sleep(7)
    print("You've arrived at the kindergarten. Looking around, you choose to: ")
    sleep(2)
    print("1. Go over to the group of boys playing soccer on the field")
    print("2. Join some kids sitting in the classroom reading a storybook")
    print("3. Stay with your parents")
    choice3 = input("Choose [1/2/3]: ")
    
  # 1 Year old Gift Choice -> Stroller
  elif choice1 == "3":
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
    choice2 = input("Choose 1, 2, or 3: ")
    # Male Choice 1
    if choice2 == "1":
      print("You try and move your left foot forward. You end up falling and sit on the ground, stunned.")
      sleep(4)
      print("The thump you made from falling catches your parents' attention. They rush over and hold you while looking for bruises.")
      sleep(6)
      print("...")
      sleep(1)
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of boys playing soccer on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")
      
    # Male Choice 1
    elif choice2 == "2":
      print(f"'Oh my, look, {firstName} has stood up!' says your dad. Your mother rushes over and cries happily.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of boys playing soccer on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")

    # Male Choice 1
    elif choice2 == "3":
      print("Sitting back down, you continue to crawl around looking for toys and fun things to do.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of boys playing soccer on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")

  # 1 Year old Gift Choice -> Secret
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

# Choose gender
elif gender == "F":
  # First name
  print("The baby's a girl! Now what should we call her...")
  firstName = input("Choose your name: ")
  print(f"That's it! You are called {firstName} {lastname}!")
  print("...")
  sleep(2)
  print("You grow up happily for a year. When you are 1 year old, your family decides to hold a birthday party for you.")
  sleep(3)
  print("You receive many presents, some big some small. They are piled up in front of you.")
  sleep(5)
  print("Your mother urges you to pick your favourite. You choose: ")
  sleep(3)
  print("1. A white crib embedded with sparkling diamonds")
  sleep(1)
  print("2. A comfy, knitted, pink and white one-piece set of pyjamas")
  sleep(1)
  print("3. A stroller painted a variety of different flowers")
  sleep(1)
  choice1 = input("Reply 1, 2, or 3: ")
  # 1 Year old Female Gift Choice ->  Crib
  if choice1 == "1":
    print(f"'Aha, {firstName} likes shiny objects, doesn't she.' says your dad.")
    print("...")
    print("Your parents are setting up your new crib. In the meantime, you are crawling around filled with energy.")
    print("Suddenly, you somehow manage to stand up. Your parents do not notice. Your options are: ")
    print("1. Try and walk forward step by step")
    print("2. Make a noise that grabs your parents' attention")
    print("3. Sit back down and pretend nothing happened")
    choice2 = input("Choose 1, 2, or 3: ")
    # Female Choice 1
    if choice2 == "1":
      print("You try and move your left foot forward. You end up falling and sit on the ground, stunned.")
      sleep(4)
      print("The thump you made from falling catches your parents' attention. They rush over and hold you while looking for bruises.")
      sleep(6)
      print("...")
      sleep(1)
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of girls playing hop scotch on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")
      
    # Female Choice 1
    elif choice2 == "2":
      print(f"'Oh my, look, {firstName} has stood up!' says your dad. Your mother rushes over and cries happily.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of girls playing hop scotch on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")
      
    # Female Choice 1
    elif choice2 == "3":
      print("Sitting back down, you continue to crawl around looking for toys and fun things to do.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of girls playing hop scotch on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")

  # 1 Year old Female Gift Choice -> Pyjamas
  elif choice1 == "2":
    sleep(0.5)
    print(f"'What a cute girl, {firstName} knows to pick the coziest, warmest present,' says your mom.")
    print("...")
    sleep(5)
    print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
    sleep(7)
    print("You've arrived at the kindergarten. Looking around, you choose to: ")
    sleep(2)
    print("1. Go over to the group of girls playing hop scotch on the field")
    print("2. Join some kids sitting in the classroom reading a storybook")
    print("3. Stay with your parents")
    choice3 = input("Choose [1/2/3]: ")
    if choice3 == "1":
      # play on field
      print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
    elif choice3 == "2":
      # read books
      print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
    elif choice3 == "3":
      # stay with parents
      print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
    else:
      print("Please restart and choose a valid choice.")
      print("GAME ENDED")
    
  # 1 Year old Female Gift Choice -> Stroller
  elif choice1 == "3":
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
    choice2 = input("Choose 1, 2, or 3: ")
    # Female Choice 1
    if choice2 == "1":
      print("You try and move your left foot forward. You end up falling and sit on the ground, stunned.")
      sleep(4)
      print("The thump you made from falling catches your parents' attention. They rush over and hold you while looking for bruises.")
      sleep(6)
      print("...")
      sleep(1)
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of girls playing hop scotch on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")
      
    # Female Choice 1
    elif choice2 == "2":
      print(f"'Oh my, look, {firstName} has stood up!' says your dad. Your mother rushes over and cries happily.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for the first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of girls playing hop scotch on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")
      
    # Female Choice 1
    elif choice2 == "3":
      print("Sitting back down, you continue to crawl around looking for toys and fun things to do.")
      print("...")
      print("Three years have passed. You are now 4 years old. Your mother is bustling around getting you ready for tahe first day of kindergarten.")
      sleep(7)
      print("You've arrived at the kindergarten. Looking around, you choose to: ")
      sleep(2)
      print("1. Go over to the group of girls playing hop scotch on the field")
      print("2. Join some kids sitting in the classroom reading a storybook")
      print("3. Stay with your parents")
      choice3 = input("Choose [1/2/3]: ")
      if choice3 == "1":
        # play on field
        print("While playing, you accidentally fall and scrape your knee. The blood makes your friends cry and the teachers come over to calm them down and treat your knee.")
      elif choice3 == "2":
        # read books
        print(f"'Oh what a sweet child {firstName} is,' says your teacher.")
      elif choice3 == "3":
        # stay with parents
        print("Your parents are patiently trying to calm you down and convince you to go to kindergarten, but your whining is annoying your parents. They are end up leaving you with the teacher and have left.")
      else:
        print("Please restart and choose a valid choice.")
        print("GAME ENDED")

  # 1 Year old Gift Choice -> Secret
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