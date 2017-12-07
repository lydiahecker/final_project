import random

def random_dare():
    number = random.randint(0,14)
    if number == 0:
        dare = "Kill a character, any character, but make it significant."
    elif number == 1:
        dare = "Have a character use a different language."
    elif number == 2:
        dare = "Someone discovers a secret about the protagonist."
    elif number == 3:
        dare = "Someone's car breaks done."
    elif number == 4:
        dare = "Your protagonist notices something about a different character for the first time."
    elif number == 5:
        dare = "Someone gets a pet."
    elif number == 6:
        dare = "A character gets caught having fun and being awkward (i.e. dancing/singing along to a song)"
    elif number == 7:
        dare = "Your main character wakes up from a nightmare."
    elif number == 8:
        dare = "Someone tells a joke that's not funny at all, they proclaim something like 'Hey, that was funny!'"
    elif number == 9:
        dare = "Foreshadow something through a facial expression or physical action."
    elif number == 10:
        dare = "Fake a death."
    elif number == 11:
        dare = "Have a character trail off after they realize no one is listening."
    elif number == 12:
        dare = "Have someone sneak up on your protagonist."
    elif number == 13:
        dare = "Have your protagonist sneak up on someone."
    elif number == 14:
        dare = "What is the overly friendly character hiding? Why?"
    return dare