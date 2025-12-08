# Lists are fundamental in Python for storing and manipulating collections of data.
# Understanding how to create, access, and modify lists is essential for many programs.
# This Python exercise helps beginners become familiar with lists and practice iterating over them.

# In this example, the user will be asked a few questions to be added to a list.
# Immediately afterwards, the data will be displayed on the screen.

# Creating the empty list
def portuguese():
    lista = []

    # Loop para confirmar dados
    while True:
    # Coletando dados do usuário
        nomeCompleto = input("\nPor favor, digite o seu nome completo: ")
        idade = int(input("Por favor, agora digite a sua idade: "))
        sexo = input("Sexo (Masculino ou Feminino): ")
        estadoCivil = input("Estado civil: ")
        cpf = input("CPF (ex; 123.456.789-00): ")
        telefone = input("Telefone (ex; 11 99999-9999): ")
        email = input("E-mail: ")
        profissao = input("Profissão: ")
        empresaOndeTrabalha = input("Empresa onde trabalha: ")

        # Mostrando dados para confirmação
        print("\n=== CONFIRA SEUS DADOS ===")
        print(f"Nome: {nomeCompleto}")
        print(f"Idade: {idade}")
        print(f"Sexo: {sexo}")
        print(f"Estado Civil: {estadoCivil}")
        print(f"CPF: {cpf}")
        print(f"Telefone: {telefone}")
        print(f"E-mail: {email}")
        print(f"Profissão: {profissao}")
        print(f"Empresa: {empresaOndeTrabalha}")

        # Perguntando se os dados estão corretos
        confirmar = input("\nOs dados estão corretos? (S/N): ").strip().lower()

        # Se estiverem corretos, salvar e sair do loop
        if confirmar == "s":
            lista.append([
                nomeCompleto,
                idade,
                sexo,
                estadoCivil,
                cpf,
                telefone,
                email,
                profissao,
                empresaOndeTrabalha
            ])
            print("\nCadastro realizado com sucesso! 🎉")
            break
        else:
            print("\nVamos refazer o cadastro...")

    # Mostrando dados salvos
    print("\n=== CADASTRO REALIZADO ===")
    print(f"\n\tNome: {lista[0][0]}")
    print(f"\tIdade: {lista[0][1]}")
    print(f"\tSexo: {lista[0][2]}")
    print(f"\tEstado Civil: {lista[0][3]}")
    print(f"\tCPF: {lista[0][4]}")
    print(f"\tTelefone: {lista[0][5]}")
    print(f"\tE-mail: {lista[0][6]}")
    print(f"\tProfissão: {lista[0][7]}")
    print(f"\tEmpresa: {lista[0][8]}")
def english():
    # Creating the empty list
    list = []

    # Loop to confirm data
    while True:
        # Collecting user data
        fullName = input("\nPlease enter your full name: ")
        age = int(input("Please enter your age now: "))
        sex = input("Gender (Male or Female): ")
        maritalStatus = input("Marital status: ")
        socialSecurityNumber = input("Social Security Number: ")
        telephone = input("Telephone: ")
        email = input("E-mail: ")
        profession = input("Profession: ")
        company = input("Company where you work: ")

        # Showing data for confirmation
        print("\n=== VERIFY YOUR DATA ===")
        print(f"Full Name: {fullName}")
        print(f"Age: {age}")
        print(f"Sex: {sex}")
        print(f"Marital status: {maritalStatus}")
        print(f"Social security number: {socialSecurityNumber}")
        print(f"Telephone: {telephone}")
        print(f"E-mail: {email}")
        print(f"Profession: {profession}")
        print(f"Company: {company}")

        # Asking if the data is correct
        confirm = input("\nIs the data correct? (Y/N): ").strip().lower()

        # If correct, save and exit the loop
        if confirm == "y":
            list.append([
                fullName,
                age,
                sex,
                maritalStatus,
                socialSecurityNumber,
                telephone,
                email,
                profession,
                company
            ])
            print("\nCadastro realizado com sucesso! 🎉")
            break
        else:
            print("\nVamos refazer o cadastro...")

    # Showing saved data
    print("\n=== REGISTRATION COMPLETED ===")
    print(f"\n\tFull Name: {list[0][0]}")
    print(f"\tAge: {list[0][1]}")
    print(f"\tSex: {list[0][2]}")
    print(f"\tMarital status: {list[0][3]}")
    print(f"\tSocial security number: {list[0][4]}")
    print(f"\tTelephone: {list[0][5]}")
    print(f"\tE-mail: {list[0][6]}")
    print(f"\tProfession: {list[0][7]}")
    print(f"\tCompany: {list[0][8]}")
