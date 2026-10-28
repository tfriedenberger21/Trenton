import random

OUNCES_PER_POUND = 16
DEFAULT_MOOD = "content"

def ounces_to_pounds(oz):
    return round(oz/OUNCES_PER_POUND, 2)

def introduce_baby(name, age, weightOZ):
    funny_things = [
        "trying to eat my own toes",
        "having a serious chat with my teddy bear",
        "making silly faces at the ceiling",
    ]
    favorite_thing = random.choice(funny_things)
    print(f"\nHi, I'm {name}! I'm {age} old and weigh {weightOZ} ounces.")
    print(f"I like {favorite_thing}!")

def eat(weightOZ, feedings):
    weightOZ += 11
    feedings += 1

    print("\nBaby: Yum Yum in my Tum Tum!")
    if feedings % 3 == 0:
        weightOZ = poop(weightOZ)

    return weightOZ, feedings, "Happy"

def drink(weightOZ, drinks):
    weightOZ += 8
    drinks += 1
    print("\nBaby: This has quenched my thirst very well.")
    if drinks % 3 == 0:
        weightOZ = pee(weightOZ)

    return weightOZ, drinks, "Content"

def poop(weightOZ):
    print("-Baby poops-")
    weightOZ -= 5
    return weightOZ

def pee(weightOZ):
    print("-Baby pees-")
    weightOZ -= 3
    return weightOZ

def laugh():
    print("\nHAHAHAHAHAHAHAHAHAHA")
    return "Happy"

def cry():
    print("\nBaby: WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWAAAAAAAAAAAAAAAAAAAAAAAA!")
    return "Sad"

def sleep():
    print("\n-Baby falls asleep dreaming about puppies-")
    return "Content"
def display_status(name, birthday, weightOZ, mood, feedings, drinks, height):
    print("\n--- Baby Status ---")
    print(f"Name: {name}")
    print(f"Birthday: {birthday}")
    print(f"Feedings: {feedings}")
    print(f"Drinks: {drinks}")
    print(f"Weight: {weightOZ} oz")
    print(f"Weight: {ounces_to_pounds(weightOZ)} lbs")
    print(f"Height: {height} in")
    print(f"Mood: {mood}")
    print("-------------------")

print("What is the baby's name?")
name = input("Name: ")

print("\nWhat is your baby's birthday?")
birthday = input("Birthday: ")

print("\nHow old is your baby? (For example: 3 months)")
age = input("Age: ")

print("\nWhat is your babies weight in ounces?")
weightOZ = int(input("Weight: "))

print("\nWhat is your babies height in inches?")
height = float(input("Height: "))

babyLoop = True
feedings = 0
drinks = 0
mood = DEFAULT_MOOD

introduce_baby(name, age, weightOZ)

while(babyLoop):
    userInput = ""

    print("\n-- Action List --")
    print("eat")
    print("drink")
    print("laugh")
    print("sleep")
    print("cry")
    print("status")
    print("home")

    userInput = input("Please type a command: ").lower()

    if userInput == "eat":
        weightOZ, feedings, mood = eat(weightOZ, feedings)
    elif userInput == "drink":
        weightOZ, drinks, mood = drink(weightOZ, drinks)
    elif userInput == "laugh":
        mood = laugh()
    elif userInput == "sleep":
        mood = sleep()
    elif userInput == "cry":
        mood = cry()
    elif userInput == "status":
        display_status(name, birthday, weightOZ, mood, feedings, drinks, height)
    elif userInput == "home":
        babyLoop = False
        display_status(name, birthday, weightOZ, mood, feedings, drinks, height)
    else:
        print("WRONG COMMAND IDIOT")

    if (drinks % 3 == 0 and feedings % 3 == 0) and (userInput == "eat" or userInput == "drink"):
        print("-Baby burps-")
