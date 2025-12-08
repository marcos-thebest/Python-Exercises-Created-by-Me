# Performing mathematical operations is one of the most common tasks in programming. Python simplifies this task with intuitive operators and built-in functions. Understanding how to perform these operations is crucial for solving numerical problems and developing efficient algorithms. This Python exercise allows anyone (including beginners) to practice manipulating numbers and performing basic calculations. 💻✨

def english():
    num1 = int(input("\nLet's begin. Enter the first number: "))
    num2 = int(input("Very good, now enter the second number: "))

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    print(f"\nAddition: {num1} + {num2} = {addition}")
    print(f"\nSubtraction: {num1} - {num2} = {subtraction}")
    print(f"\nMultiplication: {num1} x {num2} = {multiplication}")
    print(f"\nDivision: {num1} / {num2} = {division:.1f}")

    print("\nEnd of program...")
def portuguese():
    num1 = int(input("\nVamos começar. Digite o primeiro número: "))
    num2 = int(input("Muito bom, agora digite o segundo número: "))

    adicao = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2

    print(f"\nAdição: {num1} + {num2} = {adicao}")
    print(f"\nSubtração: {num1} - {num2} = {subtracao}")
    print(f"\nMultiplicação: {num1} x {num2} = {multiplicacao}")
    print(f"\nDivisão: {num1} / {num2} = {divisao:.1f}") 

    print("\nFim do programa...")
def spanish():
    num1 = int(input("\nEmpecemos. Introduzca el primer número: "))
    num2 = int(input("Muy bien, ahora ingrese el segundo número: "))

    adicion = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2

    print(f"\nAdición: {num1} + {num2} = {adicion}")
    print(f"\nResta: {num1} - {num2} = {resta}")
    print(f"\nMultiplicación: {num1} x {num2} = {multiplicacion}")
    print(f"\nDivision: {num1} / {num2} = {division:.1f}")

    print("\nFin del programa...")
def german():
    num1 = int(input("\nFangen wir an. Geben Sie die erste Zahl ein: "))
    num2 = int(input("Sehr gut, geben Sie nun die zweite Zahl ein: "))

    zusatz = num1 + num2
    subtraktion = num1 - num2
    multiplikation = num1 * num2
    abteilung = num1 / num2

    print(f"\nZusatz: {num1} + {num2} = {zusatz}")
    print(f"\nSubtraktion: {num1} - {num2} = {subtraktion}")
    print(f"\nMultiplikation: {num1} x {num2} = {multiplikation}")
    print(f"\nAbteilung: {num1} / {num2} = {abteilung:.1f}")

    print("\nEnde des Programms...")
def french():
    num1 = int(input("\nCommençons. Entrez le premier chiffre: "))
    num2 = int(input("Très bien, entrez maintenant le deuxième chiffre: "))

    ajout = num1 + num2
    soustraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    print(f"\nAjout: {num1} + {num2} = {ajout}")
    print(f"\nSoustraction: {num1} - {num2} = {soustraction}")
    print(f"\nMultiplication: {num1} x {num2} = {multiplication}")
    print(f"\nDivision: {num1} / {num2} = {division:.1f}")

    print("\nFin du programme...")
def japanese():
    num1 = int(input("\n始めましょう。最初の数字を入力してください: "))
    num2 = int(input("よくできました。次に2番目の数字を入力してください。: "))

    追加 = num1 + num2
    減算 = num1 - num2
    乗算 = num1 * num2
    部門 = num1 / num2

    print(f"\n追加: {num1} + {num2} = {追加}")
    print(f"\n減算: {num1} - {num2} = {減算}")
    print(f"\n乗算: {num1} x {num2} = {乗算}")
    print(f"\n部門: {num1} / {num2} = {部門:.1f}")

    print("\nプログラム終了...")
def italian():
    num1 = int(input("\nCominciamo. Inserisci il primo numero: "))
    num2 = int(input("Molto bene, ora inserisci il secondo numero: "))

    aggiunta = num1 + num2
    sottrazione = num1 - num2
    moltiplicazione = num1 * num2
    divisione = num1 / num2

    print(f"\nAggiunta: {num1} + {num2} = {aggiunta}")
    print(f"\nSottrazione: {num1} - {num2} = {sottrazione}")
    print(f"\nMoltiplicazione: {num1} x {num2} = {moltiplicazione}")
    print(f"\nDivisione: {num1} / {num2} = {divisione:.1f}")

    print("\nFine del programma...")

# Explanation: This Python exercise uses the input function to obtain values from the user and perform mathematical operations. The code performs and prints the sum, subtraction, multiplication, and division of the numbers provided.
print("\nWelcome to my program using the Python language. In this exercise, you will enter two numbers\nto learn addition, subtraction, multiplication, and division of the numbers provided.")

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
    italian()

print('''\n
▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄ 　 █▀▀▄ █░░█ 　 ▒█▀▄▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀ 　 ░█▀▀█ █░░ █▀▄▀█ █▀▀ ░▀░ █▀▀▄ █▀▀█ 
▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ █▀▀ █░░█ 　 █▀▀▄ █▄▄█ 　 ▒█▒█▒█ █▄▄█ █▄▄▀ █░░ █░░█ ▀▀█ 　 ▒█▄▄█ █░░ █░▀░█ █▀▀ ▀█▀ █░░█ █▄▄█ 
▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░ 　 ▀▀▀░ ▄▄▄█ 　 ▒█░░▒█ ▀░░▀ ▀░▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀░░░▀ ▀▀▀ ▀▀▀ ▀▀▀░ ▀░░▀''')