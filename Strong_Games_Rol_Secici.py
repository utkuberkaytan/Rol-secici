import colorama
from colorama import *
import random
import time
colorama.init(autoreset=True)

picked = False

roller = ["Advertising & Marketing", "Product Manager", "3D Modelling", "SFX & Music", "Animator", "Level Design"]
kisiler = ["Eren", "Efe", "Mesut", "Yiğit", "Taha"]
sanslikisi = ["Eren", "Efe", "Mesut", "Taha", "Berkay"]

print(Fore.CYAN + "STRONG MOON | STRONG GAMES")
print("")
print("")
time.sleep(1.5)
print(Fore.GREEN + "Rol Seçici")
time.sleep(1.5)
print("")


print(Fore.BLUE + "Berkay => Scripting")
time.sleep(2.0)


while len(kisiler) != 0:
    kisi1 = random.choice(kisiler)
    rol1 = random.choice(roller)
    print(Fore.BLUE + f"{kisi1} => {rol1}")
    kisiler.remove(kisi1)
    roller.remove(rol1)
    time.sleep(2.0)
print("")
print(Fore.LIGHTMAGENTA_EX + "İki rollu kişi seçiliyor...")
time.sleep(2.7)
ikirollu = random.choice(sanslikisi)
ikincirol = random.choice(roller)
print(Fore.LIGHTMAGENTA_EX + f"{ikirollu} >> {ikincirol}")
print("")
input("Bitirmek için Enter'a basın...")

