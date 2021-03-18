"""
COMP.CS.100 Programming 1.
David Nagy, david.nagy@tuni.fi, student id 150046451.
PROGRAM DESCRIPTION COMES HERE
"""


def main():
    word = ""

    while word != "quit":
        word = input("Say a word: ")
        print("You said:", word)
    if word == "quit":
        print("I'm quitting now")


if __name__ == "__main__":
    main()
