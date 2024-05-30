import pyautogui
import time
import secrets

def random_delay(min_delay=-10, max_delay=10):
    """Generate a cryptographically secure random delay between min_delay and max_delay seconds."""
    return min_delay + (max_delay - min_delay) * secrets.SystemRandom().random()

def locate_pokemon_on_screen(pokemon_images, confidence=0.9):
    """Locate any of the specified Pokémon images on the screen."""
    for pokemon, image in pokemon_images.items():
        try:
            if pyautogui.locateOnScreen(image, confidence=confidence):
                return pokemon
        except pyautogui.ImageNotFoundException:
            pass
    return None

def check_for_pokemon(pokemon_images, timeout=5):
    """Check for a Pokémon within the specified timeout period."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        pokemon = locate_pokemon_on_screen(pokemon_images)
        if pokemon:
            print(f"You are facing a {pokemon}!")
            return pokemon
        time.sleep(0.1)
    return None

def pokemon_still_alive(pokemon_images, min_alive_time=2):
    """Check if the Pokémon is still alive for at least the specified time."""
    start_time = time.time()
    while time.time() - start_time < min_alive_time:
        if not locate_pokemon_on_screen(pokemon_images):
            return False
        time.sleep(0.1)
    return True

def fight_pokemon():
    """Initiate the fight sequence by selecting 'fight' and the first move."""
    pyautogui.press('e')  # Select 'fight'
    time.sleep(random_delay(0.1, 0.5)) 
    pyautogui.press('e')  # Select the first move

def run_through_grass():
    """Run back and forth in the grass."""
    pyautogui.keyDown('a')
    time.sleep(random_delay(0.5,1))
    pyautogui.keyUp('a')
    time.sleep(random_delay(0.1,0.2))
    pyautogui.keyDown('d')
    time.sleep(random_delay(0.5, 1))
    pyautogui.keyUp('d')
    time.sleep(random_delay(0.1,0.2))
    pyautogui.keyDown('a')
    time.sleep(random_delay(0.5,1))
    pyautogui.keyUp('a')
    time.sleep(random_delay(0.1,0.2))
    pyautogui.keyDown('d')
    time.sleep(random_delay(0.5,1))
    pyautogui.keyUp('d')

def main():
    """XP Grind"""
    pokemon_images = {
        #"Rattata": "screenshots/3.png",
        #"Mankey": "screenshots/4.png",
        "HP Bar": "screenshots/7.png"
    }
    
    time.sleep(5)  # Initial delay before starting the main loop
    while True:
        run_through_grass()
        found_pokemon = check_for_pokemon(pokemon_images)
        if found_pokemon:
            if pokemon_still_alive(pokemon_images):
                while pokemon_still_alive(pokemon_images):
                    fight_pokemon()
                    time.sleep(random_delay(4, 5))  # Wait between attacks to ensure move execution
                print(f"Defeated {found_pokemon}!")
            else:
                print(f"The {found_pokemon} ran away!")
            time.sleep(random_delay(1, 2))  # Wait a moment before starting to run again

if __name__ == "__main__":
    main()
