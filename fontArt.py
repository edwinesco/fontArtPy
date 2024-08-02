# Ejemplo tomado de cloding.com

# pip install pyfiglet
# pip install colored

import pyfiglet
from termcolor import colored

text = input("Ingrese el texto que quiere fomatear: ")
fuentes = pyfiglet.FigletFont.getFonts()
print("Listado de fuentes\n")
for fuente in fuentes:
    print(fuente)
font = input("Ingrese la fuente que quiere usar (Enter para la fuente por defecto): ")
color = input("ingrese el color que quiere en Ingles (ej: red, green, yellow...): ")

if font:
    formated_text = pyfiglet.figlet_format(text, font=font)
else:
    formated_text = pyfiglet.figlet_format(text)

if color:
    colored_text = colored(formated_text ,color)
    print(colored_text)
else:
    print(formated_text)