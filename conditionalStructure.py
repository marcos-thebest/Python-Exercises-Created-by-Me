# Making decisions based on conditions is an essential skill. Conditional structures, such as if, elif, and else, allow a program to perform different actions based on different conditions. This is fundamental to creating dynamic and interactive programs. 🥷🏽❤️

def english():
    # The program asks for your age
    age = int(input("\nPlease enter your age: "))

    # Repeat loop to validate age
    while age <= 0:
        print("\nMy friend, you're joking with me that you typed that, right? Try again!")
        age = int(input("\nPlease enter your age: "))

    # Conditional Structure
    if age >= 18:
        print("\nYou are of legal age!")
    else:
        print("\nYou are underage!")

    print("\nEnd of program...")
def portuguese():
    # O programa solicita a sua idade
    idade = int(input("\nDigite a sua idade: "))

    # Laço de repetição para validar a idade
    while idade <= 0:
        print("\nMeu amigo, voce tá brincando comigo que você digitou isso, né? Tente novamente!")
        idade = int(input("\nDigite a sua idade: "))

    # Estrutura Condicional
    if idade >= 18:
        print("\nVoce é maior de idade!")
    else:
        print("\nVoce é menor de idade!")

    print("\nFim do programa...")
def spanish():
    # El programa te pregunta tu edad.
    edad = int(input("\nPor favor, ingresa tu edad: "))

    # Repite el bucle para validar la edad
    while edad <= 0:
        print("\nAmigo, ¿estás bromeando cuando dices que escribiste eso, verdad? ¡Inténtalo de nuevo!")
        edad = int(input("\nPor favor, ingresa tu edad: "))

    # Estructura condicional
    if edad >= 18:
        print("\nUsted es mayor de edad!")
    else:
        print("\nEres menor de edad!")

    print("\nFin del programa...")
def german():
    # Das Programm fragt nach Ihrem Alter
    alter = int(input("\nBitte geben Sie Ihr Alter ein: "))

    # Wiederhole Schleife, um Änderung zu validieren
    while alter <= 0:
        print("\nMein Freund, du machst doch Witze, dass du das geschrieben hast, oder? Versuch's noch mal!")
        alter = int(input("\nBitte geben Sie Ihr Alter ein: "))

    # Bedingte Struktur
    if alter >= 18:
        print("\nSie sind volljährig!")
    else:
        print("\nDu bist minderjährig!")

    print("\nEnde des Programms...")
def french():
    # Le programme vous demande votre âge
    age = int(input("\nVeuillez indiquer votre âge: "))

    # Répéter la boucle pour valider l'âge
    while age <= 0:
        print("\nMon ami, tu plaisantes en disant que tu as tapé ça, n'est-ce pas ? Réessaie !")
        age = int(input("\nVeuillez indiquer votre âge: "))

    # Structure conditionnelle
    if age >= 18:
        print("\nVous avez l'âge légal !")
    else:
        print("\nVous êtes mineur !")

    print("\nFin du programme...")
def japanese():
    # プログラムはあなたの年齢を尋ねます
    年齢 = int(input("\n年齢を入力してください: "))

    # ループを繰り返して年齢を検証する
    while 年齢 <= 0:
        print("\n友よ、君がそんなことを打ったなんて冗談だろ？やり直せ！")
        年齢 = int(input("\n年齢を入力してください: "))

    # 条件構造
    if 年齢 >= 18:
        print("\nあなたは法定年齢に達しています")
    else:
        print("\nあなたは未成年です")

    print("\nプログラム終了...")
def italian():
    # Il programma richiede la tua età
    eta = int(input("\nInserisci la tua ora di arrivo prevista: "))

    # Ripeti il ciclo per convalidare l'eta
    while eta <= 0:
        print("\nAmico mio, stai scherzando quando dici di aver scritto questo, vero? Riprova!")
        eta = int(input("\nInserisci la tua ora di arrivo prevista: "))

    # Struttura condizionale
    if eta >= 18:
        print("\nHai l'età legale!")
    else:
        print("\nSei sotto il peso!")

    print("\nFine del programma...")

# Conditional structures are essential for making decisions in a program. They allow the flow of the program to be changed based on different conditions. This Python exercise teaches beginners how to use conditionals to check a person's age and provide an appropriate response, an important step in creating more complex programs.
print("\nWelcome to my Python program. In this exercise, the program asks for the user's age, converts it\nthe value for (int) and uses a conditional structure (if-else) to check whether the user is greater than or less than\nage, printing the corresponding message.")

# Menu to choose the language that will run the code
print("\n1. English\n2. Portuguese\n3. Spanish\n4. German\n5. French\n6. Japanese\n7. Italian")

# User choice to know in which language the code will run
choose = int(input("\nSelect the language you want the program to run in: "))

# Repeat loop to make the user choose an existing number from the menu
while choose < 1 or choose > 7:
    print("\nThis option does not exist in the menu. Invalid option, please try again!")
    choose = int(input("\nSelect the language you want the program to run in: "))

# Conditional structure
if choose == 1:
    english()
elif choose == 2:
    portuguese()
elif choose == 3:
    spanish()
elif choose == 4:
    german()
elif choose == 5:
    french()
elif choose == 6:
    japanese()
else:
    italian

print('''\n
▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄ 　 █▀▀▄ █░░█ 　 ▒█▀▄▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀ 　 ░█▀▀█ █░░ █▀▄▀█ █▀▀ ░▀░ █▀▀▄ █▀▀█ 
▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ █▀▀ █░░█ 　 █▀▀▄ █▄▄█ 　 ▒█▒█▒█ █▄▄█ █▄▄▀ █░░ █░░█ ▀▀█ 　 ▒█▄▄█ █░░ █░▀░█ █▀▀ ▀█▀ █░░█ █▄▄█ 
▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░ 　 ▀▀▀░ ▄▄▄█ 　 ▒█░░▒█ ▀░░▀ ▀░▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀░░░▀ ▀▀▀ ▀▀▀ ▀▀▀░ ▀░░▀''')