print("Round 1")


def over():

    def main():
        while True:
            paper()

    def paper():
        import random
        name = ["R", "S", "P"]
        random_name = random.choice(name)

        string = input("Player 1, enter your choice (R/P/S): ")
        choice1 = str(string)

        print("Player 2, enter your choice (R/P/S): " + random_name)
        if choice1 == "P" and random_name == "R":
            print("Player 1 won! Continue? (Y/N)")
        elif choice1 == "R" and random_name == "S":
            print("Player 1 won! Continue? (Y/N)")
        elif choice1 == "S" and random_name == "P":
            print("Player 1 won! Continue? (Y/N)")
        elif choice1 == random_name:
            print("It's a tie! Continue? (Y/N)")
        else:
            print("Player 2 won! Continue? (Y/N)")

    if __name__ != '__main__':
        pass
    else:
        main()


if __name__ != '__over__': over()
