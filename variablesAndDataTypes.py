# Variables are used to store information that can be manipulated by the program. In Python, data types include integers, floats, strings, and booleans, among others. Understanding how to work with variables and data types is fundamental to programming, as it allows you to store and manipulate information efficiently.
def english():
    name = input("\nPlease enter your name: ")
    age = int(input("\nPlease enter your age: "))
    height = float(input("\nPlease enter your height: "))

    print("\nBelow are your details...")

    print(f"\n\tNAME: {name}\n\tAGE: {age}\n\tHEIGHT: {height}")

    print("\nThank you very much for testing my program!")
def portuguese():
    nome = input("Por favor, insira o seu nome: ")
    idade = int(input("\nPor favor, insira a sua idade: "))
    altura = float(input("\nPor favor, insira a sua altura: "))

    print("\nAbaixo estão os seus dados...")

    print(f"\n\tNOME: {nome}\n\tIDADE: {idade}\n\tALTURA: {altura}")

    print("\nMuito obrigado por experimentar o meu programa!")
def spanish():
    nombre = input("Por favor, ingrese su nombre: ")
    edad = int(input("\nPor favor, ingresa tu edad: "))
    altura = float(input("\nPor favor, ingresa tu altura: "))

    print("\nA continuación se muestran sus datos...")

    print(f"\n\tNOMBRE: {nombre}\n\tEDAD: {edad}\n\tALTURA: {altura}")

    print("\n¡Muchas gracias por probar mi programa!")
def german():
    name = input("\nBitte geben Sie Ihren Namen ein: ")
    alter = int(input("\nBitte geben Sie Ihr Alter ein: "))
    hohe = float(input("\nBitte geben Sie Ihre Körpergröße ein: "))

    print("\nNachfolgend finden Sie Ihre Angaben...")

    print(f"\n\tNAME: {name}\n\tALTER: {alter}\n\tHÖHE: {hohe}")

    print("\nVielen Dank, dass Sie mein Programm getestet haben!")
def french():
    nom = input("\nVeuillez saisir votre nom: ")
    age = int(input("\nVeuillez indiquer votre âge: "))
    hauteur = float(input("\nVeuillez indiquer votre taille: "))

    print("\nVous trouverez ci-dessous vos coordonnées...")

    print(f"\n\tNAME: {nom}\n\tAGE: {age}\n\tHAUTEUR: {hauteur}")

    print("\nMerci d'utiliser mon programme. À bientôt !")
def janapese():
    名前 = input("\nお名前を入力してください: ")
    年齢 = int(input("\n年齢を入力してください: "))
    高さ = float(input("\n高さを入力してください: "))

    print("\n以下がお客様の詳細情報です...")

    print(f"\n\t名前: {名前}\n\t年齢: {年齢}\n\t高さ: {高さ}")

    print("\n私のプログラムをご利用いただきありがとうございます。またお会いしましょう！")
def italian():
    nome = input("\nInserisci il tuo nome: ")
    età = int(input("\nInserisci la tua età: "))
    altezza = float(input("\nInserisci la tua altezza: "))

    print("\nBelow are your details...")

    print(f"\n\tNOME: {nome}\n\tETA: {età}\n\tALTEZZA: {altezza}")

    print("\nGrazie mille per aver provato il mio programma!")

# Here I am creating variables to store the name, age, and height. Next, I will print these values.
print("\nWelcome to my Python program. Here in this program, I created three variables (name, age, and height) and stored them\nthe values of different data types (string, integer, and float). The print function is used to display these values.")

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
    janapese()
else:
    italian()

print('''\n
▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄ 　 █▀▀▄ █░░█ 　 ▒█▀▄▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀ 　 ░█▀▀█ █░░ █▀▄▀█ █▀▀ ░▀░ █▀▀▄ █▀▀█ 
▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ █▀▀ █░░█ 　 █▀▀▄ █▄▄█ 　 ▒█▒█▒█ █▄▄█ █▄▄▀ █░░ █░░█ ▀▀█ 　 ▒█▄▄█ █░░ █░▀░█ █▀▀ ▀█▀ █░░█ █▄▄█ 
▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░ 　 ▀▀▀░ ▄▄▄█ 　 ▒█░░▒█ ▀░░▀ ▀░▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀░░░▀ ▀▀▀ ▀▀▀ ▀▀▀░ ▀░░▀''')