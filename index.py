import random
import time

def banner():
    print(
        """
███    ███ ██    ██     ███████  ██████   ██████  ██████      ██████   █████  ██ ██████  ██    ██ 
████  ████  ██  ██      ██      ██    ██ ██    ██ ██   ██     ██   ██ ██   ██ ██ ██   ██  ██  ██  
██ ████ ██   ████       █████   ██    ██ ██    ██ ██   ██     ██   ██ ███████ ██ ██████    ████   
██  ██  ██    ██        ██      ██    ██ ██    ██ ██   ██     ██   ██ ██   ██ ██ ██   ██    ██    
██      ██    ██        ██       ██████   ██████  ██████      ██████  ██   ██ ██ ██   ██    ██    


                   Baked with love. 
                   - R4P7UR3
        """
    )



def main():
    comfort_food = ["Noodles!", "Chocolate Cake!", "Ice Cream!"]
    fine_food = ["Chicken Parmi!", "Stir Fry!", "Burritos!"]


    user_mood = input("What's your current mood? [sad, fine] : ")
    
    if user_mood == "sad":
        print("I hope you feel better soon :( enjoy your: \n" + random.choice(comfort_food))
        f = open("foodlog.txt", "a")
        f.write("Sad_Choice: " + random.choice(comfort_food) + "\n")
        f.close()

    elif user_mood == "fine":
        print("I hope you enjoy your: \n" + random.choice(fine_food))
        f = open("foodlog.txt", "a")
        f.write("Fine_Choice: " + random.choice(fine_food) + "\n")
        f.close()

    else:
        print("[ X ] You have chosen an invalid option.")
        f = open("foodlog.txt", "a")
        f.write("Error Generated: Invalid choice." + "\n")
        f.close()

banner()
main()

# TODO: Implement a system to log the exact food item chosen to later exclude that from repeating.