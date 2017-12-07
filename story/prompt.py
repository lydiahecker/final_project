import random

def random_prompt():
    number = random.randint(0,6)
    if number == 0:
        prompt = "Write a story about a young mage who doesn't want to practice magic, but would rather be an adventurer."
    elif number == 1:
        prompt = "Write about two rival coffeeshops who are across the street from each other. How do they compete?"
    elif number == 2:
        prompt = "Write a story from the perspectives of both the protagonist and the antagonist. Make it so the reader doesn't know which is which. "
    elif number == 3:
        prompt = "Write a story about a family of different monsters and how they met."
    elif number == 4:
        prompt = "Write a story based on your life, but in a different world."
    elif number == 5:
        prompt = "Write a retelling of a classic fairytale with the antagonist and protagonist switched."
    elif number == 6:
        prompt = "There's a reason no one goes into the basement."
    return prompt