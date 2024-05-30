import pyautogui
import time
import secrets

def random_delay(min_delay=0.5, max_delay=1.0):
    """Generate a cryptographically secure random delay between min_delay and max_delay seconds."""
    return min_delay + (max_delay - min_delay) * secrets.SystemRandom().random()

def check_for_pokemon(timeout=5):
    pokemon_images = {
        "Rattata": "screenshots/3.png",
        "Mankey": "screenshots/4.png"
        #"HP Bar": "screenshots/5.png"
    }
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        for pokemon, image in pokemon_images.items():
            try:
                if pyautogui.locateOnScreen(image, confidence=0.8):
                    print(f"You are facing a {pokemon}!")
                    return pokemon
            except pyautogui.ImageNotFoundException:
                print(f"Image not found: {image}")
        time.sleep(0.1)
    return None

def fight_pokemon():
    # Select 'fight' and then the first move
    pyautogui.press('e')  # Select 'fight'
    time.sleep(random_delay(0.1, 0.5)) 
    pyautogui.press('e')  # Select the first move

def pokemon_still_alive():
    # Check if the Pokémon's sprite is still visible on screen
    pokemon_images = {
        "Rattata": "screenshots/3.png",
        "Mankey": "screenshots/4.png"
    }
    
    for pokemon, image in pokemon_images.items():
        try:
            if pyautogui.locateOnScreen(image, confidence=0.8):
                return True
        except pyautogui.ImageNotFoundException:
            continue
    return False

def run_back_and_forth():
    # Run back and forth in the grass
    pyautogui.keyDown('a')
    time.sleep(random_delay())
    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    time.sleep(random_delay())
    pyautogui.keyUp('d')

if __name__ == "__main__":
    time.sleep(5)
    while True:
        run_back_and_forth()
        found_pokemon = check_for_pokemon()
        if found_pokemon:
            while pokemon_still_alive():
                fight_pokemon()
                time.sleep(random_delay(5, 6))  # Wait between attacks to ensure move execution
            print(f"Defeated {found_pokemon}!")
            time.sleep(random_delay(1, 2))  # Wait a moment before starting to run again
