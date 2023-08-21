def completer(text, state):
    commands = ["exit", "quit", "bye", "hostscan", "scan", "ping", "pingsweep", "list", "show", "print", "hosts", "gethosts"]
    
    options = [cmd for cmd in commands if cmd.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None