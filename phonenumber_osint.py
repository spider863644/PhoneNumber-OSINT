import os, time as t
os.system("clear")
try:
    import colorama
    import phonenumbers
except ModuleNotFoundError:
    print("\033[1;31;40m Some requirements are missing!\n\nRun \"pip install -r requirements.txt\" then run \"python3 phonenumber_osint.py \"\033[1;37;40m" )
    t.sleep(2)
    exit()
from colorama import *
from phonenumbers import geocoder, carrier, timezone
colorama.init(autoreset=True)
print(Fore.RED + "𝔻𝕚𝕤𝕔𝕝𝕒𝕚𝕞𝕖𝕣: 𝕌𝕤𝕖 𝕥𝕙𝕚𝕤 𝕥𝕠𝕠𝕝 𝕗𝕠𝕣 𝕖𝕕𝕦𝕔𝕒𝕥𝕚𝕠𝕟𝕒𝕝 𝕡𝕦𝕣𝕡𝕠𝕤𝕖𝕤 𝕠𝕟𝕝𝕪 \n\n𝕊𝕡𝕚𝕕𝕖𝕣 𝔸𝕟𝕠𝕟𝕘𝕣𝕖𝕪𝕙𝕒𝕥 𝕨𝕠𝕟\'𝕥 𝕓𝕖 𝕣𝕖𝕤𝕡𝕠𝕟𝕤𝕚𝕓𝕝𝕖 𝕗𝕠𝕣 𝕒𝕟𝕪 𝕞𝕚𝕤𝕦𝕤𝕖 𝕠𝕗 𝕥𝕙𝕚𝕤 𝕥𝕠𝕠𝕝 🌚🌚🌝")
t.sleep(5)
os.system("clear")
def loop():
    os.system("clear")
    head = """
 ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████  ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███   ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀  ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███   ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ 
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ 
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░    
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░      ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░ ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░      
          ░  ░  ░    ░ ░           ░    ░  ░         ░    ░            ░    ░         ░  ░   ░         ░ ░        ░   ░           ░          
                                                                                 ░                                                           
"""
    print (Fore.YELLOW + head)
    print(Fore.RED + " Version 1.6".center(60))
    print(Fore.YELLOW + "[+] " + Fore.GREEN + "Tool Name:PhoneNumber OSINT\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Author:Spider Anongreyhat(Anonspidey)\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Version:1.6\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Team:TermuxHackz Society\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Github:https://github.com/spider863644\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "WhatsApp:+2349052863644")
    print(Fore.RED + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>" + Fore.CYAN + "Choose a valid option" + Fore.RED + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    print(Fore.BLUE + """
[1] Get basic information about  Phone Number
[2] Get Phone Number ISP
[3] Extract Phone Numbers and Save
[4] PhoneNumber Validator
[5] Update Program
[6] Join Our WhatsApp Group
[7] Exit Program
""")
    try:
        option = int(input (Fore.YELLOW + Back. RED + "Choose a valid option " + Style.RESET_ALL))
    except ValueError:
        print(Fore.RED + "Only Integers are allowed!")
        t.sleep(2)
        loop()
    if option == 1:
        PhoneNumber = input(Fore.GREEN + "Enter phone number with country code: " + Style.RESET_ALL)
        try:
            parse = phonenumbers.parse(PhoneNumber)
        except:
            print (Fore.RED + "Add country code! ")
            t.sleep(3)
            loop()
        region = geocoder.description_for_number(parse, 'en')
        tiimezone = timezone.time_zones_for_number(parse)
        os.system("clear")
        print(Fore.YELLOW + "Getting basic informations from " + PhoneNumber)
        t.sleep(3)
        print(Fore.GREEN + "Parsed Phone Number is : " + Fore.CYAN, parse)
        print( Fore.GREEN + "Region of Phone Number is: " + Fore.CYAN, region)
        print(Fore.GREEN + "Time Zone of the number is : " + Fore.CYAN, tiimezone)
    elif option == 2:
         PhoneNumber = input(Fore.GREEN + "Enter phone number with country code: " + Style.RESET_ALL)
         try:
             parse = phonenumbers.parse(PhoneNumber)
         except:
             print (Fore.RED + "Add country code!")
             t.sleep (2)
             loop()
         varrier = carrier.name_for_number(parse, 'en')
         print(Fore.GREEN + "The Internet Service Provider(ISP)  is : " + Fore.CYAN , varrier)
    elif option == 3:
        os.system("clear")
        print(Fore.BLUE + """
[1] Upload File
[2] Paste Text
""")
        try:
            file = int(input (Fore.YELLOW + Back. RED + "Choose a valid option: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Only Integers are allowed!")
            t.sleep(2)
            loop()
        if file == 1:
           contact_filename  = input("\n" + Fore.YELLOW + Back.RED + "Upload your file here[Enter file path]: " + Style.RESET_ALL)
           try:
               filename = open(contact_filename, "rt")
           except:
               print(Fore.RED + " File doesn't exist or invalid file path!")
               t.sleep(2)
               exit()

           country_code = input(Fore.GREEN + "Enter country code of the number you want to extract: " + Style.RESET_ALL)
           if "+" not in country_code[0]:
               print (Fore.RED + "Add \"+\" before country code ! ")
               t.sleep(2)
               loop()
           saving_directory = input (Fore.GREEN + "Enter name of the file: " + Fore.GREEN).strip()
           phone_number_file = phonenumbers.PhoneNumberMatcher (str(filename.read()), country_code)
           global extracting
           extracting = ""
           #global z
#           z = str(extracting)
           print(Fore.CYAN + "\n\nExtracting phone numbers from uploaded file ")
           for  extracting in phone_number_file:
               if country_code in str(extracting):
                   print(Fore.YELLOW + str(extracting))
                   z = str(extracting)
                   extracted_numbers = open(saving_directory + ".txt", "a")
                   
                   
                   extracted_numbers.write(z + "\n")
                   extracted_numbers.close()
                   print(Fore.GREEN + "\n\n\nFile has been saved as " + saving_directory + ".txt")

           
         #  if len(z) != 0:

           if len(str(extracting)) == 0:
               print(Fore.RED + "Couldn\'t extract phone number because phone numbers wasn't found in the file or county code wasn't added to the phone numbers")
           elif country_code not in  str(extracting):
               print(Fore.RED + "Couldn\'t find the matching country code")
               t.sleep(2.4)
        elif file == 2:
            reg = ""
            text = input(Fore.GREEN + "Paste your text here: " + Style.RESET_ALL)
            phone = phonenumbers.PhoneNumberMatcher(text, reg)
            global PhoneNumbers
            PhoneNumbers = ""
            print(Fore.BLUE + "Extracting phone numbers from text\n\n")
            for PhoneNumbers in phone:
                
                print(Fore.YELLOW + str(PhoneNumbers)) 
            if len(str(PhoneNumbers)) == 0:
                 print(Fore.RED + "Couldn\'t extract phone number because phone numbers was found in the text or county code wasn't added to the phone numbers")
        else:
            print (Fore.RED + "Invalid option")
            t.sleep (2)
            loop()
    elif option == 4:
         PhoneNumber = input(Fore.GREEN + "Enter phone number with country code: " + Style.RESET_ALL)
         try:
             parse = phonenumbers.parse(PhoneNumber)
         except:
             print(Fore.RED + "Add country code!")
             t.sleep(3)
             loop()
         ValidNumber = phonenumbers.is_valid_number(parse)
         if ValidNumber is True:
             print(Fore.GREEN + PhoneNumber + " is " + Fore.CYAN + "valid")
         else:
             print(Fore.GREEN + PhoneNumber + " is " + Fore.RED + "not valid")
    elif option == 5:
         os.system("clear")
         print(Fore.GREEN + "UPDATING...")
         t.sleep(2)
         os.system("""
         cd $HOME
         rm -rf PhoneNumber-OSINT
         git clone https://github.com/spider863644/PhoneNumber-OSINT""")
         print(Fore.BLUE + """
         type
         cd $HOME
         cd PhoneNumber-OSINT
         python3 phonenumber_osint.py
         """)
         exit()
    elif option == 6:
        print(Fore.GREEN + """


           REDIRECTING TO MY WHATSAPP GROUP""")
        t. sleep(3)
        os.system ("https://chat.whatsapp.com/FqM6BfHV2AAL8K7rOUCpbW")
    elif option == 7:
        print(Fore.YELLOW + " Thanks for using\nFollow me on GitHub")
        os.system("https://github.com/spider863644")
        exit()
    else:
        print(Fore.RED + "Invalid option")
        t.sleep(2)
        loop()
    print ("""

    """)
    cont = input(Fore.YELLOW + Back.RED + "Do you wanna continue?[n/y]: " + Style.RESET_ALL)
    if cont == "Y" or cont == "y":
        loop()
loop()