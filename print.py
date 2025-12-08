# Hello World may seem like just a simple phrase on the screen, but it represents much more than that. It is your first command, the moment when you say to the computer: “I am here and I can create things!” This small step shows that everything is working and that you are already capable of transforming ideas into code. From there, you will evolve, learn new logic, build projects, and solve real problems. So celebrate: every great programmer started exactly where you are now. Your “Hello World” is the beginning of a future full of possibilities. 🚀💻
def english():
    print("english - Hello, World!") #🇺🇸
def portuguese():
    print("portuguese - Olá, Mundo!") #🇧🇷
def spanish():
    print("¡Hola, mundo!")
def german():
    print("Hallo Welt!")
def french():
    print("Bonjour, le monde!")
def janapese():
    print("こんにちは、世界!")
def italian():
    print("Ciao, mondo!")

# Beginning of my program
print("\nWelcome to my program. Here you will choose the language in which you will see your Hello World.\nShall we get inspired to learn more languages? So choose one!\nIf there is a language you can't find, figure it out yourself and search on Google.")

# Menu to choose the language that will run the code
print("\n1. English\n2. Portuguese\n3. Spanish\n4. German\n5. French\n6. Japanese\n7. Italian")

# User choice to know in which language the code will run
selection = int(input("\nSelect the option you want to see your Hello World: "))

# Repeat loop to make the user choose an existing number from the menu
while selection < 1 or selection > 7:
    print("\nThis option does not exist in the menu. Invalid option, please try again!")
    selection = int(input("\nSelect the option you want to see your Hello World: "))

# Conditional structure
if selection == 1:
    english()
    print("\nThanks for using my program. See you around!")
elif selection == 2:
    portuguese()
    print("\nObrigado por usar o meu programa. Até mais!")
elif selection == 3:
    spanish()
    print("\nGracias por utilizar mi programa. ¡Nos vemos!")
elif selection == 4:
    german()
    print("\nDanke, dass du mein Programm benutzt hast. Bis bald!")
elif selection == 5:
    french()
    print("\nMerci d'utiliser mon programme. À bientôt !")
elif selection == 6:
    janapese()
    print("\n私のプログラムをご利用いただきありがとうございます。またお会いしましょう！")
else:
    italian()
    print("\nGrazie per aver utilizzato il mio programma. Ci vediamo!")

print('''\n
▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄ 　 █▀▀▄ █░░█ 　 ▒█▀▄▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀ 　 ░█▀▀█ █░░ █▀▄▀█ █▀▀ ░▀░ █▀▀▄ █▀▀█ 
▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ █▀▀ █░░█ 　 █▀▀▄ █▄▄█ 　 ▒█▒█▒█ █▄▄█ █▄▄▀ █░░ █░░█ ▀▀█ 　 ▒█▄▄█ █░░ █░▀░█ █▀▀ ▀█▀ █░░█ █▄▄█ 
▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░ 　 ▀▀▀░ ▄▄▄█ 　 ▒█░░▒█ ▀░░▀ ▀░▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀░░░▀ ▀▀▀ ▀▀▀ ▀▀▀░ ▀░░▀''')