def spanish():
    # Crear la lista vacía
    lista = []

    # Bucle para confirmar datos
    while True:
        # Recopilando datos del usuario
        nombreCompleto = input("\nPor favor, ingrese su nombre completo: ")
        edad = int(input("Por favor, ahora ingrese su edad: "))
        sexo = input("Sexo (Masculino o Femenino): ")
        estadoCivil = input("Estado civil: ")
        numeroSeguridadSocial = input("Número de Seguridad Social: ")
        telefono = input("Teléfono: ")
        correoElectronico = input("Correo electrónico: ")
        profesion = input("Profesión: ")
        empresaDondeTrabaja = input("Empresa donde trabaja: ")

        # Mostrando datos para confirmación
        print("\n=== VERIFIQUE SUS DATOS ===")
        print(f"Nombre completo: {nombreCompleto}")
        print(f"Edad: {edad}")
        print(f"Sexo: {sexo}")
        print(f"Estado civil: {estadoCivil}")
        print(f"Número de Seguridad Social: {numeroSeguridadSocial}")
        print(f"Teléfono: {telefono}")
        print(f"Correo electrónico: {correoElectronico}")
        print(f"Profesión: {profesion}")
        print(f"Empresa: {empresaDondeTrabaja}")

        # Preguntando si los datos son correctos
        confirmar = input("\n¿Los datos son correctos? (S/N): ").strip().lower()

        # Si son correctos, guardar y salir del bucle
        if confirmar == "s":
            lista.append([
                nombreCompleto,
                edad,
                sexo,
                estadoCivil,
                numeroSeguridadSocial,
                telefono,
                correoElectronico,
                profesion,
                empresaDondeTrabaja
            ])
            print("\n¡Registro completado con éxito! 🎉")
            break
        else:
            print("\nVamos a rehacer el registro...")

    # Mostrando datos guardados
    print("\n=== REGISTRO COMPLETADO ===")
    print(f"\n\tNombre completo: {lista[0][0]}")
    print(f"\tEdad: {lista[0][1]}")
    print(f"\tSexo: {lista[0][2]}")
    print(f"\tEstado civil: {lista[0][3]}")
    print(f"\tNúmero de Seguridad Social: {lista[0][4]}")
    print(f"\tTeléfono: {lista[0][5]}")
    print(f"\tCorreo electrónico: {lista[0][6]}")
    print(f"\tProfesión: {lista[0][7]}")
    print(f"\tEmpresa: {lista[0][8]}")
def german():
    # Erstellen der leeren Liste
    liste = []

    # Schleife zur Bestätigung der Daten
    while True:
        # Sammeln der Benutzerdaten
        vollerName = input("\nBitte geben Sie Ihren vollständigen Namen ein: ")
        alter = int(input("Bitte geben Sie jetzt Ihr Alter ein: "))
        geschlecht = input("Geschlecht (Männlich oder Weiblich): ")
        familienstand = input("Familienstand: ")
        sozialversicherungsnummer = input("Sozialversicherungsnummer: ")
        telefon = input("Telefon: ")
        email = input("E-Mail: ")
        beruf = input("Beruf: ")
        firma = input("Firma, in der Sie arbeiten: ")

        # Anzeigen der Daten zur Bestätigung
        print("\n=== ÜBERPRÜFEN SIE IHRE DATEN ===")
        print(f"Vollständiger Name: {vollerName}")
        print(f"Alter: {alter}")
        print(f"Geschlecht: {geschlecht}")
        print(f"Familienstand: {familienstand}")
        print(f"Sozialversicherungsnummer: {sozialversicherungsnummer}")
        print(f"Telefon: {telefon}")
        print(f"E-Mail: {email}")
        print(f"Beruf: {beruf}")
        print(f"Firma: {firma}")

        # Fragen, ob die Daten korrekt sind
        bestätigen = input("\nSind die Daten korrekt? (J/N): ").strip().lower()

        # Wenn korrekt, speichern und die Schleife verlassen
        if bestätigen == "j":
            liste.append([
                vollerName,
                alter,
                geschlecht,
                familienstand,
                sozialversicherungsnummer,
                telefon,
                email,
                beruf,
                firma
            ])
            print("\nRegistrierung erfolgreich abgeschlossen! 🎉")
            break
        else:
            print("\nLassen Sie uns die Registrierung erneut durchführen...")

    # Anzeigen der gespeicherten Daten
    print("\n=== REGISTRIERUNG ABGESCHLOSSEN ===")
    print(f"\n\tVollständiger Name: {liste[0][0]}")
    print(f"\tAlter: {liste[0][1]}")
    print(f"\tGeschlecht: {liste[0][2]}")
    print(f"\tFamilienstand: {liste[0][3]}")
    print(f"\tSozialversicherungsnummer: {liste[0][4]}")
    print(f"\tTelefon: {liste[0][5]}")
    print(f"\tE-Mail: {liste[0][6]}")
    print(f"\tBeruf: {liste[0][7]}")
    print(f"\tFirma: {liste[0][8]}")
