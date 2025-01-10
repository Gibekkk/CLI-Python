import os
import shutil
import sys

from assets import *
from extra_commands import *

def ls():
    items = os.listdir(os.getcwd())
    for item in items:
        if os.path.isdir(item):
            print(f"\033[34m{item}/\033[0m")
        else:
            print(f"\033[36m{item}\033[0m")
    print("\n")

def pwd(): 
    print(f"\nCurrent working directory:\n\033[32m{os.getcwd()}\033[0m\n")

def cd(path):
    try:
        if os.path.abspath(path) == os.path.abspath(os.sep):
            print("\n\033[42mI'm chill bro, but that doesn't match the vibe\033[0m\n")
            return
        os.chdir(path)
        print(f"\nDirectory changed to: \033[42m[ {os.getcwd()} ]\033[0m\n")
    except FileNotFoundError:
        print(f"\nI can't find \033[41m[ {path} ]\033[0m\n")

def mkdir(dirName):
    try:
        os.mkdir(dirName)
        print(f"\n\033[42m[ {dirName} ]\033[0m directory created\n")
    except FileExistsError:
        print(f"\n\033[42m[ {dirName} ]\033[0m already exists\n")

def rmdir(dirName):
    try:
        os.rmdir(dirName)
        print(f"\nDirectory removed: \033[42m[ {dirName} ]\033[0m\n")
    except FileNotFoundError:
        print(f"\nDirectory not found: \033[41m[ {dirName} ]\033[0m\n")
    except OSError:
        print(f"\nDirectory not empty or cannot be removed: \033[41m[ {dirName} ]\033[0m\n")

def touch(filename):
    try:
        with open(filename, 'a'):
            os.utime(filename, None)
        print(f"\nFile created: \033[42m[ {filename} ]\033[0m\n")
    except Exception as e:
        print(f"\nError creating file\033[41m{e}\033[0m\n")

def rm(filename):
    if filename.lower() in ["python_files/main.py", "python_files/assets.py", "readme.md", "python_files/extra_commands.py"]:
        print(f"\nChill bro, deleting this would ruin me\n")
        return
    try:
        os.remove(filename)
        print(f"\nFile removed: \033[42m[ {filename} ]\033[0m\n")
    except FileNotFoundError:
        print(f"\nFile not found: \033[41m[ {filename} ]\033[0m\n")
    except PermissionError:
        print(f"\nPermission denied: \033[41m[ {filename} ]\033[0m\n")

def cp(src, destinasi):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, destinasi)
            print(f"\nCopied directory \033[42m{src}\033[0m to \033[42m{destinasi}\033[0m\n")
        else:
            shutil.copy(src, destinasi)
            print(f"\nCopied file \033[42m{src}\033[0m to \033[42m{destinasi}\033[0m\n")
    except FileNotFoundError:
        print(f"\nSource not found: \033[41m[ {src} ]\033[0m\n")
    except FileExistsError:
        print(f"\nDestination already exists: \033[41m[ {destinasi} ]\033[0m\n")
    except Exception as e:
        print(f"\nError copying: \033[41m{e}\033[0m\n")

def mv(src, destinasi):
    try:
        shutil.move(src, destinasi)
        print(f"\nMoved \033[42m{src}\033[0m to \033[42m{destinasi}\033[0m\n")
    except FileNotFoundError:
        print(f"\nSource file not found: \033[41m[ {src} ]\033[0m\n")

def sos():
    print("""
\033[1;34mList of commands:\033[0m
\033[1;33m• ls:\033[0m List files and directories in the current directory.
\033[1;33m• pwd:\033[0m Show the current working directory.
\033[1;33m• cd <path>:\033[0m Change the current working directory (cd .. to go back).
\033[1;33m• mkdir <directory name>:\033[0m Create a new directory.
\033[1;33m• rmdir <directory name>:\033[0m Remove an empty directory.
\033[1;33m• touch <file name>:\033[0m Create a new empty file.
\033[1;33m• rm <file name>:\033[0m Remove a file.
\033[1;33m• cp <src> <target destination>:\033[0m Copy a file or a directory.
\033[1;33m• mv <src> <target destination>:\033[0m Move or rename a file/directory.
\033[1;33m• help:\033[0m Display the list of commands and their functions.
\033[1;33m• clear:\033[0m Clear the terminal screen.
\033[1;33m• exit:\033[0m Exit the CLI.

\033[1;34mList of chill commands:\033[0m
\033[1;33m• quote:\033[0m Random quotes from Chill Guy.
\033[1;33m• time:\033[0m Chill time is all the time.
\033[1;33m• encrypt:\033[0m Turn text to chill language.
\033[1;33m• mood:\033[0m Checks the vibe and mood for chilling.
\033[1;33m• coinflip:\033[0m Random coin flip.
""")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print(logo)
    print(introText)
    while True:
        command = input("\033[2;37;44mChillCLI>\033[0m ").strip().split()
        if not command:
            continue

        cmd = command[0]
        args = command[1:]

        if cmd == "ls":
            ls()
        elif cmd == "pwd":
            pwd()
        elif cmd == "cd" and args:
            cd(args[0])
        elif cmd == "mkdir" and args:
            mkdir(args[0])
        elif cmd == "rmdir" and args:
            rmdir(args[0])
        elif cmd == "touch" and args:
            touch(args[0])
        elif cmd == "rm" and args:
            rm(args[0])
        elif cmd == "cp" and len(args) == 2:
            cp(args[0], args[1])
        elif cmd == "mv" and len(args) == 2:
            mv(args[0], args[1])
        elif cmd == "help":
            sos()
        elif cmd == "clear":
            clear()
            
        elif cmd == "quote":
            quote()
        elif cmd == "time":
            time()
        elif cmd == "encrypt" and len(args) == 2:
            encrypt(args[1])
        elif cmd == "mood":
            mood()
        elif cmd == "coinflip":
            coinflip()
            
        elif cmd == "exit":
            print(outrotext)
            sys.exit()
            
        else:
            print(f"Unknown command / missing arguments: \033[41m[ {cmd} ]\033[0m (Failed Vibe Check)\n")

if __name__ == "__main__":
    main()