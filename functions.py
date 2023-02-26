#!/usr/bin/env python3
from math import floor
from requests import get
from PyPrintSystem.PyPrintSystem import *

def printTitle(KurishoVersion):
    print(u"\u001b[31;1m   ▄█   ▄█▄ ███    █▄     ▄████████  ▄█     ▄████████    ▄█    █▄     ▄██████▄  \u001b[0m")
    print(u"\u001b[31;1m  ███ ▄███▀ ███    ███   ███    ███ ███    ███    ███   ███    ███   ███    ███ \u001b[0m")
    print(u"\u001b[31;1m  ███▐██▀   ███    ███   ███    ███ ███▌   ███    █▀    ███    ███   ███    ███ \u001b[0m")
    print(u"\u001b[31;1m ▄█████▀    ███    ███  ▄███▄▄▄▄██▀ ███▌   ███         ▄███▄▄▄▄███▄▄ ███    ███ \u001b[0m")
    print(u"\u001b[31;1m▀▀█████▄    ███    ███ ▀▀███▀▀▀▀▀   ███▌ ▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ \u001b[0m")
    print(u"\u001b[31;1m  ███▐██▄   ███    ███ ▀███████████ ███           ███   ███    ███   ███    ███ \u001b[0m")
    print(u"\u001b[31;1m  ███ ▀███▄ ███    ███   ███    ███ ███     ▄█    ███   ███    ███   ███    ███ \u001b[0m")
    print(u"\u001b[31;1m  ███   ▀█▀ ████████▀    ███    ███ █▀    ▄████████▀    ███    █▀     ▀██████▀  \u001b[0m")
    print(u"\u001b[31;1m  ▀                      ███    ███                                             \u001b[0m")
    print(u"\u001b[31;1m" + ('─' * (floor((100 / 2) - len(KurishoVersion)))) + "┤ ~クリショ v. " + KurishoVersion + "~ ├" + ('─' * (floor((30 / 2) - len(KurishoVersion)))) + ('─' if len(KurishoVersion) % 2 != 0 else '') + u"\u001b[0m")
    print()

def versionCheck(KurishoVersion):
    p("Checking for updates...", 'i', suffix='\r')
    try:
        versionFetch = get("https://raw.githubusercontent.com/JacobC1921w/Kurisho/main/properties.json").json()["version"]
        if versionFetch == KurishoVersion:
            p("Using latest version, no need for updates!", 's')
        else:
            p(u"New version available (\u001b[32;1m" + KurishoVersion + "\u001b[0m->\u001b[32;1m" + versionFetch + "\u001b[0m), please use \u001b[31;1mgit pull\u001b[0m to update", 'w')
    except:
        p("Version check timeed out, this might be an issue on githubs end", 'w')
