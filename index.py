#!/usr/bin/env python3
from json import loads as json
from functions import *
from PyPrintSystem.PyPrintSystem import *
from PyNetTools.PyNetTools import *

KurishoVersion=json(open("./properties.json", 'r').read())["version"]

printTitle(KurishoVersion)
versionCheck(KurishoVersion)

