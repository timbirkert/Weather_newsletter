# Mainscript
# uses all function to send a personalised mail about the weather to everybody in the mail-list


from Email_senden import *
from Wetter_checken import *
from Wetter_AI import *
from Abbonennten import *

for name, details in Abos.items():
    Wohnort=details["Ort"]
    Geburtsdatum=details["Geburtstag"]
    Mail=details["Mail"]
    Wetterdaten=Wetter_check(Wohnort)
    Prompt=f"Gebe einen ausführlichen Wetterbericht basierend auf diesen Daten {Wetterdaten} (ohne Überschrift) und empfehle was {name} anziehen sollte."
    AI_Wetter_Analyse=cohere_prompt(Prompt)
    Anfang= f"Guten Morgen {name}, ich hoffe du hattest einen erholsamen Schlaf. Für einen erfolgreichen Start in den Tag brint dir der Wetterchef deinen täglichen Wetterbericht: "
    Ende=" Aber egal was für Wetter es geben wird, du wirst den Tag so oder so rocken,    dein Wetterchef"
    text=Anfang+"  "+AI_Wetter_Analyse+" "+Ende
    email_senden(Mail,text)



