from time import sleep

# Story theme: Life Simulator
print("It is a dark, stormy night. The sky outside of the window is filled with bright flashes of lightning and loud, crashing thunder. A family is growing impatient waiting for the baby to be born.")
sleep(10)

# Choose last name
print("What's the last name of the family?")
lastname = input("")
sleep(0.5)
print(f"You are born in the {lastname} family.")
print("")

# Choose gender
sleep(1)
print("'What's the gender of the baby?' asks your mom.")
sleep(0.5)
gender = input("What gender would you like to be? Reply [M] for male and [F] for female: ")

# First Loop
if gender == "M":
  # Choose name
  sleep(0.5)
  print("The baby's a boy! Now what should we call him...")
  sleep(0.5)
  maleName = input("Choose your name: ")
  sleep(0.5)
  print(f"That's it! Let's call the baby {maleName} {lastname}!")
  print("...")
  sleep(2)
  print("You grow up happily for a year. When you are 1 year old, your family decides to hold a birthday party for you.")
  sleep(2)
  print("You receive many presents, some big some small. They are piled up in front of you.")
  sleep(2)
  print("Your mother urges you to pick your favourite. You choose: ")
  sleep(2)
  print("1. A white crib outlined in real gold")
  sleep(1)
  print("2. A comfy, knitted, blue and white one-piece set")
  sleep(1)
  print("3. A stroller painted a variety of blues and greens")
  sleep(1)
  mchoice1 = input("Reply 1, 2, or 3: ")
  if mchoice1 == "1":
    sleep(0.5)
    print(f"'I knew it! {maleName} loves money just like I do. He's only one year old and he already knows to pick the most expensive gift,' says your dad.")
    sleep(2)
    print("Your parents are setting up your new crib. In the meantime, you are crawling around filled with energy.")
    sleep(2)
    print("Suddenly, you somehow manage to stand up. Your parents do not notice. Your options are: ")
    sleep(2)
    print("1. Try and walk forward step by step")
    sleep(1)
    print("2. Make a noise that grabs your parents attention")
    sleep(1)
    print("3. Sit back down and pretend nothing happened")
    mchoice2 = input("Choose 1, 2, or 3: ")
    # Second loop
    if mchoice2 == 1:
      print()
    elif mchoice2 == 2:
      print()
    elif mchoice2 == 3:
      print()
  elif mchoice1 == "2":
    sleep(0.5)
    print(f"'What a cute boy, {maleName} knows to pick the coziest, warmest present,' says your mom.")
  elif mchoice1 == "3":
    sleep(0.5)
    print(f"'You want to go outside huh? An outside person just like me!' says your dad.")
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
  print("1. A crib")
  print("2. A comfy, knitted, blue and white one-piece set")
  print("3. A stuffed elephant with blue jewels as eyes")
  giftChoice = input("Reply 1, 2, or 3: ")
else: 
  print("Please restart and choose a valid option")