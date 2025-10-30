import os 
import random
#bored
def create_character(name, character_class):
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = random.randint(50, 200)  # Random gold between 50 and 200
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character

def calculate_stats(character_class, level):
    if character_class.lower() == "barbarian":
        strength = 20 + level * 3
        magic = 2 + level
        health = 120 + level * 6
    elif character_class.lower() == "warrior":
        strength = 10 + level * 2
        magic = 2 + level
        health = 100 + level * 5
    elif character_class.lower() == "mage":
        strength = 5 + level
        magic = 15 + level * 3
        health = 80 + level * 4
    elif character_class.lower() == "rogue":
        strength = 8 + level * 2
        magic = 8 + level * 2
        health = 70 + level * 3
    elif character_class.lower() == "cleric":
        strength = 7 + level
        magic = 12 + level * 2
        health = 90 + level * 4
    else:
        strength = magic = health = 0
    return (strength, magic, health)

def save_character(character, filename):
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False  # fail if directory doesn't exist

    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True
    
def load_character(filename):
    if not os.path.exists(filename):
        return None 

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        key, value = line.strip().split(": ")
        key = key.split()[0].lower()
        if key in ["level", "strength", "magic", "health", "gold"]:
            character[key] = int(value)
        elif key == "character":
            character["name"] = value
        else:
            character[key] = value
    return character

def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health

# Main program area
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    char = create_character("Vulcan", "Barbarian")
    display_character(char)

    saved = save_character(char, "vulcan.txt")
    if saved:
        print("\nCharacter saved to vulcan.txt")

    loaded_char = load_character("vulcan.txt")
    print("\nLoaded character:")
    display_character(loaded_char)

    print("\nLeveling up...")
    level_up(loaded_char)
    display_character(loaded_char)
