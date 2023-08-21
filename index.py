#!/usr/bin/env python3
import readline
from json import loads as json
from functions import *
from PyPrintSystem.PyPrintSystem import *
from PyNetTools.PyNetTools import *
from Completer import completer

KurishoVersion=json(open("./properties.json", 'r').read())["version"]
exitNow=False
currentHostList = []
attackVectors=("Android", "BSD", "iOS", "Linux", "OSX", "Unix", "Windows", "Other")

printTitle(KurishoVersion)
versionCheck(KurishoVersion)
print()

readline.parse_and_bind("bind ^I rl_complete")
readline.set_completer(completer)

# CLI loop
while not exitNow:
    currentCommand = input(u"\u001b[31;1m[/] \u001b[0m")

    if currentCommand.lower() in ["exit", "quit", "bye"]:
        doQuit(0)
    elif currentCommand.lower() in ["hostscan", "scan", "ping", "pingsweep"]:
        p(u"Scanning subnet \u001b[31;1m" + getPrivateIP() + "/24\u001b[0m", 'i')
        currentHostList = hostScan(getPrivateIP())
        
        if len(currentHostList) == 0:
            p("Found no hosts", 'e')
        elif len(currentHostList) == 1:
            p("Found 1 host", 'w')
        else:
            p("Found \u001b[31;1m" + str(len(currentHostList)) + "\u001b[0m hosts", 's')

    elif currentCommand.lower() in ["list", "show", "print", "hosts", "gethosts"]:
        if len(currentHostList) == 0:
            p("No hosts currently saved, try using `\u001b[31;1mscan\u001b[0m` first", 'e')
        else:
            p("\u001b[31;1m" + str(len(currentHostList)) + "\u001b[0m hosts saved", 's')
            for host in currentHostList:
                p('.'.join(host.split('.')[:-1]) + ".\u001b[31;1m" + host.split('.')[3] + "\u001b[0m")

    else:
        p("Command '" + currentCommand + "' not found", 'w')

    print()