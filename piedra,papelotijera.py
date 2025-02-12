"""
se usa el modulo random para escoger una de las opciones.

"""
import random

def play():
    """Play the game"""
    user = input("Elige pi ->piedra, pa -> papel o ti -> tijera:\n")
    computer = random.choice(['pi', 'pa', 'ti'])
    if user == computer:
        print("Empate")
    if user == 'pi' and computer == 'ti':
        print("Ganaste")
    elif user == 'pa' and computer == 'pi':
        print("Ganaste")
    elif user == 'ti' and computer == 'pa':
        print("Ganaste")
    else:
        print("Perdiste")
play()
