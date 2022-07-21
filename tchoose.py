#!/usr/bin/env python3

from subprocess import run

def listSessions():
    sessions = run(["tmux","ls"],capture_output=True,text=True).stdout.split("\n")

    counter = 0
    output = []

    if sessions[0] != '':
        for i in sessions:
            if i != '':
                output.append(i.split(":")[0])
                print(f"[{counter}] - {output[counter]}")
                counter += 1

        selection = input("Sessionnumber:")

        if selection.isnumeric():
            selection = int(selection)
            if selection >= 0 and selection < len(output):
                run(f"tmux a -t {output[selection]}", shell=True)

            else:
                print("Number not in range")

        else:
            print("Input has to be a number")

    else:
        print("[-] No tmux sessions available")

def main():
    listSessions()

if __name__ == "__main__":
    main()