def french():
    # Création de la liste vide
    liste = []

    # Boucle pour confirmer les données
    while True:
        # Collecte des données utilisateur
        nomComplet = input("\nVeuillez entrer votre nom complet : ")
        age = int(input("Veuillez maintenant entrer votre âge : "))
        sexe = input("Sexe (Masculin ou Féminin) : ")
        etatCivil = input("État civil : ")
        numeroSecuriteSociale = input("Numéro de sécurité sociale : ")
        telephone = input("Téléphone : ")
        email = input("E-mail : ")
        profession = input("Profession : ")
        entreprise = input("Entreprise où vous travaillez : ")

        # Affichage des données pour confirmation
        print("\n=== VÉRIFIEZ VOS DONNÉES ===")
        print(f"Nom complet : {nomComplet}")
        print(f"Âge : {age}")
        print(f"Sexe : {sexe}")
        print(f"État civil : {etatCivil}")
        print(f"Numéro de sécurité sociale : {numeroSecuriteSociale}")
        print(f"Téléphone : {telephone}")
        print(f"E-mail : {email}")
        print(f"Profession : {profession}")
        print(f"Entreprise : {entreprise}")

        # Demande si les données sont correctes
        confirmer = input("\nLes données sont-elles correctes ? (O/N) : ").strip().lower()

        # Si elles sont correctes, enregistrer et quitter la boucle
        if confirmer == "o":
            liste.append([
                nomComplet,
                age,
                sexe,
                etatCivil,
                numeroSecuriteSociale,
                telephone,
                email,
                profession,
                entreprise
            ])
            print("\nInscription réussie ! 🎉")
            break
        else:
            print("\nRefaisons l'inscription...")

    # Affichage des données enregistrées
    print("\n=== INSCRIPTION TERMINÉE ===")
    print(f"\n\tNom complet : {liste[0][0]}")
    print(f"\tÂge : {liste[0][1]}")
    print(f"\tSexe : {liste[0][2]}")
    print(f"\tÉtat civil : {liste[0][3]}")
    print(f"\tNuméro de sécurité sociale : {liste[0][4]}")
    print(f"\tTéléphone : {liste[0][5]}")
    print(f"\tE-mail : {liste[0][6]}")
    print(f"\tProfession : {liste[0][7]}")
    print(f"\tEntreprise : {liste[0][8]}")
def japanese():
    # 空のリストの作成
    リスト = []

    # データを確認するためのループ
    while True:
        # ユーザーデータの収集
        フルネーム = input("\nフルネームを入力してください: ")
        年齢 = int(input("年齢を入力してください: "))
        性別 = input("性別 (男性または女性): ")
        婚姻状況 = input("婚姻状況: ")
        社会保障番号 = input("社会保障番号: ")
        電話番号 = input("電話番号: ")
        メールアドレス = input("メールアドレス: ")
        職業 = input("職業: ")
        勤務先 = input("勤務先: ")

        # 確認のためのデータ表示
        print("\n=== データを確認してください ===")
        print(f"フルネーム: {フルネーム}")
        print(f"年齢: {年齢}")
        print(f"性別: {性別}")
        print(f"婚姻状況: {婚姻状況}")
        print(f"社会保障番号: {社会保障番号}")
        print(f"電話番号: {電話番号}")
        print(f"メールアドレス: {メールアドレス}")
        print(f"職業: {職業}")
        print(f"勤務先: {勤務先}")

        # データが正しいかどうかを尋ねる
        確認 = input("\nデータは正しいですか？ (はい/いいえ): ").strip().lower()

        # 正しければ、保存してループを終了
        if 確認 == "はい":
            リスト.append([
                フルネーム,
                年齢,
                性別,
                婚姻状況,
                社会保障番号,
                電話番号,
                メールアドレス,
                職業,
                勤務先
            ])
            print("\n登録が完了しました！ 🎉")
            break
        else:
            print("\n登録をやり直しましょう...")

    # 保存されたデータの表示
    print("\n=== 登録完了 ===")
    print(f"\n\tフルネーム: {リスト[0][0]}")
    print(f"\t年齢: {リスト[0][1]}")
    print(f"\t性別: {リスト[0][2]}")
    print(f"\t婚姻状況: {リスト[0][3]}")
    print(f"\t社会保障番号: {リスト[0][4]}")
    print(f"\t電話番号: {リスト[0][5]}")
    print(f"\tメールアドレス: {リスト[0][6]}")
    print(f"\t職業: {リスト[0][7]}")
    print(f"\t勤務先: {リスト[0][8]}")
