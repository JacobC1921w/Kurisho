#!/usr/bin/env python3
from json import loads as json
from math import floor

KurishoVersion=json(open("./properties.json", 'r').read())["version"]

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


