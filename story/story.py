import prompt
import dare
import character

def main():
    choice = "0"
    PROMPT = "1"
    CHARACTER = "2"
    DARE = "3"
    QUIT = "4"
    print("Are you stuck in your writing? Do you just need a little idea to push you back into your story?")
    while choice != QUIT:
        print("MENU")
        print("1) Prompts")
        print("2) Character Names")
        print("3) Writing Dare")
        print("4) Quit")
        choice = input("Which one will it be? ")
        if choice == PROMPT:
            print(prompt.random_prompt())
        elif choice == CHARACTER:
            print(character.random_character())
        elif choice == DARE:
            print(dare.random_dare())
        elif choice == QUIT:
            print("Ending program.")
        else:
            print("Was that really what you wanted to do?")
main()