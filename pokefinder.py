import pyautogui
import time

def check_for_pokemon():
    # Assuming gen5sprites is in the same directory as the script
    pokemon_images = {
        "Rattata": "screenshots/3.png",
        "Mankey": "screenshots/4.png"
    }
    
    while True:
        for pokemon, image in pokemon_images.items():
            try:
                if pyautogui.locateOnScreen(image, confidence=0.8):
                    print(f"You are facing a {pokemon}!")
                    return pokemon
            except pyautogui.ImageNotFoundException:
                print(f"Image not found: {image}")
        time.sleep(1)

if __name__ == "__main__":
    found_pokemon = check_for_pokemon()
    print(f"Detected Pokemon: {found_pokemon}")