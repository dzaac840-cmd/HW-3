import colorama
from colorama import Fore, Style
colorama.init()

print("=== Атрибути Fore (кольори тексту) ===")
print(dir(Fore))
print("\n=== Атрибути Style (стиль тексту) ===")
print(dir(Style))

print(Fore.RED + "Це червоний текст")
print(Fore.GREEN + "Це зелений текст")
print(Fore.BLUE + "Це синій текст")

print(Style.BRIGHT + "Яскравий текст")
print(Style.DIM + "Тьмяний текст")

print("\nColorama дозволяє змінювати колір і стиль тексту у консолі.")
print("Основні елементи: init(), Fore, Style")