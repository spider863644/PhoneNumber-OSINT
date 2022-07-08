import os, time as t
os.system("clear")
try:
    import colorama
    import pyfiglet
    import phonenumbers
except ModuleNotFoundError:
    print("\033[1;31;40m Some requirements are missing!\n\nRun \"pip install -r requirements.txt\" then run \"python3 phonenumber_osint.py \"\033[1;37;40m" )
    t.sleep(2)
    exit()
from colorama import *
from phonenumbers import geocoder, carrier, timezone
print(Fore.RED + "𝔻𝕚𝕤𝕔𝕝𝕒𝕚𝕞𝕖𝕣: 𝕌𝕤𝕖 𝕥𝕙𝕚𝕤 𝕥𝕠𝕠𝕝 𝕗𝕠𝕣 𝕖𝕕𝕦𝕔𝕒𝕥𝕚𝕠𝕟𝕒𝕝 𝕡𝕦𝕣𝕡𝕠𝕤𝕖𝕤 𝕠𝕟𝕝𝕪 \n\n𝕊𝕡𝕚𝕕𝕖𝕣 𝔸𝕟𝕠𝕟𝕘𝕣𝕖𝕪𝕙𝕒𝕥 𝕨𝕠𝕟\'𝕥 𝕓𝕖 𝕣𝕖𝕤𝕡𝕠𝕟𝕤𝕚𝕓𝕝𝕖 𝕗𝕠𝕣 𝕒𝕟𝕪 𝕞𝕚𝕤𝕦𝕤𝕖 𝕠𝕗 𝕥𝕙𝕚𝕤 𝕥𝕠𝕠𝕝 🌚🌚🌝") 
t.sleep(5)
os.system("clear")
def loop():
    os.system("clear")
    head = pyfiglet.figlet_format("PhoneNumber-OSINT")
    print (Fore.YELLOW + head)
    print(Fore.RED + " Version 1.0".center(60))
    print(Fore.YELLOW + "[+] " + Fore.GREEN + "Tool Name:PhoneNumber OSINT\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Author:Spider Anongreyhat(Anonspidey)\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Version:1.0\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Team:TermuxHackz Society\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "Github:https://github.com/spider863644\n" + Fore.YELLOW + "[+] " + Fore.GREEN + "WhatsApp:+2349052863644")
    print(Fore.RED + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>" + Fore.CYAN + "Choose a valid option" + Fore.RED + "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<") 
    print(Fore.BLUE + """
[1] Get basic information about  Phone Number
[2] Get Phone Number ISP
[3] Extract Phone Numbers
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
[1] Upload File(CSV)
[2] Paste Text
""")
        try:
            file = int(input (Fore.YELLOW + Back. RED + "Choose a valid option: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Only Integers are allowed!")
            t.sleep(2)
            loop()
        if file == 1:
            print(Fore.RED + "Unavailable!")
            t.sleep(2)
            loop()
        elif file == 2:
            text = input(Fore.GREEN + "Paste your text here: " + Style.RESET_ALL)
            #reg = input(Fore.GREEN + "Enter region code[example \"ni\" for Nigeria] : " + Style.RESET_ALL)
            reg = 'INDIA'
            phone = phonenumbers.PhoneNumberMatcher(text, reg)
            for PhoneNumbers in phone:
                print(Fore.BLUE + "Extracting phone numbers from text")
                t.sleep(3)
                print(PhoneNumbers)
        else:
            print (Fore.RED + "Invalid option")
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
        os.system ("xdg-open https://chat.whatsapp.com/IWqGOsJPjkp2vXcMSJKYns")
    elif option == 7:
        print(Fore.YELLOW + " Thanks for using\nFollow me on GitHub")
        exit()
    else:
        print(Fore.RED + "Invalid option")
        t.sleep(2)
        loop()
    print ("""
        
    """)
    cont = input(Fore.YELLOW + Back.RED + "Do you wanna continue?[n/y]: " + Style.RESET_ALL)
    if cont.lower == "Y":
        loop()
loop()