def italian():
    # Creazione dell'elenco vuoto
    lista = []

    # Ciclo per confermare i dati
    while True:
        # Raccolta dei dati dell'utente
        nomeCompleto = input("\nPer favore, inserisci il tuo nome completo: ")
        eta = int(input("Per favore, ora inserisci la tua età: "))
        sesso = input("Sesso (Maschile o Femminile): ")
        statoCivile = input("Stato civile: ")
        numeroSicurezzaSociale = input("Numero di sicurezza sociale: ")
        telefono = input("Telefono: ")
        email = input("E-mail: ")
        professione = input("Professione: ")
        azienda = input("Azienda in cui lavori: ")

        # Mostra i dati per la conferma
        print("\n=== VERIFICA I TUOI DATI ===")
        print(f"Nome completo: {nomeCompleto}")
        print(f"Età: {eta}")
        print(f"Sesso: {sesso}")
        print(f"Stato civile: {statoCivile}")
        print(f"Numero di sicurezza sociale: {numeroSicurezzaSociale}")
        print(f"Telefono: {telefono}")
        print(f"E-mail: {email}")
        print(f"Professione: {professione}")
        print(f"Azienda: {azienda}")

        # Chiedi se i dati sono corretti
        confermare = input("\nI dati sono corretti? (S/N): ").strip().lower()

        # Se sono corretti, salva ed esci dal ciclo
        if confermare == "s":
            lista.append([
                nomeCompleto,
                eta,
                sesso,
                statoCivile,
                numeroSicurezzaSociale,
                telefono,
                email,
                professione,
                azienda
            ])
            print("\nRegistrazione completata con successo! 🎉")
            break
        else:
            print("\nRifacciamo la registrazione...")

    # Mostra i dati salvati
    print("\n=== REGISTRAZIONE COMPLETATA ===")
    print(f"\n\tNome completo: {lista[0][0]}")
    print(f"\tEtà: {lista[0][1]}")
    print(f"\tSesso: {lista[0][2]}")
    print(f"\tStato civile: {lista[0][3]}")
    print(f"\tNumero di sicurezza sociale: {lista[0][4]}")
    print(f"\tTelefono: {lista[0][5]}")
    print(f"\tE-mail: {lista[0][6]}")
    print(f"\tProfessione: {lista[0][7]}")
    print(f"\tAzienda: {lista[0][8]}")

# Beginning of my program
print("\nWelcome to my program. Here you will be asked some questions to be added to a list.\nImmediately afterwards, the data will be displayed on the screen.\nLet's get started!")

# Menu to choose the language that will run the code
print("\n1. English\n2. Portuguese\n3. Spanish\n4. German\n5. French\n6. Japanese\n7. Italian")

# User choice to know in which language the code will run
selection = int(input("\nSelect the option you want to run the program: "))

# Repeat loop to make the user choose an existing number from the menu
while selection < 1 or selection > 7:
    print("\nThis option does not exist in the menu. Invalid option, please try again!")
    selection = int(input("\nSelect the option you want to run the program: "))

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
    japanese()
    print("\n私のプログラムをご利用いただきありがとうございます。またお会いしましょう！")
else:
    italian()
    print("\nGrazie per aver utilizzato il mio programma. Ci vediamo!")

print('''\n
▒█▀▀█ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀▄ 　 █▀▀▄ █░░█ 　 ▒█▀▄▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█ █▀▀ 　 ░█▀▀█ █░░ █▀▄▀█ █▀▀ ░▀░ █▀▀▄ █▀▀█ 
▒█░░░ █▄▄▀ █▀▀ █▄▄█ ░░█░░ █▀▀ █░░█ 　 █▀▀▄ █▄▄█ 　 ▒█▒█▒█ █▄▄█ █▄▄▀ █░░ █░░█ ▀▀█ 　 ▒█▄▄█ █░░ █░▀░█ █▀▀ ▀█▀ █░░█ █▄▄█ 
▒█▄▄█ ▀░▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░ 　 ▀▀▀░ ▄▄▄█ 　 ▒█░░▒█ ▀░░▀ ▀░▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ 　 ▒█░▒█ ▀▀▀ ▀░░░▀ ▀▀▀ ▀▀▀ ▀▀▀░ ▀░░▀''')